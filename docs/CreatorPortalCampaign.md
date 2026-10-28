

# CreatorPortalCampaign

The campaign as a creator sees it: terms, never the budget.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The campaign id, as in a link-recovery URL. |  |
|**name** | **String** |  |  |
|**brandName** | **String** |  |  |
|**logoUrl** | **String** |  |  |
|**theme** | **Object** | Same keys as the &#x60;welcomeTheme&#x60; parameter of &#x60;GET /v1/connect/{platform}&#x60;. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**platforms** | **List&lt;String&gt;** |  |  |
|**contentRules** | **String** |  |  |
|**startsAt** | **OffsetDateTime** |  |  |
|**endsAt** | **OffsetDateTime** |  |  |
|**currency** | **String** |  |  |
|**economics** | [**CreatorPortalEconomics**](CreatorPortalEconomics.md) |  |  |
|**maxPostAgeMinutes** | **Integer** | A post must be submitted within this many minutes of publishing. |  |
|**holdDays** | **Integer** | Days approved earnings stay owed before they become payable. |  |
|**trackingDays** | **Integer** | Days each submitted post is tracked for views. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| CLOSED | &quot;closed&quot; |



