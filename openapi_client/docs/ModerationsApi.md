# openapi_client.ModerationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**moderations_create**](ModerationsApi.md#moderations_create) | **POST** /moderations | 
[**moderations_destroy**](ModerationsApi.md#moderations_destroy) | **DELETE** /moderations/{submission} | 
[**moderations_list**](ModerationsApi.md#moderations_list) | **GET** /moderations | 
[**moderations_partial_update**](ModerationsApi.md#moderations_partial_update) | **PATCH** /moderations/{submission} | 
[**moderations_retrieve**](ModerationsApi.md#moderations_retrieve) | **GET** /moderations/{submission} | 
[**moderations_update**](ModerationsApi.md#moderations_update) | **PUT** /moderations/{submission} | 


# **moderations_create**
> Moderation moderations_create()



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import moderations_api
from openapi_client.model.moderation import Moderation
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
    api_instance = moderations_api.ModerationsApi(api_client)
    moderation = Moderation(
        status=ModerationStatusEnum("pending"),
    ) # Moderation |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.moderations_create(moderation=moderation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moderation** | [**Moderation**](Moderation.md)|  | [optional]

### Return type

[**Moderation**](Moderation.md)

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

# **moderations_destroy**
> moderations_destroy(submission)



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import moderations_api
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
    api_instance = moderations_api.ModerationsApi(api_client)
    submission = 1 # int | A unique value identifying this moderation.

    # example passing only required values which don't have defaults set
    try:
        api_instance.moderations_destroy(submission)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this moderation. |

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

# **moderations_list**
> PaginatedModerationList moderations_list()



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import moderations_api
from openapi_client.model.paginated_moderation_list import PaginatedModerationList
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
    api_instance = moderations_api.ModerationsApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    status = "accepted" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.moderations_list(limit=limit, offset=offset, ordering=ordering, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **status** | **str**|  | [optional]

### Return type

[**PaginatedModerationList**](PaginatedModerationList.md)

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

# **moderations_partial_update**
> Moderation moderations_partial_update(submission)



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import moderations_api
from openapi_client.model.patched_moderation import PatchedModeration
from openapi_client.model.moderation import Moderation
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
    api_instance = moderations_api.ModerationsApi(api_client)
    submission = 1 # int | A unique value identifying this moderation.
    patched_moderation = PatchedModeration(
        status=ModerationStatusEnum("pending"),
    ) # PatchedModeration |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.moderations_partial_update(submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.moderations_partial_update(submission, patched_moderation=patched_moderation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this moderation. |
 **patched_moderation** | [**PatchedModeration**](PatchedModeration.md)|  | [optional]

### Return type

[**Moderation**](Moderation.md)

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

# **moderations_retrieve**
> Moderation moderations_retrieve(submission)



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import moderations_api
from openapi_client.model.moderation import Moderation
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
    api_instance = moderations_api.ModerationsApi(api_client)
    submission = 1 # int | A unique value identifying this moderation.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.moderations_retrieve(submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this moderation. |

### Return type

[**Moderation**](Moderation.md)

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

# **moderations_update**
> Moderation moderations_update(submission)



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import moderations_api
from openapi_client.model.moderation import Moderation
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
    api_instance = moderations_api.ModerationsApi(api_client)
    submission = 1 # int | A unique value identifying this moderation.
    moderation = Moderation(
        status=ModerationStatusEnum("pending"),
    ) # Moderation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.moderations_update(submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.moderations_update(submission, moderation=moderation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModerationsApi->moderations_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | **int**| A unique value identifying this moderation. |
 **moderation** | [**Moderation**](Moderation.md)|  | [optional]

### Return type

[**Moderation**](Moderation.md)

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

