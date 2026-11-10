

# ListCampaignOrders200ResponseOrdersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**platformOrderId** | **String** | The order id on the store, as in &#x60;GET /v1/commerce/orders/{orderId}&#x60;. |  |
|**orderNumber** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**participantId** | **String** |  |  |
|**creatorName** | **String** |  |  |
|**creatorAvatarUrl** | **String** | The creator&#39;s profile picture. Same source as a participant&#39;s &#x60;creator.avatarUrl&#x60;. |  |
|**matchedBy** | [**MatchedByEnum**](#MatchedByEnum) |  |  |
|**discountCode** | **String** |  |  |
|**currency** | **String** |  |  |
|**salesCents** | **Integer** |  |  |
|**refundedCents** | **Integer** |  |  |
|**commissionCents** | **Integer** | Commission the order holds now, net of refunds. |  |
|**orderCreatedAt** | **OffsetDateTime** |  |  |
|**approvedAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| MATCHED | &quot;matched&quot; |
| UNMATCHED | &quot;unmatched&quot; |



## Enum: MatchedByEnum

| Name | Value |
|---- | -----|
| CODE | &quot;code&quot; |
| LINK | &quot;link&quot; |



