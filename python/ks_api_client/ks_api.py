import ks_api_client
import base64
import json
import os
import socketio
from urllib3 import make_headers

from ks_api_client.exceptions import ApiException, ApiValueError
from ks_api_client.models import NewMTFOrder, NewNormalOrder, NewOrder, \
                NewSMOrder, NewSOROrder, ExistingMTFOrder, ExistingNormalOrder, \
                ExistingOrder, ExistingSMOrder, ExistingSOROrder, ReqMargin, \
                UserCredentials, UserDetails, NewMISOrder, InlineObject
from ks_api_client.settings import broadcast_host

class KSTradeApi():
    def __init__(self, access_token, userid, consumer_key, ip, app_id, 
            hosts=["https://tradeapi.kotaksecurities.com/apim","https://sbx.kotaksecurities.com/apim"],
            proxy_url = '', proxy_user = '', proxy_pass = '', consumer_secret = None):
        self.userid  =  userid
        self.consumer_key  =  consumer_key
        self.consumer_secret = consumer_secret
        self.ip  =  ip
        self.app_id  =  app_id
        self.access_token  =  access_token
        self._proxy_user = proxy_user
        self._proxy_pass = proxy_pass
        self._proxy_url = proxy_url
        error = None
        session_init = None
        for host in hosts:
            self.host = host
            configuration  =  self.get_config(proxy_url, proxy_user, proxy_pass)
            try:
                self.api_client  =  ks_api_client.ApiClient(configuration)
                session_init_res  =  ks_api_client.SessionApi(self.api_client).session_init(self.userid, \
                                self.consumer_key, self.ip, self.app_id)
            except ApiException as ex:
                error = ex
                continue
            if(session_init_res.get("Success")):
                session_init = session_init_res.get("Success")
            elif(session_init_res.get("success")):
                session_init = session_init_res.get("success")
            if self.host !=  session_init['redirect']['host']:
                self.host  =  session_init['redirect']['host']
                configuration  =  self.get_config(proxy_url, proxy_user, proxy_pass)
                self.api_client  =  ks_api_client.ApiClient(configuration)
                session_init  =  ks_api_client.SessionApi(self.api_client).session_init(self.userid, \
                                self.consumer_key, self.ip, self.app_id)
            break
        if not session_init and error:
            raise error

    def get_config(self, proxy_url = '', proxy_user = '', proxy_pass = ''):
        configuration  =  ks_api_client.Configuration(self.host)
        configuration.access_token  =  self.access_token
        if proxy_url:
            configuration.proxy = proxy_url
            if proxy_user:
                configuration.proxy_headers = make_headers(proxy_basic_auth = ':'.join((proxy_user,proxy_pass)))
        return configuration

    def login(self, password):
        user_credentials  =  UserCredentials(userid = self.userid, password = password)
        login_response_res  =  ks_api_client.SessionApi(self.api_client).login_with_user_id(self.consumer_key, \
                self.ip, self.app_id, UserCredentials = user_credentials)
        login_response = ''
        if(login_response_res.get("Success")):
            login_response = login_response_res.get("Success")
        elif(login_response_res.get("success")):
            login_response = login_response_res.get("success")
        self.one_time_token  =  login_response['oneTimeToken']
        return login_response_res
		
    def session_2fa(self, access_code=None):
        if self.one_time_token:
            generate_session_res = None
            if not access_code:
                inline_object = InlineObject(userid=self.userid)
                generate_session_res  =  ks_api_client.SessionApi(self.api_client)\
                        .generate_session2_fa_ott(self.one_time_token, \
                        self.consumer_key, self.ip, self.app_id, InlineObject = inline_object)
            else:
                user_details  =  UserDetails(userid = self.userid, accessCode = access_code)
                generate_session_res  =  ks_api_client.SessionApi(self.api_client)\
                        .generate_session2_fa(self.one_time_token, \
                        self.consumer_key, self.ip, self.app_id, UserDetails = user_details)
            generate_session = None				  
            if(generate_session_res.get("Success")):
                generate_session = generate_session_res.get("Success")
            elif(generate_session_res.get("success")):
                generate_session = generate_session_res.get("success")
            self.session_token  =  generate_session['sessionToken']
            return generate_session
        else:
            raise ApiValueError("No one time token found. Please invoke 'session_login_api' function first")

    def logout(self):
        logout  =  ks_api_client.SessionApi(self.api_client).session_logout(self.session_token,self.consumer_key,\
						self.ip, self.app_id, self.userid)
        return logout

