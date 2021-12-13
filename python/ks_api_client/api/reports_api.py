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


class ReportsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_fno_order_detail_by_order_id(self, orderId, consumerKey, sessionToken, isFNO, **kwargs):  # noqa: E501
        """Get order report by orderId  # noqa: E501

        Returns the specific order report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fno_order_detail_by_order_id(orderId, consumerKey, sessionToken, isFNO, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param isFNO: (required)
        :type isFNO: str
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
        return self.get_fno_order_detail_by_order_id_with_http_info(orderId, consumerKey, sessionToken, isFNO, **kwargs)  # noqa: E501

    def get_fno_order_detail_by_order_id_with_http_info(self, orderId, consumerKey, sessionToken, isFNO, **kwargs):  # noqa: E501
        """Get order report by orderId  # noqa: E501

        Returns the specific order report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fno_order_detail_by_order_id_with_http_info(orderId, consumerKey, sessionToken, isFNO, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param isFNO: (required)
        :type isFNO: str
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
            'orderId',
            'consumerKey',
            'sessionToken',
            'isFNO'
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
                    " to method get_fno_order_detail_by_order_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'orderId' is set
        if self.api_client.client_side_validation and ('orderId' not in local_var_params or  # noqa: E501
                                                        local_var_params['orderId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `orderId` when calling `get_fno_order_detail_by_order_id`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_fno_order_detail_by_order_id`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_fno_order_detail_by_order_id`")  # noqa: E501
        # verify the required parameter 'isFNO' is set
        if self.api_client.client_side_validation and ('isFNO' not in local_var_params or  # noqa: E501
                                                        local_var_params['isFNO'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `isFNO` when calling `get_fno_order_detail_by_order_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orderId' in local_var_params:
            path_params['orderId'] = local_var_params['orderId']  # noqa: E501
        if 'isFNO' in local_var_params:
            path_params['isFNO'] = local_var_params['isFNO']  # noqa: E501

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
            '/reports/1.0/orders/{orderId}/{isFNO}', 'GET',
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

    def get_order_report_by_order_id(self, orderId, consumerKey, sessionToken, **kwargs):  # noqa: E501
        """Get order report by orderId  # noqa: E501

        Returns the specific order report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_order_report_by_order_id(orderId, consumerKey, sessionToken, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
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
        return self.get_order_report_by_order_id_with_http_info(orderId, consumerKey, sessionToken, **kwargs)  # noqa: E501

    def get_order_report_by_order_id_with_http_info(self, orderId, consumerKey, sessionToken, **kwargs):  # noqa: E501
        """Get order report by orderId  # noqa: E501

        Returns the specific order report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_order_report_by_order_id_with_http_info(orderId, consumerKey, sessionToken, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
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
            'orderId',
            'consumerKey',
            'sessionToken'
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
                    " to method get_order_report_by_order_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'orderId' is set
        if self.api_client.client_side_validation and ('orderId' not in local_var_params or  # noqa: E501
                                                        local_var_params['orderId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `orderId` when calling `get_order_report_by_order_id`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_order_report_by_order_id`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_order_report_by_order_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orderId' in local_var_params:
            path_params['orderId'] = local_var_params['orderId']  # noqa: E501

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
            '/reports/1.0/orders/{orderId}', 'GET',
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

    def get_order_reports(self, consumerKey, sessionToken, **kwargs):  # noqa: E501
        """Get order report  # noqa: E501

        Returns the full order report for a client.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_order_reports(consumerKey, sessionToken, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
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
        return self.get_order_reports_with_http_info(consumerKey, sessionToken, **kwargs)  # noqa: E501

    def get_order_reports_with_http_info(self, consumerKey, sessionToken, **kwargs):  # noqa: E501
        """Get order report  # noqa: E501

        Returns the full order report for a client.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_order_reports_with_http_info(consumerKey, sessionToken, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
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
            'sessionToken'
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
                    " to method get_order_reports" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_order_reports`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_order_reports`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/reports/1.0/orders', 'GET',
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

    def get_trade_report(self, **kwargs):  # noqa: E501
        """Get trade report  # noqa: E501

        Returns the full trade report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_trade_report(async_req=True)
        >>> result = thread.get()

        :param consumerKey: Unique ID for your application
        :type consumerKey: str
        :param sessionToken: Session ID for your application
        :type sessionToken: str
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
        return self.get_trade_report_with_http_info(**kwargs)  # noqa: E501

    def get_trade_report_with_http_info(self, **kwargs):  # noqa: E501
        """Get trade report  # noqa: E501

        Returns the full trade report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_trade_report_with_http_info(async_req=True)
        >>> result = thread.get()

        :param consumerKey: Unique ID for your application
        :type consumerKey: str
        :param sessionToken: Session ID for your application
        :type sessionToken: str
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
            'sessionToken'
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
                    " to method get_trade_report" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/reports/1.0/trades', 'GET',
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

    def get_trade_report_by_order_id(self, orderId, consumerKey, sessionToken, **kwargs):  # noqa: E501
        """Get trade report by orderId  # noqa: E501

        Returns the trade report for a orderId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_trade_report_by_order_id(orderId, consumerKey, sessionToken, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID for your application (required)
        :type sessionToken: str
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
        return self.get_trade_report_by_order_id_with_http_info(orderId, consumerKey, sessionToken, **kwargs)  # noqa: E501

    def get_trade_report_by_order_id_with_http_info(self, orderId, consumerKey, sessionToken, **kwargs):  # noqa: E501
        """Get trade report by orderId  # noqa: E501

        Returns the trade report for a orderId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_trade_report_by_order_id_with_http_info(orderId, consumerKey, sessionToken, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID for your application (required)
        :type sessionToken: str
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
            'orderId',
            'consumerKey',
            'sessionToken'
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
                    " to method get_trade_report_by_order_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'orderId' is set
        if self.api_client.client_side_validation and ('orderId' not in local_var_params or  # noqa: E501
                                                        local_var_params['orderId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `orderId` when calling `get_trade_report_by_order_id`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_trade_report_by_order_id`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_trade_report_by_order_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orderId' in local_var_params:
            path_params['orderId'] = local_var_params['orderId']  # noqa: E501

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
            '/reports/1.0/trades/{orderId}', 'GET',
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

    def get_fno_trade_report_by_order_id(self, orderId, consumerKey, sessionToken, isFNO, **kwargs):  # noqa: E501
        """Get trade report by orderId  # noqa: E501

        Returns the trade report for a orderId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fno_trade_report_by_order_id(orderId, consumerKey, sessionToken, isFNO, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID for your application (required)
        :type sessionToken: str
        :param isFNO: (required)
        :type isFNO: str
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
        return self.get_fno_trade_report_by_order_id_with_http_info(orderId, consumerKey, sessionToken, isFNO, **kwargs)  # noqa: E501

    def get_fno_trade_report_by_order_id_with_http_info(self, orderId, consumerKey, sessionToken, isFNO, **kwargs):  # noqa: E501
        """Get trade report by orderId  # noqa: E501

        Returns the trade report for a orderId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fno_trade_report_by_order_id_with_http_info(orderId, consumerKey, sessionToken, isFNO, async_req=True)
        >>> result = thread.get()

        :param orderId: (required)
        :type orderId: str
        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID for your application (required)
        :type sessionToken: str
        :param isFNO: (required)
        :type isFNO: str
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
            'orderId',
            'consumerKey',
            'sessionToken',
            'isFNO'
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
                    " to method get_fno_trade_report_by_order_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'orderId' is set
        if self.api_client.client_side_validation and ('orderId' not in local_var_params or  # noqa: E501
                                                        local_var_params['orderId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `orderId` when calling `get_trade_report_by_order_id`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `get_trade_report_by_order_id`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `get_trade_report_by_order_id`")  # noqa: E501

        # verify the required parameter 'isFNO' is set
        if self.api_client.client_side_validation and ('isFNO' not in local_var_params or  # noqa: E501
                                                        local_var_params['isFNO'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `isFNO` when calling `get_fno_order_detail_by_order_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orderId' in local_var_params:
            path_params['orderId'] = local_var_params['orderId']  # noqa: E501
        if 'isFNO' in local_var_params:
            path_params['isFNO'] = local_var_params['isFNO']  # noqa: E501

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
            '/reports/1.0/trades/{orderId}/{isFNO}', 'GET',
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
