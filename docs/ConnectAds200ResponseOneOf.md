

# ConnectAds200ResponseOneOf

Ads already connected (no OAuth needed)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alreadyConnected** | **Boolean** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**tokenType** | [**TokenTypeEnum**](#TokenTypeEnum) | Present for an existing business-login connection. |  [optional] |
|**scopedAdAccountIds** | **List&lt;String&gt;** | Echo of the persisted ad-account scope when the caller passed &#x60;adAccountId&#x60; / &#x60;adAccountIds&#x60;. Omitted when no scope is set.  |  [optional] |



## Enum: TokenTypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_USER | &quot;system-user&quot; |



