

# StagedAdChange

An ad write that was validated and stored with `stage: true`, waiting to be confirmed or discarded.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The change id, used in /v1/ads/changes/{changeId}. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Which write was staged: a status route, the update route of a campaign, an ad set or an ad, the campaign targeting route, or one of the create routes (POST /v1/ads/create, POST /v1/ads/campaigns, POST /v1/ads/ad-sets). |  |
|**platform** | **String** | The ad platform of the object, as the write route names it. |  |
|**accountId** | **String** | The connected account the write goes through. |  |
|**adAccountId** | **String** | The ad account id on the platform. |  |
|**targetId** | **String** | The object the change applies to: the platform campaign id, the platform ad set id, or the Zernio ad id. Null for a create, whose object does not exist yet. |  |
|**creates** | **Boolean** | Present and true when the change creates a new object. Every diff entry then has &#x60;before: null&#x60; and &#x60;beforeAvailable: false&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | - &#x60;staged&#x60;: waiting to be confirmed or discarded. - &#x60;confirming&#x60;: a confirm is running. A change that stays here has an unknown outcome and is never applied again automatically. - &#x60;confirmed&#x60;: applied. &#x60;result&#x60; holds what the write returned. - &#x60;failed&#x60;: not applied. &#x60;error&#x60; says why.  |  |
|**diff** | [**List&lt;StagedAdChangeDiffInner&gt;**](StagedAdChangeDiffInner.md) | One entry per value of the staged request that the write would change.  - A nested field is flattened: each leaf is one entry under its dotted path (&#x60;budget.amount&#x60;, &#x60;targeting.ageMin&#x60;, &#x60;creative.headline&#x60;). - A list is one entry. - A leaf whose value on the ad network already equals the requested value is left out, so the list can be empty. - &#x60;stage&#x60; and other flags that only steer the write are never listed.  |  |
|**createdBy** | **String** | The user who staged the change. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**finishedAt** | **OffsetDateTime** | When the confirm ended, as &#x60;confirmed&#x60; or &#x60;failed&#x60;. A finished change is deleted 7 days later. |  |
|**result** | **Map&lt;String, Object&gt;** | Present once &#x60;confirmed&#x60;: the response body of the write. |  [optional] |
|**error** | [**StagedAdChangeError**](StagedAdChangeError.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN_STATUS | &quot;campaign_status&quot; |
| AD_SET_STATUS | &quot;ad_set_status&quot; |
| AD_STATUS | &quot;ad_status&quot; |
| CAMPAIGN_UPDATE | &quot;campaign_update&quot; |
| AD_SET_UPDATE | &quot;ad_set_update&quot; |
| AD_UPDATE | &quot;ad_update&quot; |
| CAMPAIGN_TARGETING | &quot;campaign_targeting&quot; |
| AD_CREATE | &quot;ad_create&quot; |
| CAMPAIGN_CREATE | &quot;campaign_create&quot; |
| AD_SET_CREATE | &quot;ad_set_create&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STAGED | &quot;staged&quot; |
| CONFIRMING | &quot;confirming&quot; |
| CONFIRMED | &quot;confirmed&quot; |
| FAILED | &quot;failed&quot; |



