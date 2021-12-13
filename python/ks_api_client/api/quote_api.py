# coding: utf-8


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ks_api_client.api_client import ApiClient
from ks_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class QuoteApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_instruments_details(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get full details  # noqa: E501

        Get full details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instruments_details(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.get_instruments_details_with_http_info(consumerKey, sessionToken, instrumentTokens, **kwargs)  # noqa: E501

    def get_instruments_details_with_http_info(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get full details  # noqa: E501

        Get full details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instruments_details_with_http_info(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'consumerKey',
            'sessionToken',
            'instrumentTokens'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_instruments_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_instruments_details`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_instruments_details`")  # noqa: E501
        # verify the required parameter 'instrumentTokens' is set
        if self.api_client.client_side_validation and ('instrumentTokens' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrumentTokens'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrumentTokens` when calling `get_instruments_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instrumentTokens' in local_var_params:
            path_params['instrumentTokens'] = local_var_params['instrumentTokens']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quotes/v1.0/instruments/{instrumentTokens}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_ltp_quote(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get LTP quote  # noqa: E501

        Returns the LTP for an array of scrips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ltp_quote(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: Instrument token of the scrip for which quote (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.get_ltp_quote_with_http_info(consumerKey, sessionToken, instrumentTokens, **kwargs)  # noqa: E501

    def get_ltp_quote_with_http_info(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get LTP quote  # noqa: E501

        Returns the LTP for an array of scrips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ltp_quote_with_http_info(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: Instrument token of the scrip for which quote (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'consumerKey',
            'sessionToken',
            'instrumentTokens'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ltp_quote" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_ltp_quote`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_ltp_quote`")  # noqa: E501
        # verify the required parameter 'instrumentTokens' is set
        if self.api_client.client_side_validation and ('instrumentTokens' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrumentTokens'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrumentTokens` when calling `get_ltp_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instrumentTokens' in local_var_params:
            path_params['instrumentTokens'] = local_var_params['instrumentTokens']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quotes/v1.0/ltp/instruments/{instrumentTokens}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_market_details_quote(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get market details quote  # noqa: E501

        Returns market depth details for an array of scrips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_market_details_quote(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: Instrument token of the scrip for which quote (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.get_market_details_quote_with_http_info(consumerKey, sessionToken, instrumentTokens, **kwargs)  # noqa: E501

    def get_market_details_quote_with_http_info(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get market details quote  # noqa: E501

        Returns market depth details for an array of scrips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_market_details_quote_with_http_info(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: Instrument token of the scrip for which quote (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'consumerKey',
            'sessionToken',
            'instrumentTokens'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_market_details_quote" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_market_details_quote`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_market_details_quote`")  # noqa: E501
        # verify the required parameter 'instrumentTokens' is set
        if self.api_client.client_side_validation and ('instrumentTokens' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrumentTokens'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrumentTokens` when calling `get_market_details_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instrumentTokens' in local_var_params:
            path_params['instrumentTokens'] = local_var_params['instrumentTokens']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quotes/v1.0/depth/instruments/{instrumentTokens}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_ohlc_quote(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get OHLC quote  # noqa: E501

        Returns the OHLC quote details for an array of scrips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ohlc_quote(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: Instrument token of the scrip for which quote (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.get_ohlc_quote_with_http_info(consumerKey, sessionToken, instrumentTokens, **kwargs)  # noqa: E501

    def get_ohlc_quote_with_http_info(self, consumerKey, sessionToken, instrumentTokens, **kwargs):  # noqa: E501
        """Get OHLC quote  # noqa: E501

        Returns the OHLC quote details for an array of scrips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ohlc_quote_with_http_info(consumerKey, sessionToken, instrumentTokens, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param instrumentTokens: Instrument token of the scrip for which quote (required)
        :type instrumentTokens: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'consumerKey',
            'sessionToken',
            'instrumentTokens'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ohlc_quote" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_ohlc_quote`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_ohlc_quote`")  # noqa: E501
        # verify the required parameter 'instrumentTokens' is set
        if self.api_client.client_side_validation and ('instrumentTokens' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrumentTokens'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrumentTokens` when calling `get_ohlc_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instrumentTokens' in local_var_params:
            path_params['instrumentTokens'] = local_var_params['instrumentTokens']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quotes/v1.0/ohlc/instruments/{instrumentTokens}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
