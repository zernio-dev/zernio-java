

# ConnectTradeDeskAdsPartnerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**partnerId** | **String** | Trade Desk Partner ID, a short code such as &#x60;ptn1234&#x60;. Stored and echoed lowercased. |  |
|**apiToken** | **String** | API token of a Trade Desk user with API access to the partner. |  |
|**adAccountIds** | **List&lt;String&gt;** | Advertiser ids to keep. Left out or empty, a new connection keeps every advertiser and a reconnect keeps its saved selection. |  [optional] |
|**name** | **String** | Optional display name for the account. |  [optional] |
|**profileId** | **String** | Your Zernio profile ID |  |
|**state** | **String** | Optional state passthrough for the connect flow. |  [optional] |
|**redirectUrl** | **String** | Optional URL to redirect to after a successful connection, echoed back as redirectUrl. |  [optional] |



