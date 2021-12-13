import unittest
import time

from ks_api_client.ks_api import KSTradeApi as TradingApi
from ks_api_client.rest import ApiValueError

from ks_api_client.settings import host, access_token, userid, \
    consumer_key, app_id, password, access_code, ip


class TestKSTradeApi(unittest.TestCase):

    ks_trade_api = TradingApi(access_token, userid, consumer_key, ip, app_id, host)

    def setUp(self):
        self.ks_trade_api.login(password)
        self.ks_trade_api.session_2fa(access_code)

    def test_a_session_login_api(self):
        self.ks_trade_api.login(password)
        print("Your login is successful. One time token is ", self.ks_trade_api.one_time_token)

    def test_b_generate_session2_fa(self):
        time.sleep(1)
        self.ks_trade_api.login(password)
        self.ks_trade_api.session_2fa(access_code)
        print("Your session is generated. Session token is ", self.ks_trade_api.session_token)
#----------------------------------------------------------------------------------------------------------------------------
 #NORMAL
    def test_c_place_order(self):
        time.sleep(1)
        place_new_order = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = self.ks_trade_api.get_order_id(place_new_order)
        if order_id:
            print("Your Normal Order Id ", order_id, "is been successfully placed")
        else:
            raise ApiValueError("Normal Order Could not be placed")

    def test_d_modify_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 2290, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = self.ks_trade_api.get_order_id(new_order_modify)
        if order_id:
            print("Your Normal Order Id ", order_id, "is been modified ")
            modify_order = self.ks_trade_api.modify_order(order_id = order_id, disclosed_quantity = 0, \
                price = 2281, quantity = 1, trigger_price = 0, validity = "GFD")
            modify_order_id = self.ks_trade_api.get_order_id(modify_order)
            if not modify_order_id:
                print("Your Normal Order Id ",modify_order_id , "is not Modified")

    def test_e_cancel_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                instrument_token = 904, variety = "REGULAR", quantity = 1, price = 17251, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = self.ks_trade_api.get_order_id(new_order_cancel)
        if order_id:
            print("Your Normal Order Id", order_id, "is been cancelled ")
            cancel_order = self.ks_trade_api.cancel_order(order_id)
            cancel_order_id = self.ks_trade_api.get_order_id(cancel_order)
            if not cancel_order_id:
                print("Your Normal Order Id ", cancel_order_id, "is not cancelled")
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# # #ORDERS
    def test_f_place_order(self):
        time.sleep(1)
        place_new_order = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smart_order_routing="string")
        order_id = self.ks_trade_api.get_order_id(place_new_order)
        if order_id:
            print("Your Order Id ", order_id, "is been successfully placed")
        else:
            raise ApiValueError("Order Could not be placed")

    def test_g_modify_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0,product = "NORMAL" ,smart_order_routing="string")
        order_id = self.ks_trade_api.get_order_id(new_order_modify)
        if order_id:
            print("Your Order Id ", order_id, "is been successfully modified")
            modify_order = self.ks_trade_api.modify_order(order_id = order_id, disclosed_quantity = 0,\
                    price = 0, quantity = 1, trigger_price = 0, validity = "GFD")
            modify_order_id = self.ks_trade_api.get_order_id(modify_order)
            if not modify_order_id:
                print("Your Order Id ", modify_order_id, "is not Modified")


    def test_h_cancel_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_order(order_type = "N", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 2071, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smart_order_routing="string")
        order_id = self.ks_trade_api.get_order_id(new_order_cancel)
        if order_id:
            print("Your Order Id", order_id, "is been cancelled")
            cancel_order = self.ks_trade_api.cancel_order(order_id)
            cancel_order_id = self.ks_trade_api.get_order_id(cancel_order)
            if cancel_order_id:
                print("Your Order Id ", cancel_order_id, "is not cancelled")
#----------------------------------------------------------------------------------------------------------------------------


