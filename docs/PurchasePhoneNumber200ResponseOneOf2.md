

# PurchasePhoneNumber200ResponseOneOf2

A number was already purchased under the supplied purchaseIntentId; no new number was provisioned. The number can still be in regulatory review or declined (phoneNumber can be \"pending\"): GET it for its status, and use a new purchaseIntentId to buy a replacement. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**numberId** | **String** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**profileId** | **String** | The profile the number was actually assigned to. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ALREADY_PURCHASED | &quot;already_purchased&quot; |



