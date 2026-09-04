# ConnectApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignGoogleBusinessLocation**](ConnectApi.md#assignGoogleBusinessLocation) | **POST** /v1/accounts/{accountId}/gmb-locations/assign | Assign GBP location to another profile |
| [**assignGoogleBusinessLocationWithHttpInfo**](ConnectApi.md#assignGoogleBusinessLocationWithHttpInfo) | **POST** /v1/accounts/{accountId}/gmb-locations/assign | Assign GBP location to another profile |
| [**completeTelegramConnect**](ConnectApi.md#completeTelegramConnect) | **PATCH** /v1/connect/telegram | Check Telegram status |
| [**completeTelegramConnectWithHttpInfo**](ConnectApi.md#completeTelegramConnectWithHttpInfo) | **PATCH** /v1/connect/telegram | Check Telegram status |
| [**completeWhatsAppPhoneSelection**](ConnectApi.md#completeWhatsAppPhoneSelection) | **POST** /v1/connect/whatsapp/select-phone-number | Complete number selection |
| [**completeWhatsAppPhoneSelectionWithHttpInfo**](ConnectApi.md#completeWhatsAppPhoneSelectionWithHttpInfo) | **POST** /v1/connect/whatsapp/select-phone-number | Complete number selection |
| [**configureTikTokAdsBrandIdentity**](ConnectApi.md#configureTikTokAdsBrandIdentity) | **PATCH** /v1/connect/tiktok-ads | Set TikTok brand identity |
| [**configureTikTokAdsBrandIdentityWithHttpInfo**](ConnectApi.md#configureTikTokAdsBrandIdentityWithHttpInfo) | **PATCH** /v1/connect/tiktok-ads | Set TikTok brand identity |
| [**connectAds**](ConnectApi.md#connectAds) | **GET** /v1/connect/{platform}/ads | Connect ads for a platform |
| [**connectAdsWithHttpInfo**](ConnectApi.md#connectAdsWithHttpInfo) | **GET** /v1/connect/{platform}/ads | Connect ads for a platform |
| [**connectBlueskyCredentials**](ConnectApi.md#connectBlueskyCredentials) | **POST** /v1/connect/bluesky/credentials | Connect Bluesky account |
| [**connectBlueskyCredentialsWithHttpInfo**](ConnectApi.md#connectBlueskyCredentialsWithHttpInfo) | **POST** /v1/connect/bluesky/credentials | Connect Bluesky account |
| [**connectDiscordChannel**](ConnectApi.md#connectDiscordChannel) | **POST** /v1/connect/discord | Connect a Discord channel |
| [**connectDiscordChannelWithHttpInfo**](ConnectApi.md#connectDiscordChannelWithHttpInfo) | **POST** /v1/connect/discord | Connect a Discord channel |
| [**connectOpenAIAdsCredentials**](ConnectApi.md#connectOpenAIAdsCredentials) | **POST** /v1/connect/openai-ads/credentials | Connect an OpenAI Ads account |
| [**connectOpenAIAdsCredentialsWithHttpInfo**](ConnectApi.md#connectOpenAIAdsCredentialsWithHttpInfo) | **POST** /v1/connect/openai-ads/credentials | Connect an OpenAI Ads account |
| [**connectShopifyWithToken**](ConnectApi.md#connectShopifyWithToken) | **POST** /v1/connect/shopify/token | Connect a Shopify store with a custom-app Admin token |
| [**connectShopifyWithTokenWithHttpInfo**](ConnectApi.md#connectShopifyWithTokenWithHttpInfo) | **POST** /v1/connect/shopify/token | Connect a Shopify store with a custom-app Admin token |
| [**connectSlackChannel**](ConnectApi.md#connectSlackChannel) | **POST** /v1/connect/slack | Connect a Slack channel |
| [**connectSlackChannelWithHttpInfo**](ConnectApi.md#connectSlackChannelWithHttpInfo) | **POST** /v1/connect/slack | Connect a Slack channel |
| [**connectWhatsAppCredentials**](ConnectApi.md#connectWhatsAppCredentials) | **POST** /v1/connect/whatsapp/credentials | Connect WhatsApp via credentials |
| [**connectWhatsAppCredentialsWithHttpInfo**](ConnectApi.md#connectWhatsAppCredentialsWithHttpInfo) | **POST** /v1/connect/whatsapp/credentials | Connect WhatsApp via credentials |
| [**connectWhatsAppEmbeddedSignup**](ConnectApi.md#connectWhatsAppEmbeddedSignup) | **POST** /v1/connect/whatsapp/embedded-signup | Connect WhatsApp from Embedded Signup |
| [**connectWhatsAppEmbeddedSignupWithHttpInfo**](ConnectApi.md#connectWhatsAppEmbeddedSignupWithHttpInfo) | **POST** /v1/connect/whatsapp/embedded-signup | Connect WhatsApp from Embedded Signup |
| [**createPinterestBoard**](ConnectApi.md#createPinterestBoard) | **POST** /v1/accounts/{accountId}/pinterest-boards | Create Pinterest board |
| [**createPinterestBoardWithHttpInfo**](ConnectApi.md#createPinterestBoardWithHttpInfo) | **POST** /v1/accounts/{accountId}/pinterest-boards | Create Pinterest board |
| [**getConnectUrl**](ConnectApi.md#getConnectUrl) | **GET** /v1/connect/{platform} | Get OAuth connect URL |
| [**getConnectUrlWithHttpInfo**](ConnectApi.md#getConnectUrlWithHttpInfo) | **GET** /v1/connect/{platform} | Get OAuth connect URL |
| [**getFacebookPages**](ConnectApi.md#getFacebookPages) | **GET** /v1/accounts/{accountId}/facebook-page | List Facebook pages |
| [**getFacebookPagesWithHttpInfo**](ConnectApi.md#getFacebookPagesWithHttpInfo) | **GET** /v1/accounts/{accountId}/facebook-page | List Facebook pages |
| [**getGmbLocations**](ConnectApi.md#getGmbLocations) | **GET** /v1/accounts/{accountId}/gmb-locations | List GBP locations |
| [**getGmbLocationsWithHttpInfo**](ConnectApi.md#getGmbLocationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-locations | List GBP locations |
| [**getLinkedInOrganizations**](ConnectApi.md#getLinkedInOrganizations) | **GET** /v1/accounts/{accountId}/linkedin-organizations | List LinkedIn orgs |
| [**getLinkedInOrganizationsWithHttpInfo**](ConnectApi.md#getLinkedInOrganizationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/linkedin-organizations | List LinkedIn orgs |
| [**getPendingOAuthData**](ConnectApi.md#getPendingOAuthData) | **GET** /v1/connect/pending-data | Get pending OAuth data |
| [**getPendingOAuthDataWithHttpInfo**](ConnectApi.md#getPendingOAuthDataWithHttpInfo) | **GET** /v1/connect/pending-data | Get pending OAuth data |
| [**getPinterestBoards**](ConnectApi.md#getPinterestBoards) | **GET** /v1/accounts/{accountId}/pinterest-boards | List Pinterest boards |
| [**getPinterestBoardsWithHttpInfo**](ConnectApi.md#getPinterestBoardsWithHttpInfo) | **GET** /v1/accounts/{accountId}/pinterest-boards | List Pinterest boards |
| [**getRedditFlairs**](ConnectApi.md#getRedditFlairs) | **GET** /v1/accounts/{accountId}/reddit-flairs | List subreddit flairs |
| [**getRedditFlairsWithHttpInfo**](ConnectApi.md#getRedditFlairsWithHttpInfo) | **GET** /v1/accounts/{accountId}/reddit-flairs | List subreddit flairs |
| [**getRedditSubreddits**](ConnectApi.md#getRedditSubreddits) | **GET** /v1/accounts/{accountId}/reddit-subreddits | List Reddit subreddits |
| [**getRedditSubredditsWithHttpInfo**](ConnectApi.md#getRedditSubredditsWithHttpInfo) | **GET** /v1/accounts/{accountId}/reddit-subreddits | List Reddit subreddits |
| [**getShopifyConnectUrl**](ConnectApi.md#getShopifyConnectUrl) | **GET** /v1/connect/shopify | Get Shopify OAuth connect URL |
| [**getShopifyConnectUrlWithHttpInfo**](ConnectApi.md#getShopifyConnectUrlWithHttpInfo) | **GET** /v1/connect/shopify | Get Shopify OAuth connect URL |
| [**getSubredditRules**](ConnectApi.md#getSubredditRules) | **GET** /v1/accounts/{accountId}/reddit-subreddits/{subreddit}/rules | Get subreddit rules |
| [**getSubredditRulesWithHttpInfo**](ConnectApi.md#getSubredditRulesWithHttpInfo) | **GET** /v1/accounts/{accountId}/reddit-subreddits/{subreddit}/rules | Get subreddit rules |
| [**getTelegramConnectStatus**](ConnectApi.md#getTelegramConnectStatus) | **GET** /v1/connect/telegram | Generate Telegram code |
| [**getTelegramConnectStatusWithHttpInfo**](ConnectApi.md#getTelegramConnectStatusWithHttpInfo) | **GET** /v1/connect/telegram | Generate Telegram code |
| [**getYoutubeCaptions**](ConnectApi.md#getYoutubeCaptions) | **GET** /v1/accounts/{accountId}/youtube-captions | Get a YouTube video transcript |
| [**getYoutubeCaptionsWithHttpInfo**](ConnectApi.md#getYoutubeCaptionsWithHttpInfo) | **GET** /v1/accounts/{accountId}/youtube-captions | Get a YouTube video transcript |
| [**getYoutubePlaylists**](ConnectApi.md#getYoutubePlaylists) | **GET** /v1/accounts/{accountId}/youtube-playlists | List YouTube playlists |
| [**getYoutubePlaylistsWithHttpInfo**](ConnectApi.md#getYoutubePlaylistsWithHttpInfo) | **GET** /v1/accounts/{accountId}/youtube-playlists | List YouTube playlists |
| [**handleOAuthCallback**](ConnectApi.md#handleOAuthCallback) | **POST** /v1/connect/{platform} | Complete OAuth callback |
| [**handleOAuthCallbackWithHttpInfo**](ConnectApi.md#handleOAuthCallbackWithHttpInfo) | **POST** /v1/connect/{platform} | Complete OAuth callback |
| [**initiateTelegramConnect**](ConnectApi.md#initiateTelegramConnect) | **POST** /v1/connect/telegram | Connect Telegram directly |
| [**initiateTelegramConnectWithHttpInfo**](ConnectApi.md#initiateTelegramConnectWithHttpInfo) | **POST** /v1/connect/telegram | Connect Telegram directly |
| [**listFacebookPages**](ConnectApi.md#listFacebookPages) | **GET** /v1/connect/facebook/select-page | List Facebook pages |
| [**listFacebookPagesWithHttpInfo**](ConnectApi.md#listFacebookPagesWithHttpInfo) | **GET** /v1/connect/facebook/select-page | List Facebook pages |
| [**listGoogleBusinessLocations**](ConnectApi.md#listGoogleBusinessLocations) | **GET** /v1/connect/googlebusiness/locations | List GBP locations |
| [**listGoogleBusinessLocationsWithHttpInfo**](ConnectApi.md#listGoogleBusinessLocationsWithHttpInfo) | **GET** /v1/connect/googlebusiness/locations | List GBP locations |
| [**listInstagramPages**](ConnectApi.md#listInstagramPages) | **GET** /v1/connect/instagram/select-account | List Pages with a linked Instagram account |
| [**listInstagramPagesWithHttpInfo**](ConnectApi.md#listInstagramPagesWithHttpInfo) | **GET** /v1/connect/instagram/select-account | List Pages with a linked Instagram account |
| [**listLinkedInOrganizations**](ConnectApi.md#listLinkedInOrganizations) | **GET** /v1/connect/linkedin/organizations | List LinkedIn orgs |
| [**listLinkedInOrganizationsWithHttpInfo**](ConnectApi.md#listLinkedInOrganizationsWithHttpInfo) | **GET** /v1/connect/linkedin/organizations | List LinkedIn orgs |
| [**listPinterestBoardsForSelection**](ConnectApi.md#listPinterestBoardsForSelection) | **GET** /v1/connect/pinterest/select-board | List Pinterest boards |
| [**listPinterestBoardsForSelectionWithHttpInfo**](ConnectApi.md#listPinterestBoardsForSelectionWithHttpInfo) | **GET** /v1/connect/pinterest/select-board | List Pinterest boards |
| [**listSnapchatProfiles**](ConnectApi.md#listSnapchatProfiles) | **GET** /v1/connect/snapchat/select-profile | List Snapchat profiles |
| [**listSnapchatProfilesWithHttpInfo**](ConnectApi.md#listSnapchatProfilesWithHttpInfo) | **GET** /v1/connect/snapchat/select-profile | List Snapchat profiles |
| [**listWhatsAppPhoneNumbers**](ConnectApi.md#listWhatsAppPhoneNumbers) | **GET** /v1/connect/whatsapp/select-phone-number | List numbers for selection |
| [**listWhatsAppPhoneNumbersWithHttpInfo**](ConnectApi.md#listWhatsAppPhoneNumbersWithHttpInfo) | **GET** /v1/connect/whatsapp/select-phone-number | List numbers for selection |
| [**selectFacebookPage**](ConnectApi.md#selectFacebookPage) | **POST** /v1/connect/facebook/select-page | Select Facebook page |
| [**selectFacebookPageWithHttpInfo**](ConnectApi.md#selectFacebookPageWithHttpInfo) | **POST** /v1/connect/facebook/select-page | Select Facebook page |
| [**selectGoogleBusinessLocation**](ConnectApi.md#selectGoogleBusinessLocation) | **POST** /v1/connect/googlebusiness/select-location | Select GBP location |
| [**selectGoogleBusinessLocationWithHttpInfo**](ConnectApi.md#selectGoogleBusinessLocationWithHttpInfo) | **POST** /v1/connect/googlebusiness/select-location | Select GBP location |
| [**selectInstagramAccount**](ConnectApi.md#selectInstagramAccount) | **POST** /v1/connect/instagram/select-account | Select the Page whose Instagram account to connect |
| [**selectInstagramAccountWithHttpInfo**](ConnectApi.md#selectInstagramAccountWithHttpInfo) | **POST** /v1/connect/instagram/select-account | Select the Page whose Instagram account to connect |
| [**selectLinkedInOrganization**](ConnectApi.md#selectLinkedInOrganization) | **POST** /v1/connect/linkedin/select-organization | Select LinkedIn org |
| [**selectLinkedInOrganizationWithHttpInfo**](ConnectApi.md#selectLinkedInOrganizationWithHttpInfo) | **POST** /v1/connect/linkedin/select-organization | Select LinkedIn org |
| [**selectPinterestBoard**](ConnectApi.md#selectPinterestBoard) | **POST** /v1/connect/pinterest/select-board | Select Pinterest board |
| [**selectPinterestBoardWithHttpInfo**](ConnectApi.md#selectPinterestBoardWithHttpInfo) | **POST** /v1/connect/pinterest/select-board | Select Pinterest board |
| [**selectSnapchatProfile**](ConnectApi.md#selectSnapchatProfile) | **POST** /v1/connect/snapchat/select-profile | Select Snapchat profile |
| [**selectSnapchatProfileWithHttpInfo**](ConnectApi.md#selectSnapchatProfileWithHttpInfo) | **POST** /v1/connect/snapchat/select-profile | Select Snapchat profile |
| [**setRedditPostFlair**](ConnectApi.md#setRedditPostFlair) | **POST** /v1/accounts/{accountId}/reddit-flairs | Set Reddit post flair |
| [**setRedditPostFlairWithHttpInfo**](ConnectApi.md#setRedditPostFlairWithHttpInfo) | **POST** /v1/accounts/{accountId}/reddit-flairs | Set Reddit post flair |
| [**updateFacebookPage**](ConnectApi.md#updateFacebookPage) | **PUT** /v1/accounts/{accountId}/facebook-page | Update Facebook page |
| [**updateFacebookPageWithHttpInfo**](ConnectApi.md#updateFacebookPageWithHttpInfo) | **PUT** /v1/accounts/{accountId}/facebook-page | Update Facebook page |
| [**updateGmbLocation**](ConnectApi.md#updateGmbLocation) | **PUT** /v1/accounts/{accountId}/gmb-locations | Update GBP location |
| [**updateGmbLocationWithHttpInfo**](ConnectApi.md#updateGmbLocationWithHttpInfo) | **PUT** /v1/accounts/{accountId}/gmb-locations | Update GBP location |
| [**updateLinkedInOrganization**](ConnectApi.md#updateLinkedInOrganization) | **PUT** /v1/accounts/{accountId}/linkedin-organization | Switch LinkedIn account type |
| [**updateLinkedInOrganizationWithHttpInfo**](ConnectApi.md#updateLinkedInOrganizationWithHttpInfo) | **PUT** /v1/accounts/{accountId}/linkedin-organization | Switch LinkedIn account type |
| [**updatePinterestBoards**](ConnectApi.md#updatePinterestBoards) | **PUT** /v1/accounts/{accountId}/pinterest-boards | Set default Pinterest board |
| [**updatePinterestBoardsWithHttpInfo**](ConnectApi.md#updatePinterestBoardsWithHttpInfo) | **PUT** /v1/accounts/{accountId}/pinterest-boards | Set default Pinterest board |
| [**updateRedditSubreddits**](ConnectApi.md#updateRedditSubreddits) | **PUT** /v1/accounts/{accountId}/reddit-subreddits | Set default subreddit |
| [**updateRedditSubredditsWithHttpInfo**](ConnectApi.md#updateRedditSubredditsWithHttpInfo) | **PUT** /v1/accounts/{accountId}/reddit-subreddits | Set default subreddit |
| [**updateYoutubeDefaultPlaylist**](ConnectApi.md#updateYoutubeDefaultPlaylist) | **PUT** /v1/accounts/{accountId}/youtube-playlists | Set default YouTube playlist |
| [**updateYoutubeDefaultPlaylistWithHttpInfo**](ConnectApi.md#updateYoutubeDefaultPlaylistWithHttpInfo) | **PUT** /v1/accounts/{accountId}/youtube-playlists | Set default YouTube playlist |
| [**voteRedditThing**](ConnectApi.md#voteRedditThing) | **POST** /v1/accounts/{accountId}/reddit-vote | Vote on a Reddit post or comment |
| [**voteRedditThingWithHttpInfo**](ConnectApi.md#voteRedditThingWithHttpInfo) | **POST** /v1/accounts/{accountId}/reddit-vote | Vote on a Reddit post or comment |



## assignGoogleBusinessLocation

> AssignGoogleBusinessLocation200Response assignGoogleBusinessLocation(accountId, assignGoogleBusinessLocationRequest)

Assign GBP location to another profile

Connect a Google Business location onto a DIFFERENT profile by reusing the OAuth grant from an already-connected GBP account — no browser, no re-authorization. Built for agencies whose single Google account has manager access to many client locations and who run one profile per client: connect one location the normal way (browser OAuth), then bulk-assign the rest onto each client&#39;s profile via this endpoint. The path &#x60;accountId&#x60; is a SOURCE connected GBP account (the token holder); the body &#x60;profileId&#x60; is the TARGET profile. Returns 409 if the target profile already has a Google Business connection (switch its location with PUT gmb-locations instead). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | A source connected GBP account whose OAuth grant is reused.
        AssignGoogleBusinessLocationRequest assignGoogleBusinessLocationRequest = new AssignGoogleBusinessLocationRequest(); // AssignGoogleBusinessLocationRequest | 
        try {
            AssignGoogleBusinessLocation200Response result = apiInstance.assignGoogleBusinessLocation(accountId, assignGoogleBusinessLocationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#assignGoogleBusinessLocation");
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
| **accountId** | **String**| A source connected GBP account whose OAuth grant is reused. | |
| **assignGoogleBusinessLocationRequest** | [**AssignGoogleBusinessLocationRequest**](AssignGoogleBusinessLocationRequest.md)|  | |

### Return type

[**AssignGoogleBusinessLocation200Response**](AssignGoogleBusinessLocation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Location assigned to the target profile |  -  |
| **400** | Invalid body, selected location not found under the Google account, or the provided googleAccountId is not one of the accounts this connection manages |  -  |
| **401** | Unauthorized |  -  |
| **403** | Payment required, or target profile exceeds plan limit |  -  |
| **404** | Source Google Business account not found |  -  |
| **409** | Target profile already has a Google Business connection (use PUT gmb-locations to switch its location) |  -  |

## assignGoogleBusinessLocationWithHttpInfo

> ApiResponse<AssignGoogleBusinessLocation200Response> assignGoogleBusinessLocation assignGoogleBusinessLocationWithHttpInfo(accountId, assignGoogleBusinessLocationRequest)

Assign GBP location to another profile

Connect a Google Business location onto a DIFFERENT profile by reusing the OAuth grant from an already-connected GBP account — no browser, no re-authorization. Built for agencies whose single Google account has manager access to many client locations and who run one profile per client: connect one location the normal way (browser OAuth), then bulk-assign the rest onto each client&#39;s profile via this endpoint. The path &#x60;accountId&#x60; is a SOURCE connected GBP account (the token holder); the body &#x60;profileId&#x60; is the TARGET profile. Returns 409 if the target profile already has a Google Business connection (switch its location with PUT gmb-locations instead). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | A source connected GBP account whose OAuth grant is reused.
        AssignGoogleBusinessLocationRequest assignGoogleBusinessLocationRequest = new AssignGoogleBusinessLocationRequest(); // AssignGoogleBusinessLocationRequest | 
        try {
            ApiResponse<AssignGoogleBusinessLocation200Response> response = apiInstance.assignGoogleBusinessLocationWithHttpInfo(accountId, assignGoogleBusinessLocationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#assignGoogleBusinessLocation");
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
| **accountId** | **String**| A source connected GBP account whose OAuth grant is reused. | |
| **assignGoogleBusinessLocationRequest** | [**AssignGoogleBusinessLocationRequest**](AssignGoogleBusinessLocationRequest.md)|  | |

### Return type

ApiResponse<[**AssignGoogleBusinessLocation200Response**](AssignGoogleBusinessLocation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Location assigned to the target profile |  -  |
| **400** | Invalid body, selected location not found under the Google account, or the provided googleAccountId is not one of the accounts this connection manages |  -  |
| **401** | Unauthorized |  -  |
| **403** | Payment required, or target profile exceeds plan limit |  -  |
| **404** | Source Google Business account not found |  -  |
| **409** | Target profile already has a Google Business connection (use PUT gmb-locations to switch its location) |  -  |


## completeTelegramConnect

> CompleteTelegramConnect200Response completeTelegramConnect(code)

Check Telegram status

Poll this endpoint to check if a Telegram access code has been used to connect a channel/group. Recommended polling interval: 3 seconds. Status values: pending (waiting for user), connected (channel/group linked), expired (generate a new code). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String code = "ZRN-ABC123"; // String | The access code to check status for
        try {
            CompleteTelegramConnect200Response result = apiInstance.completeTelegramConnect(code);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#completeTelegramConnect");
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
| **code** | **String**| The access code to check status for | |

### Return type

[**CompleteTelegramConnect200Response**](CompleteTelegramConnect200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Code not found |  -  |
| **500** | Internal error |  -  |

## completeTelegramConnectWithHttpInfo

> ApiResponse<CompleteTelegramConnect200Response> completeTelegramConnect completeTelegramConnectWithHttpInfo(code)

Check Telegram status

Poll this endpoint to check if a Telegram access code has been used to connect a channel/group. Recommended polling interval: 3 seconds. Status values: pending (waiting for user), connected (channel/group linked), expired (generate a new code). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String code = "ZRN-ABC123"; // String | The access code to check status for
        try {
            ApiResponse<CompleteTelegramConnect200Response> response = apiInstance.completeTelegramConnectWithHttpInfo(code);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#completeTelegramConnect");
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
| **code** | **String**| The access code to check status for | |

### Return type

ApiResponse<[**CompleteTelegramConnect200Response**](CompleteTelegramConnect200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Code not found |  -  |
| **500** | Internal error |  -  |


## completeWhatsAppPhoneSelection

> CompleteWhatsAppPhoneSelection200Response completeWhatsAppPhoneSelection(completeWhatsAppPhoneSelectionRequest, xConnectToken)

Complete number selection

Bind a specific WhatsApp phone number to the Zernio profile after the user picks one from &#x60;listWhatsAppPhoneNumbers&#x60;. Exchanges the short-lived OAuth token for a long-lived token, subscribes the WABA to webhooks, and creates the SocialAccount. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        CompleteWhatsAppPhoneSelectionRequest completeWhatsAppPhoneSelectionRequest = new CompleteWhatsAppPhoneSelectionRequest(); // CompleteWhatsAppPhoneSelectionRequest | 
        String xConnectToken = "xConnectToken_example"; // String | Alternative auth for API users' end customers
        try {
            CompleteWhatsAppPhoneSelection200Response result = apiInstance.completeWhatsAppPhoneSelection(completeWhatsAppPhoneSelectionRequest, xConnectToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#completeWhatsAppPhoneSelection");
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
| **completeWhatsAppPhoneSelectionRequest** | [**CompleteWhatsAppPhoneSelectionRequest**](CompleteWhatsAppPhoneSelectionRequest.md)|  | |
| **xConnectToken** | **String**| Alternative auth for API users&#39; end customers | [optional] |

### Return type

[**CompleteWhatsAppPhoneSelection200Response**](CompleteWhatsAppPhoneSelection200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number connected successfully |  -  |
| **400** | Missing required fields (profileId, phoneNumberId, wabaId, or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Profile limit exceeded for the user&#39;s plan (PROFILE_LIMIT_EXCEEDED) |  -  |
| **404** | Selected phone number not found in the specified WABA |  -  |
| **409** | Conflict with an existing connection. Either the phone number is a Zernio-provisioned number pinned to a different profile (code WHATSAPP_NUMBER_PINNED_TO_PROFILE, connect it from that profile or move it first with PATCH /v1/whatsapp/phone-numbers/{id}/profile), or the number is already actively connected on another profile or workspace (code WHATSAPP_NUMBER_ALREADY_CONNECTED, disconnect it there first). A number can only be live on one profile. |  -  |
| **500** | Failed to bind phone number |  -  |

## completeWhatsAppPhoneSelectionWithHttpInfo

> ApiResponse<CompleteWhatsAppPhoneSelection200Response> completeWhatsAppPhoneSelection completeWhatsAppPhoneSelectionWithHttpInfo(completeWhatsAppPhoneSelectionRequest, xConnectToken)

Complete number selection

Bind a specific WhatsApp phone number to the Zernio profile after the user picks one from &#x60;listWhatsAppPhoneNumbers&#x60;. Exchanges the short-lived OAuth token for a long-lived token, subscribes the WABA to webhooks, and creates the SocialAccount. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        CompleteWhatsAppPhoneSelectionRequest completeWhatsAppPhoneSelectionRequest = new CompleteWhatsAppPhoneSelectionRequest(); // CompleteWhatsAppPhoneSelectionRequest | 
        String xConnectToken = "xConnectToken_example"; // String | Alternative auth for API users' end customers
        try {
            ApiResponse<CompleteWhatsAppPhoneSelection200Response> response = apiInstance.completeWhatsAppPhoneSelectionWithHttpInfo(completeWhatsAppPhoneSelectionRequest, xConnectToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#completeWhatsAppPhoneSelection");
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
| **completeWhatsAppPhoneSelectionRequest** | [**CompleteWhatsAppPhoneSelectionRequest**](CompleteWhatsAppPhoneSelectionRequest.md)|  | |
| **xConnectToken** | **String**| Alternative auth for API users&#39; end customers | [optional] |

### Return type

ApiResponse<[**CompleteWhatsAppPhoneSelection200Response**](CompleteWhatsAppPhoneSelection200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number connected successfully |  -  |
| **400** | Missing required fields (profileId, phoneNumberId, wabaId, or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Profile limit exceeded for the user&#39;s plan (PROFILE_LIMIT_EXCEEDED) |  -  |
| **404** | Selected phone number not found in the specified WABA |  -  |
| **409** | Conflict with an existing connection. Either the phone number is a Zernio-provisioned number pinned to a different profile (code WHATSAPP_NUMBER_PINNED_TO_PROFILE, connect it from that profile or move it first with PATCH /v1/whatsapp/phone-numbers/{id}/profile), or the number is already actively connected on another profile or workspace (code WHATSAPP_NUMBER_ALREADY_CONNECTED, disconnect it there first). A number can only be live on one profile. |  -  |
| **500** | Failed to bind phone number |  -  |


## configureTikTokAdsBrandIdentity

> ConfigureTikTokAdsBrandIdentity200Response configureTikTokAdsBrandIdentity(configureTikTokAdsBrandIdentityRequest)

Set TikTok brand identity

Set or update the Brand Identity (display name + avatar) for a &#x60;tiktokads&#x60; SocialAccount. TikTok requires every ad to carry an &#x60;identity_id + identity_type&#x60; pair. The Brand Identity is the CUSTOMIZED_USER alternative to attributing ads to a real @username (TT_USER). This route uploads the supplied image to TikTok, creates the identity via &#x60;/v2/identity/create/&#x60;, and caches the resulting &#x60;identity_id&#x60; on the account so subsequent &#x60;POST /v1/ads/create&#x60; calls can opt into it via &#x60;identityType: &#39;CUSTOMIZED_USER&#39;&#x60;.  Configurable on every &#x60;tiktokads&#x60; account, including linked-mode ones (those with a posting account on the same profile). Configuration is idempotent and harmless when posting is also connected: the default ad-create path still prefers TT_USER, and CUSTOMIZED_USER is only used per-ad when the caller explicitly opts in.  TikTok identities are immutable post-creation. Re-saving creates a new identity on TikTok and swaps the cached id; the old identity stays orphaned on TikTok&#39;s side (harmless, no billing impact).  Alternative: pass &#x60;brandIdentity&#x60; directly on &#x60;POST /v1/ads/create&#x60; to configure on first ad creation in a single round-trip. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConfigureTikTokAdsBrandIdentityRequest configureTikTokAdsBrandIdentityRequest = new ConfigureTikTokAdsBrandIdentityRequest(); // ConfigureTikTokAdsBrandIdentityRequest | 
        try {
            ConfigureTikTokAdsBrandIdentity200Response result = apiInstance.configureTikTokAdsBrandIdentity(configureTikTokAdsBrandIdentityRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#configureTikTokAdsBrandIdentity");
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
| **configureTikTokAdsBrandIdentityRequest** | [**ConfigureTikTokAdsBrandIdentityRequest**](ConfigureTikTokAdsBrandIdentityRequest.md)|  | |

### Return type

[**ConfigureTikTokAdsBrandIdentity200Response**](ConfigureTikTokAdsBrandIdentity200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Brand identity configured (or updated) |  -  |
| **400** | Missing fields, invalid JSON body, invalid accountId format, invalid lengths, or no advertiser found on the account |  -  |
| **401** | Unauthorized |  -  |
| **404** | TikTok Ads account not found |  -  |
| **500** | Unexpected server error while caching the identity |  -  |
| **502** | TikTok rejected the image upload or the identity creation (type: platform_error; an upstream 4xx status is forwarded instead of 502) |  -  |

## configureTikTokAdsBrandIdentityWithHttpInfo

> ApiResponse<ConfigureTikTokAdsBrandIdentity200Response> configureTikTokAdsBrandIdentity configureTikTokAdsBrandIdentityWithHttpInfo(configureTikTokAdsBrandIdentityRequest)

Set TikTok brand identity

Set or update the Brand Identity (display name + avatar) for a &#x60;tiktokads&#x60; SocialAccount. TikTok requires every ad to carry an &#x60;identity_id + identity_type&#x60; pair. The Brand Identity is the CUSTOMIZED_USER alternative to attributing ads to a real @username (TT_USER). This route uploads the supplied image to TikTok, creates the identity via &#x60;/v2/identity/create/&#x60;, and caches the resulting &#x60;identity_id&#x60; on the account so subsequent &#x60;POST /v1/ads/create&#x60; calls can opt into it via &#x60;identityType: &#39;CUSTOMIZED_USER&#39;&#x60;.  Configurable on every &#x60;tiktokads&#x60; account, including linked-mode ones (those with a posting account on the same profile). Configuration is idempotent and harmless when posting is also connected: the default ad-create path still prefers TT_USER, and CUSTOMIZED_USER is only used per-ad when the caller explicitly opts in.  TikTok identities are immutable post-creation. Re-saving creates a new identity on TikTok and swaps the cached id; the old identity stays orphaned on TikTok&#39;s side (harmless, no billing impact).  Alternative: pass &#x60;brandIdentity&#x60; directly on &#x60;POST /v1/ads/create&#x60; to configure on first ad creation in a single round-trip. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConfigureTikTokAdsBrandIdentityRequest configureTikTokAdsBrandIdentityRequest = new ConfigureTikTokAdsBrandIdentityRequest(); // ConfigureTikTokAdsBrandIdentityRequest | 
        try {
            ApiResponse<ConfigureTikTokAdsBrandIdentity200Response> response = apiInstance.configureTikTokAdsBrandIdentityWithHttpInfo(configureTikTokAdsBrandIdentityRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#configureTikTokAdsBrandIdentity");
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
| **configureTikTokAdsBrandIdentityRequest** | [**ConfigureTikTokAdsBrandIdentityRequest**](ConfigureTikTokAdsBrandIdentityRequest.md)|  | |

### Return type

ApiResponse<[**ConfigureTikTokAdsBrandIdentity200Response**](ConfigureTikTokAdsBrandIdentity200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Brand identity configured (or updated) |  -  |
| **400** | Missing fields, invalid JSON body, invalid accountId format, invalid lengths, or no advertiser found on the account |  -  |
| **401** | Unauthorized |  -  |
| **404** | TikTok Ads account not found |  -  |
| **500** | Unexpected server error while caching the identity |  -  |
| **502** | TikTok rejected the image upload or the identity creation (type: platform_error; an upstream 4xx status is forwarded instead of 502) |  -  |


## connectAds

> ConnectAds200Response connectAds(platform, profileId, accountId, redirectUrl, headless, force, adAccountId, adAccountIds)

Connect ads for a platform

Unified ads connection endpoint. Creates a dedicated ads SocialAccount for the specified platform.  Same-token platforms (facebook, instagram, linkedin, pinterest): the ads SocialAccount (metaads, linkedinads, pinterestads) reuses the OAuth token of the parent posting account, but only when an active parent exists and, for facebook and instagram, its stored token carries ads_management and ads_read (linkedin and pinterest need no extra scope). In that case no extra OAuth happens and the response is alreadyConnected: true. When no such parent exists, or the scopes are missing, the endpoint returns an authUrl and a full OAuth round trip is required. When a parent exists but carries no token usable for ad accounts, the call fails with 400 RECONNECT_REQUIRED. Independently of the branch, the call can return 403 ADS_ADDON_REQUIRED without the ads add-on and 402 PAYMENT_REQUIRED when the billing gate is closed.  Meta Ads prerequisite: connecting Meta Ads (via facebook or instagram) requires a Facebook Page. Not because the ad account is read through a Page, but because both parent posting accounts are: the facebook flow only offers Pages you manage, and the instagram flow with loginMethod&#x3D;facebook_login only offers Instagram accounts linked to one of those Pages. Without a Page there is no parent account to inherit a token from. A user who manages no Facebook Page cannot complete this connection, and the facebook flow ends with error&#x3D;no_facebook_pages.  Separate-token platforms (tiktok, twitter): Starts the platform-specific marketing API OAuth flow and creates an ads SocialAccount (tiktokads, xads) with its own token. If the ads account already exists, returns alreadyConnected: true.   - tiktok: accountId is OPTIONAL. With accountId, the new tiktokads account links to that posting account (parentAccountId set) — Spark Ads + standalone ads using the posting TT_USER identity become available. Without accountId, ads-only mode kicks in: the new tiktokads account has parentAccountId&#x3D;null and standalone ads use a synthetic CUSTOMIZED_USER (\&quot;Brand Identity\&quot;); Spark Ads are unavailable because TikTok requires a posting account for them. The Brand Identity is configured separately via PATCH /v1/connect/tiktok-ads (or inline on POST /v1/ads/create via the brandIdentity field).   - twitter (X Ads): accountId is REQUIRED. There&#39;s no ads-only mode — tweets need to be authored by a real X user.  Standalone platforms (googleads): Starts the Google Ads OAuth flow and creates a standalone ads SocialAccount (googleads) with no parent. If the account already exists, returns alreadyConnected: true.  Ads accounts appear as regular SocialAccount documents with ads platform values (e.g., metaads, tiktokads) in GET /v1/accounts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String platform = "facebook"; // String | Platform to connect ads for. Only platforms with ads support are accepted.  `instagram` requires an Instagram account connected with loginMethod=facebook_login whose token carries ads_management and ads_read. With an account connected through the default instagram_login flow no ads account can be created; do not use this value for those accounts. 
        String profileId = "profileId_example"; // String | Your Zernio profile ID
        String accountId = "accountId_example"; // String | Existing SocialAccount ID. Required for `twitter` (X Ads). Optional for `tiktok` — omit to enter ads-only mode (no TikTok posting account linked; ad creation uses a Brand Identity instead of a TT_USER). Ignored for same-token (`facebook`, `instagram`, `linkedin`, `pinterest`) and standalone (`googleads`) platforms. 
        URI redirectUrl = new URI(); // URI | Custom URL the browser is sent to once the OAuth flow finishes. Honored on every ads platform, including the separate-token (`tiktok`, `twitter`) and standalone (`googleads`) flows. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On success `tiktok`, `twitter` and `googleads` land on the URL unchanged, while the same-token platforms (`facebook`, `instagram`, `linkedin`, `pinterest`) append `connected`, `profileId`, `accountId`, `username` and, on API-key calls, `connect_token`. On failure the same error contract applies as on GET /v1/connect/{platform}: `error` and `platform` are always appended, other params are optional, and the value list there is not exhaustive. Note that on the tiktok, twitter and googleads flows `platform` carries the ads platform id (`tiktokads`, `xads`, `googleads`), not the value used in the request path. When omitted, the browser lands on the Zernio dashboard. 
        Boolean headless = false; // Boolean | Enable headless mode (same-token platforms only)
        Boolean force = false; // Boolean | Force a fresh OAuth even when an account already exists. Normally the endpoint returns `alreadyConnected: true` whenever a connected account is found, keying off its active state rather than token liveness. Set `force=true` to bypass that and always receivean `authUrl`. Completing the returned OAuth refreshes the stored token on the existing posting and ads accounts in place. 
        String adAccountId = "act_1330190928038136"; // String | Scope ad sync to a single platform ad account. Without this param, sync covers every ad account the connected token can see. Supported on `facebook`/`instagram` (Meta, `act_<digits>`), `linkedin` (bare numeric sponsored-account id), `googleads` (bare customer id digits) and `twitter` (X Ads, base36 account id). `tiktok` scopes advertisers at OAuth and `pinterest` has no ads discovery, so both ignore it. Meta ids are additionally validated against the connected token; unreachable IDs return 400. Setting a scope also removes already synced ads from de-scoped ad accounts. For multiple accounts use `adAccountIds` instead. 
        List<String> adAccountIds = Arrays.asList(); // List<String> | Scope ad sync to multiple platform ad accounts (same platform support and id shapes as `adAccountId`). Repeat the param (`?adAccountIds=act_1&adAccountIds=act_2`) or comma-separate (`?adAccountIds=act_1,act_2`). Persisted server-side; latest call wins, and de-scoped ad accounts have their synced ads removed. Omitting both `adAccountId` and `adAccountIds` keeps any previously persisted scope unchanged. 
        try {
            ConnectAds200Response result = apiInstance.connectAds(platform, profileId, accountId, redirectUrl, headless, force, adAccountId, adAccountIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectAds");
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
| **platform** | **String**| Platform to connect ads for. Only platforms with ads support are accepted.  &#x60;instagram&#x60; requires an Instagram account connected with loginMethod&#x3D;facebook_login whose token carries ads_management and ads_read. With an account connected through the default instagram_login flow no ads account can be created; do not use this value for those accounts.  | [enum: facebook, instagram, linkedin, tiktok, twitter, pinterest, googleads] |
| **profileId** | **String**| Your Zernio profile ID | |
| **accountId** | **String**| Existing SocialAccount ID. Required for &#x60;twitter&#x60; (X Ads). Optional for &#x60;tiktok&#x60; — omit to enter ads-only mode (no TikTok posting account linked; ad creation uses a Brand Identity instead of a TT_USER). Ignored for same-token (&#x60;facebook&#x60;, &#x60;instagram&#x60;, &#x60;linkedin&#x60;, &#x60;pinterest&#x60;) and standalone (&#x60;googleads&#x60;) platforms.  | [optional] |
| **redirectUrl** | **URI**| Custom URL the browser is sent to once the OAuth flow finishes. Honored on every ads platform, including the separate-token (&#x60;tiktok&#x60;, &#x60;twitter&#x60;) and standalone (&#x60;googleads&#x60;) flows. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On success &#x60;tiktok&#x60;, &#x60;twitter&#x60; and &#x60;googleads&#x60; land on the URL unchanged, while the same-token platforms (&#x60;facebook&#x60;, &#x60;instagram&#x60;, &#x60;linkedin&#x60;, &#x60;pinterest&#x60;) append &#x60;connected&#x60;, &#x60;profileId&#x60;, &#x60;accountId&#x60;, &#x60;username&#x60; and, on API-key calls, &#x60;connect_token&#x60;. On failure the same error contract applies as on GET /v1/connect/{platform}: &#x60;error&#x60; and &#x60;platform&#x60; are always appended, other params are optional, and the value list there is not exhaustive. Note that on the tiktok, twitter and googleads flows &#x60;platform&#x60; carries the ads platform id (&#x60;tiktokads&#x60;, &#x60;xads&#x60;, &#x60;googleads&#x60;), not the value used in the request path. When omitted, the browser lands on the Zernio dashboard.  | [optional] |
| **headless** | **Boolean**| Enable headless mode (same-token platforms only) | [optional] [default to false] |
| **force** | **Boolean**| Force a fresh OAuth even when an account already exists. Normally the endpoint returns &#x60;alreadyConnected: true&#x60; whenever a connected account is found, keying off its active state rather than token liveness. Set &#x60;force&#x3D;true&#x60; to bypass that and always receivean &#x60;authUrl&#x60;. Completing the returned OAuth refreshes the stored token on the existing posting and ads accounts in place.  | [optional] [default to false] |
| **adAccountId** | **String**| Scope ad sync to a single platform ad account. Without this param, sync covers every ad account the connected token can see. Supported on &#x60;facebook&#x60;/&#x60;instagram&#x60; (Meta, &#x60;act_&lt;digits&gt;&#x60;), &#x60;linkedin&#x60; (bare numeric sponsored-account id), &#x60;googleads&#x60; (bare customer id digits) and &#x60;twitter&#x60; (X Ads, base36 account id). &#x60;tiktok&#x60; scopes advertisers at OAuth and &#x60;pinterest&#x60; has no ads discovery, so both ignore it. Meta ids are additionally validated against the connected token; unreachable IDs return 400. Setting a scope also removes already synced ads from de-scoped ad accounts. For multiple accounts use &#x60;adAccountIds&#x60; instead.  | [optional] |
| **adAccountIds** | [**List&lt;String&gt;**](String.md)| Scope ad sync to multiple platform ad accounts (same platform support and id shapes as &#x60;adAccountId&#x60;). Repeat the param (&#x60;?adAccountIds&#x3D;act_1&amp;adAccountIds&#x3D;act_2&#x60;) or comma-separate (&#x60;?adAccountIds&#x3D;act_1,act_2&#x60;). Persisted server-side; latest call wins, and de-scoped ad accounts have their synced ads removed. Omitting both &#x60;adAccountId&#x60; and &#x60;adAccountIds&#x60; keeps any previously persisted scope unchanged.  | [optional] |

### Return type

[**ConnectAds200Response**](ConnectAds200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Either an OAuth URL to redirect to, or confirmation that ads are already connected |  -  |
| **400** | Platform doesn&#39;t support ads, missing accountId for X Ads, or a non-absolute redirect_url |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or no access to profile |  -  |
| **404** | Profile or posting account not found |  -  |

## connectAdsWithHttpInfo

> ApiResponse<ConnectAds200Response> connectAds connectAdsWithHttpInfo(platform, profileId, accountId, redirectUrl, headless, force, adAccountId, adAccountIds)

Connect ads for a platform

Unified ads connection endpoint. Creates a dedicated ads SocialAccount for the specified platform.  Same-token platforms (facebook, instagram, linkedin, pinterest): the ads SocialAccount (metaads, linkedinads, pinterestads) reuses the OAuth token of the parent posting account, but only when an active parent exists and, for facebook and instagram, its stored token carries ads_management and ads_read (linkedin and pinterest need no extra scope). In that case no extra OAuth happens and the response is alreadyConnected: true. When no such parent exists, or the scopes are missing, the endpoint returns an authUrl and a full OAuth round trip is required. When a parent exists but carries no token usable for ad accounts, the call fails with 400 RECONNECT_REQUIRED. Independently of the branch, the call can return 403 ADS_ADDON_REQUIRED without the ads add-on and 402 PAYMENT_REQUIRED when the billing gate is closed.  Meta Ads prerequisite: connecting Meta Ads (via facebook or instagram) requires a Facebook Page. Not because the ad account is read through a Page, but because both parent posting accounts are: the facebook flow only offers Pages you manage, and the instagram flow with loginMethod&#x3D;facebook_login only offers Instagram accounts linked to one of those Pages. Without a Page there is no parent account to inherit a token from. A user who manages no Facebook Page cannot complete this connection, and the facebook flow ends with error&#x3D;no_facebook_pages.  Separate-token platforms (tiktok, twitter): Starts the platform-specific marketing API OAuth flow and creates an ads SocialAccount (tiktokads, xads) with its own token. If the ads account already exists, returns alreadyConnected: true.   - tiktok: accountId is OPTIONAL. With accountId, the new tiktokads account links to that posting account (parentAccountId set) — Spark Ads + standalone ads using the posting TT_USER identity become available. Without accountId, ads-only mode kicks in: the new tiktokads account has parentAccountId&#x3D;null and standalone ads use a synthetic CUSTOMIZED_USER (\&quot;Brand Identity\&quot;); Spark Ads are unavailable because TikTok requires a posting account for them. The Brand Identity is configured separately via PATCH /v1/connect/tiktok-ads (or inline on POST /v1/ads/create via the brandIdentity field).   - twitter (X Ads): accountId is REQUIRED. There&#39;s no ads-only mode — tweets need to be authored by a real X user.  Standalone platforms (googleads): Starts the Google Ads OAuth flow and creates a standalone ads SocialAccount (googleads) with no parent. If the account already exists, returns alreadyConnected: true.  Ads accounts appear as regular SocialAccount documents with ads platform values (e.g., metaads, tiktokads) in GET /v1/accounts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String platform = "facebook"; // String | Platform to connect ads for. Only platforms with ads support are accepted.  `instagram` requires an Instagram account connected with loginMethod=facebook_login whose token carries ads_management and ads_read. With an account connected through the default instagram_login flow no ads account can be created; do not use this value for those accounts. 
        String profileId = "profileId_example"; // String | Your Zernio profile ID
        String accountId = "accountId_example"; // String | Existing SocialAccount ID. Required for `twitter` (X Ads). Optional for `tiktok` — omit to enter ads-only mode (no TikTok posting account linked; ad creation uses a Brand Identity instead of a TT_USER). Ignored for same-token (`facebook`, `instagram`, `linkedin`, `pinterest`) and standalone (`googleads`) platforms. 
        URI redirectUrl = new URI(); // URI | Custom URL the browser is sent to once the OAuth flow finishes. Honored on every ads platform, including the separate-token (`tiktok`, `twitter`) and standalone (`googleads`) flows. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On success `tiktok`, `twitter` and `googleads` land on the URL unchanged, while the same-token platforms (`facebook`, `instagram`, `linkedin`, `pinterest`) append `connected`, `profileId`, `accountId`, `username` and, on API-key calls, `connect_token`. On failure the same error contract applies as on GET /v1/connect/{platform}: `error` and `platform` are always appended, other params are optional, and the value list there is not exhaustive. Note that on the tiktok, twitter and googleads flows `platform` carries the ads platform id (`tiktokads`, `xads`, `googleads`), not the value used in the request path. When omitted, the browser lands on the Zernio dashboard. 
        Boolean headless = false; // Boolean | Enable headless mode (same-token platforms only)
        Boolean force = false; // Boolean | Force a fresh OAuth even when an account already exists. Normally the endpoint returns `alreadyConnected: true` whenever a connected account is found, keying off its active state rather than token liveness. Set `force=true` to bypass that and always receivean `authUrl`. Completing the returned OAuth refreshes the stored token on the existing posting and ads accounts in place. 
        String adAccountId = "act_1330190928038136"; // String | Scope ad sync to a single platform ad account. Without this param, sync covers every ad account the connected token can see. Supported on `facebook`/`instagram` (Meta, `act_<digits>`), `linkedin` (bare numeric sponsored-account id), `googleads` (bare customer id digits) and `twitter` (X Ads, base36 account id). `tiktok` scopes advertisers at OAuth and `pinterest` has no ads discovery, so both ignore it. Meta ids are additionally validated against the connected token; unreachable IDs return 400. Setting a scope also removes already synced ads from de-scoped ad accounts. For multiple accounts use `adAccountIds` instead. 
        List<String> adAccountIds = Arrays.asList(); // List<String> | Scope ad sync to multiple platform ad accounts (same platform support and id shapes as `adAccountId`). Repeat the param (`?adAccountIds=act_1&adAccountIds=act_2`) or comma-separate (`?adAccountIds=act_1,act_2`). Persisted server-side; latest call wins, and de-scoped ad accounts have their synced ads removed. Omitting both `adAccountId` and `adAccountIds` keeps any previously persisted scope unchanged. 
        try {
            ApiResponse<ConnectAds200Response> response = apiInstance.connectAdsWithHttpInfo(platform, profileId, accountId, redirectUrl, headless, force, adAccountId, adAccountIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectAds");
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
| **platform** | **String**| Platform to connect ads for. Only platforms with ads support are accepted.  &#x60;instagram&#x60; requires an Instagram account connected with loginMethod&#x3D;facebook_login whose token carries ads_management and ads_read. With an account connected through the default instagram_login flow no ads account can be created; do not use this value for those accounts.  | [enum: facebook, instagram, linkedin, tiktok, twitter, pinterest, googleads] |
| **profileId** | **String**| Your Zernio profile ID | |
| **accountId** | **String**| Existing SocialAccount ID. Required for &#x60;twitter&#x60; (X Ads). Optional for &#x60;tiktok&#x60; — omit to enter ads-only mode (no TikTok posting account linked; ad creation uses a Brand Identity instead of a TT_USER). Ignored for same-token (&#x60;facebook&#x60;, &#x60;instagram&#x60;, &#x60;linkedin&#x60;, &#x60;pinterest&#x60;) and standalone (&#x60;googleads&#x60;) platforms.  | [optional] |
| **redirectUrl** | **URI**| Custom URL the browser is sent to once the OAuth flow finishes. Honored on every ads platform, including the separate-token (&#x60;tiktok&#x60;, &#x60;twitter&#x60;) and standalone (&#x60;googleads&#x60;) flows. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On success &#x60;tiktok&#x60;, &#x60;twitter&#x60; and &#x60;googleads&#x60; land on the URL unchanged, while the same-token platforms (&#x60;facebook&#x60;, &#x60;instagram&#x60;, &#x60;linkedin&#x60;, &#x60;pinterest&#x60;) append &#x60;connected&#x60;, &#x60;profileId&#x60;, &#x60;accountId&#x60;, &#x60;username&#x60; and, on API-key calls, &#x60;connect_token&#x60;. On failure the same error contract applies as on GET /v1/connect/{platform}: &#x60;error&#x60; and &#x60;platform&#x60; are always appended, other params are optional, and the value list there is not exhaustive. Note that on the tiktok, twitter and googleads flows &#x60;platform&#x60; carries the ads platform id (&#x60;tiktokads&#x60;, &#x60;xads&#x60;, &#x60;googleads&#x60;), not the value used in the request path. When omitted, the browser lands on the Zernio dashboard.  | [optional] |
| **headless** | **Boolean**| Enable headless mode (same-token platforms only) | [optional] [default to false] |
| **force** | **Boolean**| Force a fresh OAuth even when an account already exists. Normally the endpoint returns &#x60;alreadyConnected: true&#x60; whenever a connected account is found, keying off its active state rather than token liveness. Set &#x60;force&#x3D;true&#x60; to bypass that and always receivean &#x60;authUrl&#x60;. Completing the returned OAuth refreshes the stored token on the existing posting and ads accounts in place.  | [optional] [default to false] |
| **adAccountId** | **String**| Scope ad sync to a single platform ad account. Without this param, sync covers every ad account the connected token can see. Supported on &#x60;facebook&#x60;/&#x60;instagram&#x60; (Meta, &#x60;act_&lt;digits&gt;&#x60;), &#x60;linkedin&#x60; (bare numeric sponsored-account id), &#x60;googleads&#x60; (bare customer id digits) and &#x60;twitter&#x60; (X Ads, base36 account id). &#x60;tiktok&#x60; scopes advertisers at OAuth and &#x60;pinterest&#x60; has no ads discovery, so both ignore it. Meta ids are additionally validated against the connected token; unreachable IDs return 400. Setting a scope also removes already synced ads from de-scoped ad accounts. For multiple accounts use &#x60;adAccountIds&#x60; instead.  | [optional] |
| **adAccountIds** | [**List&lt;String&gt;**](String.md)| Scope ad sync to multiple platform ad accounts (same platform support and id shapes as &#x60;adAccountId&#x60;). Repeat the param (&#x60;?adAccountIds&#x3D;act_1&amp;adAccountIds&#x3D;act_2&#x60;) or comma-separate (&#x60;?adAccountIds&#x3D;act_1,act_2&#x60;). Persisted server-side; latest call wins, and de-scoped ad accounts have their synced ads removed. Omitting both &#x60;adAccountId&#x60; and &#x60;adAccountIds&#x60; keeps any previously persisted scope unchanged.  | [optional] |

### Return type

ApiResponse<[**ConnectAds200Response**](ConnectAds200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Either an OAuth URL to redirect to, or confirmation that ads are already connected |  -  |
| **400** | Platform doesn&#39;t support ads, missing accountId for X Ads, or a non-absolute redirect_url |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or no access to profile |  -  |
| **404** | Profile or posting account not found |  -  |


## connectBlueskyCredentials

> ConnectBlueskyCredentials200Response connectBlueskyCredentials(connectBlueskyCredentialsRequest)

Connect Bluesky account

Connect a Bluesky account using identifier (handle or email) and an app password. To get your userId for the state parameter, call GET /v1/users which includes a currentUserId field. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectBlueskyCredentialsRequest connectBlueskyCredentialsRequest = new ConnectBlueskyCredentialsRequest(); // ConnectBlueskyCredentialsRequest | 
        try {
            ConnectBlueskyCredentials200Response result = apiInstance.connectBlueskyCredentials(connectBlueskyCredentialsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectBlueskyCredentials");
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
| **connectBlueskyCredentialsRequest** | [**ConnectBlueskyCredentialsRequest**](ConnectBlueskyCredentialsRequest.md)|  | |

### Return type

[**ConnectBlueskyCredentials200Response**](ConnectBlueskyCredentials200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bluesky connected successfully |  -  |
| **400** | Invalid request - missing fields or invalid state format |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal error |  -  |

## connectBlueskyCredentialsWithHttpInfo

> ApiResponse<ConnectBlueskyCredentials200Response> connectBlueskyCredentials connectBlueskyCredentialsWithHttpInfo(connectBlueskyCredentialsRequest)

Connect Bluesky account

Connect a Bluesky account using identifier (handle or email) and an app password. To get your userId for the state parameter, call GET /v1/users which includes a currentUserId field. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectBlueskyCredentialsRequest connectBlueskyCredentialsRequest = new ConnectBlueskyCredentialsRequest(); // ConnectBlueskyCredentialsRequest | 
        try {
            ApiResponse<ConnectBlueskyCredentials200Response> response = apiInstance.connectBlueskyCredentialsWithHttpInfo(connectBlueskyCredentialsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectBlueskyCredentials");
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
| **connectBlueskyCredentialsRequest** | [**ConnectBlueskyCredentialsRequest**](ConnectBlueskyCredentialsRequest.md)|  | |

### Return type

ApiResponse<[**ConnectBlueskyCredentials200Response**](ConnectBlueskyCredentials200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bluesky connected successfully |  -  |
| **400** | Invalid request - missing fields or invalid state format |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal error |  -  |


## connectDiscordChannel

> void connectDiscordChannel(connectDiscordChannelRequest)

Connect a Discord channel

Finalize a Discord connect by binding one channel to a profile. Served by a dedicated route, so it is not reachable through POST /v1/connect/{platform}. One connected account per channel: repeat the call with a different channelId to add another.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectDiscordChannelRequest connectDiscordChannelRequest = new ConnectDiscordChannelRequest(); // ConnectDiscordChannelRequest | 
        try {
            apiInstance.connectDiscordChannel(connectDiscordChannelRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectDiscordChannel");
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
| **connectDiscordChannelRequest** | [**ConnectDiscordChannelRequest**](ConnectDiscordChannelRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **404** | Profile not found |  -  |

## connectDiscordChannelWithHttpInfo

> ApiResponse<Void> connectDiscordChannel connectDiscordChannelWithHttpInfo(connectDiscordChannelRequest)

Connect a Discord channel

Finalize a Discord connect by binding one channel to a profile. Served by a dedicated route, so it is not reachable through POST /v1/connect/{platform}. One connected account per channel: repeat the call with a different channelId to add another.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectDiscordChannelRequest connectDiscordChannelRequest = new ConnectDiscordChannelRequest(); // ConnectDiscordChannelRequest | 
        try {
            ApiResponse<Void> response = apiInstance.connectDiscordChannelWithHttpInfo(connectDiscordChannelRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectDiscordChannel");
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
| **connectDiscordChannelRequest** | [**ConnectDiscordChannelRequest**](ConnectDiscordChannelRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **404** | Profile not found |  -  |


## connectOpenAIAdsCredentials

> ConnectOpenAIAdsCredentials200Response connectOpenAIAdsCredentials(connectOpenAIAdsCredentialsRequest)

Connect an OpenAI Ads account

Connect an OpenAI Ads account using an API key from ChatGPT Ads Manager.  The key grants full campaign write access on OpenAI&#39;s side (OpenAI does not offer a read-only key scope). Zernio uses it to read ads and performance, and to create and manage campaigns you set up through Zernio (create, status, budget, and cancel). Campaigns created directly in ChatGPT Ads Manager can still be managed there. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectOpenAIAdsCredentialsRequest connectOpenAIAdsCredentialsRequest = new ConnectOpenAIAdsCredentialsRequest(); // ConnectOpenAIAdsCredentialsRequest | 
        try {
            ConnectOpenAIAdsCredentials200Response result = apiInstance.connectOpenAIAdsCredentials(connectOpenAIAdsCredentialsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectOpenAIAdsCredentials");
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
| **connectOpenAIAdsCredentialsRequest** | [**ConnectOpenAIAdsCredentialsRequest**](ConnectOpenAIAdsCredentialsRequest.md)|  | |

### Return type

[**ConnectOpenAIAdsCredentials200Response**](ConnectOpenAIAdsCredentials200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OpenAI Ads connected successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized, or the API key could not read an OpenAI ad account (code invalid_credentials). |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Ads add-on required. |  -  |

## connectOpenAIAdsCredentialsWithHttpInfo

> ApiResponse<ConnectOpenAIAdsCredentials200Response> connectOpenAIAdsCredentials connectOpenAIAdsCredentialsWithHttpInfo(connectOpenAIAdsCredentialsRequest)

Connect an OpenAI Ads account

Connect an OpenAI Ads account using an API key from ChatGPT Ads Manager.  The key grants full campaign write access on OpenAI&#39;s side (OpenAI does not offer a read-only key scope). Zernio uses it to read ads and performance, and to create and manage campaigns you set up through Zernio (create, status, budget, and cancel). Campaigns created directly in ChatGPT Ads Manager can still be managed there. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectOpenAIAdsCredentialsRequest connectOpenAIAdsCredentialsRequest = new ConnectOpenAIAdsCredentialsRequest(); // ConnectOpenAIAdsCredentialsRequest | 
        try {
            ApiResponse<ConnectOpenAIAdsCredentials200Response> response = apiInstance.connectOpenAIAdsCredentialsWithHttpInfo(connectOpenAIAdsCredentialsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectOpenAIAdsCredentials");
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
| **connectOpenAIAdsCredentialsRequest** | [**ConnectOpenAIAdsCredentialsRequest**](ConnectOpenAIAdsCredentialsRequest.md)|  | |

### Return type

ApiResponse<[**ConnectOpenAIAdsCredentials200Response**](ConnectOpenAIAdsCredentials200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OpenAI Ads connected successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized, or the API key could not read an OpenAI ad account (code invalid_credentials). |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Ads add-on required. |  -  |


## connectShopifyWithToken

> ConnectShopifyWithToken200Response connectShopifyWithToken(connectShopifyWithTokenRequest)

Connect a Shopify store with a custom-app Admin token

Token-paste alternative to the OAuth flow: connect a store using the Admin API access token of a custom app the merchant created in their own Shopify admin (Settings → Apps and sales channels → Develop apps, with the &#x60;read_content&#x60;/&#x60;write_content&#x60; scopes). Use this when the one-click OAuth connect is unavailable or when your users prefer not to install a third-party app on their store. The token is validated against the store before anything is saved; custom-app tokens do not expire. Connecting the same profile to a store again replaces the stored token in place. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectShopifyWithTokenRequest connectShopifyWithTokenRequest = new ConnectShopifyWithTokenRequest(); // ConnectShopifyWithTokenRequest | 
        try {
            ConnectShopifyWithToken200Response result = apiInstance.connectShopifyWithToken(connectShopifyWithTokenRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectShopifyWithToken");
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
| **connectShopifyWithTokenRequest** | [**ConnectShopifyWithTokenRequest**](ConnectShopifyWithTokenRequest.md)|  | |

### Return type

[**ConnectShopifyWithToken200Response**](ConnectShopifyWithToken200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Store connected as a platform account |  -  |
| **400** | Invalid &#x60;profileId&#x60; format, &#x60;shop&#x60; is not a myshopify.com store domain, or Shopify rejected the access token for that store. |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | API key does not have access to this profile. |  -  |

## connectShopifyWithTokenWithHttpInfo

> ApiResponse<ConnectShopifyWithToken200Response> connectShopifyWithToken connectShopifyWithTokenWithHttpInfo(connectShopifyWithTokenRequest)

Connect a Shopify store with a custom-app Admin token

Token-paste alternative to the OAuth flow: connect a store using the Admin API access token of a custom app the merchant created in their own Shopify admin (Settings → Apps and sales channels → Develop apps, with the &#x60;read_content&#x60;/&#x60;write_content&#x60; scopes). Use this when the one-click OAuth connect is unavailable or when your users prefer not to install a third-party app on their store. The token is validated against the store before anything is saved; custom-app tokens do not expire. Connecting the same profile to a store again replaces the stored token in place. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectShopifyWithTokenRequest connectShopifyWithTokenRequest = new ConnectShopifyWithTokenRequest(); // ConnectShopifyWithTokenRequest | 
        try {
            ApiResponse<ConnectShopifyWithToken200Response> response = apiInstance.connectShopifyWithTokenWithHttpInfo(connectShopifyWithTokenRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectShopifyWithToken");
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
| **connectShopifyWithTokenRequest** | [**ConnectShopifyWithTokenRequest**](ConnectShopifyWithTokenRequest.md)|  | |

### Return type

ApiResponse<[**ConnectShopifyWithToken200Response**](ConnectShopifyWithToken200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Store connected as a platform account |  -  |
| **400** | Invalid &#x60;profileId&#x60; format, &#x60;shop&#x60; is not a myshopify.com store domain, or Shopify rejected the access token for that store. |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | API key does not have access to this profile. |  -  |


## connectSlackChannel

> void connectSlackChannel(connectSlackChannelRequest)

Connect a Slack channel

Finalize a Slack connect by creating the per-channel account. Served by a dedicated route, so it is not reachable through POST /v1/connect/{platform}. Send pendingDataToken for a first connect (the nonce from the OAuth redirect) or accountId to add another channel to a workspace already connected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectSlackChannelRequest connectSlackChannelRequest = new ConnectSlackChannelRequest(); // ConnectSlackChannelRequest | 
        try {
            apiInstance.connectSlackChannel(connectSlackChannelRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectSlackChannel");
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
| **connectSlackChannelRequest** | [**ConnectSlackChannelRequest**](ConnectSlackChannelRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Slack connections are temporarily unavailable |  -  |
| **404** | Profile not found |  -  |

## connectSlackChannelWithHttpInfo

> ApiResponse<Void> connectSlackChannel connectSlackChannelWithHttpInfo(connectSlackChannelRequest)

Connect a Slack channel

Finalize a Slack connect by creating the per-channel account. Served by a dedicated route, so it is not reachable through POST /v1/connect/{platform}. Send pendingDataToken for a first connect (the nonce from the OAuth redirect) or accountId to add another channel to a workspace already connected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectSlackChannelRequest connectSlackChannelRequest = new ConnectSlackChannelRequest(); // ConnectSlackChannelRequest | 
        try {
            ApiResponse<Void> response = apiInstance.connectSlackChannelWithHttpInfo(connectSlackChannelRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectSlackChannel");
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
| **connectSlackChannelRequest** | [**ConnectSlackChannelRequest**](ConnectSlackChannelRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Slack connections are temporarily unavailable |  -  |
| **404** | Profile not found |  -  |


## connectWhatsAppCredentials

> ConnectWhatsAppCredentials200Response connectWhatsAppCredentials(connectWhatsAppCredentialsRequest)

Connect WhatsApp via credentials

Connect a WhatsApp Business Account by providing Meta credentials directly. This is the headless alternative to the Embedded Signup browser flow.  To get the required credentials: 1. Go to Meta Business Suite (business.facebook.com) 2. Create or select a WhatsApp Business Account 3. In Business Settings &gt; System Users, create a System User 4. Assign it the whatsapp_business_management and whatsapp_business_messaging permissions 5. Generate a permanent access token 6. Get the WABA ID from WhatsApp Manager &gt; Account Tools &gt; Phone Numbers 7. Get the Phone Number ID from the same page (click on the number)  Warning: connecting subscribes your own Meta app to this WABA with an override callback that redirects its webhook delivery to Zernio. This WABA&#39;s events stop reaching any callback URL you had configured before, immediately and with no overlap window. Do not unsubscribe your app from the WABA afterward: that also cuts off Zernio&#39;s delivery, and recovery requires calling this endpoint again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectWhatsAppCredentialsRequest connectWhatsAppCredentialsRequest = new ConnectWhatsAppCredentialsRequest(); // ConnectWhatsAppCredentialsRequest | 
        try {
            ConnectWhatsAppCredentials200Response result = apiInstance.connectWhatsAppCredentials(connectWhatsAppCredentialsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectWhatsAppCredentials");
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
| **connectWhatsAppCredentialsRequest** | [**ConnectWhatsAppCredentialsRequest**](ConnectWhatsAppCredentialsRequest.md)|  | |

### Return type

[**ConnectWhatsAppCredentials200Response**](ConnectWhatsAppCredentials200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WhatsApp connected successfully |  -  |
| **400** | Invalid request. Missing fields, a &#x60;pin&#x60; that is not 6 digits, or the phoneNumberId was not found in the specified WABA. If the phone was not found, the response includes availablePhoneNumbers to help identify the correct ID.  |  -  |
| **401** | Invalid or expired access token |  -  |
| **403** | Profile limit exceeded for this plan |  -  |
| **409** | Conflict with an existing connection. Either the phone number is a Zernio-provisioned number pinned to a different profile (code WHATSAPP_NUMBER_PINNED_TO_PROFILE, connect it from that profile or move it first with PATCH /v1/whatsapp/phone-numbers/{id}/profile), or the number is already actively connected on another profile or workspace (code WHATSAPP_NUMBER_ALREADY_CONNECTED, disconnect it there first). A number can only be live on one profile. |  -  |

## connectWhatsAppCredentialsWithHttpInfo

> ApiResponse<ConnectWhatsAppCredentials200Response> connectWhatsAppCredentials connectWhatsAppCredentialsWithHttpInfo(connectWhatsAppCredentialsRequest)

Connect WhatsApp via credentials

Connect a WhatsApp Business Account by providing Meta credentials directly. This is the headless alternative to the Embedded Signup browser flow.  To get the required credentials: 1. Go to Meta Business Suite (business.facebook.com) 2. Create or select a WhatsApp Business Account 3. In Business Settings &gt; System Users, create a System User 4. Assign it the whatsapp_business_management and whatsapp_business_messaging permissions 5. Generate a permanent access token 6. Get the WABA ID from WhatsApp Manager &gt; Account Tools &gt; Phone Numbers 7. Get the Phone Number ID from the same page (click on the number)  Warning: connecting subscribes your own Meta app to this WABA with an override callback that redirects its webhook delivery to Zernio. This WABA&#39;s events stop reaching any callback URL you had configured before, immediately and with no overlap window. Do not unsubscribe your app from the WABA afterward: that also cuts off Zernio&#39;s delivery, and recovery requires calling this endpoint again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectWhatsAppCredentialsRequest connectWhatsAppCredentialsRequest = new ConnectWhatsAppCredentialsRequest(); // ConnectWhatsAppCredentialsRequest | 
        try {
            ApiResponse<ConnectWhatsAppCredentials200Response> response = apiInstance.connectWhatsAppCredentialsWithHttpInfo(connectWhatsAppCredentialsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectWhatsAppCredentials");
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
| **connectWhatsAppCredentialsRequest** | [**ConnectWhatsAppCredentialsRequest**](ConnectWhatsAppCredentialsRequest.md)|  | |

### Return type

ApiResponse<[**ConnectWhatsAppCredentials200Response**](ConnectWhatsAppCredentials200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WhatsApp connected successfully |  -  |
| **400** | Invalid request. Missing fields, a &#x60;pin&#x60; that is not 6 digits, or the phoneNumberId was not found in the specified WABA. If the phone was not found, the response includes availablePhoneNumbers to help identify the correct ID.  |  -  |
| **401** | Invalid or expired access token |  -  |
| **403** | Profile limit exceeded for this plan |  -  |
| **409** | Conflict with an existing connection. Either the phone number is a Zernio-provisioned number pinned to a different profile (code WHATSAPP_NUMBER_PINNED_TO_PROFILE, connect it from that profile or move it first with PATCH /v1/whatsapp/phone-numbers/{id}/profile), or the number is already actively connected on another profile or workspace (code WHATSAPP_NUMBER_ALREADY_CONNECTED, disconnect it there first). A number can only be live on one profile. |  -  |


## connectWhatsAppEmbeddedSignup

> void connectWhatsAppEmbeddedSignup(connectWhatsAppEmbeddedSignupRequest)

Connect WhatsApp from Embedded Signup

Exchange the authorization code Meta Embedded Signup returns to your browser SDK. This is the headless completion path for WhatsApp: the code never passes through a redirect_uri, so POST /v1/connect/{platform} cannot accept it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectWhatsAppEmbeddedSignupRequest connectWhatsAppEmbeddedSignupRequest = new ConnectWhatsAppEmbeddedSignupRequest(); // ConnectWhatsAppEmbeddedSignupRequest | 
        try {
            apiInstance.connectWhatsAppEmbeddedSignup(connectWhatsAppEmbeddedSignupRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectWhatsAppEmbeddedSignup");
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
| **connectWhatsAppEmbeddedSignupRequest** | [**ConnectWhatsAppEmbeddedSignupRequest**](ConnectWhatsAppEmbeddedSignupRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **409** | The number is already connected on another profile or workspace |  -  |

## connectWhatsAppEmbeddedSignupWithHttpInfo

> ApiResponse<Void> connectWhatsAppEmbeddedSignup connectWhatsAppEmbeddedSignupWithHttpInfo(connectWhatsAppEmbeddedSignupRequest)

Connect WhatsApp from Embedded Signup

Exchange the authorization code Meta Embedded Signup returns to your browser SDK. This is the headless completion path for WhatsApp: the code never passes through a redirect_uri, so POST /v1/connect/{platform} cannot accept it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        ConnectWhatsAppEmbeddedSignupRequest connectWhatsAppEmbeddedSignupRequest = new ConnectWhatsAppEmbeddedSignupRequest(); // ConnectWhatsAppEmbeddedSignupRequest | 
        try {
            ApiResponse<Void> response = apiInstance.connectWhatsAppEmbeddedSignupWithHttpInfo(connectWhatsAppEmbeddedSignupRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#connectWhatsAppEmbeddedSignup");
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
| **connectWhatsAppEmbeddedSignupRequest** | [**ConnectWhatsAppEmbeddedSignupRequest**](ConnectWhatsAppEmbeddedSignupRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **409** | The number is already connected on another profile or workspace |  -  |


## createPinterestBoard

> CreatePinterestBoard201Response createPinterestBoard(accountId, createPinterestBoardRequest)

Create Pinterest board

Creates a new board on the connected Pinterest account. The returned board ID can be used immediately as &#x60;platformSpecificData.boardId&#x60; when creating a Pinterest post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        CreatePinterestBoardRequest createPinterestBoardRequest = new CreatePinterestBoardRequest(); // CreatePinterestBoardRequest | 
        try {
            CreatePinterestBoard201Response result = apiInstance.createPinterestBoard(accountId, createPinterestBoardRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#createPinterestBoard");
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
| **createPinterestBoardRequest** | [**CreatePinterestBoardRequest**](CreatePinterestBoardRequest.md)|  | |

### Return type

[**CreatePinterestBoard201Response**](CreatePinterestBoard201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Board created |  -  |
| **400** | Invalid request or not a Pinterest account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Pinterest rejected the request (e.g. duplicate board name) |  -  |

## createPinterestBoardWithHttpInfo

> ApiResponse<CreatePinterestBoard201Response> createPinterestBoard createPinterestBoardWithHttpInfo(accountId, createPinterestBoardRequest)

Create Pinterest board

Creates a new board on the connected Pinterest account. The returned board ID can be used immediately as &#x60;platformSpecificData.boardId&#x60; when creating a Pinterest post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        CreatePinterestBoardRequest createPinterestBoardRequest = new CreatePinterestBoardRequest(); // CreatePinterestBoardRequest | 
        try {
            ApiResponse<CreatePinterestBoard201Response> response = apiInstance.createPinterestBoardWithHttpInfo(accountId, createPinterestBoardRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#createPinterestBoard");
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
| **createPinterestBoardRequest** | [**CreatePinterestBoardRequest**](CreatePinterestBoardRequest.md)|  | |

### Return type

ApiResponse<[**CreatePinterestBoard201Response**](CreatePinterestBoard201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Board created |  -  |
| **400** | Invalid request or not a Pinterest account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Pinterest rejected the request (e.g. duplicate board name) |  -  |


## getConnectUrl

> GetConnectUrl200Response getConnectUrl(platform, profileId, redirectUrl, headless, loginMethod, onboarding)

Get OAuth connect URL

Initiate an OAuth connection flow. Returns an authUrl to redirect the user to. Standard flow: Zernio hosts the selection UI, then redirects to your redirect_url. Headless mode (headless&#x3D;true): user is redirected to your redirect_url with OAuth data for custom UI. Use the platform-specific selection endpoints to complete. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String platform = "facebook"; // String | Social media platform to connect
        String profileId = "profileId_example"; // String | Your Zernio profile ID (get from /v1/profiles). For WhatsApp, a Zernio-provisioned number can only be connected on the profile it was provisioned to; connecting from any other profile is rejected with a 409.
        URI redirectUrl = new URI(); // URI | Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. Result params are appended with the URL API, so an existing query string is preserved. Standard mode appends connected={platform}&profileId=X&accountId=Y&username=Z. Headless mode appends OAuth data params for platforms requiring selection (e.g. LinkedIn orgs, Facebook pages). If no selection is needed, the account is created directly and the redirect includes accountId.  On failure, the browser is sent to the same redirect_url with `error` and `platform` appended. `error` and `platform` are always present. `error_message`, `is_user_fixable`, `reason` and `dashboard_url` are conditional and must be treated as optional.  This list is NOT exhaustive and new values may be added at any time. Treat an unrecognized value as a generic failure rather than matching it exhaustively. Existing values are not renamed or removed without notice.  OAuth and callback:   oauth_denied, invalid_callback, invalid_state, unsupported_platform, connection_failed,   internal_error, token_exchange_failed, byok_config_error, personal_account_not_supported,   missing_google_permissions, platform_requires_destination, reconnect_account_mismatch,   invalid_request  Access and limits:   profile_not_found, invalid_profile_id, access_denied, account_limit_exceeded,   profile_limit_exceeded, payment_required  Destination selection:   no_facebook_pages, facebook_pages_error, no_google_locations, google_locations_error,   google_permission_denied, no_snapchat_public_profiles, snapchat_profiles_error,   discord_no_guild, slack_no_team  WhatsApp:   whatsapp_error, one_whatsapp_per_profile, whatsapp_number_already_connected,   whatsapp_number_pinned_to_profile, connection_cancelled  Google Ads (platform=googleads):   google_ads_auth_failed, google_ads_invalid_state, google_ads_config_error,   google_ads_token_failed, google_ads_quota_exhausted, google_ads_callback_error  TikTok Ads (platform=tiktokads):   tiktok_ads_auth_failed, tiktok_ads_invalid_state, tiktok_ads_access_denied,   tiktok_ads_config_error, tiktok_ads_token_failed, tiktok_ads_account_not_found,   tiktok_ads_callback_error  X Ads (platform=xads):   x_ads_denied, x_ads_auth_failed, x_ads_config_error, x_ads_account_not_found,   x_ads_state_error, x_ads_token_failed, x_ads_token_missing, x_ads_callback_error  Shopify (platform=shopify):   shopify_auth_failed, shopify_config_error, shopify_invalid_state, shopify_invalid_hmac,   shopify_invalid_shop, shopify_missing_scopes, shopify_callback_error  1. On this endpoint every upstream OAuth error is collapsed into `oauth_denied`. The provider's own value (for example Meta's `access_denied`) is not forwarded. The dedicated ads flows below are different: they use their own denial slugs and `google_ads_auth_failed` and `tiktok_ads_auth_failed` may carry the provider's raw error string in `error_message`.  2. On the tiktok and twitter ads flows `platform` carries the ads platform id (`tiktokads`, `xads`), not the value used in the request path. The googleads and shopify flows report `googleads` and `shopify`. 
        Boolean headless = false; // Boolean | When true, the user is redirected to your redirect_url with raw OAuth data (code, state) instead of Zernio's default account selection UI. Use this to build a custom connect experience.
        String loginMethod = "instagram_login"; // String | Instagram only. Which of the two Instagram connection methods to use. Ignored for every other platform.  `instagram_login` (the default, and what you get if you omit this): the Instagram Login dialog. The user authorizes their Instagram professional account directly, no Facebook Page required.  `facebook_login`: the Facebook Login dialog, i.e. \"Instagram API with Facebook Login\". The user authorizes a Facebook Page that has a linked Instagram professional account, and every API call for that account then runs through the Page. Use this when the customer manages Instagram through a Page and expects the Facebook consent screen. Because the user has to pick which Page to connect, the callback continues at the account-selection step, `/v1/connect/instagram/select-account`.  `facebook_login` supports `headless=true` like the other selection platforms: the callback redirects to your `redirect_url` with `profileId`, `tempToken`, `platform=instagram`, `step=select_account` and `connect_token`, which you pass into the select-account endpoints to finish. The default `instagram_login` has no selection step, so it connects the account directly. 
        String onboarding = "api"; // String | WhatsApp only. Ignored for every other platform. Controls which screen Meta's Embedded Signup popup shows.  If omitted, the connection defaults to coexistence (same as `business_app` below), preserving existing behavior for numbers already on the WhatsApp Business app.  `api`: standard Embedded Signup, showing Meta's WABA/number picker. Use this to connect a phone number already on Cloud API elsewhere.  `business_app`: coexistence, i.e. 'Connect existing WhatsApp Business app' (a number shared between Cloud API and the consumer WhatsApp Business app). 
        try {
            GetConnectUrl200Response result = apiInstance.getConnectUrl(platform, profileId, redirectUrl, headless, loginMethod, onboarding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getConnectUrl");
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
| **platform** | **String**| Social media platform to connect | [enum: facebook, instagram, linkedin, twitter, tiktok, youtube, threads, reddit, pinterest, bluesky, googlebusiness, telegram, snapchat, discord, slack, whatsapp] |
| **profileId** | **String**| Your Zernio profile ID (get from /v1/profiles). For WhatsApp, a Zernio-provisioned number can only be connected on the profile it was provisioned to; connecting from any other profile is rejected with a 409. | |
| **redirectUrl** | **URI**| Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. Result params are appended with the URL API, so an existing query string is preserved. Standard mode appends connected&#x3D;{platform}&amp;profileId&#x3D;X&amp;accountId&#x3D;Y&amp;username&#x3D;Z. Headless mode appends OAuth data params for platforms requiring selection (e.g. LinkedIn orgs, Facebook pages). If no selection is needed, the account is created directly and the redirect includes accountId.  On failure, the browser is sent to the same redirect_url with &#x60;error&#x60; and &#x60;platform&#x60; appended. &#x60;error&#x60; and &#x60;platform&#x60; are always present. &#x60;error_message&#x60;, &#x60;is_user_fixable&#x60;, &#x60;reason&#x60; and &#x60;dashboard_url&#x60; are conditional and must be treated as optional.  This list is NOT exhaustive and new values may be added at any time. Treat an unrecognized value as a generic failure rather than matching it exhaustively. Existing values are not renamed or removed without notice.  OAuth and callback:   oauth_denied, invalid_callback, invalid_state, unsupported_platform, connection_failed,   internal_error, token_exchange_failed, byok_config_error, personal_account_not_supported,   missing_google_permissions, platform_requires_destination, reconnect_account_mismatch,   invalid_request  Access and limits:   profile_not_found, invalid_profile_id, access_denied, account_limit_exceeded,   profile_limit_exceeded, payment_required  Destination selection:   no_facebook_pages, facebook_pages_error, no_google_locations, google_locations_error,   google_permission_denied, no_snapchat_public_profiles, snapchat_profiles_error,   discord_no_guild, slack_no_team  WhatsApp:   whatsapp_error, one_whatsapp_per_profile, whatsapp_number_already_connected,   whatsapp_number_pinned_to_profile, connection_cancelled  Google Ads (platform&#x3D;googleads):   google_ads_auth_failed, google_ads_invalid_state, google_ads_config_error,   google_ads_token_failed, google_ads_quota_exhausted, google_ads_callback_error  TikTok Ads (platform&#x3D;tiktokads):   tiktok_ads_auth_failed, tiktok_ads_invalid_state, tiktok_ads_access_denied,   tiktok_ads_config_error, tiktok_ads_token_failed, tiktok_ads_account_not_found,   tiktok_ads_callback_error  X Ads (platform&#x3D;xads):   x_ads_denied, x_ads_auth_failed, x_ads_config_error, x_ads_account_not_found,   x_ads_state_error, x_ads_token_failed, x_ads_token_missing, x_ads_callback_error  Shopify (platform&#x3D;shopify):   shopify_auth_failed, shopify_config_error, shopify_invalid_state, shopify_invalid_hmac,   shopify_invalid_shop, shopify_missing_scopes, shopify_callback_error  1. On this endpoint every upstream OAuth error is collapsed into &#x60;oauth_denied&#x60;. The provider&#39;s own value (for example Meta&#39;s &#x60;access_denied&#x60;) is not forwarded. The dedicated ads flows below are different: they use their own denial slugs and &#x60;google_ads_auth_failed&#x60; and &#x60;tiktok_ads_auth_failed&#x60; may carry the provider&#39;s raw error string in &#x60;error_message&#x60;.  2. On the tiktok and twitter ads flows &#x60;platform&#x60; carries the ads platform id (&#x60;tiktokads&#x60;, &#x60;xads&#x60;), not the value used in the request path. The googleads and shopify flows report &#x60;googleads&#x60; and &#x60;shopify&#x60;.  | [optional] |
| **headless** | **Boolean**| When true, the user is redirected to your redirect_url with raw OAuth data (code, state) instead of Zernio&#39;s default account selection UI. Use this to build a custom connect experience. | [optional] [default to false] |
| **loginMethod** | **String**| Instagram only. Which of the two Instagram connection methods to use. Ignored for every other platform.  &#x60;instagram_login&#x60; (the default, and what you get if you omit this): the Instagram Login dialog. The user authorizes their Instagram professional account directly, no Facebook Page required.  &#x60;facebook_login&#x60;: the Facebook Login dialog, i.e. \&quot;Instagram API with Facebook Login\&quot;. The user authorizes a Facebook Page that has a linked Instagram professional account, and every API call for that account then runs through the Page. Use this when the customer manages Instagram through a Page and expects the Facebook consent screen. Because the user has to pick which Page to connect, the callback continues at the account-selection step, &#x60;/v1/connect/instagram/select-account&#x60;.  &#x60;facebook_login&#x60; supports &#x60;headless&#x3D;true&#x60; like the other selection platforms: the callback redirects to your &#x60;redirect_url&#x60; with &#x60;profileId&#x60;, &#x60;tempToken&#x60;, &#x60;platform&#x3D;instagram&#x60;, &#x60;step&#x3D;select_account&#x60; and &#x60;connect_token&#x60;, which you pass into the select-account endpoints to finish. The default &#x60;instagram_login&#x60; has no selection step, so it connects the account directly.  | [optional] [default to instagram_login] [enum: instagram_login, facebook_login] |
| **onboarding** | **String**| WhatsApp only. Ignored for every other platform. Controls which screen Meta&#39;s Embedded Signup popup shows.  If omitted, the connection defaults to coexistence (same as &#x60;business_app&#x60; below), preserving existing behavior for numbers already on the WhatsApp Business app.  &#x60;api&#x60;: standard Embedded Signup, showing Meta&#39;s WABA/number picker. Use this to connect a phone number already on Cloud API elsewhere.  &#x60;business_app&#x60;: coexistence, i.e. &#39;Connect existing WhatsApp Business app&#39; (a number shared between Cloud API and the consumer WhatsApp Business app).  | [optional] [enum: api, business_app] |

### Return type

[**GetConnectUrl200Response**](GetConnectUrl200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth authorization URL to redirect user to |  -  |
| **400** | Missing/invalid parameters (e.g., invalid profileId format, or a non-absolute redirect_url) |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | No access to profile, or BYOK required for AppSumo Twitter |  -  |
| **404** | Profile not found |  -  |

## getConnectUrlWithHttpInfo

> ApiResponse<GetConnectUrl200Response> getConnectUrl getConnectUrlWithHttpInfo(platform, profileId, redirectUrl, headless, loginMethod, onboarding)

Get OAuth connect URL

Initiate an OAuth connection flow. Returns an authUrl to redirect the user to. Standard flow: Zernio hosts the selection UI, then redirects to your redirect_url. Headless mode (headless&#x3D;true): user is redirected to your redirect_url with OAuth data for custom UI. Use the platform-specific selection endpoints to complete. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String platform = "facebook"; // String | Social media platform to connect
        String profileId = "profileId_example"; // String | Your Zernio profile ID (get from /v1/profiles). For WhatsApp, a Zernio-provisioned number can only be connected on the profile it was provisioned to; connecting from any other profile is rejected with a 409.
        URI redirectUrl = new URI(); // URI | Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. Result params are appended with the URL API, so an existing query string is preserved. Standard mode appends connected={platform}&profileId=X&accountId=Y&username=Z. Headless mode appends OAuth data params for platforms requiring selection (e.g. LinkedIn orgs, Facebook pages). If no selection is needed, the account is created directly and the redirect includes accountId.  On failure, the browser is sent to the same redirect_url with `error` and `platform` appended. `error` and `platform` are always present. `error_message`, `is_user_fixable`, `reason` and `dashboard_url` are conditional and must be treated as optional.  This list is NOT exhaustive and new values may be added at any time. Treat an unrecognized value as a generic failure rather than matching it exhaustively. Existing values are not renamed or removed without notice.  OAuth and callback:   oauth_denied, invalid_callback, invalid_state, unsupported_platform, connection_failed,   internal_error, token_exchange_failed, byok_config_error, personal_account_not_supported,   missing_google_permissions, platform_requires_destination, reconnect_account_mismatch,   invalid_request  Access and limits:   profile_not_found, invalid_profile_id, access_denied, account_limit_exceeded,   profile_limit_exceeded, payment_required  Destination selection:   no_facebook_pages, facebook_pages_error, no_google_locations, google_locations_error,   google_permission_denied, no_snapchat_public_profiles, snapchat_profiles_error,   discord_no_guild, slack_no_team  WhatsApp:   whatsapp_error, one_whatsapp_per_profile, whatsapp_number_already_connected,   whatsapp_number_pinned_to_profile, connection_cancelled  Google Ads (platform=googleads):   google_ads_auth_failed, google_ads_invalid_state, google_ads_config_error,   google_ads_token_failed, google_ads_quota_exhausted, google_ads_callback_error  TikTok Ads (platform=tiktokads):   tiktok_ads_auth_failed, tiktok_ads_invalid_state, tiktok_ads_access_denied,   tiktok_ads_config_error, tiktok_ads_token_failed, tiktok_ads_account_not_found,   tiktok_ads_callback_error  X Ads (platform=xads):   x_ads_denied, x_ads_auth_failed, x_ads_config_error, x_ads_account_not_found,   x_ads_state_error, x_ads_token_failed, x_ads_token_missing, x_ads_callback_error  Shopify (platform=shopify):   shopify_auth_failed, shopify_config_error, shopify_invalid_state, shopify_invalid_hmac,   shopify_invalid_shop, shopify_missing_scopes, shopify_callback_error  1. On this endpoint every upstream OAuth error is collapsed into `oauth_denied`. The provider's own value (for example Meta's `access_denied`) is not forwarded. The dedicated ads flows below are different: they use their own denial slugs and `google_ads_auth_failed` and `tiktok_ads_auth_failed` may carry the provider's raw error string in `error_message`.  2. On the tiktok and twitter ads flows `platform` carries the ads platform id (`tiktokads`, `xads`), not the value used in the request path. The googleads and shopify flows report `googleads` and `shopify`. 
        Boolean headless = false; // Boolean | When true, the user is redirected to your redirect_url with raw OAuth data (code, state) instead of Zernio's default account selection UI. Use this to build a custom connect experience.
        String loginMethod = "instagram_login"; // String | Instagram only. Which of the two Instagram connection methods to use. Ignored for every other platform.  `instagram_login` (the default, and what you get if you omit this): the Instagram Login dialog. The user authorizes their Instagram professional account directly, no Facebook Page required.  `facebook_login`: the Facebook Login dialog, i.e. \"Instagram API with Facebook Login\". The user authorizes a Facebook Page that has a linked Instagram professional account, and every API call for that account then runs through the Page. Use this when the customer manages Instagram through a Page and expects the Facebook consent screen. Because the user has to pick which Page to connect, the callback continues at the account-selection step, `/v1/connect/instagram/select-account`.  `facebook_login` supports `headless=true` like the other selection platforms: the callback redirects to your `redirect_url` with `profileId`, `tempToken`, `platform=instagram`, `step=select_account` and `connect_token`, which you pass into the select-account endpoints to finish. The default `instagram_login` has no selection step, so it connects the account directly. 
        String onboarding = "api"; // String | WhatsApp only. Ignored for every other platform. Controls which screen Meta's Embedded Signup popup shows.  If omitted, the connection defaults to coexistence (same as `business_app` below), preserving existing behavior for numbers already on the WhatsApp Business app.  `api`: standard Embedded Signup, showing Meta's WABA/number picker. Use this to connect a phone number already on Cloud API elsewhere.  `business_app`: coexistence, i.e. 'Connect existing WhatsApp Business app' (a number shared between Cloud API and the consumer WhatsApp Business app). 
        try {
            ApiResponse<GetConnectUrl200Response> response = apiInstance.getConnectUrlWithHttpInfo(platform, profileId, redirectUrl, headless, loginMethod, onboarding);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getConnectUrl");
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
| **platform** | **String**| Social media platform to connect | [enum: facebook, instagram, linkedin, twitter, tiktok, youtube, threads, reddit, pinterest, bluesky, googlebusiness, telegram, snapchat, discord, slack, whatsapp] |
| **profileId** | **String**| Your Zernio profile ID (get from /v1/profiles). For WhatsApp, a Zernio-provisioned number can only be connected on the profile it was provisioned to; connecting from any other profile is rejected with a 409. | |
| **redirectUrl** | **URI**| Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. Result params are appended with the URL API, so an existing query string is preserved. Standard mode appends connected&#x3D;{platform}&amp;profileId&#x3D;X&amp;accountId&#x3D;Y&amp;username&#x3D;Z. Headless mode appends OAuth data params for platforms requiring selection (e.g. LinkedIn orgs, Facebook pages). If no selection is needed, the account is created directly and the redirect includes accountId.  On failure, the browser is sent to the same redirect_url with &#x60;error&#x60; and &#x60;platform&#x60; appended. &#x60;error&#x60; and &#x60;platform&#x60; are always present. &#x60;error_message&#x60;, &#x60;is_user_fixable&#x60;, &#x60;reason&#x60; and &#x60;dashboard_url&#x60; are conditional and must be treated as optional.  This list is NOT exhaustive and new values may be added at any time. Treat an unrecognized value as a generic failure rather than matching it exhaustively. Existing values are not renamed or removed without notice.  OAuth and callback:   oauth_denied, invalid_callback, invalid_state, unsupported_platform, connection_failed,   internal_error, token_exchange_failed, byok_config_error, personal_account_not_supported,   missing_google_permissions, platform_requires_destination, reconnect_account_mismatch,   invalid_request  Access and limits:   profile_not_found, invalid_profile_id, access_denied, account_limit_exceeded,   profile_limit_exceeded, payment_required  Destination selection:   no_facebook_pages, facebook_pages_error, no_google_locations, google_locations_error,   google_permission_denied, no_snapchat_public_profiles, snapchat_profiles_error,   discord_no_guild, slack_no_team  WhatsApp:   whatsapp_error, one_whatsapp_per_profile, whatsapp_number_already_connected,   whatsapp_number_pinned_to_profile, connection_cancelled  Google Ads (platform&#x3D;googleads):   google_ads_auth_failed, google_ads_invalid_state, google_ads_config_error,   google_ads_token_failed, google_ads_quota_exhausted, google_ads_callback_error  TikTok Ads (platform&#x3D;tiktokads):   tiktok_ads_auth_failed, tiktok_ads_invalid_state, tiktok_ads_access_denied,   tiktok_ads_config_error, tiktok_ads_token_failed, tiktok_ads_account_not_found,   tiktok_ads_callback_error  X Ads (platform&#x3D;xads):   x_ads_denied, x_ads_auth_failed, x_ads_config_error, x_ads_account_not_found,   x_ads_state_error, x_ads_token_failed, x_ads_token_missing, x_ads_callback_error  Shopify (platform&#x3D;shopify):   shopify_auth_failed, shopify_config_error, shopify_invalid_state, shopify_invalid_hmac,   shopify_invalid_shop, shopify_missing_scopes, shopify_callback_error  1. On this endpoint every upstream OAuth error is collapsed into &#x60;oauth_denied&#x60;. The provider&#39;s own value (for example Meta&#39;s &#x60;access_denied&#x60;) is not forwarded. The dedicated ads flows below are different: they use their own denial slugs and &#x60;google_ads_auth_failed&#x60; and &#x60;tiktok_ads_auth_failed&#x60; may carry the provider&#39;s raw error string in &#x60;error_message&#x60;.  2. On the tiktok and twitter ads flows &#x60;platform&#x60; carries the ads platform id (&#x60;tiktokads&#x60;, &#x60;xads&#x60;), not the value used in the request path. The googleads and shopify flows report &#x60;googleads&#x60; and &#x60;shopify&#x60;.  | [optional] |
| **headless** | **Boolean**| When true, the user is redirected to your redirect_url with raw OAuth data (code, state) instead of Zernio&#39;s default account selection UI. Use this to build a custom connect experience. | [optional] [default to false] |
| **loginMethod** | **String**| Instagram only. Which of the two Instagram connection methods to use. Ignored for every other platform.  &#x60;instagram_login&#x60; (the default, and what you get if you omit this): the Instagram Login dialog. The user authorizes their Instagram professional account directly, no Facebook Page required.  &#x60;facebook_login&#x60;: the Facebook Login dialog, i.e. \&quot;Instagram API with Facebook Login\&quot;. The user authorizes a Facebook Page that has a linked Instagram professional account, and every API call for that account then runs through the Page. Use this when the customer manages Instagram through a Page and expects the Facebook consent screen. Because the user has to pick which Page to connect, the callback continues at the account-selection step, &#x60;/v1/connect/instagram/select-account&#x60;.  &#x60;facebook_login&#x60; supports &#x60;headless&#x3D;true&#x60; like the other selection platforms: the callback redirects to your &#x60;redirect_url&#x60; with &#x60;profileId&#x60;, &#x60;tempToken&#x60;, &#x60;platform&#x3D;instagram&#x60;, &#x60;step&#x3D;select_account&#x60; and &#x60;connect_token&#x60;, which you pass into the select-account endpoints to finish. The default &#x60;instagram_login&#x60; has no selection step, so it connects the account directly.  | [optional] [default to instagram_login] [enum: instagram_login, facebook_login] |
| **onboarding** | **String**| WhatsApp only. Ignored for every other platform. Controls which screen Meta&#39;s Embedded Signup popup shows.  If omitted, the connection defaults to coexistence (same as &#x60;business_app&#x60; below), preserving existing behavior for numbers already on the WhatsApp Business app.  &#x60;api&#x60;: standard Embedded Signup, showing Meta&#39;s WABA/number picker. Use this to connect a phone number already on Cloud API elsewhere.  &#x60;business_app&#x60;: coexistence, i.e. &#39;Connect existing WhatsApp Business app&#39; (a number shared between Cloud API and the consumer WhatsApp Business app).  | [optional] [enum: api, business_app] |

### Return type

ApiResponse<[**GetConnectUrl200Response**](GetConnectUrl200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth authorization URL to redirect user to |  -  |
| **400** | Missing/invalid parameters (e.g., invalid profileId format, or a non-absolute redirect_url) |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | No access to profile, or BYOK required for AppSumo Twitter |  -  |
| **404** | Profile not found |  -  |


## getFacebookPages

> GetFacebookPages200Response getFacebookPages(accountId, refresh)

List Facebook pages

Returns all Facebook pages the connected account has access to, including the currently selected page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        Boolean refresh = true; // Boolean | When true, bypasses the page cache and fetches fresh pages from Meta. Rate-limited server-side to 1 refresh per 60s. Pages no longer accessible to the connected account will be removed from the list on refresh. 
        try {
            GetFacebookPages200Response result = apiInstance.getFacebookPages(accountId, refresh);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getFacebookPages");
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
| **refresh** | **Boolean**| When true, bypasses the page cache and fetches fresh pages from Meta. Rate-limited server-side to 1 refresh per 60s. Pages no longer accessible to the connected account will be removed from the list on refresh.  | [optional] |

### Return type

[**GetFacebookPages200Response**](GetFacebookPages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getFacebookPagesWithHttpInfo

> ApiResponse<GetFacebookPages200Response> getFacebookPages getFacebookPagesWithHttpInfo(accountId, refresh)

List Facebook pages

Returns all Facebook pages the connected account has access to, including the currently selected page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        Boolean refresh = true; // Boolean | When true, bypasses the page cache and fetches fresh pages from Meta. Rate-limited server-side to 1 refresh per 60s. Pages no longer accessible to the connected account will be removed from the list on refresh. 
        try {
            ApiResponse<GetFacebookPages200Response> response = apiInstance.getFacebookPagesWithHttpInfo(accountId, refresh);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getFacebookPages");
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
| **refresh** | **Boolean**| When true, bypasses the page cache and fetches fresh pages from Meta. Rate-limited server-side to 1 refresh per 60s. Pages no longer accessible to the connected account will be removed from the list on refresh.  | [optional] |

### Return type

ApiResponse<[**GetFacebookPages200Response**](GetFacebookPages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getGmbLocations

> GetGmbLocations200Response getGmbLocations(accountId, search, filter, limit)

List GBP locations

Returns Google Business Profile locations the connected account can access, plus the currently selected location. The list is bounded (see hasMore); for accounts that own many locations, use the search or filter query params to find a specific one instead of loading them all, or raise limit to enumerate an account with more than 100 locations. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String search = "search_example"; // String | Free-text search on the business name, applied server-side by Google. Use for accounts with many locations.
        String filter = "filter_example"; // String | Raw Google Business Information API filter expression (advanced; takes precedence over search), e.g. storeCode=\"LH279411\".
        Integer limit = 100; // Integer | Max locations to return (default 100, max 500). Raise it to enumerate an account with more than 100 locations; for accounts with thousands, use search/filter instead.
        try {
            GetGmbLocations200Response result = apiInstance.getGmbLocations(accountId, search, filter, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getGmbLocations");
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
| **search** | **String**| Free-text search on the business name, applied server-side by Google. Use for accounts with many locations. | [optional] |
| **filter** | **String**| Raw Google Business Information API filter expression (advanced; takes precedence over search), e.g. storeCode&#x3D;\&quot;LH279411\&quot;. | [optional] |
| **limit** | **Integer**| Max locations to return (default 100, max 500). Raise it to enumerate an account with more than 100 locations; for accounts with thousands, use search/filter instead. | [optional] [default to 100] |

### Return type

[**GetGmbLocations200Response**](GetGmbLocations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations list |  -  |
| **400** | Invalid query parameter (e.g. limit out of range) |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getGmbLocationsWithHttpInfo

> ApiResponse<GetGmbLocations200Response> getGmbLocations getGmbLocationsWithHttpInfo(accountId, search, filter, limit)

List GBP locations

Returns Google Business Profile locations the connected account can access, plus the currently selected location. The list is bounded (see hasMore); for accounts that own many locations, use the search or filter query params to find a specific one instead of loading them all, or raise limit to enumerate an account with more than 100 locations. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String search = "search_example"; // String | Free-text search on the business name, applied server-side by Google. Use for accounts with many locations.
        String filter = "filter_example"; // String | Raw Google Business Information API filter expression (advanced; takes precedence over search), e.g. storeCode=\"LH279411\".
        Integer limit = 100; // Integer | Max locations to return (default 100, max 500). Raise it to enumerate an account with more than 100 locations; for accounts with thousands, use search/filter instead.
        try {
            ApiResponse<GetGmbLocations200Response> response = apiInstance.getGmbLocationsWithHttpInfo(accountId, search, filter, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getGmbLocations");
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
| **search** | **String**| Free-text search on the business name, applied server-side by Google. Use for accounts with many locations. | [optional] |
| **filter** | **String**| Raw Google Business Information API filter expression (advanced; takes precedence over search), e.g. storeCode&#x3D;\&quot;LH279411\&quot;. | [optional] |
| **limit** | **Integer**| Max locations to return (default 100, max 500). Raise it to enumerate an account with more than 100 locations; for accounts with thousands, use search/filter instead. | [optional] [default to 100] |

### Return type

ApiResponse<[**GetGmbLocations200Response**](GetGmbLocations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations list |  -  |
| **400** | Invalid query parameter (e.g. limit out of range) |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getLinkedInOrganizations

> GetLinkedInOrganizations200Response getLinkedInOrganizations(accountId)

List LinkedIn orgs

Returns LinkedIn organizations (company pages) the connected account has admin access to.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetLinkedInOrganizations200Response result = apiInstance.getLinkedInOrganizations(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getLinkedInOrganizations");
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

[**GetLinkedInOrganizations200Response**](GetLinkedInOrganizations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organizations list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getLinkedInOrganizationsWithHttpInfo

> ApiResponse<GetLinkedInOrganizations200Response> getLinkedInOrganizations getLinkedInOrganizationsWithHttpInfo(accountId)

List LinkedIn orgs

Returns LinkedIn organizations (company pages) the connected account has admin access to.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetLinkedInOrganizations200Response> response = apiInstance.getLinkedInOrganizationsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getLinkedInOrganizations");
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

ApiResponse<[**GetLinkedInOrganizations200Response**](GetLinkedInOrganizations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organizations list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getPendingOAuthData

> GetPendingOAuthData200Response getPendingOAuthData(token)

Get pending OAuth data

Fetch pending OAuth data for headless mode using the pendingDataToken from the redirect URL.  **Scope**: This endpoint is used for LinkedIn organizations, Google Business locations, Slack channels, Snapchat profiles, and Pinterest boards, where the selection list is too large to fit in URL params. The redirect carries a &#x60;pendingDataToken&#x60; instead of the full payload; the response includes the corresponding selection array (e.g. &#x60;boards&#x60; for Pinterest). WhatsApp, Facebook and other platforms pass selection state directly via URL query params on the redirect (&#x60;profileId&#x60;, &#x60;tempToken&#x60;, &#x60;step&#x60;), no pending record is created, so this endpoint will return 404 for those flows. Use the platform-specific selection endpoint instead (e.g. &#x60;/v1/connect/whatsapp/select-phone-number&#x60;).  Reading the token does not consume it, so this fetch is repeatable until the token expires 1 hour after issuance. Completing the platform selection deletes the pending record, so the token stops working from then on. No authentication required. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String token = "token_example"; // String | The pending data token from the OAuth redirect URL (pendingDataToken parameter)
        try {
            GetPendingOAuthData200Response result = apiInstance.getPendingOAuthData(token);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getPendingOAuthData");
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
| **token** | **String**| The pending data token from the OAuth redirect URL (pendingDataToken parameter) | |

### Return type

[**GetPendingOAuthData200Response**](GetPendingOAuthData200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth data fetched successfully |  -  |
| **400** | Missing token parameter |  -  |
| **404** | Token not found or expired |  -  |

## getPendingOAuthDataWithHttpInfo

> ApiResponse<GetPendingOAuthData200Response> getPendingOAuthData getPendingOAuthDataWithHttpInfo(token)

Get pending OAuth data

Fetch pending OAuth data for headless mode using the pendingDataToken from the redirect URL.  **Scope**: This endpoint is used for LinkedIn organizations, Google Business locations, Slack channels, Snapchat profiles, and Pinterest boards, where the selection list is too large to fit in URL params. The redirect carries a &#x60;pendingDataToken&#x60; instead of the full payload; the response includes the corresponding selection array (e.g. &#x60;boards&#x60; for Pinterest). WhatsApp, Facebook and other platforms pass selection state directly via URL query params on the redirect (&#x60;profileId&#x60;, &#x60;tempToken&#x60;, &#x60;step&#x60;), no pending record is created, so this endpoint will return 404 for those flows. Use the platform-specific selection endpoint instead (e.g. &#x60;/v1/connect/whatsapp/select-phone-number&#x60;).  Reading the token does not consume it, so this fetch is repeatable until the token expires 1 hour after issuance. Completing the platform selection deletes the pending record, so the token stops working from then on. No authentication required. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String token = "token_example"; // String | The pending data token from the OAuth redirect URL (pendingDataToken parameter)
        try {
            ApiResponse<GetPendingOAuthData200Response> response = apiInstance.getPendingOAuthDataWithHttpInfo(token);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getPendingOAuthData");
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
| **token** | **String**| The pending data token from the OAuth redirect URL (pendingDataToken parameter) | |

### Return type

ApiResponse<[**GetPendingOAuthData200Response**](GetPendingOAuthData200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth data fetched successfully |  -  |
| **400** | Missing token parameter |  -  |
| **404** | Token not found or expired |  -  |


## getPinterestBoards

> GetPinterestBoards200Response getPinterestBoards(accountId)

List Pinterest boards

Returns the boards available for a connected Pinterest account. Use this to get a board ID when creating a Pinterest post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetPinterestBoards200Response result = apiInstance.getPinterestBoards(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getPinterestBoards");
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

[**GetPinterestBoards200Response**](GetPinterestBoards200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Boards list |  -  |
| **400** | Not a Pinterest account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getPinterestBoardsWithHttpInfo

> ApiResponse<GetPinterestBoards200Response> getPinterestBoards getPinterestBoardsWithHttpInfo(accountId)

List Pinterest boards

Returns the boards available for a connected Pinterest account. Use this to get a board ID when creating a Pinterest post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetPinterestBoards200Response> response = apiInstance.getPinterestBoardsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getPinterestBoards");
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

ApiResponse<[**GetPinterestBoards200Response**](GetPinterestBoards200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Boards list |  -  |
| **400** | Not a Pinterest account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getRedditFlairs

> GetRedditFlairs200Response getRedditFlairs(accountId, subreddit)

List subreddit flairs

Returns available post flairs for a subreddit. Some subreddits require a flair when posting.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String subreddit = "subreddit_example"; // String | Subreddit name (without \"r/\" prefix) to fetch flairs for
        try {
            GetRedditFlairs200Response result = apiInstance.getRedditFlairs(accountId, subreddit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getRedditFlairs");
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
| **subreddit** | **String**| Subreddit name (without \&quot;r/\&quot; prefix) to fetch flairs for | |

### Return type

[**GetRedditFlairs200Response**](GetRedditFlairs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flairs list |  -  |
| **400** | Not a Reddit account or missing subreddit parameter |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getRedditFlairsWithHttpInfo

> ApiResponse<GetRedditFlairs200Response> getRedditFlairs getRedditFlairsWithHttpInfo(accountId, subreddit)

List subreddit flairs

Returns available post flairs for a subreddit. Some subreddits require a flair when posting.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String subreddit = "subreddit_example"; // String | Subreddit name (without \"r/\" prefix) to fetch flairs for
        try {
            ApiResponse<GetRedditFlairs200Response> response = apiInstance.getRedditFlairsWithHttpInfo(accountId, subreddit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getRedditFlairs");
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
| **subreddit** | **String**| Subreddit name (without \&quot;r/\&quot; prefix) to fetch flairs for | |

### Return type

ApiResponse<[**GetRedditFlairs200Response**](GetRedditFlairs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flairs list |  -  |
| **400** | Not a Reddit account or missing subreddit parameter |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getRedditSubreddits

> GetRedditSubreddits200Response getRedditSubreddits(accountId)

List Reddit subreddits

Returns the subreddits the connected Reddit account can post to. Use this to get a subreddit name when creating a Reddit post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetRedditSubreddits200Response result = apiInstance.getRedditSubreddits(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getRedditSubreddits");
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

[**GetRedditSubreddits200Response**](GetRedditSubreddits200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subreddits list |  -  |
| **400** | Not a Reddit account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getRedditSubredditsWithHttpInfo

> ApiResponse<GetRedditSubreddits200Response> getRedditSubreddits getRedditSubredditsWithHttpInfo(accountId)

List Reddit subreddits

Returns the subreddits the connected Reddit account can post to. Use this to get a subreddit name when creating a Reddit post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetRedditSubreddits200Response> response = apiInstance.getRedditSubredditsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getRedditSubreddits");
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

ApiResponse<[**GetRedditSubreddits200Response**](GetRedditSubreddits200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subreddits list |  -  |
| **400** | Not a Reddit account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getShopifyConnectUrl

> GetConnectUrl200Response getShopifyConnectUrl(profileId, shop, redirectUrl)

Get Shopify OAuth connect URL

Initiate the Shopify OAuth flow for a store. Shopify is a connect-only platform: the connected account does not publish social posts, it powers the Blogs API (&#x60;/v1/accounts/{accountId}/blogs&#x60;). Returns an &#x60;authUrl&#x60; to redirect the merchant to; after they approve the install, Shopify redirects their browser to Zernio&#39;s callback, the account is created on the profile (platform &#x60;shopify&#x60;), and the browser is redirected to &#x60;redirect_url&#x60; (or the Zernio dashboard when omitted). Requested scopes are &#x60;read_content&#x60; and &#x60;write_content&#x60; (content only; no customer or order data). Connecting the same profile to a store again refreshes the stored token in place. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Your Zernio profile ID (get from /v1/profiles).
        String shop = "shop_example"; // String | The myshopify.com store domain to connect, e.g. `your-store.myshopify.com` (the bare `your-store` prefix is accepted too).
        URI redirectUrl = new URI(); // URI | Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On failure an `error` query param is appended.
        try {
            GetConnectUrl200Response result = apiInstance.getShopifyConnectUrl(profileId, shop, redirectUrl);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getShopifyConnectUrl");
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
| **profileId** | **String**| Your Zernio profile ID (get from /v1/profiles). | |
| **shop** | **String**| The myshopify.com store domain to connect, e.g. &#x60;your-store.myshopify.com&#x60; (the bare &#x60;your-store&#x60; prefix is accepted too). | |
| **redirectUrl** | **URI**| Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On failure an &#x60;error&#x60; query param is appended. | [optional] |

### Return type

[**GetConnectUrl200Response**](GetConnectUrl200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth authorization URL to redirect the merchant to |  -  |
| **400** | Invalid &#x60;profileId&#x60; format, &#x60;shop&#x60; is not a myshopify.com store domain, or &#x60;redirect_url&#x60; is not an absolute http(s) URL or custom app scheme. |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | API key does not have access to this profile. |  -  |
| **404** | Profile not found or access denied. |  -  |
| **500** | Shopify API not configured (missing credentials). |  -  |

## getShopifyConnectUrlWithHttpInfo

> ApiResponse<GetConnectUrl200Response> getShopifyConnectUrl getShopifyConnectUrlWithHttpInfo(profileId, shop, redirectUrl)

Get Shopify OAuth connect URL

Initiate the Shopify OAuth flow for a store. Shopify is a connect-only platform: the connected account does not publish social posts, it powers the Blogs API (&#x60;/v1/accounts/{accountId}/blogs&#x60;). Returns an &#x60;authUrl&#x60; to redirect the merchant to; after they approve the install, Shopify redirects their browser to Zernio&#39;s callback, the account is created on the profile (platform &#x60;shopify&#x60;), and the browser is redirected to &#x60;redirect_url&#x60; (or the Zernio dashboard when omitted). Requested scopes are &#x60;read_content&#x60; and &#x60;write_content&#x60; (content only; no customer or order data). Connecting the same profile to a store again refreshes the stored token in place. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Your Zernio profile ID (get from /v1/profiles).
        String shop = "shop_example"; // String | The myshopify.com store domain to connect, e.g. `your-store.myshopify.com` (the bare `your-store` prefix is accepted too).
        URI redirectUrl = new URI(); // URI | Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On failure an `error` query param is appended.
        try {
            ApiResponse<GetConnectUrl200Response> response = apiInstance.getShopifyConnectUrlWithHttpInfo(profileId, shop, redirectUrl);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getShopifyConnectUrl");
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
| **profileId** | **String**| Your Zernio profile ID (get from /v1/profiles). | |
| **shop** | **String**| The myshopify.com store domain to connect, e.g. &#x60;your-store.myshopify.com&#x60; (the bare &#x60;your-store&#x60; prefix is accepted too). | |
| **redirectUrl** | **URI**| Your custom redirect URL after connection completes. MUST be an absolute http(s) URL or a custom app scheme for mobile deeplinks (e.g. myapp://callback); a relative path is rejected with 400 INVALID_REDIRECT_URL. On failure an &#x60;error&#x60; query param is appended. | [optional] |

### Return type

ApiResponse<[**GetConnectUrl200Response**](GetConnectUrl200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth authorization URL to redirect the merchant to |  -  |
| **400** | Invalid &#x60;profileId&#x60; format, &#x60;shop&#x60; is not a myshopify.com store domain, or &#x60;redirect_url&#x60; is not an absolute http(s) URL or custom app scheme. |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | API key does not have access to this profile. |  -  |
| **404** | Profile not found or access denied. |  -  |
| **500** | Shopify API not configured (missing credentials). |  -  |


## getSubredditRules

> GetSubredditRules200Response getSubredditRules(accountId, subreddit)

Get subreddit rules

Returns a subreddit&#39;s posting rules plus Reddit&#39;s site-wide rules, so you can check them before submitting and avoid a removal.  Use this alongside &#x60;POST /v1/tools/validate/subreddit&#x60;, which only confirms that a subreddit exists and reports its basic posting settings. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The ID of the Reddit account
        String subreddit = "webdev"; // String | Subreddit name (without the \"r/\" prefix)
        try {
            GetSubredditRules200Response result = apiInstance.getSubredditRules(accountId, subreddit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getSubredditRules");
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
| **accountId** | **String**| The ID of the Reddit account | |
| **subreddit** | **String**| Subreddit name (without the \&quot;r/\&quot; prefix) | |

### Return type

[**GetSubredditRules200Response**](GetSubredditRules200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subreddit and site rules |  -  |
| **400** | Not a Reddit account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account or subreddit not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses are forwarded as-is. |  -  |

## getSubredditRulesWithHttpInfo

> ApiResponse<GetSubredditRules200Response> getSubredditRules getSubredditRulesWithHttpInfo(accountId, subreddit)

Get subreddit rules

Returns a subreddit&#39;s posting rules plus Reddit&#39;s site-wide rules, so you can check them before submitting and avoid a removal.  Use this alongside &#x60;POST /v1/tools/validate/subreddit&#x60;, which only confirms that a subreddit exists and reports its basic posting settings. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The ID of the Reddit account
        String subreddit = "webdev"; // String | Subreddit name (without the \"r/\" prefix)
        try {
            ApiResponse<GetSubredditRules200Response> response = apiInstance.getSubredditRulesWithHttpInfo(accountId, subreddit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getSubredditRules");
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
| **accountId** | **String**| The ID of the Reddit account | |
| **subreddit** | **String**| Subreddit name (without the \&quot;r/\&quot; prefix) | |

### Return type

ApiResponse<[**GetSubredditRules200Response**](GetSubredditRules200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subreddit and site rules |  -  |
| **400** | Not a Reddit account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account or subreddit not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses are forwarded as-is. |  -  |


## getTelegramConnectStatus

> GetTelegramConnectStatus200Response getTelegramConnectStatus(profileId)

Generate Telegram code

Generate an access code (valid 15 minutes) for connecting a Telegram channel or group. Add the bot as admin, then send the code + @yourchannel to the bot. Poll PATCH /v1/connect/telegram to check status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | The profile ID to connect the Telegram account to
        try {
            GetTelegramConnectStatus200Response result = apiInstance.getTelegramConnectStatus(profileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getTelegramConnectStatus");
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
| **profileId** | **String**| The profile ID to connect the Telegram account to | |

### Return type

[**GetTelegramConnectStatus200Response**](GetTelegramConnectStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Access code generated |  -  |
| **400** | Profile ID required or invalid format |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to this profile |  -  |
| **404** | Profile not found |  -  |
| **500** | Internal error |  -  |

## getTelegramConnectStatusWithHttpInfo

> ApiResponse<GetTelegramConnectStatus200Response> getTelegramConnectStatus getTelegramConnectStatusWithHttpInfo(profileId)

Generate Telegram code

Generate an access code (valid 15 minutes) for connecting a Telegram channel or group. Add the bot as admin, then send the code + @yourchannel to the bot. Poll PATCH /v1/connect/telegram to check status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | The profile ID to connect the Telegram account to
        try {
            ApiResponse<GetTelegramConnectStatus200Response> response = apiInstance.getTelegramConnectStatusWithHttpInfo(profileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getTelegramConnectStatus");
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
| **profileId** | **String**| The profile ID to connect the Telegram account to | |

### Return type

ApiResponse<[**GetTelegramConnectStatus200Response**](GetTelegramConnectStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Access code generated |  -  |
| **400** | Profile ID required or invalid format |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to this profile |  -  |
| **404** | Profile not found |  -  |
| **500** | Internal error |  -  |


## getYoutubeCaptions

> GetYoutubeCaptions200Response getYoutubeCaptions(accountId, videoId, language, format, refresh)

Get a YouTube video transcript

Returns the caption track YouTube already holds for one of the connected channel&#39;s own videos, as plain text plus timed cues. Use it instead of downloading and transcribing the video yourself.  Auto-generated (ASR) tracks are included: YouTube serves them to the channel owner, which is what the connected account is. Uploaded tracks win over auto-generated ones when both exist for a language.  Caching: we store the transcript on first read and serve it from there afterwards, so you do not need to cache it yourself. A cached read costs no YouTube quota and does not call YouTube at all. &#x60;source&#x60; tells you which happened (&#x60;youtube&#x60; on the first read, &#x60;cache&#x60; after). Pass &#x60;refresh&#x3D;true&#x60; only when the captions actually changed on YouTube, since that re-downloads.  Notes: - Only videos owned by this connected channel. Anything else returns 404. - &#x60;contentDetails.caption&#x60; in YouTube&#39;s own API reads &#x60;false&#x60; on videos that DO have a serving auto-generated track, so it is not a usable availability signal. Call this endpoint and handle the 404. - YouTube generates auto-captions only for videos with recognisable speech, and can take a few hours after upload to publish them. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected YouTube account.
        String videoId = "videoId_example"; // String | The YouTube video id (the `platformPostId` on a synced external post).
        String language = "language_example"; // String | BCP-47 language tag as YouTube labels the track. `en` also matches an `en-GB` track. Omit to take the best available track.
        String format = "json"; // String | `json` returns timed `cues`; `srt` returns the raw SubRip body instead. `text` is present either way.
        Boolean refresh = false; // Boolean | Re-download from YouTube instead of serving the stored copy. Spends 200 quota units.
        try {
            GetYoutubeCaptions200Response result = apiInstance.getYoutubeCaptions(accountId, videoId, language, format, refresh);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getYoutubeCaptions");
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
| **accountId** | **String**| The connected YouTube account. | |
| **videoId** | **String**| The YouTube video id (the &#x60;platformPostId&#x60; on a synced external post). | |
| **language** | **String**| BCP-47 language tag as YouTube labels the track. &#x60;en&#x60; also matches an &#x60;en-GB&#x60; track. Omit to take the best available track. | [optional] |
| **format** | **String**| &#x60;json&#x60; returns timed &#x60;cues&#x60;; &#x60;srt&#x60; returns the raw SubRip body instead. &#x60;text&#x60; is present either way. | [optional] [default to json] [enum: json, srt] |
| **refresh** | **Boolean**| Re-download from YouTube instead of serving the stored copy. Spends 200 quota units. | [optional] [default to false] |

### Return type

[**GetYoutubeCaptions200Response**](GetYoutubeCaptions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The transcript. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found, the video does not belong to this channel (&#x60;video_not_found&#x60;), or the video has no caption track in the requested language (&#x60;captions_not_found&#x60;). |  -  |

## getYoutubeCaptionsWithHttpInfo

> ApiResponse<GetYoutubeCaptions200Response> getYoutubeCaptions getYoutubeCaptionsWithHttpInfo(accountId, videoId, language, format, refresh)

Get a YouTube video transcript

Returns the caption track YouTube already holds for one of the connected channel&#39;s own videos, as plain text plus timed cues. Use it instead of downloading and transcribing the video yourself.  Auto-generated (ASR) tracks are included: YouTube serves them to the channel owner, which is what the connected account is. Uploaded tracks win over auto-generated ones when both exist for a language.  Caching: we store the transcript on first read and serve it from there afterwards, so you do not need to cache it yourself. A cached read costs no YouTube quota and does not call YouTube at all. &#x60;source&#x60; tells you which happened (&#x60;youtube&#x60; on the first read, &#x60;cache&#x60; after). Pass &#x60;refresh&#x3D;true&#x60; only when the captions actually changed on YouTube, since that re-downloads.  Notes: - Only videos owned by this connected channel. Anything else returns 404. - &#x60;contentDetails.caption&#x60; in YouTube&#39;s own API reads &#x60;false&#x60; on videos that DO have a serving auto-generated track, so it is not a usable availability signal. Call this endpoint and handle the 404. - YouTube generates auto-captions only for videos with recognisable speech, and can take a few hours after upload to publish them. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected YouTube account.
        String videoId = "videoId_example"; // String | The YouTube video id (the `platformPostId` on a synced external post).
        String language = "language_example"; // String | BCP-47 language tag as YouTube labels the track. `en` also matches an `en-GB` track. Omit to take the best available track.
        String format = "json"; // String | `json` returns timed `cues`; `srt` returns the raw SubRip body instead. `text` is present either way.
        Boolean refresh = false; // Boolean | Re-download from YouTube instead of serving the stored copy. Spends 200 quota units.
        try {
            ApiResponse<GetYoutubeCaptions200Response> response = apiInstance.getYoutubeCaptionsWithHttpInfo(accountId, videoId, language, format, refresh);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getYoutubeCaptions");
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
| **accountId** | **String**| The connected YouTube account. | |
| **videoId** | **String**| The YouTube video id (the &#x60;platformPostId&#x60; on a synced external post). | |
| **language** | **String**| BCP-47 language tag as YouTube labels the track. &#x60;en&#x60; also matches an &#x60;en-GB&#x60; track. Omit to take the best available track. | [optional] |
| **format** | **String**| &#x60;json&#x60; returns timed &#x60;cues&#x60;; &#x60;srt&#x60; returns the raw SubRip body instead. &#x60;text&#x60; is present either way. | [optional] [default to json] [enum: json, srt] |
| **refresh** | **Boolean**| Re-download from YouTube instead of serving the stored copy. Spends 200 quota units. | [optional] [default to false] |

### Return type

ApiResponse<[**GetYoutubeCaptions200Response**](GetYoutubeCaptions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The transcript. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found, the video does not belong to this channel (&#x60;video_not_found&#x60;), or the video has no caption track in the requested language (&#x60;captions_not_found&#x60;). |  -  |


## getYoutubePlaylists

> GetYoutubePlaylists200Response getYoutubePlaylists(accountId)

List YouTube playlists

Returns the playlists available for a connected YouTube account. Use this to get a playlist ID when creating a YouTube post with the playlistId field.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetYoutubePlaylists200Response result = apiInstance.getYoutubePlaylists(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getYoutubePlaylists");
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

[**GetYoutubePlaylists200Response**](GetYoutubePlaylists200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Playlists list |  -  |
| **400** | Not a YouTube account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getYoutubePlaylistsWithHttpInfo

> ApiResponse<GetYoutubePlaylists200Response> getYoutubePlaylists getYoutubePlaylistsWithHttpInfo(accountId)

List YouTube playlists

Returns the playlists available for a connected YouTube account. Use this to get a playlist ID when creating a YouTube post with the playlistId field.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetYoutubePlaylists200Response> response = apiInstance.getYoutubePlaylistsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#getYoutubePlaylists");
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

ApiResponse<[**GetYoutubePlaylists200Response**](GetYoutubePlaylists200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Playlists list |  -  |
| **400** | Not a YouTube account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## handleOAuthCallback

> void handleOAuthCallback(platform, handleOAuthCallbackRequest)

Complete OAuth callback

Exchange the OAuth authorization code for tokens and connect the account to the specified profile.  Facebook, Google Business, Snapchat and WhatsApp are not accepted here: their account identity is a destination chosen after OAuth, which this single-shot exchange cannot do. Connect them through the redirect flow from &#x60;GET /v1/connect/{platform}&#x60;, or, for WhatsApp Embedded Signup, through &#x60;POST /v1/connect/whatsapp/embedded-signup&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String platform = "instagram"; // String | Social platform to complete the connect for. Discord, Slack and Telegram are absent because they are served by their own dedicated routes, documented separately. 
        HandleOAuthCallbackRequest handleOAuthCallbackRequest = new HandleOAuthCallbackRequest(); // HandleOAuthCallbackRequest | 
        try {
            apiInstance.handleOAuthCallback(platform, handleOAuthCallbackRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#handleOAuthCallback");
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
| **platform** | **String**| Social platform to complete the connect for. Discord, Slack and Telegram are absent because they are served by their own dedicated routes, documented separately.  | [enum: instagram, twitter, threads, linkedin, youtube, tiktok, reddit, pinterest] |
| **handleOAuthCallbackRequest** | [**HandleOAuthCallbackRequest**](HandleOAuthCallbackRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account connected |  -  |
| **400** | Invalid params, or the platform requires choosing a destination (code: platform_requires_destination) |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | No access to the profile, or BYOK required for AppSumo Twitter |  -  |
| **404** | Profile not found |  -  |
| **500** | Internal error while connecting the account |  -  |
| **502** | The platform rejected the token exchange (type: platform_error; an upstream 4xx status is forwarded instead of 502) |  -  |
| **503** | Connections for this platform are temporarily disabled (code: platform_disabled) |  -  |

## handleOAuthCallbackWithHttpInfo

> ApiResponse<Void> handleOAuthCallback handleOAuthCallbackWithHttpInfo(platform, handleOAuthCallbackRequest)

Complete OAuth callback

Exchange the OAuth authorization code for tokens and connect the account to the specified profile.  Facebook, Google Business, Snapchat and WhatsApp are not accepted here: their account identity is a destination chosen after OAuth, which this single-shot exchange cannot do. Connect them through the redirect flow from &#x60;GET /v1/connect/{platform}&#x60;, or, for WhatsApp Embedded Signup, through &#x60;POST /v1/connect/whatsapp/embedded-signup&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String platform = "instagram"; // String | Social platform to complete the connect for. Discord, Slack and Telegram are absent because they are served by their own dedicated routes, documented separately. 
        HandleOAuthCallbackRequest handleOAuthCallbackRequest = new HandleOAuthCallbackRequest(); // HandleOAuthCallbackRequest | 
        try {
            ApiResponse<Void> response = apiInstance.handleOAuthCallbackWithHttpInfo(platform, handleOAuthCallbackRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#handleOAuthCallback");
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
| **platform** | **String**| Social platform to complete the connect for. Discord, Slack and Telegram are absent because they are served by their own dedicated routes, documented separately.  | [enum: instagram, twitter, threads, linkedin, youtube, tiktok, reddit, pinterest] |
| **handleOAuthCallbackRequest** | [**HandleOAuthCallbackRequest**](HandleOAuthCallbackRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account connected |  -  |
| **400** | Invalid params, or the platform requires choosing a destination (code: platform_requires_destination) |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | No access to the profile, or BYOK required for AppSumo Twitter |  -  |
| **404** | Profile not found |  -  |
| **500** | Internal error while connecting the account |  -  |
| **502** | The platform rejected the token exchange (type: platform_error; an upstream 4xx status is forwarded instead of 502) |  -  |
| **503** | Connections for this platform are temporarily disabled (code: platform_disabled) |  -  |


## initiateTelegramConnect

> InitiateTelegramConnect200Response initiateTelegramConnect(initiateTelegramConnectRequest)

Connect Telegram directly

Connect a Telegram channel/group directly using the chat ID. Alternative to the access code flow. The bot must already be an admin in the channel/group.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        InitiateTelegramConnectRequest initiateTelegramConnectRequest = new InitiateTelegramConnectRequest(); // InitiateTelegramConnectRequest | 
        try {
            InitiateTelegramConnect200Response result = apiInstance.initiateTelegramConnect(initiateTelegramConnectRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#initiateTelegramConnect");
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
| **initiateTelegramConnectRequest** | [**InitiateTelegramConnectRequest**](InitiateTelegramConnectRequest.md)|  | |

### Return type

[**InitiateTelegramConnect200Response**](InitiateTelegramConnect200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Telegram channel connected successfully |  -  |
| **400** | Chat ID required, bot not admin, or cannot access chat |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to this profile |  -  |
| **404** | Profile not found |  -  |
| **500** | Internal error |  -  |

## initiateTelegramConnectWithHttpInfo

> ApiResponse<InitiateTelegramConnect200Response> initiateTelegramConnect initiateTelegramConnectWithHttpInfo(initiateTelegramConnectRequest)

Connect Telegram directly

Connect a Telegram channel/group directly using the chat ID. Alternative to the access code flow. The bot must already be an admin in the channel/group.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        InitiateTelegramConnectRequest initiateTelegramConnectRequest = new InitiateTelegramConnectRequest(); // InitiateTelegramConnectRequest | 
        try {
            ApiResponse<InitiateTelegramConnect200Response> response = apiInstance.initiateTelegramConnectWithHttpInfo(initiateTelegramConnectRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#initiateTelegramConnect");
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
| **initiateTelegramConnectRequest** | [**InitiateTelegramConnectRequest**](InitiateTelegramConnectRequest.md)|  | |

### Return type

ApiResponse<[**InitiateTelegramConnect200Response**](InitiateTelegramConnect200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Telegram channel connected successfully |  -  |
| **400** | Chat ID required, bot not admin, or cannot access chat |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to this profile |  -  |
| **404** | Profile not found |  -  |
| **500** | Internal error |  -  |


## listFacebookPages

> ListFacebookPages200Response listFacebookPages(profileId, tempToken)

List Facebook pages

Returns the list of Facebook Pages the user can manage after OAuth. Extract tempToken and userProfile from the OAuth redirect params and pass them here. Use the X-Connect-Token header if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Profile ID from your connection flow
        String tempToken = "tempToken_example"; // String | Temporary Facebook access token from the OAuth callback redirect
        try {
            ListFacebookPages200Response result = apiInstance.listFacebookPages(profileId, tempToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listFacebookPages");
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
| **profileId** | **String**| Profile ID from your connection flow | |
| **tempToken** | **String**| Temporary Facebook access token from the OAuth callback redirect | |

### Return type

[**ListFacebookPages200Response**](ListFacebookPages200Response.md)


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Facebook Pages available for connection |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to fetch pages (e.g., invalid token, insufficient permissions) |  -  |

## listFacebookPagesWithHttpInfo

> ApiResponse<ListFacebookPages200Response> listFacebookPages listFacebookPagesWithHttpInfo(profileId, tempToken)

List Facebook pages

Returns the list of Facebook Pages the user can manage after OAuth. Extract tempToken and userProfile from the OAuth redirect params and pass them here. Use the X-Connect-Token header if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Profile ID from your connection flow
        String tempToken = "tempToken_example"; // String | Temporary Facebook access token from the OAuth callback redirect
        try {
            ApiResponse<ListFacebookPages200Response> response = apiInstance.listFacebookPagesWithHttpInfo(profileId, tempToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listFacebookPages");
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
| **profileId** | **String**| Profile ID from your connection flow | |
| **tempToken** | **String**| Temporary Facebook access token from the OAuth callback redirect | |

### Return type

ApiResponse<[**ListFacebookPages200Response**](ListFacebookPages200Response.md)>


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Facebook Pages available for connection |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to fetch pages (e.g., invalid token, insufficient permissions) |  -  |


## listGoogleBusinessLocations

> ListGoogleBusinessLocations200Response listGoogleBusinessLocations(profileId, pendingDataToken, tempToken, search, filter)

List GBP locations

For headless flows. Returns the list of GBP locations the user can manage. Use pendingDataToken (from the OAuth callback redirect) to list locations without consuming the token, so it remains available for select-location. Use X-Connect-Token header if connecting via API key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Profile ID from your connection flow. Required for auth validation when provided.
        String pendingDataToken = "pendingDataToken_example"; // String | Token from the OAuth callback redirect. Preferred over tempToken because it preserves server-side token storage. One of pendingDataToken or tempToken is required.
        String tempToken = "tempToken_example"; // String | Legacy. Direct Google access token. Use pendingDataToken instead when available.
        String search = "search_example"; // String | Free-text search on the business name, applied server-side by Google. Use this for accounts that own many locations (the response is bounded, see hasMore) so the user can find a specific location without loading the full list. 
        String filter = "filter_example"; // String | Raw Google Business Information API filter expression (advanced; takes precedence over search). Supports fields such as title, storeCode, storefront_address.postal_code, labels and categories, e.g. storeCode=\"LH279411\". See Google's \"Work with location data\" guide. 
        try {
            ListGoogleBusinessLocations200Response result = apiInstance.listGoogleBusinessLocations(profileId, pendingDataToken, tempToken, search, filter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listGoogleBusinessLocations");
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
| **profileId** | **String**| Profile ID from your connection flow. Required for auth validation when provided. | [optional] |
| **pendingDataToken** | **String**| Token from the OAuth callback redirect. Preferred over tempToken because it preserves server-side token storage. One of pendingDataToken or tempToken is required. | [optional] |
| **tempToken** | **String**| Legacy. Direct Google access token. Use pendingDataToken instead when available. | [optional] |
| **search** | **String**| Free-text search on the business name, applied server-side by Google. Use this for accounts that own many locations (the response is bounded, see hasMore) so the user can find a specific location without loading the full list.  | [optional] |
| **filter** | **String**| Raw Google Business Information API filter expression (advanced; takes precedence over search). Supports fields such as title, storeCode, storefront_address.postal_code, labels and categories, e.g. storeCode&#x3D;\&quot;LH279411\&quot;. See Google&#39;s \&quot;Work with location data\&quot; guide.  | [optional] |

### Return type

[**ListGoogleBusinessLocations200Response**](ListGoogleBusinessLocations200Response.md)


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Google Business locations available for connection |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to fetch locations (e.g., invalid token, insufficient permissions) |  -  |

## listGoogleBusinessLocationsWithHttpInfo

> ApiResponse<ListGoogleBusinessLocations200Response> listGoogleBusinessLocations listGoogleBusinessLocationsWithHttpInfo(profileId, pendingDataToken, tempToken, search, filter)

List GBP locations

For headless flows. Returns the list of GBP locations the user can manage. Use pendingDataToken (from the OAuth callback redirect) to list locations without consuming the token, so it remains available for select-location. Use X-Connect-Token header if connecting via API key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Profile ID from your connection flow. Required for auth validation when provided.
        String pendingDataToken = "pendingDataToken_example"; // String | Token from the OAuth callback redirect. Preferred over tempToken because it preserves server-side token storage. One of pendingDataToken or tempToken is required.
        String tempToken = "tempToken_example"; // String | Legacy. Direct Google access token. Use pendingDataToken instead when available.
        String search = "search_example"; // String | Free-text search on the business name, applied server-side by Google. Use this for accounts that own many locations (the response is bounded, see hasMore) so the user can find a specific location without loading the full list. 
        String filter = "filter_example"; // String | Raw Google Business Information API filter expression (advanced; takes precedence over search). Supports fields such as title, storeCode, storefront_address.postal_code, labels and categories, e.g. storeCode=\"LH279411\". See Google's \"Work with location data\" guide. 
        try {
            ApiResponse<ListGoogleBusinessLocations200Response> response = apiInstance.listGoogleBusinessLocationsWithHttpInfo(profileId, pendingDataToken, tempToken, search, filter);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listGoogleBusinessLocations");
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
| **profileId** | **String**| Profile ID from your connection flow. Required for auth validation when provided. | [optional] |
| **pendingDataToken** | **String**| Token from the OAuth callback redirect. Preferred over tempToken because it preserves server-side token storage. One of pendingDataToken or tempToken is required. | [optional] |
| **tempToken** | **String**| Legacy. Direct Google access token. Use pendingDataToken instead when available. | [optional] |
| **search** | **String**| Free-text search on the business name, applied server-side by Google. Use this for accounts that own many locations (the response is bounded, see hasMore) so the user can find a specific location without loading the full list.  | [optional] |
| **filter** | **String**| Raw Google Business Information API filter expression (advanced; takes precedence over search). Supports fields such as title, storeCode, storefront_address.postal_code, labels and categories, e.g. storeCode&#x3D;\&quot;LH279411\&quot;. See Google&#39;s \&quot;Work with location data\&quot; guide.  | [optional] |

### Return type

ApiResponse<[**ListGoogleBusinessLocations200Response**](ListGoogleBusinessLocations200Response.md)>


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Google Business locations available for connection |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to fetch locations (e.g., invalid token, insufficient permissions) |  -  |


## listInstagramPages

> ListInstagramPages200Response listInstagramPages(profileId, tempToken)

List Pages with a linked Instagram account

Completes the &#x60;loginMethod&#x3D;facebook_login&#x60; Instagram flow, i.e. \&quot;Instagram API with Facebook Login\&quot;.  After the user authorizes on Facebook, extract &#x60;tempToken&#x60; from the redirect params (headless mode adds &#x60;step&#x3D;select_account&#x60;) and pass it here to list the Facebook Pages they manage. Only Pages that have a linked Instagram professional account are returned, so an empty array means the user has no eligible Page. Use the X-Connect-Token header if connecting via API key.  Not used by the default &#x60;instagram_login&#x60; flow, which creates the account without a selection step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Profile ID from your connection flow
        String tempToken = "tempToken_example"; // String | Long-lived Facebook user access token from the OAuth callback redirect
        try {
            ListInstagramPages200Response result = apiInstance.listInstagramPages(profileId, tempToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listInstagramPages");
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
| **profileId** | **String**| Profile ID from your connection flow | |
| **tempToken** | **String**| Long-lived Facebook user access token from the OAuth callback redirect | |

### Return type

[**ListInstagramPages200Response**](ListInstagramPages200Response.md)


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Facebook Pages that have a linked Instagram professional account |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **403** | User does not have access to the specified profile |  -  |

## listInstagramPagesWithHttpInfo

> ApiResponse<ListInstagramPages200Response> listInstagramPages listInstagramPagesWithHttpInfo(profileId, tempToken)

List Pages with a linked Instagram account

Completes the &#x60;loginMethod&#x3D;facebook_login&#x60; Instagram flow, i.e. \&quot;Instagram API with Facebook Login\&quot;.  After the user authorizes on Facebook, extract &#x60;tempToken&#x60; from the redirect params (headless mode adds &#x60;step&#x3D;select_account&#x60;) and pass it here to list the Facebook Pages they manage. Only Pages that have a linked Instagram professional account are returned, so an empty array means the user has no eligible Page. Use the X-Connect-Token header if connecting via API key.  Not used by the default &#x60;instagram_login&#x60; flow, which creates the account without a selection step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | Profile ID from your connection flow
        String tempToken = "tempToken_example"; // String | Long-lived Facebook user access token from the OAuth callback redirect
        try {
            ApiResponse<ListInstagramPages200Response> response = apiInstance.listInstagramPagesWithHttpInfo(profileId, tempToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listInstagramPages");
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
| **profileId** | **String**| Profile ID from your connection flow | |
| **tempToken** | **String**| Long-lived Facebook user access token from the OAuth callback redirect | |

### Return type

ApiResponse<[**ListInstagramPages200Response**](ListInstagramPages200Response.md)>


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Facebook Pages that have a linked Instagram professional account |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **403** | User does not have access to the specified profile |  -  |


## listLinkedInOrganizations

> ListLinkedInOrganizations200Response listLinkedInOrganizations(tempToken, orgIds)

List LinkedIn orgs

Fetch full LinkedIn organization details (logos, vanity names, websites) for custom UI. No authentication required, just the tempToken from OAuth.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String tempToken = "tempToken_example"; // String | The temporary LinkedIn access token from the OAuth redirect
        String orgIds = "12345678,87654321,11111111"; // String | Comma-separated list of organization IDs to fetch details for (max 100)
        try {
            ListLinkedInOrganizations200Response result = apiInstance.listLinkedInOrganizations(tempToken, orgIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listLinkedInOrganizations");
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
| **tempToken** | **String**| The temporary LinkedIn access token from the OAuth redirect | |
| **orgIds** | **String**| Comma-separated list of organization IDs to fetch details for (max 100) | |

### Return type

[**ListLinkedInOrganizations200Response**](ListLinkedInOrganizations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization details fetched successfully |  -  |
| **400** | Missing required parameters or too many organization IDs |  -  |
| **500** | Failed to fetch organization details |  -  |

## listLinkedInOrganizationsWithHttpInfo

> ApiResponse<ListLinkedInOrganizations200Response> listLinkedInOrganizations listLinkedInOrganizationsWithHttpInfo(tempToken, orgIds)

List LinkedIn orgs

Fetch full LinkedIn organization details (logos, vanity names, websites) for custom UI. No authentication required, just the tempToken from OAuth.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String tempToken = "tempToken_example"; // String | The temporary LinkedIn access token from the OAuth redirect
        String orgIds = "12345678,87654321,11111111"; // String | Comma-separated list of organization IDs to fetch details for (max 100)
        try {
            ApiResponse<ListLinkedInOrganizations200Response> response = apiInstance.listLinkedInOrganizationsWithHttpInfo(tempToken, orgIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listLinkedInOrganizations");
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
| **tempToken** | **String**| The temporary LinkedIn access token from the OAuth redirect | |
| **orgIds** | **String**| Comma-separated list of organization IDs to fetch details for (max 100) | |

### Return type

ApiResponse<[**ListLinkedInOrganizations200Response**](ListLinkedInOrganizations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization details fetched successfully |  -  |
| **400** | Missing required parameters or too many organization IDs |  -  |
| **500** | Failed to fetch organization details |  -  |


## listPinterestBoardsForSelection

> ListPinterestBoardsForSelection200Response listPinterestBoardsForSelection(xConnectToken, profileId, tempToken)

List Pinterest boards

For headless flows. Returns Pinterest boards the user can post to. Use X-Connect-Token from the redirect URL.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String xConnectToken = "xConnectToken_example"; // String | Short-lived connect token from the OAuth redirect
        String profileId = "profileId_example"; // String | Your Zernio profile ID
        String tempToken = "tempToken_example"; // String | Temporary Pinterest access token from the OAuth callback redirect
        try {
            ListPinterestBoardsForSelection200Response result = apiInstance.listPinterestBoardsForSelection(xConnectToken, profileId, tempToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listPinterestBoardsForSelection");
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
| **xConnectToken** | **String**| Short-lived connect token from the OAuth redirect | |
| **profileId** | **String**| Your Zernio profile ID | |
| **tempToken** | **String**| Temporary Pinterest access token from the OAuth callback redirect | |

### Return type

[**ListPinterestBoardsForSelection200Response**](ListPinterestBoardsForSelection200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Pinterest Boards available for connection |  -  |
| **400** | Missing required parameters |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile |  -  |
| **500** | Failed to fetch boards |  -  |

## listPinterestBoardsForSelectionWithHttpInfo

> ApiResponse<ListPinterestBoardsForSelection200Response> listPinterestBoardsForSelection listPinterestBoardsForSelectionWithHttpInfo(xConnectToken, profileId, tempToken)

List Pinterest boards

For headless flows. Returns Pinterest boards the user can post to. Use X-Connect-Token from the redirect URL.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String xConnectToken = "xConnectToken_example"; // String | Short-lived connect token from the OAuth redirect
        String profileId = "profileId_example"; // String | Your Zernio profile ID
        String tempToken = "tempToken_example"; // String | Temporary Pinterest access token from the OAuth callback redirect
        try {
            ApiResponse<ListPinterestBoardsForSelection200Response> response = apiInstance.listPinterestBoardsForSelectionWithHttpInfo(xConnectToken, profileId, tempToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listPinterestBoardsForSelection");
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
| **xConnectToken** | **String**| Short-lived connect token from the OAuth redirect | |
| **profileId** | **String**| Your Zernio profile ID | |
| **tempToken** | **String**| Temporary Pinterest access token from the OAuth callback redirect | |

### Return type

ApiResponse<[**ListPinterestBoardsForSelection200Response**](ListPinterestBoardsForSelection200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Pinterest Boards available for connection |  -  |
| **400** | Missing required parameters |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile |  -  |
| **500** | Failed to fetch boards |  -  |


## listSnapchatProfiles

> ListSnapchatProfiles200Response listSnapchatProfiles(xConnectToken, profileId, tempToken)

List Snapchat profiles

For headless flows. Returns Snapchat Public Profiles the user can post to. Use X-Connect-Token from the redirect URL.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String xConnectToken = "xConnectToken_example"; // String | Short-lived connect token from the OAuth redirect
        String profileId = "profileId_example"; // String | Your Zernio profile ID
        String tempToken = "tempToken_example"; // String | Temporary Snapchat access token from the OAuth callback redirect
        try {
            ListSnapchatProfiles200Response result = apiInstance.listSnapchatProfiles(xConnectToken, profileId, tempToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listSnapchatProfiles");
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
| **xConnectToken** | **String**| Short-lived connect token from the OAuth redirect | |
| **profileId** | **String**| Your Zernio profile ID | |
| **tempToken** | **String**| Temporary Snapchat access token from the OAuth callback redirect | |

### Return type

[**ListSnapchatProfiles200Response**](ListSnapchatProfiles200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Snapchat Public Profiles available for connection |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile |  -  |
| **500** | Failed to fetch public profiles |  -  |

## listSnapchatProfilesWithHttpInfo

> ApiResponse<ListSnapchatProfiles200Response> listSnapchatProfiles listSnapchatProfilesWithHttpInfo(xConnectToken, profileId, tempToken)

List Snapchat profiles

For headless flows. Returns Snapchat Public Profiles the user can post to. Use X-Connect-Token from the redirect URL.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String xConnectToken = "xConnectToken_example"; // String | Short-lived connect token from the OAuth redirect
        String profileId = "profileId_example"; // String | Your Zernio profile ID
        String tempToken = "tempToken_example"; // String | Temporary Snapchat access token from the OAuth callback redirect
        try {
            ApiResponse<ListSnapchatProfiles200Response> response = apiInstance.listSnapchatProfilesWithHttpInfo(xConnectToken, profileId, tempToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listSnapchatProfiles");
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
| **xConnectToken** | **String**| Short-lived connect token from the OAuth redirect | |
| **profileId** | **String**| Your Zernio profile ID | |
| **tempToken** | **String**| Temporary Snapchat access token from the OAuth callback redirect | |

### Return type

ApiResponse<[**ListSnapchatProfiles200Response**](ListSnapchatProfiles200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Snapchat Public Profiles available for connection |  -  |
| **400** | Missing required parameters (profileId or tempToken) |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile |  -  |
| **500** | Failed to fetch public profiles |  -  |


## listWhatsAppPhoneNumbers

> ListWhatsAppPhoneNumbers200Response listWhatsAppPhoneNumbers(profileId, tempToken, xConnectToken)

List numbers for selection

Fetch the WhatsApp phone numbers available across the user&#39;s WhatsApp Business Accounts (WABAs) after a headless OAuth flow.  WhatsApp OAuth grants access at the WABA level. When a connected WABA has 2 or more phone numbers, you must call this endpoint to list them and then &#x60;POST /v1/connect/whatsapp/select-phone-number&#x60; to bind one to the Zernio profile. Single-phone WABAs auto-complete during the OAuth callback and never reach this endpoint.  Use the &#x60;profileId&#x60; and &#x60;tempToken&#x60; returned in the headless redirect (&#x60;step&#x3D;select_phone_number&#x60;).  Alternative: if you already know &#x60;wabaId&#x60; and &#x60;phoneNumberId&#x60; (e.g. from Meta Business Suite), use &#x60;connectWhatsAppCredentials&#x60; instead, which skips this two-step flow. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | The Zernio profile ID from the headless redirect
        String tempToken = "tempToken_example"; // String | The temporary access token from the headless redirect
        String xConnectToken = "xConnectToken_example"; // String | Alternative auth for API users' end customers (used when the bearer token is scoped to a different user)
        try {
            ListWhatsAppPhoneNumbers200Response result = apiInstance.listWhatsAppPhoneNumbers(profileId, tempToken, xConnectToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listWhatsAppPhoneNumbers");
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
| **profileId** | **String**| The Zernio profile ID from the headless redirect | |
| **tempToken** | **String**| The temporary access token from the headless redirect | |
| **xConnectToken** | **String**| Alternative auth for API users&#39; end customers (used when the bearer token is scoped to a different user) | [optional] |

### Return type

[**ListWhatsAppPhoneNumbers200Response**](ListWhatsAppPhoneNumbers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone numbers fetched successfully |  -  |
| **400** | Missing profileId or tempToken |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to fetch phone numbers (Meta API error, expired token, or insufficient permissions) |  -  |

## listWhatsAppPhoneNumbersWithHttpInfo

> ApiResponse<ListWhatsAppPhoneNumbers200Response> listWhatsAppPhoneNumbers listWhatsAppPhoneNumbersWithHttpInfo(profileId, tempToken, xConnectToken)

List numbers for selection

Fetch the WhatsApp phone numbers available across the user&#39;s WhatsApp Business Accounts (WABAs) after a headless OAuth flow.  WhatsApp OAuth grants access at the WABA level. When a connected WABA has 2 or more phone numbers, you must call this endpoint to list them and then &#x60;POST /v1/connect/whatsapp/select-phone-number&#x60; to bind one to the Zernio profile. Single-phone WABAs auto-complete during the OAuth callback and never reach this endpoint.  Use the &#x60;profileId&#x60; and &#x60;tempToken&#x60; returned in the headless redirect (&#x60;step&#x3D;select_phone_number&#x60;).  Alternative: if you already know &#x60;wabaId&#x60; and &#x60;phoneNumberId&#x60; (e.g. from Meta Business Suite), use &#x60;connectWhatsAppCredentials&#x60; instead, which skips this two-step flow. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String profileId = "profileId_example"; // String | The Zernio profile ID from the headless redirect
        String tempToken = "tempToken_example"; // String | The temporary access token from the headless redirect
        String xConnectToken = "xConnectToken_example"; // String | Alternative auth for API users' end customers (used when the bearer token is scoped to a different user)
        try {
            ApiResponse<ListWhatsAppPhoneNumbers200Response> response = apiInstance.listWhatsAppPhoneNumbersWithHttpInfo(profileId, tempToken, xConnectToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#listWhatsAppPhoneNumbers");
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
| **profileId** | **String**| The Zernio profile ID from the headless redirect | |
| **tempToken** | **String**| The temporary access token from the headless redirect | |
| **xConnectToken** | **String**| Alternative auth for API users&#39; end customers (used when the bearer token is scoped to a different user) | [optional] |

### Return type

ApiResponse<[**ListWhatsAppPhoneNumbers200Response**](ListWhatsAppPhoneNumbers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone numbers fetched successfully |  -  |
| **400** | Missing profileId or tempToken |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to fetch phone numbers (Meta API error, expired token, or insufficient permissions) |  -  |


## selectFacebookPage

> SelectFacebookPage200Response selectFacebookPage(selectFacebookPageRequest)

Select Facebook page

Complete the headless flow by saving the user&#39;s selected Facebook page. Pass the userProfile from the OAuth redirect and use X-Connect-Token if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectFacebookPageRequest selectFacebookPageRequest = new SelectFacebookPageRequest(); // SelectFacebookPageRequest | 
        try {
            SelectFacebookPage200Response result = apiInstance.selectFacebookPage(selectFacebookPageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectFacebookPage");
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
| **selectFacebookPageRequest** | [**SelectFacebookPageRequest**](SelectFacebookPageRequest.md)|  | |

### Return type

[**SelectFacebookPage200Response**](SelectFacebookPage200Response.md)


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Facebook Page connected successfully |  -  |
| **400** | Missing required fields (profileId, pageId, tempToken, or userProfile) |  -  |
| **401** | Unauthorized |  -  |
| **403** | User does not have access to the specified profile |  -  |
| **404** | Selected page not found in available pages |  -  |
| **409** | Reconnect identity mismatch. The OAuth was initiated as a &#x60;force&#x3D;true&#x60; token-recovery re-auth (&#x60;GET /v1/connect/{platform}/ads&#x60;), but the grant landed on a different Facebook user or page than the connected account. The existing account is left untouched.  |  -  |
| **500** | Failed to save Facebook connection |  -  |

## selectFacebookPageWithHttpInfo

> ApiResponse<SelectFacebookPage200Response> selectFacebookPage selectFacebookPageWithHttpInfo(selectFacebookPageRequest)

Select Facebook page

Complete the headless flow by saving the user&#39;s selected Facebook page. Pass the userProfile from the OAuth redirect and use X-Connect-Token if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectFacebookPageRequest selectFacebookPageRequest = new SelectFacebookPageRequest(); // SelectFacebookPageRequest | 
        try {
            ApiResponse<SelectFacebookPage200Response> response = apiInstance.selectFacebookPageWithHttpInfo(selectFacebookPageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectFacebookPage");
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
| **selectFacebookPageRequest** | [**SelectFacebookPageRequest**](SelectFacebookPageRequest.md)|  | |

### Return type

ApiResponse<[**SelectFacebookPage200Response**](SelectFacebookPage200Response.md)>


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Facebook Page connected successfully |  -  |
| **400** | Missing required fields (profileId, pageId, tempToken, or userProfile) |  -  |
| **401** | Unauthorized |  -  |
| **403** | User does not have access to the specified profile |  -  |
| **404** | Selected page not found in available pages |  -  |
| **409** | Reconnect identity mismatch. The OAuth was initiated as a &#x60;force&#x3D;true&#x60; token-recovery re-auth (&#x60;GET /v1/connect/{platform}/ads&#x60;), but the grant landed on a different Facebook user or page than the connected account. The existing account is left untouched.  |  -  |
| **500** | Failed to save Facebook connection |  -  |


## selectGoogleBusinessLocation

> SelectGoogleBusinessLocation200Response selectGoogleBusinessLocation(selectGoogleBusinessLocationRequest)

Select GBP location

Complete the headless GBP flow by saving the user&#39;s selected location. The pendingDataToken is returned in your redirect URL after OAuth completes (step&#x3D;select_location). Tokens and profile data are stored server-side, so only the pendingDataToken is needed here. Use X-Connect-Token header if connecting via API key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectGoogleBusinessLocationRequest selectGoogleBusinessLocationRequest = new SelectGoogleBusinessLocationRequest(); // SelectGoogleBusinessLocationRequest | 
        try {
            SelectGoogleBusinessLocation200Response result = apiInstance.selectGoogleBusinessLocation(selectGoogleBusinessLocationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectGoogleBusinessLocation");
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
| **selectGoogleBusinessLocationRequest** | [**SelectGoogleBusinessLocationRequest**](SelectGoogleBusinessLocationRequest.md)|  | |

### Return type

[**SelectGoogleBusinessLocation200Response**](SelectGoogleBusinessLocation200Response.md)


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Google Business location connected successfully |  -  |
| **400** | Missing required fields (profileId, locationId, or tempToken), or the provided accountId is not one of the accounts this connection manages |  -  |
| **401** | Unauthorized |  -  |
| **403** | User does not have access to the specified profile |  -  |
| **404** | Selected location not found in available locations |  -  |
| **500** | Failed to save Google Business connection |  -  |

## selectGoogleBusinessLocationWithHttpInfo

> ApiResponse<SelectGoogleBusinessLocation200Response> selectGoogleBusinessLocation selectGoogleBusinessLocationWithHttpInfo(selectGoogleBusinessLocationRequest)

Select GBP location

Complete the headless GBP flow by saving the user&#39;s selected location. The pendingDataToken is returned in your redirect URL after OAuth completes (step&#x3D;select_location). Tokens and profile data are stored server-side, so only the pendingDataToken is needed here. Use X-Connect-Token header if connecting via API key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectGoogleBusinessLocationRequest selectGoogleBusinessLocationRequest = new SelectGoogleBusinessLocationRequest(); // SelectGoogleBusinessLocationRequest | 
        try {
            ApiResponse<SelectGoogleBusinessLocation200Response> response = apiInstance.selectGoogleBusinessLocationWithHttpInfo(selectGoogleBusinessLocationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectGoogleBusinessLocation");
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
| **selectGoogleBusinessLocationRequest** | [**SelectGoogleBusinessLocationRequest**](SelectGoogleBusinessLocationRequest.md)|  | |

### Return type

ApiResponse<[**SelectGoogleBusinessLocation200Response**](SelectGoogleBusinessLocation200Response.md)>


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Google Business location connected successfully |  -  |
| **400** | Missing required fields (profileId, locationId, or tempToken), or the provided accountId is not one of the accounts this connection manages |  -  |
| **401** | Unauthorized |  -  |
| **403** | User does not have access to the specified profile |  -  |
| **404** | Selected location not found in available locations |  -  |
| **500** | Failed to save Google Business connection |  -  |


## selectInstagramAccount

> SelectInstagramAccount200Response selectInstagramAccount(selectInstagramAccountRequest)

Select the Page whose Instagram account to connect

Saves the selected Page as an Instagram account connected via Facebook Login. The Page access token becomes the account&#39;s access token, so every Instagram call for it runs against the Facebook Graph host.  One Instagram account per profile: if the profile already has an Instagram account, this replaces it, and picking a different Instagram identity purges the previous account&#39;s conversations, external posts and stats. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectInstagramAccountRequest selectInstagramAccountRequest = new SelectInstagramAccountRequest(); // SelectInstagramAccountRequest | 
        try {
            SelectInstagramAccount200Response result = apiInstance.selectInstagramAccount(selectInstagramAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectInstagramAccount");
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
| **selectInstagramAccountRequest** | [**SelectInstagramAccountRequest**](SelectInstagramAccountRequest.md)|  | |

### Return type

[**SelectInstagramAccount200Response**](SelectInstagramAccount200Response.md)


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instagram account connected |  -  |
| **400** | Missing required fields, or the selected Page has no linked Instagram professional account |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | User does not have access to the specified profile |  -  |
| **404** | Selected page not found among the pages this token can manage |  -  |

## selectInstagramAccountWithHttpInfo

> ApiResponse<SelectInstagramAccount200Response> selectInstagramAccount selectInstagramAccountWithHttpInfo(selectInstagramAccountRequest)

Select the Page whose Instagram account to connect

Saves the selected Page as an Instagram account connected via Facebook Login. The Page access token becomes the account&#39;s access token, so every Instagram call for it runs against the Facebook Graph host.  One Instagram account per profile: if the profile already has an Instagram account, this replaces it, and picking a different Instagram identity purges the previous account&#39;s conversations, external posts and stats. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure API key authorization: connectToken
        ApiKeyAuth connectToken = (ApiKeyAuth) defaultClient.getAuthentication("connectToken");
        connectToken.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //connectToken.setApiKeyPrefix("Token");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectInstagramAccountRequest selectInstagramAccountRequest = new SelectInstagramAccountRequest(); // SelectInstagramAccountRequest | 
        try {
            ApiResponse<SelectInstagramAccount200Response> response = apiInstance.selectInstagramAccountWithHttpInfo(selectInstagramAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectInstagramAccount");
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
| **selectInstagramAccountRequest** | [**SelectInstagramAccountRequest**](SelectInstagramAccountRequest.md)|  | |

### Return type

ApiResponse<[**SelectInstagramAccount200Response**](SelectInstagramAccount200Response.md)>


### Authorization

[connectToken](../README.md#connectToken), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instagram account connected |  -  |
| **400** | Missing required fields, or the selected Page has no linked Instagram professional account |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X (Twitter) account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not just the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connection cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60;, redirect the end-user to &#x60;dashboard_url&#x60; to add a payment method via Zernio&#39;s hosted Stripe Setup Checkout. For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | User does not have access to the specified profile |  -  |
| **404** | Selected page not found among the pages this token can manage |  -  |


## selectLinkedInOrganization

> SelectLinkedInOrganization200Response selectLinkedInOrganization(selectLinkedInOrganizationRequest)

Select LinkedIn org

Complete the LinkedIn connection flow. Set accountType to \&quot;personal\&quot; or \&quot;organization\&quot; to connect as a company page. Use X-Connect-Token if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectLinkedInOrganizationRequest selectLinkedInOrganizationRequest = new SelectLinkedInOrganizationRequest(); // SelectLinkedInOrganizationRequest | 
        try {
            SelectLinkedInOrganization200Response result = apiInstance.selectLinkedInOrganization(selectLinkedInOrganizationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectLinkedInOrganization");
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
| **selectLinkedInOrganizationRequest** | [**SelectLinkedInOrganizationRequest**](SelectLinkedInOrganizationRequest.md)|  | |

### Return type

[**SelectLinkedInOrganization200Response**](SelectLinkedInOrganization200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | LinkedIn account connected |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to connect LinkedIn account |  -  |

## selectLinkedInOrganizationWithHttpInfo

> ApiResponse<SelectLinkedInOrganization200Response> selectLinkedInOrganization selectLinkedInOrganizationWithHttpInfo(selectLinkedInOrganizationRequest)

Select LinkedIn org

Complete the LinkedIn connection flow. Set accountType to \&quot;personal\&quot; or \&quot;organization\&quot; to connect as a company page. Use X-Connect-Token if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectLinkedInOrganizationRequest selectLinkedInOrganizationRequest = new SelectLinkedInOrganizationRequest(); // SelectLinkedInOrganizationRequest | 
        try {
            ApiResponse<SelectLinkedInOrganization200Response> response = apiInstance.selectLinkedInOrganizationWithHttpInfo(selectLinkedInOrganizationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectLinkedInOrganization");
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
| **selectLinkedInOrganizationRequest** | [**SelectLinkedInOrganizationRequest**](SelectLinkedInOrganizationRequest.md)|  | |

### Return type

ApiResponse<[**SelectLinkedInOrganization200Response**](SelectLinkedInOrganization200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | LinkedIn account connected |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **500** | Failed to connect LinkedIn account |  -  |


## selectPinterestBoard

> SelectPinterestBoard200Response selectPinterestBoard(selectPinterestBoardRequest)

Select Pinterest board

Complete the Pinterest connection flow. After OAuth, use this endpoint to save the selected board and complete the account connection. Use the X-Connect-Token header if you initiated the connection via API key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectPinterestBoardRequest selectPinterestBoardRequest = new SelectPinterestBoardRequest(); // SelectPinterestBoardRequest | 
        try {
            SelectPinterestBoard200Response result = apiInstance.selectPinterestBoard(selectPinterestBoardRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectPinterestBoard");
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
| **selectPinterestBoardRequest** | [**SelectPinterestBoardRequest**](SelectPinterestBoardRequest.md)|  | |

### Return type

[**SelectPinterestBoard200Response**](SelectPinterestBoard200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pinterest Board connected successfully |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile or profile limit exceeded |  -  |
| **500** | Failed to save Pinterest connection |  -  |

## selectPinterestBoardWithHttpInfo

> ApiResponse<SelectPinterestBoard200Response> selectPinterestBoard selectPinterestBoardWithHttpInfo(selectPinterestBoardRequest)

Select Pinterest board

Complete the Pinterest connection flow. After OAuth, use this endpoint to save the selected board and complete the account connection. Use the X-Connect-Token header if you initiated the connection via API key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectPinterestBoardRequest selectPinterestBoardRequest = new SelectPinterestBoardRequest(); // SelectPinterestBoardRequest | 
        try {
            ApiResponse<SelectPinterestBoard200Response> response = apiInstance.selectPinterestBoardWithHttpInfo(selectPinterestBoardRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectPinterestBoard");
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
| **selectPinterestBoardRequest** | [**SelectPinterestBoardRequest**](SelectPinterestBoardRequest.md)|  | |

### Return type

ApiResponse<[**SelectPinterestBoard200Response**](SelectPinterestBoard200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pinterest Board connected successfully |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile or profile limit exceeded |  -  |
| **500** | Failed to save Pinterest connection |  -  |


## selectSnapchatProfile

> SelectSnapchatProfile200Response selectSnapchatProfile(selectSnapchatProfileRequest, xConnectToken)

Select Snapchat profile

Complete the Snapchat connection flow by saving the selected Public Profile. Snapchat requires a Public Profile to publish content. Use X-Connect-Token if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectSnapchatProfileRequest selectSnapchatProfileRequest = new SelectSnapchatProfileRequest(); // SelectSnapchatProfileRequest | 
        String xConnectToken = "xConnectToken_example"; // String | Short-lived connect token from the OAuth redirect (for API users)
        try {
            SelectSnapchatProfile200Response result = apiInstance.selectSnapchatProfile(selectSnapchatProfileRequest, xConnectToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectSnapchatProfile");
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
| **selectSnapchatProfileRequest** | [**SelectSnapchatProfileRequest**](SelectSnapchatProfileRequest.md)|  | |
| **xConnectToken** | **String**| Short-lived connect token from the OAuth redirect (for API users) | [optional] |

### Return type

[**SelectSnapchatProfile200Response**](SelectSnapchatProfile200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapchat Public Profile connected successfully |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile or profile limit exceeded |  -  |
| **500** | Failed to connect Snapchat account |  -  |

## selectSnapchatProfileWithHttpInfo

> ApiResponse<SelectSnapchatProfile200Response> selectSnapchatProfile selectSnapchatProfileWithHttpInfo(selectSnapchatProfileRequest, xConnectToken)

Select Snapchat profile

Complete the Snapchat connection flow by saving the selected Public Profile. Snapchat requires a Public Profile to publish content. Use X-Connect-Token if connecting via API key.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        SelectSnapchatProfileRequest selectSnapchatProfileRequest = new SelectSnapchatProfileRequest(); // SelectSnapchatProfileRequest | 
        String xConnectToken = "xConnectToken_example"; // String | Short-lived connect token from the OAuth redirect (for API users)
        try {
            ApiResponse<SelectSnapchatProfile200Response> response = apiInstance.selectSnapchatProfileWithHttpInfo(selectSnapchatProfileRequest, xConnectToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#selectSnapchatProfile");
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
| **selectSnapchatProfileRequest** | [**SelectSnapchatProfileRequest**](SelectSnapchatProfileRequest.md)|  | |
| **xConnectToken** | **String**| Short-lived connect token from the OAuth redirect (for API users) | [optional] |

### Return type

ApiResponse<[**SelectSnapchatProfile200Response**](SelectSnapchatProfile200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapchat Public Profile connected successfully |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **403** | No access to profile or profile limit exceeded |  -  |
| **500** | Failed to connect Snapchat account |  -  |


## setRedditPostFlair

> UpdateYoutubeDefaultPlaylist200Response setRedditPostFlair(accountId, setRedditPostFlairRequest)

Set Reddit post flair

Applies a flair to a post the connected account already published. Use the GET on this path to list the available &#x60;flairTemplateId&#x60; values for the subreddit.  Flair can also be set at submit time by passing &#x60;flairId&#x60; in &#x60;platformSpecificData&#x60; when creating the post. This endpoint is for changing it afterwards.  The subreddit must allow users to select their own post flair. Setting flair on another user&#39;s post requires moderator permissions, which Zernio does not request. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The ID of the Reddit account that owns the post
        SetRedditPostFlairRequest setRedditPostFlairRequest = new SetRedditPostFlairRequest(); // SetRedditPostFlairRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.setRedditPostFlair(accountId, setRedditPostFlairRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#setRedditPostFlair");
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
| **accountId** | **String**| The ID of the Reddit account that owns the post | |
| **setRedditPostFlairRequest** | [**SetRedditPostFlairRequest**](SetRedditPostFlairRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flair applied |  -  |
| **400** | Not a Reddit account, or missing subreddit/postId/flairTemplateId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses (e.g. subreddit does not allow user flair selection) are forwarded as-is. |  -  |

## setRedditPostFlairWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> setRedditPostFlair setRedditPostFlairWithHttpInfo(accountId, setRedditPostFlairRequest)

Set Reddit post flair

Applies a flair to a post the connected account already published. Use the GET on this path to list the available &#x60;flairTemplateId&#x60; values for the subreddit.  Flair can also be set at submit time by passing &#x60;flairId&#x60; in &#x60;platformSpecificData&#x60; when creating the post. This endpoint is for changing it afterwards.  The subreddit must allow users to select their own post flair. Setting flair on another user&#39;s post requires moderator permissions, which Zernio does not request. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The ID of the Reddit account that owns the post
        SetRedditPostFlairRequest setRedditPostFlairRequest = new SetRedditPostFlairRequest(); // SetRedditPostFlairRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.setRedditPostFlairWithHttpInfo(accountId, setRedditPostFlairRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#setRedditPostFlair");
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
| **accountId** | **String**| The ID of the Reddit account that owns the post | |
| **setRedditPostFlairRequest** | [**SetRedditPostFlairRequest**](SetRedditPostFlairRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flair applied |  -  |
| **400** | Not a Reddit account, or missing subreddit/postId/flairTemplateId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses (e.g. subreddit does not allow user flair selection) are forwarded as-is. |  -  |


## updateFacebookPage

> UpdateFacebookPage200Response updateFacebookPage(accountId, updateFacebookPageRequest)

Update Facebook page

Switch which Facebook Page is active for a connected account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateFacebookPageRequest updateFacebookPageRequest = new UpdateFacebookPageRequest(); // UpdateFacebookPageRequest | 
        try {
            UpdateFacebookPage200Response result = apiInstance.updateFacebookPage(accountId, updateFacebookPageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateFacebookPage");
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
| **updateFacebookPageRequest** | [**UpdateFacebookPageRequest**](UpdateFacebookPageRequest.md)|  | |

### Return type

[**UpdateFacebookPage200Response**](UpdateFacebookPage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page updated |  -  |
| **400** | Page not in available pages |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## updateFacebookPageWithHttpInfo

> ApiResponse<UpdateFacebookPage200Response> updateFacebookPage updateFacebookPageWithHttpInfo(accountId, updateFacebookPageRequest)

Update Facebook page

Switch which Facebook Page is active for a connected account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateFacebookPageRequest updateFacebookPageRequest = new UpdateFacebookPageRequest(); // UpdateFacebookPageRequest | 
        try {
            ApiResponse<UpdateFacebookPage200Response> response = apiInstance.updateFacebookPageWithHttpInfo(accountId, updateFacebookPageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateFacebookPage");
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
| **updateFacebookPageRequest** | [**UpdateFacebookPageRequest**](UpdateFacebookPageRequest.md)|  | |

### Return type

ApiResponse<[**UpdateFacebookPage200Response**](UpdateFacebookPage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page updated |  -  |
| **400** | Page not in available pages |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## updateGmbLocation

> UpdateGmbLocation200Response updateGmbLocation(accountId, updateGmbLocationRequest)

Update GBP location

Switch which GBP location is active for a connected account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGmbLocationRequest updateGmbLocationRequest = new UpdateGmbLocationRequest(); // UpdateGmbLocationRequest | 
        try {
            UpdateGmbLocation200Response result = apiInstance.updateGmbLocation(accountId, updateGmbLocationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateGmbLocation");
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
| **updateGmbLocationRequest** | [**UpdateGmbLocationRequest**](UpdateGmbLocationRequest.md)|  | |

### Return type

[**UpdateGmbLocation200Response**](UpdateGmbLocation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Location updated |  -  |
| **400** | Location not in available locations, or the provided googleAccountId is not one of the accounts this connection manages |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## updateGmbLocationWithHttpInfo

> ApiResponse<UpdateGmbLocation200Response> updateGmbLocation updateGmbLocationWithHttpInfo(accountId, updateGmbLocationRequest)

Update GBP location

Switch which GBP location is active for a connected account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGmbLocationRequest updateGmbLocationRequest = new UpdateGmbLocationRequest(); // UpdateGmbLocationRequest | 
        try {
            ApiResponse<UpdateGmbLocation200Response> response = apiInstance.updateGmbLocationWithHttpInfo(accountId, updateGmbLocationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateGmbLocation");
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
| **updateGmbLocationRequest** | [**UpdateGmbLocationRequest**](UpdateGmbLocationRequest.md)|  | |

### Return type

ApiResponse<[**UpdateGmbLocation200Response**](UpdateGmbLocation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Location updated |  -  |
| **400** | Location not in available locations, or the provided googleAccountId is not one of the accounts this connection manages |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## updateLinkedInOrganization

> UpdateLinkedInOrganization200Response updateLinkedInOrganization(accountId, updateLinkedInOrganizationRequest)

Switch LinkedIn account type

Switch a LinkedIn account between personal profile and organization (company page) posting.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateLinkedInOrganizationRequest updateLinkedInOrganizationRequest = new UpdateLinkedInOrganizationRequest(); // UpdateLinkedInOrganizationRequest | 
        try {
            UpdateLinkedInOrganization200Response result = apiInstance.updateLinkedInOrganization(accountId, updateLinkedInOrganizationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateLinkedInOrganization");
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
| **updateLinkedInOrganizationRequest** | [**UpdateLinkedInOrganizationRequest**](UpdateLinkedInOrganizationRequest.md)|  | |

### Return type

[**UpdateLinkedInOrganization200Response**](UpdateLinkedInOrganization200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## updateLinkedInOrganizationWithHttpInfo

> ApiResponse<UpdateLinkedInOrganization200Response> updateLinkedInOrganization updateLinkedInOrganizationWithHttpInfo(accountId, updateLinkedInOrganizationRequest)

Switch LinkedIn account type

Switch a LinkedIn account between personal profile and organization (company page) posting.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateLinkedInOrganizationRequest updateLinkedInOrganizationRequest = new UpdateLinkedInOrganizationRequest(); // UpdateLinkedInOrganizationRequest | 
        try {
            ApiResponse<UpdateLinkedInOrganization200Response> response = apiInstance.updateLinkedInOrganizationWithHttpInfo(accountId, updateLinkedInOrganizationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateLinkedInOrganization");
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
| **updateLinkedInOrganizationRequest** | [**UpdateLinkedInOrganizationRequest**](UpdateLinkedInOrganizationRequest.md)|  | |

### Return type

ApiResponse<[**UpdateLinkedInOrganization200Response**](UpdateLinkedInOrganization200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## updatePinterestBoards

> ConnectBlueskyCredentials200Response updatePinterestBoards(accountId, updatePinterestBoardsRequest)

Set default Pinterest board

Sets the default board used when publishing pins for this account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdatePinterestBoardsRequest updatePinterestBoardsRequest = new UpdatePinterestBoardsRequest(); // UpdatePinterestBoardsRequest | 
        try {
            ConnectBlueskyCredentials200Response result = apiInstance.updatePinterestBoards(accountId, updatePinterestBoardsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updatePinterestBoards");
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
| **updatePinterestBoardsRequest** | [**UpdatePinterestBoardsRequest**](UpdatePinterestBoardsRequest.md)|  | |

### Return type

[**ConnectBlueskyCredentials200Response**](ConnectBlueskyCredentials200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default board set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## updatePinterestBoardsWithHttpInfo

> ApiResponse<ConnectBlueskyCredentials200Response> updatePinterestBoards updatePinterestBoardsWithHttpInfo(accountId, updatePinterestBoardsRequest)

Set default Pinterest board

Sets the default board used when publishing pins for this account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdatePinterestBoardsRequest updatePinterestBoardsRequest = new UpdatePinterestBoardsRequest(); // UpdatePinterestBoardsRequest | 
        try {
            ApiResponse<ConnectBlueskyCredentials200Response> response = apiInstance.updatePinterestBoardsWithHttpInfo(accountId, updatePinterestBoardsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updatePinterestBoards");
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
| **updatePinterestBoardsRequest** | [**UpdatePinterestBoardsRequest**](UpdatePinterestBoardsRequest.md)|  | |

### Return type

ApiResponse<[**ConnectBlueskyCredentials200Response**](ConnectBlueskyCredentials200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default board set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## updateRedditSubreddits

> UpdateYoutubeDefaultPlaylist200Response updateRedditSubreddits(accountId, updateRedditSubredditsRequest)

Set default subreddit

Sets the default subreddit used when publishing posts for this Reddit account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateRedditSubredditsRequest updateRedditSubredditsRequest = new UpdateRedditSubredditsRequest(); // UpdateRedditSubredditsRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.updateRedditSubreddits(accountId, updateRedditSubredditsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateRedditSubreddits");
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
| **updateRedditSubredditsRequest** | [**UpdateRedditSubredditsRequest**](UpdateRedditSubredditsRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default subreddit set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## updateRedditSubredditsWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> updateRedditSubreddits updateRedditSubredditsWithHttpInfo(accountId, updateRedditSubredditsRequest)

Set default subreddit

Sets the default subreddit used when publishing posts for this Reddit account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateRedditSubredditsRequest updateRedditSubredditsRequest = new UpdateRedditSubredditsRequest(); // UpdateRedditSubredditsRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.updateRedditSubredditsWithHttpInfo(accountId, updateRedditSubredditsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateRedditSubreddits");
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
| **updateRedditSubredditsRequest** | [**UpdateRedditSubredditsRequest**](UpdateRedditSubredditsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default subreddit set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## updateYoutubeDefaultPlaylist

> UpdateYoutubeDefaultPlaylist200Response updateYoutubeDefaultPlaylist(accountId, updateYoutubeDefaultPlaylistRequest)

Set default YouTube playlist

Sets the default playlist used when publishing videos for this account. When a post does not specify a playlistId, the default playlist is not automatically used (it is stored for client-side convenience).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateYoutubeDefaultPlaylistRequest updateYoutubeDefaultPlaylistRequest = new UpdateYoutubeDefaultPlaylistRequest(); // UpdateYoutubeDefaultPlaylistRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.updateYoutubeDefaultPlaylist(accountId, updateYoutubeDefaultPlaylistRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateYoutubeDefaultPlaylist");
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
| **updateYoutubeDefaultPlaylistRequest** | [**UpdateYoutubeDefaultPlaylistRequest**](UpdateYoutubeDefaultPlaylistRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default playlist set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## updateYoutubeDefaultPlaylistWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> updateYoutubeDefaultPlaylist updateYoutubeDefaultPlaylistWithHttpInfo(accountId, updateYoutubeDefaultPlaylistRequest)

Set default YouTube playlist

Sets the default playlist used when publishing videos for this account. When a post does not specify a playlistId, the default playlist is not automatically used (it is stored for client-side convenience).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateYoutubeDefaultPlaylistRequest updateYoutubeDefaultPlaylistRequest = new UpdateYoutubeDefaultPlaylistRequest(); // UpdateYoutubeDefaultPlaylistRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.updateYoutubeDefaultPlaylistWithHttpInfo(accountId, updateYoutubeDefaultPlaylistRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#updateYoutubeDefaultPlaylist");
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
| **updateYoutubeDefaultPlaylistRequest** | [**UpdateYoutubeDefaultPlaylistRequest**](UpdateYoutubeDefaultPlaylistRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default playlist set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## voteRedditThing

> UpdateYoutubeDefaultPlaylist200Response voteRedditThing(accountId, voteRedditThingRequest)

Vote on a Reddit post or comment

Cast, change, or clear the connected account&#39;s vote on a Reddit post or comment.  **Reddit requires that votes be cast by humans.** Reddit&#39;s API terms permit a client to proxy a human&#39;s action one-for-one, and prohibit a bot from deciding how to vote or from amplifying a human&#39;s vote. Call this endpoint only in direct response to an explicit action by the account owner. Automated or agent-decided voting is vote manipulation and puts API access at risk. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The ID of the Reddit account casting the vote
        VoteRedditThingRequest voteRedditThingRequest = new VoteRedditThingRequest(); // VoteRedditThingRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.voteRedditThing(accountId, voteRedditThingRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#voteRedditThing");
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
| **accountId** | **String**| The ID of the Reddit account casting the vote | |
| **voteRedditThingRequest** | [**VoteRedditThingRequest**](VoteRedditThingRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vote registered |  -  |
| **400** | Not a Reddit account, or invalid thingId/direction |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses are forwarded as-is. |  -  |

## voteRedditThingWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> voteRedditThing voteRedditThingWithHttpInfo(accountId, voteRedditThingRequest)

Vote on a Reddit post or comment

Cast, change, or clear the connected account&#39;s vote on a Reddit post or comment.  **Reddit requires that votes be cast by humans.** Reddit&#39;s API terms permit a client to proxy a human&#39;s action one-for-one, and prohibit a bot from deciding how to vote or from amplifying a human&#39;s vote. Call this endpoint only in direct response to an explicit action by the account owner. Automated or agent-decided voting is vote manipulation and puts API access at risk. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectApi apiInstance = new ConnectApi(defaultClient);
        String accountId = "accountId_example"; // String | The ID of the Reddit account casting the vote
        VoteRedditThingRequest voteRedditThingRequest = new VoteRedditThingRequest(); // VoteRedditThingRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.voteRedditThingWithHttpInfo(accountId, voteRedditThingRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectApi#voteRedditThing");
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
| **accountId** | **String**| The ID of the Reddit account casting the vote | |
| **voteRedditThingRequest** | [**VoteRedditThingRequest**](VoteRedditThingRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vote registered |  -  |
| **400** | Not a Reddit account, or invalid thingId/direction |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses are forwarded as-is. |  -  |

