# CalendarApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarAvailability**](CalendarApi.md#calendarAvailability) | **POST** /v1/calendar/availability | Find meeting slots across accounts |
| [**calendarAvailabilityWithHttpInfo**](CalendarApi.md#calendarAvailabilityWithHttpInfo) | **POST** /v1/calendar/availability | Find meeting slots across accounts |
| [**calendarFreeBusy**](CalendarApi.md#calendarFreeBusy) | **POST** /v1/calendar/free-busy | Busy blocks for one or more accounts |
| [**calendarFreeBusyWithHttpInfo**](CalendarApi.md#calendarFreeBusyWithHttpInfo) | **POST** /v1/calendar/free-busy | Busy blocks for one or more accounts |
| [**createCalendarEvent**](CalendarApi.md#createCalendarEvent) | **POST** /v1/calendar/events | Create an event |
| [**createCalendarEventWithHttpInfo**](CalendarApi.md#createCalendarEventWithHttpInfo) | **POST** /v1/calendar/events | Create an event |
| [**deleteCalendarEvent**](CalendarApi.md#deleteCalendarEvent) | **DELETE** /v1/calendar/events/{eventId} | Delete an event |
| [**deleteCalendarEventWithHttpInfo**](CalendarApi.md#deleteCalendarEventWithHttpInfo) | **DELETE** /v1/calendar/events/{eventId} | Delete an event |
| [**getCalendarEvent**](CalendarApi.md#getCalendarEvent) | **GET** /v1/calendar/events/{eventId} | Get an event |
| [**getCalendarEventWithHttpInfo**](CalendarApi.md#getCalendarEventWithHttpInfo) | **GET** /v1/calendar/events/{eventId} | Get an event |
| [**listCalendarEvents**](CalendarApi.md#listCalendarEvents) | **GET** /v1/calendar/events | List events in a window |
| [**listCalendarEventsWithHttpInfo**](CalendarApi.md#listCalendarEventsWithHttpInfo) | **GET** /v1/calendar/events | List events in a window |
| [**listCalendars**](CalendarApi.md#listCalendars) | **GET** /v1/calendar/calendars | List calendars |
| [**listCalendarsWithHttpInfo**](CalendarApi.md#listCalendarsWithHttpInfo) | **GET** /v1/calendar/calendars | List calendars |
| [**rsvpCalendarEvent**](CalendarApi.md#rsvpCalendarEvent) | **POST** /v1/calendar/events/{eventId}/rsvp | Respond to an invitation |
| [**rsvpCalendarEventWithHttpInfo**](CalendarApi.md#rsvpCalendarEventWithHttpInfo) | **POST** /v1/calendar/events/{eventId}/rsvp | Respond to an invitation |
| [**updateCalendarEvent**](CalendarApi.md#updateCalendarEvent) | **PATCH** /v1/calendar/events/{eventId} | Update an event |
| [**updateCalendarEventWithHttpInfo**](CalendarApi.md#updateCalendarEventWithHttpInfo) | **PATCH** /v1/calendar/events/{eventId} | Update an event |



## calendarAvailability

> CalendarAvailability200Response calendarAvailability(calendarAvailabilityRequest)

Find meeting slots across accounts

Slots of &#x60;durationMinutes&#x60; every &#x60;intervalMinutes&#x60; between &#x60;from&#x60; and &#x60;to&#x60; that are free for every participant (&#x60;collective&#x60;) or for at least one (&#x60;max_availability&#x60;). Buffers pad the participants&#39; existing meetings. Open hours are evaluated in each participant&#39;s own timezone; &#x60;defaultOpenHours&#x60; applies to participants without their own.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        CalendarAvailabilityRequest calendarAvailabilityRequest = new CalendarAvailabilityRequest(); // CalendarAvailabilityRequest | 
        try {
            CalendarAvailability200Response result = apiInstance.calendarAvailability(calendarAvailabilityRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#calendarAvailability");
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
| **calendarAvailabilityRequest** | [**CalendarAvailabilityRequest**](CalendarAvailabilityRequest.md)|  | |

### Return type

[**CalendarAvailability200Response**](CalendarAvailability200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Candidate slots |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## calendarAvailabilityWithHttpInfo

> ApiResponse<CalendarAvailability200Response> calendarAvailability calendarAvailabilityWithHttpInfo(calendarAvailabilityRequest)

Find meeting slots across accounts

Slots of &#x60;durationMinutes&#x60; every &#x60;intervalMinutes&#x60; between &#x60;from&#x60; and &#x60;to&#x60; that are free for every participant (&#x60;collective&#x60;) or for at least one (&#x60;max_availability&#x60;). Buffers pad the participants&#39; existing meetings. Open hours are evaluated in each participant&#39;s own timezone; &#x60;defaultOpenHours&#x60; applies to participants without their own.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        CalendarAvailabilityRequest calendarAvailabilityRequest = new CalendarAvailabilityRequest(); // CalendarAvailabilityRequest | 
        try {
            ApiResponse<CalendarAvailability200Response> response = apiInstance.calendarAvailabilityWithHttpInfo(calendarAvailabilityRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#calendarAvailability");
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
| **calendarAvailabilityRequest** | [**CalendarAvailabilityRequest**](CalendarAvailabilityRequest.md)|  | |

### Return type

ApiResponse<[**CalendarAvailability200Response**](CalendarAvailability200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Candidate slots |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## calendarFreeBusy

> CalendarFreeBusy200Response calendarFreeBusy(calendarFreeBusyRequest)

Busy blocks for one or more accounts

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        CalendarFreeBusyRequest calendarFreeBusyRequest = new CalendarFreeBusyRequest(); // CalendarFreeBusyRequest | 
        try {
            CalendarFreeBusy200Response result = apiInstance.calendarFreeBusy(calendarFreeBusyRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#calendarFreeBusy");
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
| **calendarFreeBusyRequest** | [**CalendarFreeBusyRequest**](CalendarFreeBusyRequest.md)|  | |

### Return type

[**CalendarFreeBusy200Response**](CalendarFreeBusy200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One entry per account, busy blocks in UTC |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## calendarFreeBusyWithHttpInfo

> ApiResponse<CalendarFreeBusy200Response> calendarFreeBusy calendarFreeBusyWithHttpInfo(calendarFreeBusyRequest)

Busy blocks for one or more accounts

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        CalendarFreeBusyRequest calendarFreeBusyRequest = new CalendarFreeBusyRequest(); // CalendarFreeBusyRequest | 
        try {
            ApiResponse<CalendarFreeBusy200Response> response = apiInstance.calendarFreeBusyWithHttpInfo(calendarFreeBusyRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#calendarFreeBusy");
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
| **calendarFreeBusyRequest** | [**CalendarFreeBusyRequest**](CalendarFreeBusyRequest.md)|  | |

### Return type

ApiResponse<[**CalendarFreeBusy200Response**](CalendarFreeBusy200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One entry per account, busy blocks in UTC |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## createCalendarEvent

> CreateCalendarEvent201Response createCalendarEvent(createCalendarEventRequest)

Create an event

&#x60;conferencing: teams&#x60; adds a Teams meeting on Microsoft accounts; the created event comes back with &#x60;conferencing: null&#x60; when the tenant has no Teams (the EEA Business Basic SKUs ship without it). &#x60;google_meet&#x60; is rejected there with 400 (&#x60;param: conferencing&#x60;). On Google accounts &#x60;conferencing: google_meet&#x60; adds a Meet link, &#x60;teams&#x60; is rejected with 400, and &#x60;recurrence&#x60; accepts any RRULE Google Calendar supports. &#x60;recurrence&#x60; takes one RRULE line with FREQ, INTERVAL, COUNT, UNTIL, BYDAY and BYSETPOS; other parts are rejected with 400 (&#x60;param: recurrence&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        CreateCalendarEventRequest createCalendarEventRequest = new CreateCalendarEventRequest(); // CreateCalendarEventRequest | 
        try {
            CreateCalendarEvent201Response result = apiInstance.createCalendarEvent(createCalendarEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#createCalendarEvent");
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
| **createCalendarEventRequest** | [**CreateCalendarEventRequest**](CreateCalendarEventRequest.md)|  | |

### Return type

[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created event |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## createCalendarEventWithHttpInfo

> ApiResponse<CreateCalendarEvent201Response> createCalendarEvent createCalendarEventWithHttpInfo(createCalendarEventRequest)

Create an event

&#x60;conferencing: teams&#x60; adds a Teams meeting on Microsoft accounts; the created event comes back with &#x60;conferencing: null&#x60; when the tenant has no Teams (the EEA Business Basic SKUs ship without it). &#x60;google_meet&#x60; is rejected there with 400 (&#x60;param: conferencing&#x60;). On Google accounts &#x60;conferencing: google_meet&#x60; adds a Meet link, &#x60;teams&#x60; is rejected with 400, and &#x60;recurrence&#x60; accepts any RRULE Google Calendar supports. &#x60;recurrence&#x60; takes one RRULE line with FREQ, INTERVAL, COUNT, UNTIL, BYDAY and BYSETPOS; other parts are rejected with 400 (&#x60;param: recurrence&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        CreateCalendarEventRequest createCalendarEventRequest = new CreateCalendarEventRequest(); // CreateCalendarEventRequest | 
        try {
            ApiResponse<CreateCalendarEvent201Response> response = apiInstance.createCalendarEventWithHttpInfo(createCalendarEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#createCalendarEvent");
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
| **createCalendarEventRequest** | [**CreateCalendarEventRequest**](CreateCalendarEventRequest.md)|  | |

### Return type

ApiResponse<[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created event |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## deleteCalendarEvent

> DeleteCalendarEvent200Response deleteCalendarEvent(eventId, accountId, calendarId)

Delete an event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String calendarId = "calendarId_example"; // String | The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar.
        try {
            DeleteCalendarEvent200Response result = apiInstance.deleteCalendarEvent(eventId, accountId, calendarId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#deleteCalendarEvent");
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
| **eventId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **calendarId** | **String**| The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar. | [optional] |

### Return type

[**DeleteCalendarEvent200Response**](DeleteCalendarEvent200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## deleteCalendarEventWithHttpInfo

> ApiResponse<DeleteCalendarEvent200Response> deleteCalendarEvent deleteCalendarEventWithHttpInfo(eventId, accountId, calendarId)

Delete an event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String calendarId = "calendarId_example"; // String | The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar.
        try {
            ApiResponse<DeleteCalendarEvent200Response> response = apiInstance.deleteCalendarEventWithHttpInfo(eventId, accountId, calendarId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#deleteCalendarEvent");
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
| **eventId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **calendarId** | **String**| The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar. | [optional] |

### Return type

ApiResponse<[**DeleteCalendarEvent200Response**](DeleteCalendarEvent200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## getCalendarEvent

> CreateCalendarEvent201Response getCalendarEvent(eventId, accountId, calendarId, timezone)

Get an event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String calendarId = "calendarId_example"; // String | The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar.
        String timezone = "timezone_example"; // String | 
        try {
            CreateCalendarEvent201Response result = apiInstance.getCalendarEvent(eventId, accountId, calendarId, timezone);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#getCalendarEvent");
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
| **eventId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **calendarId** | **String**| The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar. | [optional] |
| **timezone** | **String**|  | [optional] |

### Return type

[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The event |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## getCalendarEventWithHttpInfo

> ApiResponse<CreateCalendarEvent201Response> getCalendarEvent getCalendarEventWithHttpInfo(eventId, accountId, calendarId, timezone)

Get an event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String calendarId = "calendarId_example"; // String | The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar.
        String timezone = "timezone_example"; // String | 
        try {
            ApiResponse<CreateCalendarEvent201Response> response = apiInstance.getCalendarEventWithHttpInfo(eventId, accountId, calendarId, timezone);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#getCalendarEvent");
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
| **eventId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **calendarId** | **String**| The calendar holding the event (an id from GET /v1/calendar/calendars). Defaults to the primary calendar. | [optional] |
| **timezone** | **String**|  | [optional] |

### Return type

ApiResponse<[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The event |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## listCalendarEvents

> ListCalendarEvents200Response listCalendarEvents(accountId, from, to, calendarId, title, location, showCancelled, expandRecurring, icalUid, sortOrder, cursor, limit, timezone)

List events in a window

Recurring series are expanded into their occurrences inside the window by default (&#x60;expandRecurring&#x3D;false&#x60; lists the masters instead). &#x60;title&#x60; and &#x60;location&#x60; are substring matches applied to the fetched page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | 
        String calendarId = "calendarId_example"; // String | Defaults to the primary calendar.
        String title = "title_example"; // String | 
        String location = "location_example"; // String | 
        Boolean showCancelled = false; // Boolean | 
        Boolean expandRecurring = true; // Boolean | 
        String icalUid = "icalUid_example"; // String | 
        String sortOrder = "asc"; // String | 
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        String timezone = "timezone_example"; // String | IANA zone the `start` and `end` offsets are rendered in. Default UTC.
        try {
            ListCalendarEvents200Response result = apiInstance.listCalendarEvents(accountId, from, to, calendarId, title, location, showCancelled, expandRecurring, icalUid, sortOrder, cursor, limit, timezone);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#listCalendarEvents");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **from** | **OffsetDateTime**|  | |
| **to** | **OffsetDateTime**|  | |
| **calendarId** | **String**| Defaults to the primary calendar. | [optional] |
| **title** | **String**|  | [optional] |
| **location** | **String**|  | [optional] |
| **showCancelled** | **Boolean**|  | [optional] [default to false] |
| **expandRecurring** | **Boolean**|  | [optional] [default to true] |
| **icalUid** | **String**|  | [optional] |
| **sortOrder** | **String**|  | [optional] [default to asc] [enum: asc, desc] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **timezone** | **String**| IANA zone the &#x60;start&#x60; and &#x60;end&#x60; offsets are rendered in. Default UTC. | [optional] |

### Return type

[**ListCalendarEvents200Response**](ListCalendarEvents200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Events |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  YouTube Analytics: reads (channel-insights, demographics, daily-views, video-retention) run on the \&quot;Queries per day\&quot; quota of the Google Cloud project the YouTube account is connected through, shared with other Zernio customers, so a 429 there is not your own volume. It resets at midnight Pacific Time. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  Pinterest ads: Pinterest rate-limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when it sends one, otherwise 60 seconds.  TikTok ads: TikTok limits requests per app and per endpoint (per second, per minute and per day) and answers overage with code 40100 or with code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (for example one ad at a time per advertiser) instead of retrying at once. The Smart+ review read (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has a stricter quota of its own on TikTok: after an overage Zernio answers 429 for that advertiser and connection, without calling TikTok, for about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, each with up to 10% of random jitter. A successful call holds nothing back, and the next overage after it pauses about 60 seconds again; &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## listCalendarEventsWithHttpInfo

> ApiResponse<ListCalendarEvents200Response> listCalendarEvents listCalendarEventsWithHttpInfo(accountId, from, to, calendarId, title, location, showCancelled, expandRecurring, icalUid, sortOrder, cursor, limit, timezone)

List events in a window

Recurring series are expanded into their occurrences inside the window by default (&#x60;expandRecurring&#x3D;false&#x60; lists the masters instead). &#x60;title&#x60; and &#x60;location&#x60; are substring matches applied to the fetched page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | 
        String calendarId = "calendarId_example"; // String | Defaults to the primary calendar.
        String title = "title_example"; // String | 
        String location = "location_example"; // String | 
        Boolean showCancelled = false; // Boolean | 
        Boolean expandRecurring = true; // Boolean | 
        String icalUid = "icalUid_example"; // String | 
        String sortOrder = "asc"; // String | 
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        String timezone = "timezone_example"; // String | IANA zone the `start` and `end` offsets are rendered in. Default UTC.
        try {
            ApiResponse<ListCalendarEvents200Response> response = apiInstance.listCalendarEventsWithHttpInfo(accountId, from, to, calendarId, title, location, showCancelled, expandRecurring, icalUid, sortOrder, cursor, limit, timezone);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#listCalendarEvents");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **from** | **OffsetDateTime**|  | |
| **to** | **OffsetDateTime**|  | |
| **calendarId** | **String**| Defaults to the primary calendar. | [optional] |
| **title** | **String**|  | [optional] |
| **location** | **String**|  | [optional] |
| **showCancelled** | **Boolean**|  | [optional] [default to false] |
| **expandRecurring** | **Boolean**|  | [optional] [default to true] |
| **icalUid** | **String**|  | [optional] |
| **sortOrder** | **String**|  | [optional] [default to asc] [enum: asc, desc] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **timezone** | **String**| IANA zone the &#x60;start&#x60; and &#x60;end&#x60; offsets are rendered in. Default UTC. | [optional] |

### Return type

ApiResponse<[**ListCalendarEvents200Response**](ListCalendarEvents200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Events |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  YouTube Analytics: reads (channel-insights, demographics, daily-views, video-retention) run on the \&quot;Queries per day\&quot; quota of the Google Cloud project the YouTube account is connected through, shared with other Zernio customers, so a 429 there is not your own volume. It resets at midnight Pacific Time. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  Pinterest ads: Pinterest rate-limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when it sends one, otherwise 60 seconds.  TikTok ads: TikTok limits requests per app and per endpoint (per second, per minute and per day) and answers overage with code 40100 or with code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (for example one ad at a time per advertiser) instead of retrying at once. The Smart+ review read (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has a stricter quota of its own on TikTok: after an overage Zernio answers 429 for that advertiser and connection, without calling TikTok, for about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, each with up to 10% of random jitter. A successful call holds nothing back, and the next overage after it pauses about 60 seconds again; &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## listCalendars

> ListCalendars200Response listCalendars(accountId)

List calendars

The account must have been connected with &#x60;scopes&#x3D;calendar&#x60; (412 &#x60;account_scope_missing&#x60; otherwise).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ListCalendars200Response result = apiInstance.listCalendars(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#listCalendars");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**ListCalendars200Response**](ListCalendars200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calendars |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## listCalendarsWithHttpInfo

> ApiResponse<ListCalendars200Response> listCalendars listCalendarsWithHttpInfo(accountId)

List calendars

The account must have been connected with &#x60;scopes&#x3D;calendar&#x60; (412 &#x60;account_scope_missing&#x60; otherwise).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<ListCalendars200Response> response = apiInstance.listCalendarsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#listCalendars");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**ListCalendars200Response**](ListCalendars200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calendars |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## rsvpCalendarEvent

> CreateCalendarEvent201Response rsvpCalendarEvent(eventId, rsvpCalendarEventRequest)

Respond to an invitation

Accepts, declines or tentatively accepts on behalf of the mailbox and notifies the organizer.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        RsvpCalendarEventRequest rsvpCalendarEventRequest = new RsvpCalendarEventRequest(); // RsvpCalendarEventRequest | 
        try {
            CreateCalendarEvent201Response result = apiInstance.rsvpCalendarEvent(eventId, rsvpCalendarEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#rsvpCalendarEvent");
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
| **eventId** | **String**|  | |
| **rsvpCalendarEventRequest** | [**RsvpCalendarEventRequest**](RsvpCalendarEventRequest.md)|  | |

### Return type

[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The event after the response |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## rsvpCalendarEventWithHttpInfo

> ApiResponse<CreateCalendarEvent201Response> rsvpCalendarEvent rsvpCalendarEventWithHttpInfo(eventId, rsvpCalendarEventRequest)

Respond to an invitation

Accepts, declines or tentatively accepts on behalf of the mailbox and notifies the organizer.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        RsvpCalendarEventRequest rsvpCalendarEventRequest = new RsvpCalendarEventRequest(); // RsvpCalendarEventRequest | 
        try {
            ApiResponse<CreateCalendarEvent201Response> response = apiInstance.rsvpCalendarEventWithHttpInfo(eventId, rsvpCalendarEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#rsvpCalendarEvent");
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
| **eventId** | **String**|  | |
| **rsvpCalendarEventRequest** | [**RsvpCalendarEventRequest**](RsvpCalendarEventRequest.md)|  | |

### Return type

ApiResponse<[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The event after the response |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## updateCalendarEvent

> CreateCalendarEvent201Response updateCalendarEvent(eventId, updateCalendarEventRequest)

Update an event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        UpdateCalendarEventRequest updateCalendarEventRequest = new UpdateCalendarEventRequest(); // UpdateCalendarEventRequest | 
        try {
            CreateCalendarEvent201Response result = apiInstance.updateCalendarEvent(eventId, updateCalendarEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#updateCalendarEvent");
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
| **eventId** | **String**|  | |
| **updateCalendarEventRequest** | [**UpdateCalendarEventRequest**](UpdateCalendarEventRequest.md)|  | |

### Return type

[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated event |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## updateCalendarEventWithHttpInfo

> ApiResponse<CreateCalendarEvent201Response> updateCalendarEvent updateCalendarEventWithHttpInfo(eventId, updateCalendarEventRequest)

Update an event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CalendarApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CalendarApi apiInstance = new CalendarApi(defaultClient);
        String eventId = "eventId_example"; // String | 
        UpdateCalendarEventRequest updateCalendarEventRequest = new UpdateCalendarEventRequest(); // UpdateCalendarEventRequest | 
        try {
            ApiResponse<CreateCalendarEvent201Response> response = apiInstance.updateCalendarEventWithHttpInfo(eventId, updateCalendarEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CalendarApi#updateCalendarEvent");
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
| **eventId** | **String**|  | |
| **updateCalendarEventRequest** | [**UpdateCalendarEventRequest**](UpdateCalendarEventRequest.md)|  | |

### Return type

ApiResponse<[**CreateCalendarEvent201Response**](CreateCalendarEvent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated event |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

