# DiscordApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addDiscordMemberRole**](DiscordApi.md#addDiscordMemberRole) | **PUT** /v1/discord/guilds/{guildId}/members/{userId}/roles/{roleId} | Assign a role to a guild member |
| [**addDiscordMemberRoleWithHttpInfo**](DiscordApi.md#addDiscordMemberRoleWithHttpInfo) | **PUT** /v1/discord/guilds/{guildId}/members/{userId}/roles/{roleId} | Assign a role to a guild member |
| [**createDiscordGuildRole**](DiscordApi.md#createDiscordGuildRole) | **POST** /v1/discord/guilds/{guildId}/roles | Create a Discord guild role |
| [**createDiscordGuildRoleWithHttpInfo**](DiscordApi.md#createDiscordGuildRoleWithHttpInfo) | **POST** /v1/discord/guilds/{guildId}/roles | Create a Discord guild role |
| [**createDiscordScheduledEvent**](DiscordApi.md#createDiscordScheduledEvent) | **POST** /v1/discord/guilds/{guildId}/events | Create a Discord scheduled event |
| [**createDiscordScheduledEventWithHttpInfo**](DiscordApi.md#createDiscordScheduledEventWithHttpInfo) | **POST** /v1/discord/guilds/{guildId}/events | Create a Discord scheduled event |
| [**createDiscordThread**](DiscordApi.md#createDiscordThread) | **POST** /v1/discord/channels/{channelId}/threads | Create a Discord public thread |
| [**createDiscordThreadWithHttpInfo**](DiscordApi.md#createDiscordThreadWithHttpInfo) | **POST** /v1/discord/channels/{channelId}/threads | Create a Discord public thread |
| [**crosspostDiscordMessage**](DiscordApi.md#crosspostDiscordMessage) | **POST** /v1/discord/channels/{channelId}/messages/{messageId}/crosspost | Crosspost a Discord announcement message |
| [**crosspostDiscordMessageWithHttpInfo**](DiscordApi.md#crosspostDiscordMessageWithHttpInfo) | **POST** /v1/discord/channels/{channelId}/messages/{messageId}/crosspost | Crosspost a Discord announcement message |
| [**deleteDiscordGuildRole**](DiscordApi.md#deleteDiscordGuildRole) | **DELETE** /v1/discord/guilds/{guildId}/roles/{roleId} | Delete a Discord guild role |
| [**deleteDiscordGuildRoleWithHttpInfo**](DiscordApi.md#deleteDiscordGuildRoleWithHttpInfo) | **DELETE** /v1/discord/guilds/{guildId}/roles/{roleId} | Delete a Discord guild role |
| [**deleteDiscordMessage**](DiscordApi.md#deleteDiscordMessage) | **DELETE** /v1/discord/channels/{channelId}/messages/{messageId} | Delete a Discord channel message |
| [**deleteDiscordMessageWithHttpInfo**](DiscordApi.md#deleteDiscordMessageWithHttpInfo) | **DELETE** /v1/discord/channels/{channelId}/messages/{messageId} | Delete a Discord channel message |
| [**deleteDiscordScheduledEvent**](DiscordApi.md#deleteDiscordScheduledEvent) | **DELETE** /v1/discord/guilds/{guildId}/events/{eventId} | Delete a Discord scheduled event |
| [**deleteDiscordScheduledEventWithHttpInfo**](DiscordApi.md#deleteDiscordScheduledEventWithHttpInfo) | **DELETE** /v1/discord/guilds/{guildId}/events/{eventId} | Delete a Discord scheduled event |
| [**editDiscordGuildRole**](DiscordApi.md#editDiscordGuildRole) | **PATCH** /v1/discord/guilds/{guildId}/roles/{roleId} | Edit a Discord guild role |
| [**editDiscordGuildRoleWithHttpInfo**](DiscordApi.md#editDiscordGuildRoleWithHttpInfo) | **PATCH** /v1/discord/guilds/{guildId}/roles/{roleId} | Edit a Discord guild role |
| [**getDiscordChannels**](DiscordApi.md#getDiscordChannels) | **GET** /v1/accounts/{accountId}/discord-channels | List Discord guild channels |
| [**getDiscordChannelsWithHttpInfo**](DiscordApi.md#getDiscordChannelsWithHttpInfo) | **GET** /v1/accounts/{accountId}/discord-channels | List Discord guild channels |
| [**getDiscordScheduledEvent**](DiscordApi.md#getDiscordScheduledEvent) | **GET** /v1/discord/guilds/{guildId}/events/{eventId} | Get a Discord scheduled event |
| [**getDiscordScheduledEventWithHttpInfo**](DiscordApi.md#getDiscordScheduledEventWithHttpInfo) | **GET** /v1/discord/guilds/{guildId}/events/{eventId} | Get a Discord scheduled event |
| [**getDiscordSettings**](DiscordApi.md#getDiscordSettings) | **GET** /v1/accounts/{accountId}/discord-settings | Get Discord account settings |
| [**getDiscordSettingsWithHttpInfo**](DiscordApi.md#getDiscordSettingsWithHttpInfo) | **GET** /v1/accounts/{accountId}/discord-settings | Get Discord account settings |
| [**listDiscordGuildMembers**](DiscordApi.md#listDiscordGuildMembers) | **GET** /v1/discord/guilds/{guildId}/members | List Discord guild members |
| [**listDiscordGuildMembersWithHttpInfo**](DiscordApi.md#listDiscordGuildMembersWithHttpInfo) | **GET** /v1/discord/guilds/{guildId}/members | List Discord guild members |
| [**listDiscordGuildRoles**](DiscordApi.md#listDiscordGuildRoles) | **GET** /v1/discord/guilds/{guildId}/roles | List Discord guild roles |
| [**listDiscordGuildRolesWithHttpInfo**](DiscordApi.md#listDiscordGuildRolesWithHttpInfo) | **GET** /v1/discord/guilds/{guildId}/roles | List Discord guild roles |
| [**listDiscordPinnedMessages**](DiscordApi.md#listDiscordPinnedMessages) | **GET** /v1/discord/channels/{channelId}/pins | List pinned messages |
| [**listDiscordPinnedMessagesWithHttpInfo**](DiscordApi.md#listDiscordPinnedMessagesWithHttpInfo) | **GET** /v1/discord/channels/{channelId}/pins | List pinned messages |
| [**listDiscordScheduledEvents**](DiscordApi.md#listDiscordScheduledEvents) | **GET** /v1/discord/guilds/{guildId}/events | List Discord scheduled events |
| [**listDiscordScheduledEventsWithHttpInfo**](DiscordApi.md#listDiscordScheduledEventsWithHttpInfo) | **GET** /v1/discord/guilds/{guildId}/events | List Discord scheduled events |
| [**pinDiscordMessage**](DiscordApi.md#pinDiscordMessage) | **PUT** /v1/discord/channels/{channelId}/pins/{messageId} | Pin a Discord message |
| [**pinDiscordMessageWithHttpInfo**](DiscordApi.md#pinDiscordMessageWithHttpInfo) | **PUT** /v1/discord/channels/{channelId}/pins/{messageId} | Pin a Discord message |
| [**removeDiscordMemberRole**](DiscordApi.md#removeDiscordMemberRole) | **DELETE** /v1/discord/guilds/{guildId}/members/{userId}/roles/{roleId} | Remove a role from a guild member |
| [**removeDiscordMemberRoleWithHttpInfo**](DiscordApi.md#removeDiscordMemberRoleWithHttpInfo) | **DELETE** /v1/discord/guilds/{guildId}/members/{userId}/roles/{roleId} | Remove a role from a guild member |
| [**sendDiscordDirectMessage**](DiscordApi.md#sendDiscordDirectMessage) | **POST** /v1/discord/dms | Send a Discord Direct Message |
| [**sendDiscordDirectMessageWithHttpInfo**](DiscordApi.md#sendDiscordDirectMessageWithHttpInfo) | **POST** /v1/discord/dms | Send a Discord Direct Message |
| [**unpinDiscordMessage**](DiscordApi.md#unpinDiscordMessage) | **DELETE** /v1/discord/channels/{channelId}/pins/{messageId} | Unpin a Discord message |
| [**unpinDiscordMessageWithHttpInfo**](DiscordApi.md#unpinDiscordMessageWithHttpInfo) | **DELETE** /v1/discord/channels/{channelId}/pins/{messageId} | Unpin a Discord message |
| [**updateDiscordScheduledEvent**](DiscordApi.md#updateDiscordScheduledEvent) | **PATCH** /v1/discord/guilds/{guildId}/events/{eventId} | Update a Discord scheduled event |
| [**updateDiscordScheduledEventWithHttpInfo**](DiscordApi.md#updateDiscordScheduledEventWithHttpInfo) | **PATCH** /v1/discord/guilds/{guildId}/events/{eventId} | Update a Discord scheduled event |
| [**updateDiscordSettings**](DiscordApi.md#updateDiscordSettings) | **PATCH** /v1/accounts/{accountId}/discord-settings | Update Discord settings |
| [**updateDiscordSettingsWithHttpInfo**](DiscordApi.md#updateDiscordSettingsWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/discord-settings | Update Discord settings |



## addDiscordMemberRole

> AddDiscordMemberRole200Response addDiscordMemberRole(guildId, userId, roleId, accountId)

Assign a role to a guild member

Assign one role to one member. Idempotent on Discord&#39;s side — re-running on a member who already has the role is a 204 no-op.  Path shape mirrors Discord&#39;s own API (&#x60;PUT /guilds/{guild}/members/{user}/roles/{role}&#x60;) for zero-translation mental mapping.  Bot needs MANAGE_ROLES permission in the guild AND its highest role must be above the target role (Discord hierarchy rule). The &#x60;@everyone&#x60; role (where roleId &#x3D;&#x3D; guildId) cannot be assigned. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String userId = "userId_example"; // String | Discord user snowflake to assign the role to.
        String roleId = "roleId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            AddDiscordMemberRole200Response result = apiInstance.addDiscordMemberRole(guildId, userId, roleId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#addDiscordMemberRole");
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
| **guildId** | **String**|  | |
| **userId** | **String**| Discord user snowflake to assign the role to. | |
| **roleId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**AddDiscordMemberRole200Response**](AddDiscordMemberRole200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role assigned (or already present — idempotent). |  -  |
| **400** | Validation error (malformed snowflake) or @everyone manipulation attempt. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |
| **403** | Discord refused the request: bot lacks MANAGE_ROLES, or target role is at or above the bot&#39;s highest role. |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## addDiscordMemberRoleWithHttpInfo

> ApiResponse<AddDiscordMemberRole200Response> addDiscordMemberRole addDiscordMemberRoleWithHttpInfo(guildId, userId, roleId, accountId)

Assign a role to a guild member

Assign one role to one member. Idempotent on Discord&#39;s side — re-running on a member who already has the role is a 204 no-op.  Path shape mirrors Discord&#39;s own API (&#x60;PUT /guilds/{guild}/members/{user}/roles/{role}&#x60;) for zero-translation mental mapping.  Bot needs MANAGE_ROLES permission in the guild AND its highest role must be above the target role (Discord hierarchy rule). The &#x60;@everyone&#x60; role (where roleId &#x3D;&#x3D; guildId) cannot be assigned. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String userId = "userId_example"; // String | Discord user snowflake to assign the role to.
        String roleId = "roleId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<AddDiscordMemberRole200Response> response = apiInstance.addDiscordMemberRoleWithHttpInfo(guildId, userId, roleId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#addDiscordMemberRole");
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
| **guildId** | **String**|  | |
| **userId** | **String**| Discord user snowflake to assign the role to. | |
| **roleId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**AddDiscordMemberRole200Response**](AddDiscordMemberRole200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role assigned (or already present — idempotent). |  -  |
| **400** | Validation error (malformed snowflake) or @everyone manipulation attempt. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |
| **403** | Discord refused the request: bot lacks MANAGE_ROLES, or target role is at or above the bot&#39;s highest role. |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## createDiscordGuildRole

> CreateDiscordGuildRole201Response createDiscordGuildRole(guildId, accountId, createDiscordGuildRoleRequest)

Create a Discord guild role

Creates a new role in the guild.  Requires the bot to hold the Manage Roles permission. Guilds that added the Zernio bot before role management shipped must re-invite it, because Discord applies the permission set at invite time.  Discord&#39;s role hierarchy applies: the bot cannot create a role positioned at or above its own highest role, and cannot grant permissions it does not itself hold. Either attempt returns a 403 carrying Discord&#39;s own error. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        CreateDiscordGuildRoleRequest createDiscordGuildRoleRequest = new CreateDiscordGuildRoleRequest(); // CreateDiscordGuildRoleRequest | 
        try {
            CreateDiscordGuildRole201Response result = apiInstance.createDiscordGuildRole(guildId, accountId, createDiscordGuildRoleRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#createDiscordGuildRole");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |
| **createDiscordGuildRoleRequest** | [**CreateDiscordGuildRoleRequest**](CreateDiscordGuildRoleRequest.md)|  | |

### Return type

[**CreateDiscordGuildRole201Response**](CreateDiscordGuildRole201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Role created. |  -  |
| **400** | Invalid accountId, guildId, or role body. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Roles, or the new role would sit at or above the bot&#39;s highest role). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## createDiscordGuildRoleWithHttpInfo

> ApiResponse<CreateDiscordGuildRole201Response> createDiscordGuildRole createDiscordGuildRoleWithHttpInfo(guildId, accountId, createDiscordGuildRoleRequest)

Create a Discord guild role

Creates a new role in the guild.  Requires the bot to hold the Manage Roles permission. Guilds that added the Zernio bot before role management shipped must re-invite it, because Discord applies the permission set at invite time.  Discord&#39;s role hierarchy applies: the bot cannot create a role positioned at or above its own highest role, and cannot grant permissions it does not itself hold. Either attempt returns a 403 carrying Discord&#39;s own error. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        CreateDiscordGuildRoleRequest createDiscordGuildRoleRequest = new CreateDiscordGuildRoleRequest(); // CreateDiscordGuildRoleRequest | 
        try {
            ApiResponse<CreateDiscordGuildRole201Response> response = apiInstance.createDiscordGuildRoleWithHttpInfo(guildId, accountId, createDiscordGuildRoleRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#createDiscordGuildRole");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |
| **createDiscordGuildRoleRequest** | [**CreateDiscordGuildRoleRequest**](CreateDiscordGuildRoleRequest.md)|  | |

### Return type

ApiResponse<[**CreateDiscordGuildRole201Response**](CreateDiscordGuildRole201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Role created. |  -  |
| **400** | Invalid accountId, guildId, or role body. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Roles, or the new role would sit at or above the bot&#39;s highest role). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## createDiscordScheduledEvent

> CreateDiscordScheduledEvent200Response createDiscordScheduledEvent(guildId, createDiscordScheduledEventRequest)

Create a Discord scheduled event

Create a guild scheduled event. Three event types, selected via the discriminator on &#x60;entity.type&#x60;:    - &#x60;external&#x60; — off-platform (Zoom, in-person, livestream). Requires     both &#x60;location&#x60; and &#x60;endsAt&#x60;. Most common type for scheduler     integrations.   - &#x60;voice&#x60; — hosted in a Discord voice channel. Requires &#x60;channelId&#x60;.   - &#x60;stage&#x60; — hosted in a Discord stage channel. Requires &#x60;channelId&#x60;.  Bot needs MANAGE_EVENTS in the guild. Existing installs (pre-events PR) need a re-invite OR a server admin manually granting the permission — see route header for details. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        CreateDiscordScheduledEventRequest createDiscordScheduledEventRequest = new CreateDiscordScheduledEventRequest(); // CreateDiscordScheduledEventRequest | 
        try {
            CreateDiscordScheduledEvent200Response result = apiInstance.createDiscordScheduledEvent(guildId, createDiscordScheduledEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#createDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **createDiscordScheduledEventRequest** | [**CreateDiscordScheduledEventRequest**](CreateDiscordScheduledEventRequest.md)|  | |

### Return type

[**CreateDiscordScheduledEvent200Response**](CreateDiscordScheduledEvent200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event created. |  -  |
| **400** | Validation error (missing required fields for the chosen entity type, malformed snowflake, past startsAt, etc.). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_EVENTS in the guild. |  -  |

## createDiscordScheduledEventWithHttpInfo

> ApiResponse<CreateDiscordScheduledEvent200Response> createDiscordScheduledEvent createDiscordScheduledEventWithHttpInfo(guildId, createDiscordScheduledEventRequest)

Create a Discord scheduled event

Create a guild scheduled event. Three event types, selected via the discriminator on &#x60;entity.type&#x60;:    - &#x60;external&#x60; — off-platform (Zoom, in-person, livestream). Requires     both &#x60;location&#x60; and &#x60;endsAt&#x60;. Most common type for scheduler     integrations.   - &#x60;voice&#x60; — hosted in a Discord voice channel. Requires &#x60;channelId&#x60;.   - &#x60;stage&#x60; — hosted in a Discord stage channel. Requires &#x60;channelId&#x60;.  Bot needs MANAGE_EVENTS in the guild. Existing installs (pre-events PR) need a re-invite OR a server admin manually granting the permission — see route header for details. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        CreateDiscordScheduledEventRequest createDiscordScheduledEventRequest = new CreateDiscordScheduledEventRequest(); // CreateDiscordScheduledEventRequest | 
        try {
            ApiResponse<CreateDiscordScheduledEvent200Response> response = apiInstance.createDiscordScheduledEventWithHttpInfo(guildId, createDiscordScheduledEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#createDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **createDiscordScheduledEventRequest** | [**CreateDiscordScheduledEventRequest**](CreateDiscordScheduledEventRequest.md)|  | |

### Return type

ApiResponse<[**CreateDiscordScheduledEvent200Response**](CreateDiscordScheduledEvent200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event created. |  -  |
| **400** | Validation error (missing required fields for the chosen entity type, malformed snowflake, past startsAt, etc.). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_EVENTS in the guild. |  -  |


## createDiscordThread

> CreateDiscordThread200Response createDiscordThread(channelId, accountId, createDiscordThreadRequest)

Create a Discord public thread

Creates a public thread in a channel. Pass &#x60;messageId&#x60; to start the thread from an existing message, or omit it to create a standalone thread.  Threads created here are always public. Requires the bot to hold Create Public Threads, which the Zernio bot requests at install time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord channel snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this channel's guild
        CreateDiscordThreadRequest createDiscordThreadRequest = new CreateDiscordThreadRequest(); // CreateDiscordThreadRequest | 
        try {
            CreateDiscordThread200Response result = apiInstance.createDiscordThread(channelId, accountId, createDiscordThreadRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#createDiscordThread");
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
| **channelId** | **String**| Discord channel snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this channel&#39;s guild | |
| **createDiscordThreadRequest** | [**CreateDiscordThreadRequest**](CreateDiscordThreadRequest.md)|  | |

### Return type

[**CreateDiscordThread200Response**](CreateDiscordThread200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Thread created. |  -  |
| **400** | Invalid accountId, channelId, messageId, name, or autoArchiveDuration. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this channel&#39;s guild. |  -  |
| **403** | Discord refused the action (bot lacks Create Public Threads). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## createDiscordThreadWithHttpInfo

> ApiResponse<CreateDiscordThread200Response> createDiscordThread createDiscordThreadWithHttpInfo(channelId, accountId, createDiscordThreadRequest)

Create a Discord public thread

Creates a public thread in a channel. Pass &#x60;messageId&#x60; to start the thread from an existing message, or omit it to create a standalone thread.  Threads created here are always public. Requires the bot to hold Create Public Threads, which the Zernio bot requests at install time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord channel snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this channel's guild
        CreateDiscordThreadRequest createDiscordThreadRequest = new CreateDiscordThreadRequest(); // CreateDiscordThreadRequest | 
        try {
            ApiResponse<CreateDiscordThread200Response> response = apiInstance.createDiscordThreadWithHttpInfo(channelId, accountId, createDiscordThreadRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#createDiscordThread");
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
| **channelId** | **String**| Discord channel snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this channel&#39;s guild | |
| **createDiscordThreadRequest** | [**CreateDiscordThreadRequest**](CreateDiscordThreadRequest.md)|  | |

### Return type

ApiResponse<[**CreateDiscordThread200Response**](CreateDiscordThread200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Thread created. |  -  |
| **400** | Invalid accountId, channelId, messageId, name, or autoArchiveDuration. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this channel&#39;s guild. |  -  |
| **403** | Discord refused the action (bot lacks Create Public Threads). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## crosspostDiscordMessage

> CrosspostDiscordMessage200Response crosspostDiscordMessage(channelId, messageId, accountId)

Crosspost a Discord announcement message

Publishes a message from an announcement channel so it propagates to every server following that channel.  The source channel must be an announcement channel. Calling this on a regular text channel returns a 400 before Discord is contacted, because Discord&#39;s own error for this case is opaque. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord announcement channel snowflake ID
        String messageId = "messageId_example"; // String | Discord message snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this channel's guild
        try {
            CrosspostDiscordMessage200Response result = apiInstance.crosspostDiscordMessage(channelId, messageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#crosspostDiscordMessage");
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
| **channelId** | **String**| Discord announcement channel snowflake ID | |
| **messageId** | **String**| Discord message snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this channel&#39;s guild | |

### Return type

[**CrosspostDiscordMessage200Response**](CrosspostDiscordMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message crossposted. |  -  |
| **400** | Invalid ids, or the channel is not an announcement channel. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this channel&#39;s guild. |  -  |
| **403** | Discord refused the action (bot lacks the required permission). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## crosspostDiscordMessageWithHttpInfo

> ApiResponse<CrosspostDiscordMessage200Response> crosspostDiscordMessage crosspostDiscordMessageWithHttpInfo(channelId, messageId, accountId)

Crosspost a Discord announcement message

Publishes a message from an announcement channel so it propagates to every server following that channel.  The source channel must be an announcement channel. Calling this on a regular text channel returns a 400 before Discord is contacted, because Discord&#39;s own error for this case is opaque. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord announcement channel snowflake ID
        String messageId = "messageId_example"; // String | Discord message snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this channel's guild
        try {
            ApiResponse<CrosspostDiscordMessage200Response> response = apiInstance.crosspostDiscordMessageWithHttpInfo(channelId, messageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#crosspostDiscordMessage");
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
| **channelId** | **String**| Discord announcement channel snowflake ID | |
| **messageId** | **String**| Discord message snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this channel&#39;s guild | |

### Return type

ApiResponse<[**CrosspostDiscordMessage200Response**](CrosspostDiscordMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message crossposted. |  -  |
| **400** | Invalid ids, or the channel is not an announcement channel. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this channel&#39;s guild. |  -  |
| **403** | Discord refused the action (bot lacks the required permission). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## deleteDiscordGuildRole

> UpdateYoutubeDefaultPlaylist200Response deleteDiscordGuildRole(guildId, roleId, accountId)

Delete a Discord guild role

Permanently deletes a role from the guild and removes it from every member. This cannot be undone.  Requires the bot to hold Manage Roles, and the target role must sit below the bot&#39;s highest role. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String roleId = "roleId_example"; // String | Discord role snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteDiscordGuildRole(guildId, roleId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#deleteDiscordGuildRole");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **roleId** | **String**| Discord role snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role deleted. |  -  |
| **400** | Invalid accountId, guildId, or roleId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Roles, or the target role sits at or above the bot&#39;s highest role). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## deleteDiscordGuildRoleWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteDiscordGuildRole deleteDiscordGuildRoleWithHttpInfo(guildId, roleId, accountId)

Delete a Discord guild role

Permanently deletes a role from the guild and removes it from every member. This cannot be undone.  Requires the bot to hold Manage Roles, and the target role must sit below the bot&#39;s highest role. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String roleId = "roleId_example"; // String | Discord role snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteDiscordGuildRoleWithHttpInfo(guildId, roleId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#deleteDiscordGuildRole");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **roleId** | **String**| Discord role snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role deleted. |  -  |
| **400** | Invalid accountId, guildId, or roleId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Roles, or the target role sits at or above the bot&#39;s highest role). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## deleteDiscordMessage

> UpdateYoutubeDefaultPlaylist200Response deleteDiscordMessage(channelId, messageId, accountId)

Delete a Discord channel message

Deletes a message from a channel, for moderation and cleanup. This cannot be undone.  Deleting a message the bot did not send requires the bot to hold the Manage Messages permission, which the Zernio bot requests at install time. Deleting the bot&#39;s own message needs no extra permission.  Ownership is verified by resolving the channel&#39;s guild and confirming the caller owns a Discord account bound to it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord channel snowflake ID
        String messageId = "messageId_example"; // String | Discord message snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this channel's guild
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteDiscordMessage(channelId, messageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#deleteDiscordMessage");
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
| **channelId** | **String**| Discord channel snowflake ID | |
| **messageId** | **String**| Discord message snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this channel&#39;s guild | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message deleted. |  -  |
| **400** | Invalid accountId, channelId, or messageId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this channel&#39;s guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Messages). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## deleteDiscordMessageWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteDiscordMessage deleteDiscordMessageWithHttpInfo(channelId, messageId, accountId)

Delete a Discord channel message

Deletes a message from a channel, for moderation and cleanup. This cannot be undone.  Deleting a message the bot did not send requires the bot to hold the Manage Messages permission, which the Zernio bot requests at install time. Deleting the bot&#39;s own message needs no extra permission.  Ownership is verified by resolving the channel&#39;s guild and confirming the caller owns a Discord account bound to it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord channel snowflake ID
        String messageId = "messageId_example"; // String | Discord message snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this channel's guild
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteDiscordMessageWithHttpInfo(channelId, messageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#deleteDiscordMessage");
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
| **channelId** | **String**| Discord channel snowflake ID | |
| **messageId** | **String**| Discord message snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this channel&#39;s guild | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message deleted. |  -  |
| **400** | Invalid accountId, channelId, or messageId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this channel&#39;s guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Messages). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## deleteDiscordScheduledEvent

> DeleteDiscordScheduledEvent200Response deleteDiscordScheduledEvent(guildId, eventId, accountId)

Delete a Discord scheduled event

Hard-delete an event. Use PATCH with &#x60;status: &#39;cancelled&#39;&#x60; instead if you want the event preserved in the guild&#39;s history. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            DeleteDiscordScheduledEvent200Response result = apiInstance.deleteDiscordScheduledEvent(guildId, eventId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#deleteDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **eventId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**DeleteDiscordScheduledEvent200Response**](DeleteDiscordScheduledEvent200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event deleted. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Event or Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_EVENTS in the guild. |  -  |

## deleteDiscordScheduledEventWithHttpInfo

> ApiResponse<DeleteDiscordScheduledEvent200Response> deleteDiscordScheduledEvent deleteDiscordScheduledEventWithHttpInfo(guildId, eventId, accountId)

Delete a Discord scheduled event

Hard-delete an event. Use PATCH with &#x60;status: &#39;cancelled&#39;&#x60; instead if you want the event preserved in the guild&#39;s history. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<DeleteDiscordScheduledEvent200Response> response = apiInstance.deleteDiscordScheduledEventWithHttpInfo(guildId, eventId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#deleteDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **eventId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**DeleteDiscordScheduledEvent200Response**](DeleteDiscordScheduledEvent200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event deleted. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Event or Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_EVENTS in the guild. |  -  |


## editDiscordGuildRole

> CreateDiscordGuildRole201Response editDiscordGuildRole(guildId, roleId, accountId, editDiscordGuildRoleRequest)

Edit a Discord guild role

Updates a role&#39;s name, color, hoist, mentionable flag, or permission bitfield. At least one field must be supplied. Omitted fields are left unchanged.  Requires the bot to hold Manage Roles, and the target role must sit below the bot&#39;s highest role. See the create-role operation for the re-invite requirement. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String roleId = "roleId_example"; // String | Discord role snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        EditDiscordGuildRoleRequest editDiscordGuildRoleRequest = new EditDiscordGuildRoleRequest(); // EditDiscordGuildRoleRequest | 
        try {
            CreateDiscordGuildRole201Response result = apiInstance.editDiscordGuildRole(guildId, roleId, accountId, editDiscordGuildRoleRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#editDiscordGuildRole");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **roleId** | **String**| Discord role snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |
| **editDiscordGuildRoleRequest** | [**EditDiscordGuildRoleRequest**](EditDiscordGuildRoleRequest.md)|  | |

### Return type

[**CreateDiscordGuildRole201Response**](CreateDiscordGuildRole201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role updated. |  -  |
| **400** | Invalid ids, or no fields supplied to edit. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Roles, or the target role sits at or above the bot&#39;s highest role). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## editDiscordGuildRoleWithHttpInfo

> ApiResponse<CreateDiscordGuildRole201Response> editDiscordGuildRole editDiscordGuildRoleWithHttpInfo(guildId, roleId, accountId, editDiscordGuildRoleRequest)

Edit a Discord guild role

Updates a role&#39;s name, color, hoist, mentionable flag, or permission bitfield. At least one field must be supplied. Omitted fields are left unchanged.  Requires the bot to hold Manage Roles, and the target role must sit below the bot&#39;s highest role. See the create-role operation for the re-invite requirement. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String roleId = "roleId_example"; // String | Discord role snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        EditDiscordGuildRoleRequest editDiscordGuildRoleRequest = new EditDiscordGuildRoleRequest(); // EditDiscordGuildRoleRequest | 
        try {
            ApiResponse<CreateDiscordGuildRole201Response> response = apiInstance.editDiscordGuildRoleWithHttpInfo(guildId, roleId, accountId, editDiscordGuildRoleRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#editDiscordGuildRole");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **roleId** | **String**| Discord role snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |
| **editDiscordGuildRoleRequest** | [**EditDiscordGuildRoleRequest**](EditDiscordGuildRoleRequest.md)|  | |

### Return type

ApiResponse<[**CreateDiscordGuildRole201Response**](CreateDiscordGuildRole201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role updated. |  -  |
| **400** | Invalid ids, or no fields supplied to edit. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the action (bot lacks Manage Roles, or the target role sits at or above the bot&#39;s highest role). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## getDiscordChannels

> GetDiscordChannels200Response getDiscordChannels(accountId)

List Discord guild channels

Returns the text, announcement, and forum channels in the connected Discord guild. Use this to discover available channels when switching the connected channel via PATCH /v1/accounts/{accountId}/discord-settings.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetDiscordChannels200Response result = apiInstance.getDiscordChannels(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordChannels");
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
| **accountId** | **String**|  | |

### Return type

[**GetDiscordChannels200Response**](GetDiscordChannels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel list |  -  |
| **400** | Not a Discord account or missing guild info |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getDiscordChannelsWithHttpInfo

> ApiResponse<GetDiscordChannels200Response> getDiscordChannels getDiscordChannelsWithHttpInfo(accountId)

List Discord guild channels

Returns the text, announcement, and forum channels in the connected Discord guild. Use this to discover available channels when switching the connected channel via PATCH /v1/accounts/{accountId}/discord-settings.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetDiscordChannels200Response> response = apiInstance.getDiscordChannelsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordChannels");
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
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**GetDiscordChannels200Response**](GetDiscordChannels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel list |  -  |
| **400** | Not a Discord account or missing guild info |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getDiscordScheduledEvent

> CreateDiscordScheduledEvent200Response getDiscordScheduledEvent(guildId, eventId, accountId)

Get a Discord scheduled event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            CreateDiscordScheduledEvent200Response result = apiInstance.getDiscordScheduledEvent(guildId, eventId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **eventId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**CreateDiscordScheduledEvent200Response**](CreateDiscordScheduledEvent200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Event or Discord account not found. |  -  |

## getDiscordScheduledEventWithHttpInfo

> ApiResponse<CreateDiscordScheduledEvent200Response> getDiscordScheduledEvent getDiscordScheduledEventWithHttpInfo(guildId, eventId, accountId)

Get a Discord scheduled event

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String eventId = "eventId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<CreateDiscordScheduledEvent200Response> response = apiInstance.getDiscordScheduledEventWithHttpInfo(guildId, eventId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **eventId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**CreateDiscordScheduledEvent200Response**](CreateDiscordScheduledEvent200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Event or Discord account not found. |  -  |


## getDiscordSettings

> GetDiscordSettings200Response getDiscordSettings(accountId)

Get Discord account settings

Returns the current Discord account settings including webhook identity (display name and avatar), connected channel, and guild information.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetDiscordSettings200Response result = apiInstance.getDiscordSettings(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordSettings");
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
| **accountId** | **String**|  | |

### Return type

[**GetDiscordSettings200Response**](GetDiscordSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discord account settings |  -  |
| **400** | Not a Discord account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getDiscordSettingsWithHttpInfo

> ApiResponse<GetDiscordSettings200Response> getDiscordSettings getDiscordSettingsWithHttpInfo(accountId)

Get Discord account settings

Returns the current Discord account settings including webhook identity (display name and avatar), connected channel, and guild information.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetDiscordSettings200Response> response = apiInstance.getDiscordSettingsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordSettings");
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
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**GetDiscordSettings200Response**](GetDiscordSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discord account settings |  -  |
| **400** | Not a Discord account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## listDiscordGuildMembers

> ListDiscordGuildMembers200Response listDiscordGuildMembers(guildId, accountId, limit, after)

List Discord guild members

Cursor-paginated list of guild members. Returns Discord&#39;s raw member objects so callers can build community-ops automation (e.g. \&quot;add role to all members joined in the last 7 days\&quot;) on the actual platform shape.  **Important:** this endpoint requires the privileged \&quot;Server Members Intent\&quot; enabled on the Discord app (Developer Portal → Bot tab → toggle \&quot;Server Members Intent\&quot; ON, then Save). Without it, Discord returns an empty array with no error. Verify the intent is enabled before relying on this endpoint.  Pagination: pass &#x60;after&#x60; &#x3D; the last &#x60;user.id&#x60; from the previous page. Omit on the first call. Response includes a &#x60;nextCursor&#x60; and &#x60;hasMore&#x60; flag so callers don&#39;t need to know Discord&#39;s pagination shape. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Integer limit = 100; // Integer | Page size (1-1000).
        String after = "after_example"; // String | Snowflake of the last member from the previous page.
        try {
            ListDiscordGuildMembers200Response result = apiInstance.listDiscordGuildMembers(guildId, accountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordGuildMembers");
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
| **guildId** | **String**|  | |
| **accountId** | **String**|  | |
| **limit** | **Integer**| Page size (1-1000). | [optional] [default to 100] |
| **after** | **String**| Snowflake of the last member from the previous page. | [optional] |

### Return type

[**ListDiscordGuildMembers200Response**](ListDiscordGuildMembers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of guild members. |  -  |
| **400** | Invalid query params. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |

## listDiscordGuildMembersWithHttpInfo

> ApiResponse<ListDiscordGuildMembers200Response> listDiscordGuildMembers listDiscordGuildMembersWithHttpInfo(guildId, accountId, limit, after)

List Discord guild members

Cursor-paginated list of guild members. Returns Discord&#39;s raw member objects so callers can build community-ops automation (e.g. \&quot;add role to all members joined in the last 7 days\&quot;) on the actual platform shape.  **Important:** this endpoint requires the privileged \&quot;Server Members Intent\&quot; enabled on the Discord app (Developer Portal → Bot tab → toggle \&quot;Server Members Intent\&quot; ON, then Save). Without it, Discord returns an empty array with no error. Verify the intent is enabled before relying on this endpoint.  Pagination: pass &#x60;after&#x60; &#x3D; the last &#x60;user.id&#x60; from the previous page. Omit on the first call. Response includes a &#x60;nextCursor&#x60; and &#x60;hasMore&#x60; flag so callers don&#39;t need to know Discord&#39;s pagination shape. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Integer limit = 100; // Integer | Page size (1-1000).
        String after = "after_example"; // String | Snowflake of the last member from the previous page.
        try {
            ApiResponse<ListDiscordGuildMembers200Response> response = apiInstance.listDiscordGuildMembersWithHttpInfo(guildId, accountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordGuildMembers");
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
| **guildId** | **String**|  | |
| **accountId** | **String**|  | |
| **limit** | **Integer**| Page size (1-1000). | [optional] [default to 100] |
| **after** | **String**| Snowflake of the last member from the previous page. | [optional] |

### Return type

ApiResponse<[**ListDiscordGuildMembers200Response**](ListDiscordGuildMembers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of guild members. |  -  |
| **400** | Invalid query params. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |


## listDiscordGuildRoles

> ListDiscordGuildRoles200Response listDiscordGuildRoles(guildId, accountId)

List Discord guild roles

Returns all roles in a Discord guild. Useful for building role-mention pickers, role-permission UIs, or finding the role ID before calling the role-assign endpoint.  Roles are returned unordered — sort client-side by &#x60;position&#x60; if you need Discord&#39;s UI ordering.  Caller must pass &#x60;accountId&#x60; of a Discord SocialAccount bound to this guild (route verifies team access + guild match). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        try {
            ListDiscordGuildRoles200Response result = apiInstance.listDiscordGuildRoles(guildId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordGuildRoles");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |

### Return type

[**ListDiscordGuildRoles200Response**](ListDiscordGuildRoles200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of guild roles. |  -  |
| **400** | Invalid accountId or guildId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the request (bot lacks View Channels permission in the guild). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## listDiscordGuildRolesWithHttpInfo

> ApiResponse<ListDiscordGuildRoles200Response> listDiscordGuildRoles listDiscordGuildRolesWithHttpInfo(guildId, accountId)

List Discord guild roles

Returns all roles in a Discord guild. Useful for building role-mention pickers, role-permission UIs, or finding the role ID before calling the role-assign endpoint.  Roles are returned unordered — sort client-side by &#x60;position&#x60; if you need Discord&#39;s UI ordering.  Caller must pass &#x60;accountId&#x60; of a Discord SocialAccount bound to this guild (route verifies team access + guild match). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | Discord guild snowflake ID
        String accountId = "accountId_example"; // String | SocialAccount _id of the Discord account bound to this guild
        try {
            ApiResponse<ListDiscordGuildRoles200Response> response = apiInstance.listDiscordGuildRolesWithHttpInfo(guildId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordGuildRoles");
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
| **guildId** | **String**| Discord guild snowflake ID | |
| **accountId** | **String**| SocialAccount _id of the Discord account bound to this guild | |

### Return type

ApiResponse<[**ListDiscordGuildRoles200Response**](ListDiscordGuildRoles200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of guild roles. |  -  |
| **400** | Invalid accountId or guildId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found, not accessible, or not bound to this guild. |  -  |
| **403** | Discord refused the request (bot lacks View Channels permission in the guild). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## listDiscordPinnedMessages

> ListDiscordPinnedMessages200Response listDiscordPinnedMessages(channelId, accountId)

List pinned messages

Returns the channel&#39;s pinned messages, sorted most-recently-pinned first. Discord caps a channel at 50 pinned messages and returns the full list unpaginated.  Bot needs READ_MESSAGE_HISTORY in the channel (granted by default BOT_PERMISSIONS). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord channel snowflake.
        String accountId = "accountId_example"; // String | SocialAccount _id of any Discord account in the same guild.
        try {
            ListDiscordPinnedMessages200Response result = apiInstance.listDiscordPinnedMessages(channelId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordPinnedMessages");
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
| **channelId** | **String**| Discord channel snowflake. | |
| **accountId** | **String**| SocialAccount _id of any Discord account in the same guild. | |

### Return type

[**ListDiscordPinnedMessages200Response**](ListDiscordPinnedMessages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pinned messages. |  -  |
| **400** | Invalid channelId or accountId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not accessible. |  -  |
| **502** | Bot lacks access to the channel. |  -  |

## listDiscordPinnedMessagesWithHttpInfo

> ApiResponse<ListDiscordPinnedMessages200Response> listDiscordPinnedMessages listDiscordPinnedMessagesWithHttpInfo(channelId, accountId)

List pinned messages

Returns the channel&#39;s pinned messages, sorted most-recently-pinned first. Discord caps a channel at 50 pinned messages and returns the full list unpaginated.  Bot needs READ_MESSAGE_HISTORY in the channel (granted by default BOT_PERMISSIONS). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | Discord channel snowflake.
        String accountId = "accountId_example"; // String | SocialAccount _id of any Discord account in the same guild.
        try {
            ApiResponse<ListDiscordPinnedMessages200Response> response = apiInstance.listDiscordPinnedMessagesWithHttpInfo(channelId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordPinnedMessages");
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
| **channelId** | **String**| Discord channel snowflake. | |
| **accountId** | **String**| SocialAccount _id of any Discord account in the same guild. | |

### Return type

ApiResponse<[**ListDiscordPinnedMessages200Response**](ListDiscordPinnedMessages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pinned messages. |  -  |
| **400** | Invalid channelId or accountId format. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not accessible. |  -  |
| **502** | Bot lacks access to the channel. |  -  |


## listDiscordScheduledEvents

> ListDiscordScheduledEvents200Response listDiscordScheduledEvents(guildId, accountId, withUserCount)

List Discord scheduled events

Return all scheduled events in the guild. Events are distinct from messages — they appear in the server&#39;s Events panel and Discord auto-notifies interested members ahead of start time.  Pass &#x60;withUserCount&#x3D;true&#x60; to include &#x60;user_count&#x60; (number of members who RSVP&#39;d) on each event. Useful for surfacing engagement. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Boolean withUserCount = true; // Boolean | Include user_count on each event.
        try {
            ListDiscordScheduledEvents200Response result = apiInstance.listDiscordScheduledEvents(guildId, accountId, withUserCount);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordScheduledEvents");
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
| **guildId** | **String**|  | |
| **accountId** | **String**|  | |
| **withUserCount** | **Boolean**| Include user_count on each event. | [optional] |

### Return type

[**ListDiscordScheduledEvents200Response**](ListDiscordScheduledEvents200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of scheduled events. |  -  |
| **400** | Invalid params. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |
| **502** | Bot lacks access to the guild&#39;s events. |  -  |

## listDiscordScheduledEventsWithHttpInfo

> ApiResponse<ListDiscordScheduledEvents200Response> listDiscordScheduledEvents listDiscordScheduledEventsWithHttpInfo(guildId, accountId, withUserCount)

List Discord scheduled events

Return all scheduled events in the guild. Events are distinct from messages — they appear in the server&#39;s Events panel and Discord auto-notifies interested members ahead of start time.  Pass &#x60;withUserCount&#x3D;true&#x60; to include &#x60;user_count&#x60; (number of members who RSVP&#39;d) on each event. Useful for surfacing engagement. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Boolean withUserCount = true; // Boolean | Include user_count on each event.
        try {
            ApiResponse<ListDiscordScheduledEvents200Response> response = apiInstance.listDiscordScheduledEventsWithHttpInfo(guildId, accountId, withUserCount);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#listDiscordScheduledEvents");
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
| **guildId** | **String**|  | |
| **accountId** | **String**|  | |
| **withUserCount** | **Boolean**| Include user_count on each event. | [optional] |

### Return type

ApiResponse<[**ListDiscordScheduledEvents200Response**](ListDiscordScheduledEvents200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of scheduled events. |  -  |
| **400** | Invalid params. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |
| **502** | Bot lacks access to the guild&#39;s events. |  -  |


## pinDiscordMessage

> PinDiscordMessage200Response pinDiscordMessage(channelId, messageId, accountId)

Pin a Discord message

Pin a specific message in a channel. Path shape mirrors Discord&#39;s own API (&#x60;PUT /channels/{cid}/pins/{mid}&#x60;).  Idempotent — re-pinning an already-pinned message is a 204 no-op.  Constraints:   - Bot needs MANAGE_MESSAGES in the channel.   - 50-pin cap per channel — hitting it returns 400 (Discord-side).     Caller should unpin one first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | 
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            PinDiscordMessage200Response result = apiInstance.pinDiscordMessage(channelId, messageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#pinDiscordMessage");
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
| **channelId** | **String**|  | |
| **messageId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**PinDiscordMessage200Response**](PinDiscordMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message pinned (or was already pinned — idempotent). |  -  |
| **400** | Validation error or pin cap (50) reached. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_MESSAGES in the channel. |  -  |

## pinDiscordMessageWithHttpInfo

> ApiResponse<PinDiscordMessage200Response> pinDiscordMessage pinDiscordMessageWithHttpInfo(channelId, messageId, accountId)

Pin a Discord message

Pin a specific message in a channel. Path shape mirrors Discord&#39;s own API (&#x60;PUT /channels/{cid}/pins/{mid}&#x60;).  Idempotent — re-pinning an already-pinned message is a 204 no-op.  Constraints:   - Bot needs MANAGE_MESSAGES in the channel.   - 50-pin cap per channel — hitting it returns 400 (Discord-side).     Caller should unpin one first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | 
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<PinDiscordMessage200Response> response = apiInstance.pinDiscordMessageWithHttpInfo(channelId, messageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#pinDiscordMessage");
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
| **channelId** | **String**|  | |
| **messageId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**PinDiscordMessage200Response**](PinDiscordMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message pinned (or was already pinned — idempotent). |  -  |
| **400** | Validation error or pin cap (50) reached. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_MESSAGES in the channel. |  -  |


## removeDiscordMemberRole

> RemoveDiscordMemberRole200Response removeDiscordMemberRole(guildId, userId, roleId, accountId)

Remove a role from a guild member

Remove one role from one member. Idempotent — removing a role the member doesn&#39;t have returns 204 no-op.  Same permission + hierarchy constraints as the PUT counterpart. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String userId = "userId_example"; // String | 
        String roleId = "roleId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            RemoveDiscordMemberRole200Response result = apiInstance.removeDiscordMemberRole(guildId, userId, roleId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#removeDiscordMemberRole");
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
| **guildId** | **String**|  | |
| **userId** | **String**|  | |
| **roleId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**RemoveDiscordMemberRole200Response**](RemoveDiscordMemberRole200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role removed (or was already absent — idempotent). |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |
| **403** | Discord refused the request (permission or hierarchy issue). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## removeDiscordMemberRoleWithHttpInfo

> ApiResponse<RemoveDiscordMemberRole200Response> removeDiscordMemberRole removeDiscordMemberRoleWithHttpInfo(guildId, userId, roleId, accountId)

Remove a role from a guild member

Remove one role from one member. Idempotent — removing a role the member doesn&#39;t have returns 204 no-op.  Same permission + hierarchy constraints as the PUT counterpart. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String userId = "userId_example"; // String | 
        String roleId = "roleId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<RemoveDiscordMemberRole200Response> response = apiInstance.removeDiscordMemberRoleWithHttpInfo(guildId, userId, roleId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#removeDiscordMemberRole");
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
| **guildId** | **String**|  | |
| **userId** | **String**|  | |
| **roleId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**RemoveDiscordMemberRole200Response**](RemoveDiscordMemberRole200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role removed (or was already absent — idempotent). |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not in this guild. |  -  |
| **403** | Discord refused the request (permission or hierarchy issue). |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## sendDiscordDirectMessage

> SendDiscordDirectMessage200Response sendDiscordDirectMessage(sendDiscordDirectMessageRequest)

Send a Discord Direct Message

Send a 1:1 Direct Message from the bot to a Discord user (by snowflake ID). Supports the same payload shape as channel posts — content, embeds, media attachments, and TTS.  Constraints (Discord platform limits):   - The bot can only DM users it shares at least one guild with.   - If the recipient has DMs disabled for non-friends, Discord returns 403     (surfaces as a 502 platform error).   - &#x60;content&#x60; capped at 2,000 chars.   - At least one of &#x60;content&#x60;, &#x60;embeds&#x60;, or &#x60;attachments&#x60; is required.   - The recipient must be identified by Discord snowflake ID (not username).  This is a dedicated endpoint rather than a &#x60;POST /v1/posts&#x60; variant because DMs are 1:1 operational messages (onboarding, billing reminders, support pings) with a different lifecycle than scheduled channel posts. DMs are not persisted to &#x60;Post&#x60; / &#x60;ExternalPost&#x60; and are always sent immediately. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        SendDiscordDirectMessageRequest sendDiscordDirectMessageRequest = new SendDiscordDirectMessageRequest(); // SendDiscordDirectMessageRequest | 
        try {
            SendDiscordDirectMessage200Response result = apiInstance.sendDiscordDirectMessage(sendDiscordDirectMessageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#sendDiscordDirectMessage");
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
| **sendDiscordDirectMessageRequest** | [**SendDiscordDirectMessageRequest**](SendDiscordDirectMessageRequest.md)|  | |

### Return type

[**SendDiscordDirectMessage200Response**](SendDiscordDirectMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DM sent successfully. |  -  |
| **400** | Validation error (missing required fields, content &gt; 2000 chars, malformed snowflake, or all of content/embeds/attachments missing). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not accessible to this user. |  -  |
| **403** | Discord refused the message (most commonly: bot doesn&#39;t share a guild with the recipient, OR the recipient has DMs disabled). Error body contains Discord&#39;s response. |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## sendDiscordDirectMessageWithHttpInfo

> ApiResponse<SendDiscordDirectMessage200Response> sendDiscordDirectMessage sendDiscordDirectMessageWithHttpInfo(sendDiscordDirectMessageRequest)

Send a Discord Direct Message

Send a 1:1 Direct Message from the bot to a Discord user (by snowflake ID). Supports the same payload shape as channel posts — content, embeds, media attachments, and TTS.  Constraints (Discord platform limits):   - The bot can only DM users it shares at least one guild with.   - If the recipient has DMs disabled for non-friends, Discord returns 403     (surfaces as a 502 platform error).   - &#x60;content&#x60; capped at 2,000 chars.   - At least one of &#x60;content&#x60;, &#x60;embeds&#x60;, or &#x60;attachments&#x60; is required.   - The recipient must be identified by Discord snowflake ID (not username).  This is a dedicated endpoint rather than a &#x60;POST /v1/posts&#x60; variant because DMs are 1:1 operational messages (onboarding, billing reminders, support pings) with a different lifecycle than scheduled channel posts. DMs are not persisted to &#x60;Post&#x60; / &#x60;ExternalPost&#x60; and are always sent immediately. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        SendDiscordDirectMessageRequest sendDiscordDirectMessageRequest = new SendDiscordDirectMessageRequest(); // SendDiscordDirectMessageRequest | 
        try {
            ApiResponse<SendDiscordDirectMessage200Response> response = apiInstance.sendDiscordDirectMessageWithHttpInfo(sendDiscordDirectMessageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#sendDiscordDirectMessage");
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
| **sendDiscordDirectMessageRequest** | [**SendDiscordDirectMessageRequest**](SendDiscordDirectMessageRequest.md)|  | |

### Return type

ApiResponse<[**SendDiscordDirectMessage200Response**](SendDiscordDirectMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DM sent successfully. |  -  |
| **400** | Validation error (missing required fields, content &gt; 2000 chars, malformed snowflake, or all of content/embeds/attachments missing). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found or not accessible to this user. |  -  |
| **403** | Discord refused the message (most commonly: bot doesn&#39;t share a guild with the recipient, OR the recipient has DMs disabled). Error body contains Discord&#39;s response. |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## unpinDiscordMessage

> UnpinDiscordMessage200Response unpinDiscordMessage(channelId, messageId, accountId)

Unpin a Discord message

Unpin a message. Same MANAGE_MESSAGES permission requirement as pin. Idempotent — unpinning a non-pinned message is a 204 no-op. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | 
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            UnpinDiscordMessage200Response result = apiInstance.unpinDiscordMessage(channelId, messageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#unpinDiscordMessage");
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
| **channelId** | **String**|  | |
| **messageId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**UnpinDiscordMessage200Response**](UnpinDiscordMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message unpinned (or was not pinned — idempotent). |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_MESSAGES in the channel. |  -  |

## unpinDiscordMessageWithHttpInfo

> ApiResponse<UnpinDiscordMessage200Response> unpinDiscordMessage unpinDiscordMessageWithHttpInfo(channelId, messageId, accountId)

Unpin a Discord message

Unpin a message. Same MANAGE_MESSAGES permission requirement as pin. Idempotent — unpinning a non-pinned message is a 204 no-op. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String channelId = "channelId_example"; // String | 
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<UnpinDiscordMessage200Response> response = apiInstance.unpinDiscordMessageWithHttpInfo(channelId, messageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#unpinDiscordMessage");
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
| **channelId** | **String**|  | |
| **messageId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**UnpinDiscordMessage200Response**](UnpinDiscordMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message unpinned (or was not pinned — idempotent). |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found. |  -  |
| **502** | Bot lacks MANAGE_MESSAGES in the channel. |  -  |


## updateDiscordScheduledEvent

> CreateDiscordScheduledEvent200Response updateDiscordScheduledEvent(guildId, eventId, updateDiscordScheduledEventRequest)

Update a Discord scheduled event

Patch any subset of fields. Passing &#x60;status: &#39;cancelled&#39;&#x60; is how you cancel an event — Discord doesn&#39;t have a dedicated cancel endpoint, it&#39;s a status transition.  Most status transitions Discord enforces (you can&#39;t go SCHEDULED → COMPLETED directly). The common consumer case is SCHEDULED → CANCELED. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String eventId = "eventId_example"; // String | 
        UpdateDiscordScheduledEventRequest updateDiscordScheduledEventRequest = new UpdateDiscordScheduledEventRequest(); // UpdateDiscordScheduledEventRequest | 
        try {
            CreateDiscordScheduledEvent200Response result = apiInstance.updateDiscordScheduledEvent(guildId, eventId, updateDiscordScheduledEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#updateDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **eventId** | **String**|  | |
| **updateDiscordScheduledEventRequest** | [**UpdateDiscordScheduledEventRequest**](UpdateDiscordScheduledEventRequest.md)|  | |

### Return type

[**CreateDiscordScheduledEvent200Response**](CreateDiscordScheduledEvent200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event updated. |  -  |
| **400** | Validation error, no updatable fields beyond accountId provided, or Discord rejected the update (invalid status transition). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Discord refused the update (bot permissions). |  -  |
| **404** | Event or Discord account not found. |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |

## updateDiscordScheduledEventWithHttpInfo

> ApiResponse<CreateDiscordScheduledEvent200Response> updateDiscordScheduledEvent updateDiscordScheduledEventWithHttpInfo(guildId, eventId, updateDiscordScheduledEventRequest)

Update a Discord scheduled event

Patch any subset of fields. Passing &#x60;status: &#39;cancelled&#39;&#x60; is how you cancel an event — Discord doesn&#39;t have a dedicated cancel endpoint, it&#39;s a status transition.  Most status transitions Discord enforces (you can&#39;t go SCHEDULED → COMPLETED directly). The common consumer case is SCHEDULED → CANCELED. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String guildId = "guildId_example"; // String | 
        String eventId = "eventId_example"; // String | 
        UpdateDiscordScheduledEventRequest updateDiscordScheduledEventRequest = new UpdateDiscordScheduledEventRequest(); // UpdateDiscordScheduledEventRequest | 
        try {
            ApiResponse<CreateDiscordScheduledEvent200Response> response = apiInstance.updateDiscordScheduledEventWithHttpInfo(guildId, eventId, updateDiscordScheduledEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#updateDiscordScheduledEvent");
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
| **guildId** | **String**|  | |
| **eventId** | **String**|  | |
| **updateDiscordScheduledEventRequest** | [**UpdateDiscordScheduledEventRequest**](UpdateDiscordScheduledEventRequest.md)|  | |

### Return type

ApiResponse<[**CreateDiscordScheduledEvent200Response**](CreateDiscordScheduledEvent200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event updated. |  -  |
| **400** | Validation error, no updatable fields beyond accountId provided, or Discord rejected the update (invalid status transition). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Discord refused the update (bot permissions). |  -  |
| **404** | Event or Discord account not found. |  -  |
| **502** | Discord was unreachable or returned an unclassified error. |  -  |


## updateDiscordSettings

> UpdateDiscordSettings200Response updateDiscordSettings(accountId, updateDiscordSettingsRequest)

Update Discord settings

Update Discord account settings. Supports two operations (can be combined):  1. **Webhook identity** - Set the default display name and avatar that appear as the message author on every post. These are account-level defaults; individual posts can override them via platformSpecificData.webhookUsername / webhookAvatarUrl.  2. **Switch channel** - Move the connection to a different channel in the same guild. A new webhook is automatically created in the target channel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateDiscordSettingsRequest updateDiscordSettingsRequest = new UpdateDiscordSettingsRequest(); // UpdateDiscordSettingsRequest | 
        try {
            UpdateDiscordSettings200Response result = apiInstance.updateDiscordSettings(accountId, updateDiscordSettingsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#updateDiscordSettings");
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
| **accountId** | **String**|  | |
| **updateDiscordSettingsRequest** | [**UpdateDiscordSettingsRequest**](UpdateDiscordSettingsRequest.md)|  | |

### Return type

[**UpdateDiscordSettings200Response**](UpdateDiscordSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings updated |  -  |
| **400** | Invalid request (no changes, invalid channel type, or bot cannot access channel) |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found |  -  |

## updateDiscordSettingsWithHttpInfo

> ApiResponse<UpdateDiscordSettings200Response> updateDiscordSettings updateDiscordSettingsWithHttpInfo(accountId, updateDiscordSettingsRequest)

Update Discord settings

Update Discord account settings. Supports two operations (can be combined):  1. **Webhook identity** - Set the default display name and avatar that appear as the message author on every post. These are account-level defaults; individual posts can override them via platformSpecificData.webhookUsername / webhookAvatarUrl.  2. **Switch channel** - Move the connection to a different channel in the same guild. A new webhook is automatically created in the target channel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateDiscordSettingsRequest updateDiscordSettingsRequest = new UpdateDiscordSettingsRequest(); // UpdateDiscordSettingsRequest | 
        try {
            ApiResponse<UpdateDiscordSettings200Response> response = apiInstance.updateDiscordSettingsWithHttpInfo(accountId, updateDiscordSettingsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#updateDiscordSettings");
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
| **accountId** | **String**|  | |
| **updateDiscordSettingsRequest** | [**UpdateDiscordSettingsRequest**](UpdateDiscordSettingsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateDiscordSettings200Response**](UpdateDiscordSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings updated |  -  |
| **400** | Invalid request (no changes, invalid channel type, or bot cannot access channel) |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found |  -  |

