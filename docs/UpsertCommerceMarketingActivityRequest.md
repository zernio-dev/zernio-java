

# UpsertCommerceMarketingActivityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**remoteId** | **String** |  |  |
|**title** | **String** |  |  |
|**url** | **URI** |  |  |
|**previewImageUrl** | **URI** |  |  [optional] |
|**utm** | [**UpsertCommerceMarketingActivityRequestUtm**](UpsertCommerceMarketingActivityRequestUtm.md) |  |  [optional] |
|**tactic** | [**TacticEnum**](#TacticEnum) |  |  |
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**budget** | [**UpsertCommerceMarketingActivityRequestBudget**](UpsertCommerceMarketingActivityRequestBudget.md) |  |  [optional] |
|**adSpend** | **String** | Decimal in the store currency. |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**endedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: TacticEnum

| Name | Value |
|---- | -----|
| AD | &quot;ad&quot; |
| POST | &quot;post&quot; |
| MESSAGE | &quot;message&quot; |
| NEWSLETTER | &quot;newsletter&quot; |
| LINK | &quot;link&quot; |
| AFFILIATE | &quot;affiliate&quot; |
| RETARGETING | &quot;retargeting&quot; |
| LOYALTY | &quot;loyalty&quot; |
| SEO | &quot;seo&quot; |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SOCIAL | &quot;social&quot; |
| SEARCH | &quot;search&quot; |
| DISPLAY | &quot;display&quot; |
| EMAIL | &quot;email&quot; |
| REFERRAL | &quot;referral&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| PAUSED | &quot;paused&quot; |
| SCHEDULED | &quot;scheduled&quot; |



