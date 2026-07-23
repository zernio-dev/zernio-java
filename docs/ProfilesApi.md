# ProfilesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProfile**](ProfilesApi.md#createProfile) | **POST** /v1/profiles | Create profile |
| [**createProfileWithHttpInfo**](ProfilesApi.md#createProfileWithHttpInfo) | **POST** /v1/profiles | Create profile |
| [**deleteProfile**](ProfilesApi.md#deleteProfile) | **DELETE** /v1/profiles/{profileId} | Delete profile |
| [**deleteProfileWithHttpInfo**](ProfilesApi.md#deleteProfileWithHttpInfo) | **DELETE** /v1/profiles/{profileId} | Delete profile |
| [**getProfile**](ProfilesApi.md#getProfile) | **GET** /v1/profiles/{profileId} | Get profile |
| [**getProfileWithHttpInfo**](ProfilesApi.md#getProfileWithHttpInfo) | **GET** /v1/profiles/{profileId} | Get profile |
| [**listProfiles**](ProfilesApi.md#listProfiles) | **GET** /v1/profiles | List profiles |
| [**listProfilesWithHttpInfo**](ProfilesApi.md#listProfilesWithHttpInfo) | **GET** /v1/profiles | List profiles |
| [**updateProfile**](ProfilesApi.md#updateProfile) | **PUT** /v1/profiles/{profileId} | Update profile |
| [**updateProfileWithHttpInfo**](ProfilesApi.md#updateProfileWithHttpInfo) | **PUT** /v1/profiles/{profileId} | Update profile |



## createProfile

> ProfileCreateResponse createProfile(createProfileRequest, idempotencyKey)

Create profile

Creates a new profile with a name, optional description, and color. Names are unique per workspace: a duplicate returns a 409 whose details.existingProfileId carries the id of the existing profile. Send an Idempotency-Key header to make retries safe: a retried create with the same key and body replays the original 201 (same _id) instead of conflicting.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        CreateProfileRequest createProfileRequest = new CreateProfileRequest(); // CreateProfileRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ProfileCreateResponse result = apiInstance.createProfile(createProfileRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#createProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createProfileRequest** | [**CreateProfileRequest**](CreateProfileRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**ProfileCreateResponse**](ProfileCreateResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Profile limit exceeded |  -  |
| **409** | A profile with this name already exists (code: profile_name_conflict); details.existingProfileId carries the id of the existing profile. Also returned while a request with the same Idempotency-Key is still processing. |  -  |
| **422** | Idempotency-Key reused with a different body |  -  |

## createProfileWithHttpInfo

> ApiResponse<ProfileCreateResponse> createProfile createProfileWithHttpInfo(createProfileRequest, idempotencyKey)

Create profile

Creates a new profile with a name, optional description, and color. Names are unique per workspace: a duplicate returns a 409 whose details.existingProfileId carries the id of the existing profile. Send an Idempotency-Key header to make retries safe: a retried create with the same key and body replays the original 201 (same _id) instead of conflicting.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        CreateProfileRequest createProfileRequest = new CreateProfileRequest(); // CreateProfileRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<ProfileCreateResponse> response = apiInstance.createProfileWithHttpInfo(createProfileRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#createProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createProfileRequest** | [**CreateProfileRequest**](CreateProfileRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**ProfileCreateResponse**](ProfileCreateResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Profile limit exceeded |  -  |
| **409** | A profile with this name already exists (code: profile_name_conflict); details.existingProfileId carries the id of the existing profile. Also returned while a request with the same Idempotency-Key is still processing. |  -  |
| **422** | Idempotency-Key reused with a different body |  -  |


## deleteProfile

> ProfileDeleteResponse deleteProfile(profileId)

Delete profile

Permanently deletes a profile. Active connected accounts block deletion (returns 400) - disconnect them first. Any remaining disconnected accounts and provisioned WhatsApp numbers are moved to another of your profiles (a new one is created only if needed), never deleted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        try {
            ProfileDeleteResponse result = apiInstance.deleteProfile(profileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#deleteProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | **String**|  | |

### Return type

[**ProfileDeleteResponse**](ProfileDeleteResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Profile has active connected accounts; disconnect them first |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

## deleteProfileWithHttpInfo

> ApiResponse<ProfileDeleteResponse> deleteProfile deleteProfileWithHttpInfo(profileId)

Delete profile

Permanently deletes a profile. Active connected accounts block deletion (returns 400) - disconnect them first. Any remaining disconnected accounts and provisioned WhatsApp numbers are moved to another of your profiles (a new one is created only if needed), never deleted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        try {
            ApiResponse<ProfileDeleteResponse> response = apiInstance.deleteProfileWithHttpInfo(profileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#deleteProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | **String**|  | |

### Return type

ApiResponse<[**ProfileDeleteResponse**](ProfileDeleteResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Profile has active connected accounts; disconnect them first |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |


## getProfile

> ProfileGetResponse getProfile(profileId)

Get profile

Returns a single profile by ID, including its name, color, and default status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        try {
            ProfileGetResponse result = apiInstance.getProfile(profileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#getProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | **String**|  | |

### Return type

[**ProfileGetResponse**](ProfileGetResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getProfileWithHttpInfo

> ApiResponse<ProfileGetResponse> getProfile getProfileWithHttpInfo(profileId)

Get profile

Returns a single profile by ID, including its name, color, and default status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        try {
            ApiResponse<ProfileGetResponse> response = apiInstance.getProfileWithHttpInfo(profileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#getProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | **String**|  | |

### Return type

ApiResponse<[**ProfileGetResponse**](ProfileGetResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## listProfiles

> ProfilesListResponse listProfiles(includeOverLimit, name, limit, skip)

List profiles

Returns profiles sorted default-first, then by creation date. Filter with name (exact match) and paginate with limit/skip; without those params the full list is returned unchanged. Use includeOverLimit&#x3D;true to include profiles that exceed the plan limit.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        Boolean includeOverLimit = false; // Boolean | When true, includes over-limit profiles (marked with isOverLimit: true).
        String name = "name_example"; // String | Exact-match filter on the profile name. Useful to recover a profile id after an ambiguous create (timeout followed by a 409 on retry).
        Integer limit = 56; // Integer | Page size. When limit or skip is present, the response includes total and skip (and echoes limit).
        Integer skip = 56; // Integer | Number of profiles to skip, applied after sorting and filtering.
        try {
            ProfilesListResponse result = apiInstance.listProfiles(includeOverLimit, name, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#listProfiles");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **includeOverLimit** | **Boolean**| When true, includes over-limit profiles (marked with isOverLimit: true). | [optional] [default to false] |
| **name** | **String**| Exact-match filter on the profile name. Useful to recover a profile id after an ambiguous create (timeout followed by a 409 on retry). | [optional] |
| **limit** | **Integer**| Page size. When limit or skip is present, the response includes total and skip (and echoes limit). | [optional] |
| **skip** | **Integer**| Number of profiles to skip, applied after sorting and filtering. | [optional] |

### Return type

[**ProfilesListResponse**](ProfilesListResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profiles |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## listProfilesWithHttpInfo

> ApiResponse<ProfilesListResponse> listProfiles listProfilesWithHttpInfo(includeOverLimit, name, limit, skip)

List profiles

Returns profiles sorted default-first, then by creation date. Filter with name (exact match) and paginate with limit/skip; without those params the full list is returned unchanged. Use includeOverLimit&#x3D;true to include profiles that exceed the plan limit.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        Boolean includeOverLimit = false; // Boolean | When true, includes over-limit profiles (marked with isOverLimit: true).
        String name = "name_example"; // String | Exact-match filter on the profile name. Useful to recover a profile id after an ambiguous create (timeout followed by a 409 on retry).
        Integer limit = 56; // Integer | Page size. When limit or skip is present, the response includes total and skip (and echoes limit).
        Integer skip = 56; // Integer | Number of profiles to skip, applied after sorting and filtering.
        try {
            ApiResponse<ProfilesListResponse> response = apiInstance.listProfilesWithHttpInfo(includeOverLimit, name, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#listProfiles");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **includeOverLimit** | **Boolean**| When true, includes over-limit profiles (marked with isOverLimit: true). | [optional] [default to false] |
| **name** | **String**| Exact-match filter on the profile name. Useful to recover a profile id after an ambiguous create (timeout followed by a 409 on retry). | [optional] |
| **limit** | **Integer**| Page size. When limit or skip is present, the response includes total and skip (and echoes limit). | [optional] |
| **skip** | **Integer**| Number of profiles to skip, applied after sorting and filtering. | [optional] |

### Return type

ApiResponse<[**ProfilesListResponse**](ProfilesListResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profiles |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## updateProfile

> ProfileUpdateResponse updateProfile(profileId, updateProfileRequest)

Update profile

Updates a profile&#39;s name, description, color, or default status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        UpdateProfileRequest updateProfileRequest = new UpdateProfileRequest(); // UpdateProfileRequest | 
        try {
            ProfileUpdateResponse result = apiInstance.updateProfile(profileId, updateProfileRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#updateProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | **String**|  | |
| **updateProfileRequest** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | |

### Return type

[**ProfileUpdateResponse**](ProfileUpdateResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **409** | A profile with this name already exists (code: profile_name_conflict). |  -  |

## updateProfileWithHttpInfo

> ApiResponse<ProfileUpdateResponse> updateProfile updateProfileWithHttpInfo(profileId, updateProfileRequest)

Update profile

Updates a profile&#39;s name, description, color, or default status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProfilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProfilesApi apiInstance = new ProfilesApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        UpdateProfileRequest updateProfileRequest = new UpdateProfileRequest(); // UpdateProfileRequest | 
        try {
            ApiResponse<ProfileUpdateResponse> response = apiInstance.updateProfileWithHttpInfo(profileId, updateProfileRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProfilesApi#updateProfile");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | **String**|  | |
| **updateProfileRequest** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | |

### Return type

ApiResponse<[**ProfileUpdateResponse**](ProfileUpdateResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **409** | A profile with this name already exists (code: profile_name_conflict). |  -  |

