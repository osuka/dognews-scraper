# openapi_client.ApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_schema_retrieve**](ApiApi.md#api_schema_retrieve) | **GET** /api/schema/ | 
[**api_token_create**](ApiApi.md#api_token_create) | **POST** /api/token/ | 
[**api_token_refresh_create**](ApiApi.md#api_token_refresh_create) | **POST** /api/token/refresh/ | 
[**api_token_verify_create**](ApiApi.md#api_token_verify_create) | **POST** /api/token/verify/ | 


# **api_schema_retrieve**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} api_schema_retrieve()



OpenApi3 schema for this API. Format can be selected via content negotiation.  - YAML: application/vnd.oai.openapi - JSON: application/vnd.oai.openapi+json  **Permission restrictions:** + `AllowAny`: *Allow any access.     This isn't strictly required, since you could use an empty     permission_classes list, but it's useful because it makes the intention     more explicit.*

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):
* Api Key Authentication (tokenAuth):
```python
import time
import openapi_client
from openapi_client.api import api_api
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
    api_instance = api_api.ApiApi(api_client)
    format = "json" # str |  (optional)
    lang = "af" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_schema_retrieve(format=format, lang=lang)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApiApi->api_schema_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional]
 **lang** | **str**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.oai.openapi, application/yaml, application/vnd.oai.openapi+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_create**
> TokenObtainPair api_token_create(token_obtain_pair)



Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Example

```python
import time
import openapi_client
from openapi_client.api import api_api
from openapi_client.model.token_obtain_pair import TokenObtainPair
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    token_obtain_pair = TokenObtainPair(
        username="username_example",
        password="password_example",
    ) # TokenObtainPair | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_token_create(token_obtain_pair)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApiApi->api_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_obtain_pair** | [**TokenObtainPair**](TokenObtainPair.md)|  |

### Return type

[**TokenObtainPair**](TokenObtainPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_refresh_create**
> TokenRefresh api_token_refresh_create(token_refresh)



Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Example

```python
import time
import openapi_client
from openapi_client.api import api_api
from openapi_client.model.token_refresh import TokenRefresh
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    token_refresh = TokenRefresh(
        refresh="refresh_example",
    ) # TokenRefresh | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_token_refresh_create(token_refresh)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApiApi->api_token_refresh_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_refresh** | [**TokenRefresh**](TokenRefresh.md)|  |

### Return type

[**TokenRefresh**](TokenRefresh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_verify_create**
> TokenVerify api_token_verify_create(token_verify)



Takes a token and indicates if it is valid.  This view provides no information about a token's fitness for a particular use.

### Example

```python
import time
import openapi_client
from openapi_client.api import api_api
from openapi_client.model.token_verify import TokenVerify
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    token_verify = TokenVerify(
        token="token_example",
    ) # TokenVerify | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_token_verify_create(token_verify)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApiApi->api_token_verify_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_verify** | [**TokenVerify**](TokenVerify.md)|  |

### Return type

[**TokenVerify**](TokenVerify.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

