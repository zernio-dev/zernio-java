

# CreatorPortalReferralOrdersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**number** | **String** |  |  |
|**placedAt** | **OffsetDateTime** |  |  |
|**matchedBy** | [**MatchedByEnum**](#MatchedByEnum) |  |  |
|**salesCents** | **Integer** |  |  |
|**refundedCents** | **Integer** |  |  |
|**commissionCents** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**confirmsAt** | **OffsetDateTime** | Order date plus the campaign hold, when the commission is approved. |  |



## Enum: MatchedByEnum

| Name | Value |
|---- | -----|
| CODE | &quot;code&quot; |
| LINK | &quot;link&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IN_REFUND_WINDOW | &quot;in_refund_window&quot; |
| CONFIRMED | &quot;confirmed&quot; |
| REFUNDED | &quot;refunded&quot; |



