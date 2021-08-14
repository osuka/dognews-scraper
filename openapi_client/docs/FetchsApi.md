# openapi_client.FetchsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchs_create**](FetchsApi.md#fetchs_create) | **POST** /fetchs | 
[**fetchs_destroy**](FetchsApi.md#fetchs_destroy) | **DELETE** /fetchs/{submission} | 
[**fetchs_list**](FetchsApi.md#fetchs_list) | **GET** /fetchs | 
[**fetchs_partial_update**](FetchsApi.md#fetchs_partial_update) | **PATCH** /fetchs/{submission} | 
[**fetchs_retrieve**](FetchsApi.md#fetchs_retrieve) | **GET** /fetchs/{submission} | 
[**fetchs_update**](FetchsApi.md#fetchs_update) | **PUT** /fetchs/{submission} | 


# **fetchs_create**
> Fetch fetchs_create()



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import fetchs_api
from openapi_client.model.fetch import Fetch
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetchs_api.FetchsApi(api_client)
    fetch = Fetch(
        status=FetchStatusEnum("pending"),
        title="title_example",
        description="description_example",
        thumbnail="thumbnail_example",
        generated_thumbnail="generated_thumbnail_example",
        thumbnail_image="thumbnail_image_example",
        fetched_page="fetched_page_example",
    ) # Fetch |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetchs_create(fetch=fetch)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch** | [**Fetch**](Fetch.md)|  | [optional]

### Return type

[**Fetch**](Fetch.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetchs_destroy**
> fetchs_destroy(submission)



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import fetchs_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetchs_api.FetchsApi(api_client)
    submission = 1 # int | A unique value identifying this fetch.

    # example passing only required values which don't have defaults set
    try:
        api_instance.fetchs_destroy(submission)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this fetch. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetchs_list**
> PaginatedFetchList fetchs_list()



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import fetchs_api
from openapi_client.model.paginated_fetch_list import PaginatedFetchList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetchs_api.FetchsApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    status = "fetched" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetchs_list(limit=limit, offset=offset, ordering=ordering, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **status** | **str**|  | [optional]

### Return type

[**PaginatedFetchList**](PaginatedFetchList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetchs_partial_update**
> Fetch fetchs_partial_update(submission)



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import fetchs_api
from openapi_client.model.fetch import Fetch
from openapi_client.model.patched_fetch import PatchedFetch
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetchs_api.FetchsApi(api_client)
    submission = 1 # int | A unique value identifying this fetch.
    patched_fetch = PatchedFetch(
        status=FetchStatusEnum("pending"),
        title="title_example",
        description="description_example",
        thumbnail="thumbnail_example",
        generated_thumbnail="generated_thumbnail_example",
        thumbnail_image="thumbnail_image_example",
        fetched_page="fetched_page_example",
    ) # PatchedFetch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetchs_partial_update(submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetchs_partial_update(submission, patched_fetch=patched_fetch)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this fetch. |
 **patched_fetch** | [**PatchedFetch**](PatchedFetch.md)|  | [optional]

### Return type

[**Fetch**](Fetch.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetchs_retrieve**
> Fetch fetchs_retrieve(submission)



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import fetchs_api
from openapi_client.model.fetch import Fetch
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetchs_api.FetchsApi(api_client)
    submission = 1 # int | A unique value identifying this fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetchs_retrieve(submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this fetch. |

### Return type

[**Fetch**](Fetch.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetchs_update**
> Fetch fetchs_update(submission)



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import fetchs_api
from openapi_client.model.fetch import Fetch
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetchs_api.FetchsApi(api_client)
    submission = 1 # int | A unique value identifying this fetch.
    fetch = Fetch(
        status=FetchStatusEnum("pending"),
        title="title_example",
        description="description_example",
        thumbnail="thumbnail_example",
        generated_thumbnail="generated_thumbnail_example",
        thumbnail_image="thumbnail_image_example",
        fetched_page="fetched_page_example",
    ) # Fetch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetchs_update(submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetchs_update(submission, fetch=fetch)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FetchsApi->fetchs_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this fetch. |
 **fetch** | [**Fetch**](Fetch.md)|  | [optional]

### Return type

[**Fetch**](Fetch.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