#-------------------------------------------------------------------------------
# Common methods for placing order

    def place_order(self, order_type, instrument_token, transaction_type,  \
                                quantity, price, disclosed_quantity = 0,trigger_price = 0 , tag = "string", \
								validity ="GFD", variety = "REGULAR", product = None, smart_order_routing = None):
        """
        Method executes placing_orders according to it's order type.
        return response.
        """
        place_order  =  None
        if not 'session_token'  in self.__dict__:
            raise ApiValueError("Please invoke 'session_2fa' function first")
        if order_type != "O" and product:
            raise ApiValueError("Product can be supplied only if Order Type value is 'O'")
        if order_type == "O" and not product:
            raise ApiValueError("Please supply the 'product' paramater for order_type = 'O'")
        if order_type == "O":
            order  =  NewOrder(instrumentToken  =  instrument_token, tag = tag, transactionType = transaction_type,\
                                    variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity,\
                                    validity = validity, triggerPrice = trigger_price, product = product,smartOrderRouting = smart_order_routing)
            place_order  =  ks_api_client.OrderApi(self.api_client).place_new_order(self.consumer_key,
                            self.session_token, order)
        elif order_type  ==  'N':
            order  =  NewNormalOrder(instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                        variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity,\
                        validity = validity, triggerPrice = trigger_price)
            place_order  =  ks_api_client.NormalOrderApi(self.api_client).place_new_normal_order(self.consumer_key,
                            self.session_token, order)
        elif order_type  ==  'SM':
            order  =  NewSMOrder( instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                    variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity, \
                    validity = validity, triggerPrice = trigger_price)
            place_order  =  ks_api_client.SuperMultipleOrderApi(self.api_client).place_new_sm_order(self.consumer_key,\
                            self.session_token, order)
        elif order_type  ==  'SOR':
            order  =  NewSOROrder( instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                    variety = variety, quantity = quantity, price = price, validity = validity, disclosedQuantity = disclosed_quantity,triggerPrice = trigger_price )
            place_order  =  ks_api_client.SmartOrderRoutingApi(self.api_client).place_new_sor_order(self.consumer_key,\
                            self.session_token, order)
        elif order_type  ==  'MTF':
            order  =  NewMTFOrder(instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity, \
                validity = validity, triggerPrice = trigger_price)
            place_order  =  ks_api_client.MarginTradingApi(self.api_client).place_new_mtf_order(self.consumer_key, \
                            self.session_token, order)
        elif order_type  ==  'MIS':
            order  =  NewMISOrder(instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                        variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity,\
                        validity = validity, triggerPrice = trigger_price)
            place_order  =  ks_api_client.MISOrderApi(self.api_client).place_new_mis_order(self.consumer_key,
                            self.session_token, order)
        else:
            raise TypeError("Provided order type is invalid, use either of O(Order), N(Normal Order), SM(Super Multiple Order), SOR(Smart Order Routing), MTF(Margin Tading Facility) or MIS")

        return place_order

# Common methods for modifiying order

		
    def modify_order(self, order_id, price , quantity , disclosed_quantity , trigger_price , validity):
        """
        Method executes modifying_orders
        return response.
        """				
        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'session_2fa' function first")
        
        modify_order = ExistingOrder(orderId = order_id, disclosedQuantity = disclosed_quantity, price = price,\
                  quantity = quantity, triggerPrice = trigger_price,validity = validity)
        modified_order_res  =  ks_api_client.OrderApi(self.api_client).modify_order(self.consumer_key,
                            self.session_token, modify_order)
        return modified_order_res

# Common methods for cancelling order		
		
    def cancel_order(self, order_id):
        """
        Method executes cancelling_order 
        return response.
        """
        order  =  False

        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'session_2fa' function first")
            
        order  =  ks_api_client.OrderApi(self.api_client).cancel_order(self.consumer_key,
                            self.session_token, order_id)
        return order

#-------------------POSITIONS---------------------

    def positions(self, position_type):
        if position_type  ==  'TODAYS':
            positions_res  =  ks_api_client.PositionsApi(self.api_client).positions_today(self.consumer_key,self.session_token)
        elif position_type  ==  'OPEN':
            positions_res = ks_api_client.PositionsApi(self.api_client).positions_open(self.consumer_key,self.session_token)
        elif position_type  ==  'STOCKS':
            positions_res = ks_api_client.PositionsApi(self.api_client).positions_stocks(self.consumer_key,self.session_token)
        else:
            raise TypeError("Provided position type is invalid, use either of TODAYS, OPEN or STOCKS")
        return positions_res

