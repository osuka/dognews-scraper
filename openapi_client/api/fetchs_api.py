"""
    Dognews Server API

    Dognews Server client API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.fetch import Fetch
from openapi_client.model.paginated_fetch_list import PaginatedFetchList
from openapi_client.model.patched_fetch import PatchedFetch


class FetchsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __fetchs_create(
            self,
            **kwargs
        ):
            """fetchs_create  # noqa: E501

            SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetchs_create(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                fetch (Fetch): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Fetch
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.fetchs_create = _Endpoint(
            settings={
                'response_type': (Fetch,),
                'auth': [
                    'basicAuth',
                    'cookieAuth',
                    'jwtAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/fetchs',
                'operation_id': 'fetchs_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'fetch',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'fetch':
                        (Fetch,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'fetch': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__fetchs_create
        )

        def __fetchs_destroy(
            self,
            submission,
            **kwargs
        ):
            """fetchs_destroy  # noqa: E501

            SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetchs_destroy(submission, async_req=True)
            >>> result = thread.get()

            Args:
                submission (int): A unique value identifying this fetch.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['submission'] = \
                submission
            return self.call_with_http_info(**kwargs)

        self.fetchs_destroy = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth',
                    'cookieAuth',
                    'jwtAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/fetchs/{submission}',
                'operation_id': 'fetchs_destroy',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'submission',
                ],
                'required': [
                    'submission',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'submission':
                        (int,),
                },
                'attribute_map': {
                    'submission': 'submission',
                },
                'location_map': {
                    'submission': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetchs_destroy
        )

        def __fetchs_list(
            self,
            **kwargs
        ):
            """fetchs_list  # noqa: E501

            SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetchs_list(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): Number of results to return per page.. [optional]
                offset (int): The initial index from which to return the results.. [optional]
                ordering (str): Which field to use when ordering the results.. [optional]
                status (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaginatedFetchList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.fetchs_list = _Endpoint(
            settings={
                'response_type': (PaginatedFetchList,),
                'auth': [
                    'basicAuth',
                    'cookieAuth',
                    'jwtAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/fetchs',
                'operation_id': 'fetchs_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'offset',
                    'ordering',
                    'status',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'status',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('status',): {

                        "FETCHED": "fetched",
                        "PENDING": "pending",
                        "REJ_ERROR": "rej_error",
                        "REJ_FETCH": "rej_fetch"
                    },
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'ordering':
                        (str,),
                    'status':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'offset': 'offset',
                    'ordering': 'ordering',
                    'status': 'status',
                },
                'location_map': {
                    'limit': 'query',
                    'offset': 'query',
                    'ordering': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetchs_list
        )

        def __fetchs_partial_update(
            self,
            submission,
            **kwargs
        ):
            """fetchs_partial_update  # noqa: E501

            SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetchs_partial_update(submission, async_req=True)
            >>> result = thread.get()

            Args:
                submission (int): A unique value identifying this fetch.

            Keyword Args:
                patched_fetch (PatchedFetch): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Fetch
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['submission'] = \
                submission
            return self.call_with_http_info(**kwargs)

        self.fetchs_partial_update = _Endpoint(
            settings={
                'response_type': (Fetch,),
                'auth': [
                    'basicAuth',
                    'cookieAuth',
                    'jwtAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/fetchs/{submission}',
                'operation_id': 'fetchs_partial_update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'submission',
                    'patched_fetch',
                ],
                'required': [
                    'submission',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'submission':
                        (int,),
                    'patched_fetch':
                        (PatchedFetch,),
                },
                'attribute_map': {
                    'submission': 'submission',
                },
                'location_map': {
                    'submission': 'path',
                    'patched_fetch': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__fetchs_partial_update
        )

        def __fetchs_retrieve(
            self,
            submission,
            **kwargs
        ):
            """fetchs_retrieve  # noqa: E501

            SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetchs_retrieve(submission, async_req=True)
            >>> result = thread.get()

            Args:
                submission (int): A unique value identifying this fetch.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Fetch
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['submission'] = \
                submission
            return self.call_with_http_info(**kwargs)

        self.fetchs_retrieve = _Endpoint(
            settings={
                'response_type': (Fetch,),
                'auth': [
                    'basicAuth',
                    'cookieAuth',
                    'jwtAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/fetchs/{submission}',
                'operation_id': 'fetchs_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'submission',
                ],
                'required': [
                    'submission',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'submission':
                        (int,),
                },
                'attribute_map': {
                    'submission': 'submission',
                },
                'location_map': {
                    'submission': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetchs_retrieve
        )

        def __fetchs_update(
            self,
            submission,
            **kwargs
        ):
            """fetchs_update  # noqa: E501

            SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetchs_update(submission, async_req=True)
            >>> result = thread.get()

            Args:
                submission (int): A unique value identifying this fetch.

            Keyword Args:
                fetch (Fetch): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Fetch
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['submission'] = \
                submission
            return self.call_with_http_info(**kwargs)

        self.fetchs_update = _Endpoint(
            settings={
                'response_type': (Fetch,),
                'auth': [
                    'basicAuth',
                    'cookieAuth',
                    'jwtAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/fetchs/{submission}',
                'operation_id': 'fetchs_update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'submission',
                    'fetch',
                ],
                'required': [
                    'submission',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'submission':
                        (int,),
                    'fetch':
                        (Fetch,),
                },
                'attribute_map': {
                    'submission': 'submission',
                },
                'location_map': {
                    'submission': 'path',
                    'fetch': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__fetchs_update
        )
