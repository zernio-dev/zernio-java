

# StagedAdChange

An ad write that was validated and stored with `stage: true`, waiting to be confirmed or discarded.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The change id, used in /v1/ads/changes/{changeId}. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Which write was staged. |  |
|**platform** | **String** | The ad platform of the object, as the write route names it. |  |
|**accountId** | **String** | The connected account the write goes through. |  |
|**adAccountId** | **String** | The ad account id on the platform. |  |
|**targetId** | **String** | The object the change applies to: the platform campaign id, the platform ad set id, or the Zernio ad id. |  |
|**status** | [**StatusEnum**](#StatusEnum) | - &#x60;staged&#x60;: waiting to be confirmed or discarded. - &#x60;confirming&#x60;: a confirm is running. A change that stays here has an unknown outcome and is never applied again automatically. - &#x60;confirmed&#x60;: applied. &#x60;result&#x60; holds what the write returned. - &#x60;failed&#x60;: not applied. &#x60;error&#x60; says why.  |  |
|**diff** | [**List&lt;StagedAdChangeDiffInner&gt;**](StagedAdChangeDiffInner.md) | One entry per field of the staged request. |  |
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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STAGED | &quot;staged&quot; |
| CONFIRMING | &quot;confirming&quot; |
| CONFIRMED | &quot;confirmed&quot; |
| FAILED | &quot;failed&quot; |



