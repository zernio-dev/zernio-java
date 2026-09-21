

# OrderImessageSenderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**region** | [**RegionEnum**](#RegionEnum) | Required for phone senders. Without availableNumberId the number is carrier-assigned in this region and revealed once the sender activates. |  [optional] |
|**availableNumberId** | **String** | A number from GET /v1/imessage/senders/available-numbers. It is assigned and activated on order instead of waiting for provisioning. Phone senders only. |  [optional] |
|**zipCode** | **String** | US phone senders only. Preferred area for a carrier-assigned number (ignored with availableNumberId). |  [optional] |
|**emailName** | **String** | Local part for email senders (required for kind: email) |  [optional] |
|**emailDomain** | **String** | Domain for email senders (required for kind: email) |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**purchaseIntentId** | **String** | Idempotency key for safe retries |  [optional] |
|**contact** | [**OrderImessageSenderRequestContact**](OrderImessageSenderRequestContact.md) |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| PHONE | &quot;phone&quot; |
| EMAIL | &quot;email&quot; |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| GB | &quot;GB&quot; |