#---------------------ORDERS REPORTS----------------------------

    def order_report(self, order_id = None, is_fno = ""):
        if order_id is None:
            order_report  =  ks_api_client.ReportsApi(self.api_client).get_order_reports(self.consumer_key, \
                    self.session_token)
        elif is_fno and is_fno in ("Y", "N", "y", "n"):
            is_fno = is_fno.capitalize()
            order_report = ks_api_client.ReportsApi(self.api_client)\
                .get_fno_order_detail_by_order_id(order_id, self.consumer_key, \
                self.session_token, is_fno)
        else:
            order_report  =  ks_api_client.ReportsApi(self.api_client)\
                .get_order_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return order_report

#--------------------------TRADES REPORTS---------------------------------

    def trade_report(self, order_id  = None, is_fno = ""):
        if order_id is None:
            trade_report  =  ks_api_client.ReportsApi(self.api_client).get_trade_report(consumerKey = self.consumer_key,
                sessionToken = self.session_token)
        elif is_fno and is_fno in ("Y", "N", "y", "n"):
            is_fno = is_fno.capitalize()
            trade_report  =  ks_api_client.ReportsApi(self.api_client).get_fno_trade_report_by_order_id(order_id,self.consumer_key, \
                self.session_token, is_fno)
        else:
            trade_report  =  ks_api_client.ReportsApi(self.api_client).get_trade_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return trade_report

#-----------------------Margins------------------------

    def margin_required(self, transaction_type, order_info):
        req_margin  =  ReqMargin(transactionType = transaction_type, orderInfo = self.convertArray(order_info))
        if not isinstance(req_margin, ReqMargin):
            raise ApiValueError("ReqMargin with type ",type(req_margin)," is not valid.")
        margin_required  =  ks_api_client.MarginApi(self.api_client).margin_required(self.consumer_key,self.session_token,
                ReqMargin = req_margin)
        return margin_required

    def margin(self):
        margins = ks_api_client.MarginApi(self.api_client).get_margins(self.consumer_key,self.session_token)
        return margins
		
#-----------------------Quote Api------------------------	

    def quote(self, instrument_token, quote_type = None):
        if quote_type is None:
            quote  =  ks_api_client.QuoteApi(self.api_client).get_instruments_details(self.consumer_key, \
                self.session_token, instrument_token)
        elif quote_type  ==  'LTP':
             quote  =  ks_api_client.QuoteApi(self.api_client).get_ltp_quote(self.consumer_key, \
                self.session_token, instrument_token)
        elif quote_type  ==  'DEPTH':
            quote  =  ks_api_client.QuoteApi(self.api_client).get_market_details_quote(self.consumer_key, \
                self.session_token, instrument_token)
        elif quote_type  ==  'OHLC':
            quote  =  ks_api_client.QuoteApi(self.api_client).get_ohlc_quote(self.consumer_key, \
                self.session_token, instrument_token)
        else:
            raise TypeError("Provided quote type is invalid, use either of LTP, DEPTH or OHLC")
        return quote

#-----------------------Get Order Id-------------
    def get_order_id(self, order_res):
        if(order_res.get("Success")):
            order = order_res.get("Success")
        elif(order_res.get("success")):
            order = order_res.get("success")
        if (order.get("NSE") and order.get("BSE")):
            if(order.get("NSE").get("orderId")):
                order = order.get("NSE")
            elif(order.get("BSE").get("orderId")):
                order = order.get("BSE")
        else:
            if(order.get("NSE")):
                order = order.get("NSE")
            elif(order.get("BSE")):
                order = order.get("BSE")
        return str(order['orderId'])

#-------------------Historical---------------------
    def history(self, resource, json_input):
        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'session_2fa' function first")
        if(resource == 'historicalprices'):
            if (json_input.keys() != {"exchange":"","cocode":"","fromdate":"","todate":""}.keys()):
                raise ApiValueError("exchange,cocode,fromdate,todate fields are required.")
        elif(resource == 'historicalprices-unadjusted'):
            if (json_input.keys() != {"exchange":"","co_code":"","date":""}.keys()):
                raise ApiValueError("exchange,co_code,date fields are required.")
        elif(resource == 'NSEFNO_HistoricalContinuousChart'):
            if (json_input.keys() != {"symbol":"","expiry type":""}.keys()):
                raise ApiValueError("symbol,expiry type fields are required.")
        elif(resource == 'LiveorEODHistorical'):
            if (json_input.keys() != {"exchange":"","co_code":"","period":"","cnt":""}.keys()):
                raise ApiValueError("exchange,co_code,period,cnt fields are required.")    
        encoded_json = base64.urlsafe_b64encode(json.dumps(json_input).encode()).decode()
        data = ks_api_client.HistoricalApi(self.api_client).get_resource(resource,encoded_json)
        return data					 
