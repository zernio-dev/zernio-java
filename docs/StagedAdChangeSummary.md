

# StagedAdChangeSummary

A staged or failed ad change as the list returns it: what it targets and who staged it, without the diff.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The change id, used in /v1/ads/changes/{changeId}. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Which write was staged. &#x60;operation&#x60; is a write staged as its request, named by &#x60;request&#x60;. |  |
|**request** | [**StagedAdChangeSummaryRequest**](StagedAdChangeSummaryRequest.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status the list was asked for. |  |
|**stale** | **Boolean** | Present and true on a staged change whose object was edited on the ad network after staging. Refresh it with PATCH /v1/ads/changes/{changeId}. |  [optional] |
|**error** | [**StagedAdChangeSummaryError**](StagedAdChangeSummaryError.md) |  |  [optional] |
|**platform** | **String** | The ad platform of the object, as the write route names it. |  |
|**accountId** | **String** | The connected account the write goes through. |  |
|**adAccountId** | **String** | The ad account id on the platform. |  |
|**targetId** | **String** | The object the change applies to. Null for a create, whose object does not exist yet. |  |
|**targetName** | **String** | The name of the object when the change was staged, or the name a create will give it. Null when it is not known. |  |
|**creates** | **Boolean** | True when the change creates a new object. |  |
|**createdBy** | **String** | The user who staged the change. |  |
|**createdAt** | **OffsetDateTime** |  |  |



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
| OPERATION | &quot;operation&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STAGED | &quot;staged&quot; |
| FAILED | &quot;failed&quot; |



