# openapi_client.SubmissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submissions_create**](SubmissionsApi.md#submissions_create) | **POST** /submissions | 
[**submissions_destroy**](SubmissionsApi.md#submissions_destroy) | **DELETE** /submissions/{id} | 
[**submissions_fetch_destroy**](SubmissionsApi.md#submissions_fetch_destroy) | **DELETE** /submissions/{submission_id}/fetch | 
[**submissions_fetch_retrieve**](SubmissionsApi.md#submissions_fetch_retrieve) | **GET** /submissions/{submission_id}/fetch | 
[**submissions_fetch_update**](SubmissionsApi.md#submissions_fetch_update) | **PUT** /submissions/{submission_id}/fetch | 
[**submissions_list**](SubmissionsApi.md#submissions_list) | **GET** /submissions | 
[**submissions_moderation_destroy**](SubmissionsApi.md#submissions_moderation_destroy) | **DELETE** /submissions/{submission_id}/moderation | 
[**submissions_moderation_retrieve**](SubmissionsApi.md#submissions_moderation_retrieve) | **GET** /submissions/{submission_id}/moderation | 
[**submissions_moderation_update**](SubmissionsApi.md#submissions_moderation_update) | **PUT** /submissions/{submission_id}/moderation | 
[**submissions_partial_update**](SubmissionsApi.md#submissions_partial_update) | **PATCH** /submissions/{id} | 
[**submissions_retrieve**](SubmissionsApi.md#submissions_retrieve) | **GET** /submissions/{id} | 
[**submissions_update**](SubmissionsApi.md#submissions_update) | **PUT** /submissions/{id} | 
[**submissions_votes_create**](SubmissionsApi.md#submissions_votes_create) | **POST** /submissions/{submission_id}/votes | 
[**submissions_votes_list**](SubmissionsApi.md#submissions_votes_list) | **GET** /submissions/{submission_id}/votes | 


# **submissions_create**
> Submission submissions_create(submission)



Submitted articles for review  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.submission import Submission
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission = Submission(
        target_url="target_url_example",
        title="title_example",
        description="description_example",
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Submission | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_create(submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission** | [**Submission**](Submission.md)|  |

### Return type

[**Submission**](Submission.md)

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

# **submissions_destroy**
> submissions_destroy(id)



Submitted articles for review  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    id = 1 # int | A unique integer value identifying this submission.

    # example passing only required values which don't have defaults set
    try:
        api_instance.submissions_destroy(id)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this submission. |

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

# **submissions_fetch_destroy**
> submissions_fetch_destroy(submission_id)



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | A unique value identifying this fetch.

    # example passing only required values which don't have defaults set
    try:
        api_instance.submissions_fetch_destroy(submission_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_fetch_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**| A unique value identifying this fetch. |

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

# **submissions_fetch_retrieve**
> Fetch submissions_fetch_retrieve(submission_id)



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | A unique value identifying this fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_fetch_retrieve(submission_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_fetch_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**| A unique value identifying this fetch. |

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

# **submissions_fetch_update**
> Fetch submissions_fetch_update(submission_id)



SFetching results attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | A unique value identifying this fetch.
    fetch = Fetch(
        status=FetchStatusEnum("pending"),
        title="title_example",
        description="description_example",
        thumbnail="thumbnail_example",
        thumbnail_image="thumbnail_image_example",
        fetched_page="fetched_page_example",
    ) # Fetch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_fetch_update(submission_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_fetch_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submissions_fetch_update(submission_id, fetch=fetch)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_fetch_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**| A unique value identifying this fetch. |
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

# **submissions_list**
> PaginatedSubmissionList submissions_list()



Submitted articles for review  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.paginated_submission_list import PaginatedSubmissionList
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    analysis__status = "failed" # str |  (optional)
    analysis__status__isnull = True # bool |  (optional)
    fetch__isnull = True # bool |  (optional)
    fetch__status = "fetched" # str |  (optional)
    fetch__status__isnull = True # bool |  (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    moderation__isnull = True # bool |  (optional)
    moderation__status = "accepted" # str |  (optional)
    moderation__status__isnull = True # bool |  (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    status = "accepted" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submissions_list(analysis__status=analysis__status, analysis__status__isnull=analysis__status__isnull, fetch__isnull=fetch__isnull, fetch__status=fetch__status, fetch__status__isnull=fetch__status__isnull, limit=limit, moderation__isnull=moderation__isnull, moderation__status=moderation__status, moderation__status__isnull=moderation__status__isnull, offset=offset, ordering=ordering, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis__status** | **str**|  | [optional]
 **analysis__status__isnull** | **bool**|  | [optional]
 **fetch__isnull** | **bool**|  | [optional]
 **fetch__status** | **str**|  | [optional]
 **fetch__status__isnull** | **bool**|  | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **moderation__isnull** | **bool**|  | [optional]
 **moderation__status** | **str**|  | [optional]
 **moderation__status__isnull** | **bool**|  | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **status** | **str**|  | [optional]

### Return type

[**PaginatedSubmissionList**](PaginatedSubmissionList.md)

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

# **submissions_moderation_destroy**
> submissions_moderation_destroy(submission_id)



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | A unique value identifying this moderation.

    # example passing only required values which don't have defaults set
    try:
        api_instance.submissions_moderation_destroy(submission_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_moderation_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**| A unique value identifying this moderation. |

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

# **submissions_moderation_retrieve**
> Moderation submissions_moderation_retrieve(submission_id)



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | A unique value identifying this moderation.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_moderation_retrieve(submission_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_moderation_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**| A unique value identifying this moderation. |

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

# **submissions_moderation_update**
> Moderation submissions_moderation_update(submission_id)



Moderation attached to a submission  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | A unique value identifying this moderation.
    moderation = Moderation(
        status=ModerationStatusEnum("pending"),
    ) # Moderation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_moderation_update(submission_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_moderation_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submissions_moderation_update(submission_id, moderation=moderation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_moderation_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**| A unique value identifying this moderation. |
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

# **submissions_partial_update**
> Submission submissions_partial_update(id)



Submitted articles for review  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.submission import Submission
from openapi_client.model.patched_submission import PatchedSubmission
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    id = 1 # int | A unique integer value identifying this submission.
    patched_submission = PatchedSubmission(
        target_url="target_url_example",
        title="title_example",
        description="description_example",
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # PatchedSubmission |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_partial_update(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submissions_partial_update(id, patched_submission=patched_submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this submission. |
 **patched_submission** | [**PatchedSubmission**](PatchedSubmission.md)|  | [optional]

### Return type

[**Submission**](Submission.md)

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

# **submissions_retrieve**
> Submission submissions_retrieve(id)



Submitted articles for review  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.submission import Submission
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    id = 1 # int | A unique integer value identifying this submission.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_retrieve(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this submission. |

### Return type

[**Submission**](Submission.md)

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

# **submissions_update**
> Submission submissions_update(id, submission)



Submitted articles for review  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.submission import Submission
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    id = 1 # int | A unique integer value identifying this submission.
    submission = Submission(
        target_url="target_url_example",
        title="title_example",
        description="description_example",
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Submission | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_update(id, submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this submission. |
 **submission** | [**Submission**](Submission.md)|  |

### Return type

[**Submission**](Submission.md)

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

# **submissions_votes_create**
> Vote submissions_votes_create(submission_id)



Vote management /submissions/(id)/votes (get, post)  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrModeratorOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     * AND if the user is not in the Moderators group     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.vote import Vote
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | 
    vote = Vote(
        value=ValueEnum(1),
    ) # Vote |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_votes_create(submission_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_votes_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submissions_votes_create(submission_id, vote=vote)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_votes_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**|  |
 **vote** | [**Vote**](Vote.md)|  | [optional]

### Return type

[**Vote**](Vote.md)

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

# **submissions_votes_list**
> PaginatedVoteList submissions_votes_list(submission_id)



Vote management /submissions/(id)/votes (get, post)  **Permission restrictions:** + `IsAuthenticated`: *Rejects all operations if the user is not authenticated* + `IsOwnerOrModeratorOrStaff`: *Blocks update/partial_updated/destroy if:     * the user is NOT in the staff group     * AND if the model has a property called 'owner' and its value differs from the request user     * AND if the user is not in the Moderators group     Everything else is allowed* + `DjangoModelPermissions`: *The request is authenticated using `django.contrib.auth` permissions.     See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions      It ensures that the user is authenticated, and has the appropriate     `add`/`change`/`delete` permissions on the model.      This permission can only be applied against view classes that     provide a `.queryset` attribute.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.paginated_vote_list import PaginatedVoteList
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_id = 1 # int | 
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submissions_votes_list(submission_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_votes_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submissions_votes_list(submission_id, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionsApi->submissions_votes_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedVoteList**](PaginatedVoteList.md)

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