#-------- Convert Array and object snake_case keys to camelCase -----------

    def convertObject(self, object):  
        newObj={}
        for key in object .keys():
            new_key='';
            for idx , word in enumerate(key.split('_')): 
                if(idx==0):
                    new_key = ''+str(word)
                else:
                    new_key=new_key+(word.title())
            newObj[new_key] = object[key]
            
        return newObj
 
    def convertArray(self, array): 
        new_array = []
        for obj in array:
            new_array.append(self.convertObject(obj))
        return new_array


    def subscribe(self, input_tokens, callback, broadcast_host=broadcast_host):
        try:
            if self.consumer_secret == None:
                raise ApiValueError("Please pass the consumer secret while creating client")
            proxy = ""
            auth_token = self.consumer_key+":"+self.consumer_secret
            if self._proxy_pass or self._proxy_url or self._proxy_user:
                import urllib.parse
                import requests
                session = requests.session()
                scheme = ""
                parsed = urllib.parse.urlparse(self._proxy_url)
                if not parsed.scheme:
                    scheme = "http://"
                else:
                    scheme += parsed.scheme+"://"
                if self._proxy_pass and self._proxy_user:
                    proxy += scheme + ":".join((self._proxy_user, self._proxy_pass)) +\
                        "@" + parsed.hostname
                    if parsed.port:
                        proxy += ":" + str(parsed.port)
                    session.proxies.update({'http':proxy, 'https':proxy})
                    session.verify = 's' in scheme
            # Generating base64 encoding of consumer credentials
            AUTH_BASE64 = base64.b64encode(auth_token.encode("UTF-8"))
            PAYLOAD = {"authentication": AUTH_BASE64.decode("UTF-8")}
            # Getting access token
            response = session.post(urllib.parse.urljoin(broadcast_host,"feed/auth/token"),
                data=PAYLOAD)
            jsonResponse = response.json()
            # Check if we got access token
            if jsonResponse['result']['token'] is None:
                print('Token not found')
            else:
                parsed_broadcast_host = urllib.parse.urlparse(broadcast_host)
                socketio_path = parsed_broadcast_host.path
                self.sio = socketio.Client(
                    reconnection=True, request_timeout=20, reconnection_attempts=5, engineio_logger=True,
                            logger=True,http_session=session, ssl_verify=session.verify)

                @self.sio.event
                def connect():
                    self.sio.emit('pageload', {'inputtoken': input_tokens})

                @self.sio.event
                def connect_error(data):
                    print("Connection failed")

                @self.sio.event
                def disconnect():
                    print('Connection closed')

                @self.sio.on('getdata')
                def on_getdata(data, callback=callback):
                    callback(data)

                # Do the connection using above access token
                self.sio.connect(broadcast_host, 
                        headers={'Authorization': 'Bearer ' + jsonResponse['result']['token']},
                        transports=["websocket"], socketio_path=socketio_path)
        except Exception as err:
            print(f'Other error occurred: {err}')

    def unsubscribe(self):
        self.sio.disconnect()


    def token(self, grant_type, username, password, refresh_token):
        if self.consumer_secret == None:
            raise ApiValueError("Please pass the consumer secret while creating client")
        auth_token = self.consumer_key+":"+self.consumer_secret
        AUTH_BASE64 = base64.b64encode(auth_token.encode("UTF-8"))
        authorization = AUTH_BASE64.decode("UTF-8")
        token = ks_api_client.TokenApi(self.api_client).token_post(authorization = authorization, grant_type = grant_type, username = username, \
             password = password, refresh_token = refresh_token)
        return token

    def revoke(self, token, token_type_hint):
        if self.consumer_secret == None:
            raise ApiValueError("Please pass the consumer secret while creating client")
        auth_token = self.consumer_key+":"+self.consumer_secret
        AUTH_BASE64 = base64.b64encode(auth_token.encode("UTF-8"))
        authorization = AUTH_BASE64.decode("UTF-8")
        revoke = ks_api_client.TokenApi(self.api_client).revoke_post(authorization = authorization, token = token, token_type_hint = token_type_hint)
        return revoke