# #----------------------------------------------------------------------------------------------------------------------------
# #MULTIPLE ORDER

    def test_c_place_new_sm_order(self):
        time.sleep(1)
        place_new_sm_order = self.ks_trade_api.place_order(order_type = "SM", tag="string", transaction_type="BUY", \
                    instrument_token=727, variety="REGULAR", quantity=1, price=2292.25, \
                    validity="GFD", trigger_price=2057)
        order_id = self.ks_trade_api.get_order_id(place_new_sm_order)
        if order_id:
            print("Your Multiple Order Id ", order_id, "is been successfully placed")
        else:
            raise ApiValueError("Multiple Order Could not be placed")

    def test_d_modify_sm_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_order(order_type = "SM", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 2058, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 2037.03)
        order_id = self.ks_trade_api.get_order_id(new_order_modify)
        if order_id:
            print("Your Multiple Order Id ", order_id, "is  Modified")
            modify_sm_order = self.ks_trade_api.modify_order(order_id = order_id, disclosed_quantity = 0,\
                    price = 2059, quantity = 0, trigger_price = 2037.04, validity = "GFD")


    def test_e_cancel_sm_order(self):
        time.sleep(1)
        cancel_sm_order = self.ks_trade_api.place_order(order_type = "SM", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 2, price = 2208, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = self.ks_trade_api.get_order_id(cancel_sm_order)
        if order_id:
            print("Your Multiple Order Id", order_id, "is  cancelled")
            cancel_sm_order = self.ks_trade_api.cancel_order(order_id)


# #----------------------------------------------------------------------------------------------------------------------------
#SOR
    def test_s_place_new_sor_order(self):
        time.sleep(1)
        place_new_sor_order = self.ks_trade_api.place_order(order_type = "SOR", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, validity = "GFD")
        order_id = self.ks_trade_api.get_order_id(place_new_sor_order)
        if order_id:
            print("Your SOR Order ", order_id, "is been successfully placed")
        else:
            raise ApiValueError("Order Could not be placed")

    def test_t_modify_sor_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_order(order_type = "SOR", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                validity = "GFD")
        order_id = self.ks_trade_api.get_order_id(new_order_modify)
        if order_id:
            print("Your Order ", order_id, "is been successfully placed")
            modify_order = self.ks_trade_api.modify_order(order_id = order_id, price = 0, quantity = 1, disclosed_quantity = 0, \
                trigger_price = 0, validity = "GFD")
            modify_order_id = self.ks_trade_api.get_order_id(modify_order)
            if modify_order_id:
                print("Your SOR Order ", modify_order_id, "is been successfully Modified")


    def test_u_cancel_sor_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_order(order_type = "SOR", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                validity = "GFD")
        order_id = self.ks_trade_api.get_order_id(new_order_cancel)
        if new_order_cancel:
            print("Your Order ", new_order_cancel, "is been successfully placed")
            cancel_order = self.ks_trade_api.cancel_order(order_id = order_id)
            cancel_order_id = self.ks_trade_api.get_order_id(cancel_order)
            if cancel_order_id :
                print("Your SOR Order  ", cancel_order_id, "is been successfully cancelled")

#----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
#MTF
    def test_f_place_new_mtf_order(self):
        time.sleep(1)
        place_new_order = self.ks_trade_api.place_order(order_type = "MTF", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = self.ks_trade_api.get_order_id(place_new_order)
        if order_id:
            print("Your MTF Order Id ", order_id, "is been successfully placed")
        else:
            raise ApiValueError("MTF Order Couldnot be placed")

    def test_g_modify_mtf_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_order(order_type = "MTF", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = self.ks_trade_api.get_order_id(new_order_modify)
        if order_id:
            print("Your MTF Order Id ", order_id, "is been modified ")
            modify_mtf_order = self.ks_trade_api.modify_order(order_id = order_id, disclosed_quantity = 1,\
                    price = 0, quantity = 1, trigger_price = 0, validity = "GFD")
            modify_mtf_order_id = self.ks_trade_api.get_order_id(modify_mtf_order)
            if modify_mtf_order_id:
                print("Your MTF Order Id ", modify_mtf_order_id, "is not Modified")

    def test_h_cancel_mtf_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_order(order_type = "MTF", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        order_id = self.ks_trade_api.get_order_id(new_order_cancel)
        if order_id:
            print("Your MTF Order Id", order_id, "is cancelled")
            cancel_mtf_order = self.ks_trade_api.cancel_order(order_id = order_id)
            cancel_mtf_order_id = self.ks_trade_api.get_order_id(cancel_mtf_order)
            if cancel_mtf_order_id:
                print("Your MTF Order Id ", cancel_mtf_order_id, "is not cancelled")
#----------------------------------------------------------------------------------------------------------------------------
# POSITION

    def test_c_positions_today(self):
        positions_today=self.ks_trade_api.positions(position_type = "TODAYS")
        print(positions_today,"Position today")

    def test_d_positions_open(self):
        positions_open=self.ks_trade_api.positions(position_type = "OPEN")
        print(positions_open," Position open ")

    def test_e_positions_stocks(self):
        positions_stocks=self.ks_trade_api.positions(position_type = "STOCKS")
        print(positions_stocks,"Position stock")

# #----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
 #REPORTS
    def test_o_get_order_report(self):

        time.sleep(1)
        get_order_report = self.ks_trade_api.place_order(order_type = "O", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smart_order_routing="string")
        order_id = self.ks_trade_api.get_order_id(get_order_report)
        if order_id:
            print("Your Report has been succesfully generated")
            get_order_report = self.ks_trade_api.order_report(order_id = order_id)


    def test_p_get_order_report_by_order_id(self):
        time.sleep(1)
        get_order_report_by_order_id = self.ks_trade_api.place_order(order_type = "O", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smart_order_routing="string")
        order_id = self.ks_trade_api.get_order_id(get_order_report_by_order_id)
        if order_id:
            print("Your get order report by order id is: ", order_id ,"has been succesfully genrated")
            get_order_report_by_order_id = self.ks_trade_api.order_report(order_id = order_id)
# #----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
 #TRADS
    def test_q_get_trade_report(self):
        time.sleep(1)
        get_trade_report = self.ks_trade_api.place_order(order_type = "O" , tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smart_order_routing="string")
        order_id = self.ks_trade_api.get_order_id(get_trade_report)
        if order_id:
            print("Your trade Report for get order  : ", order_id ,"has been succesfully genrated")
            get_trade_report = self.ks_trade_api.trade_report()


    def test_r_get_trade_report_by_order_id(self):

        time.sleep(1)
        get_trade_report_by_order_id = self.ks_trade_api.place_order(order_type = "O", tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smart_order_routing="string")
        order_id = self.ks_trade_api.get_order_id(get_trade_report_by_order_id)
        if order_id:
            print("Your trade order report by order id is: ", order_id ,"has been succesfully genrated")
            get_trade_report_by_order_id = self.ks_trade_api.trade_report(order_id)
#-----------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
#MARGIN
    def test_i_margin_required(self):
        order_info = [
            {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
            {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
        ]
        margin_required = self.ks_trade_api.margin_required(transaction_type = "BUY",order_info = order_info)
        print("margin_required: ",margin_required)

#----------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main
