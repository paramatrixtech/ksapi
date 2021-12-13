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


class SessionApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def generate_session2_fa(self, oneTimeToken, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Generate final Session Token  # noqa: E501

        API to generate final session for user based on one time token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_session2_fa(oneTimeToken, consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param oneTimeToken: (required)
        :type oneTimeToken: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param UserDetails:
        :type UserDetails: UserDetails
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
        return self.generate_session2_fa_with_http_info(oneTimeToken, consumerKey, ip, appId, **kwargs)  # noqa: E501

    def generate_session2_fa_with_http_info(self, oneTimeToken, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Generate final Session Token  # noqa: E501

        API to generate final session for user based on one time token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_session2_fa_with_http_info(oneTimeToken, consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param oneTimeToken: (required)
        :type oneTimeToken: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param UserDetails:
        :type UserDetails: UserDetails
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
            'oneTimeToken',
            'consumerKey',
            'ip',
            'appId',
            'UserDetails'
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
                    " to method generate_session2_fa" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'oneTimeToken' is set
        if self.api_client.client_side_validation and ('oneTimeToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['oneTimeToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `oneTimeToken` when calling `generate_session2_fa`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `generate_session2_fa`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if self.api_client.client_side_validation and ('ip' not in local_var_params or  # noqa: E501
                                                        local_var_params['ip'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ip` when calling `generate_session2_fa`")  # noqa: E501
        # verify the required parameter 'appId' is set
        if self.api_client.client_side_validation and ('appId' not in local_var_params or  # noqa: E501
                                                        local_var_params['appId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `appId` when calling `generate_session2_fa`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'oneTimeToken' in local_var_params:
            header_params['oneTimeToken'] = local_var_params['oneTimeToken']  # noqa: E501
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'ip' in local_var_params:
            header_params['ip'] = local_var_params['ip']  # noqa: E501
        if 'appId' in local_var_params:
            header_params['appId'] = local_var_params['appId']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'UserDetails' in local_var_params:
            body_params = local_var_params['UserDetails']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/session/1.0/session/2FA/accesscode', 'POST',
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

    def generate_session2_fa_ott(self, oneTimeToken, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Generate Final Session Token using One Time Token for Trade API subcribed clients  # noqa: E501

        API to generate final session token for user based on One time token Generated using Login API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_session2_fa_ott(oneTimeToken, consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param oneTimeToken: (required)
        :type oneTimeToken: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param InlineObject:
        :type InlineObject: InlineObject
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
        return self.generate_session2_fa_ott_with_http_info(oneTimeToken, consumerKey, ip, appId, **kwargs)  # noqa: E501

    def generate_session2_fa_ott_with_http_info(self, oneTimeToken, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Generate Final Session Token using One Time Token for Trade API subcribed clients  # noqa: E501

        API to generate final session token for user based on One time token Generated using Login API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_session2_fa_ott_with_http_info(oneTimeToken, consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param oneTimeToken: (required)
        :type oneTimeToken: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param InlineObject:
        :type InlineObject: InlineObject
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
            'oneTimeToken',
            'consumerKey',
            'ip',
            'appId',
            'InlineObject'
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
                    " to method generate_session2_fa_ott" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'oneTimeToken' is set
        if self.api_client.client_side_validation and ('oneTimeToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['oneTimeToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `oneTimeToken` when calling `generate_session2_fa_ott`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `generate_session2_fa_ott`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if self.api_client.client_side_validation and ('ip' not in local_var_params or  # noqa: E501
                                                        local_var_params['ip'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ip` when calling `generate_session2_fa_ott`")  # noqa: E501
        # verify the required parameter 'appId' is set
        if self.api_client.client_side_validation and ('appId' not in local_var_params or  # noqa: E501
                                                        local_var_params['appId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `appId` when calling `generate_session2_fa_ott`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'oneTimeToken' in local_var_params:
            header_params['oneTimeToken'] = local_var_params['oneTimeToken']  # noqa: E501
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'ip' in local_var_params:
            header_params['ip'] = local_var_params['ip']  # noqa: E501
        if 'appId' in local_var_params:
            header_params['appId'] = local_var_params['appId']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'InlineObject' in local_var_params:
            body_params = local_var_params['InlineObject']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501
        return self.api_client.call_api(
            '/session/1.0/session/2FA/oneTimeToken', 'POST',
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

    def login_with_user_id(self, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Login using Userid  # noqa: E501

        Authenticate userid and password to gnerrated one time token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.login_with_user_id(consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param UserCredentials:
        :type UserCredentials: UserCredentials
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
        return self.login_with_user_id_with_http_info(consumerKey, ip, appId, **kwargs)  # noqa: E501

    def login_with_user_id_with_http_info(self, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Login using Userid  # noqa: E501

        Authenticate userid and password to gnerrated one time token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.login_with_user_id_with_http_info(consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param UserCredentials:
        :type UserCredentials: UserCredentials
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
            'ip',
            'appId',
            'UserCredentials'
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
                    " to method login_with_user_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `login_with_user_id`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if self.api_client.client_side_validation and ('ip' not in local_var_params or  # noqa: E501
                                                        local_var_params['ip'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ip` when calling `login_with_user_id`")  # noqa: E501
        # verify the required parameter 'appId' is set
        if self.api_client.client_side_validation and ('appId' not in local_var_params or  # noqa: E501
                                                        local_var_params['appId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `appId` when calling `login_with_user_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'ip' in local_var_params:
            header_params['ip'] = local_var_params['ip']  # noqa: E501
        if 'appId' in local_var_params:
            header_params['appId'] = local_var_params['appId']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'UserCredentials' in local_var_params:
            body_params = local_var_params['UserCredentials']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/session/1.0/session/login/userid', 'POST',
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

    def session_init(self, userid, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Initialise Session  # noqa: E501

        API to initiate trading session for a UserId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.session_init(userid, consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param userid: (required)
        :type userid: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
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
        return self.session_init_with_http_info(userid, consumerKey, ip, appId, **kwargs)  # noqa: E501

    def session_init_with_http_info(self, userid, consumerKey, ip, appId, **kwargs):  # noqa: E501
        """Initialise Session  # noqa: E501

        API to initiate trading session for a UserId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.session_init_with_http_info(userid, consumerKey, ip, appId, async_req=True)
        >>> result = thread.get()

        :param userid: (required)
        :type userid: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
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
            'userid',
            'consumerKey',
            'ip',
            'appId'
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
                    " to method session_init" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'userid' is set
        if self.api_client.client_side_validation and ('userid' not in local_var_params or  # noqa: E501
                                                        local_var_params['userid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `userid` when calling `session_init`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `session_init`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if self.api_client.client_side_validation and ('ip' not in local_var_params or  # noqa: E501
                                                        local_var_params['ip'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ip` when calling `session_init`")  # noqa: E501
        # verify the required parameter 'appId' is set
        if self.api_client.client_side_validation and ('appId' not in local_var_params or  # noqa: E501
                                                        local_var_params['appId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `appId` when calling `session_init`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'userid' in local_var_params:
            header_params['userid'] = local_var_params['userid']  # noqa: E501
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'ip' in local_var_params:
            header_params['ip'] = local_var_params['ip']  # noqa: E501
        if 'appId' in local_var_params:
            header_params['appId'] = local_var_params['appId']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/session/1.0/session/init', 'GET',
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

    def session_logout(self, sessionToken, consumerKey, ip, appId, userid, **kwargs):  # noqa: E501
        """Invalidate Session Token  # noqa: E501

        API to invalidate final session for user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.session_logout(sessionToken, consumerKey, ip, appId, userid, async_req=True)
        >>> result = thread.get()

        :param sessionToken: (required)
        :type sessionToken: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param userid: (required)
        :type userid: str
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
        return self.session_logout_with_http_info(sessionToken, consumerKey, ip, appId, userid, **kwargs)  # noqa: E501

    def session_logout_with_http_info(self, sessionToken, consumerKey, ip, appId, userid, **kwargs):  # noqa: E501
        """Invalidate Session Token  # noqa: E501

        API to invalidate final session for user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.session_logout_with_http_info(sessionToken, consumerKey, ip, appId, userid, async_req=True)
        >>> result = thread.get()

        :param sessionToken: (required)
        :type sessionToken: str
        :param consumerKey: (required)
        :type consumerKey: str
        :param ip: (required)
        :type ip: str
        :param appId: (required)
        :type appId: str
        :param userid: (required)
        :type userid: str
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
            'sessionToken',
            'consumerKey',
            'ip',
            'appId',
            'userid'
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
                    " to method session_logout" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `session_logout`")  # noqa: E501
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `session_logout`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if self.api_client.client_side_validation and ('ip' not in local_var_params or  # noqa: E501
                                                        local_var_params['ip'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ip` when calling `session_logout`")  # noqa: E501
        # verify the required parameter 'appId' is set
        if self.api_client.client_side_validation and ('appId' not in local_var_params or  # noqa: E501
                                                        local_var_params['appId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `appId` when calling `session_logout`")  # noqa: E501
        # verify the required parameter 'userid' is set
        if self.api_client.client_side_validation and ('userid' not in local_var_params or  # noqa: E501
                                                        local_var_params['userid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `userid` when calling `session_logout`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'ip' in local_var_params:
            header_params['ip'] = local_var_params['ip']  # noqa: E501
        if 'appId' in local_var_params:
            header_params['appId'] = local_var_params['appId']  # noqa: E501
        if 'userid' in local_var_params:
            header_params['userid'] = local_var_params['userid']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/session/1.0/session/logout', 'DELETE',
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
