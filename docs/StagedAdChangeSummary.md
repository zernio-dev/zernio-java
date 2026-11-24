

# StagedAdChangeSummary

A staged ad change as the list returns it: what it targets and who staged it, without the diff.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The change id, used in /v1/ads/changes/{changeId}. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Which write was staged. |  |
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
| AD_CREATE | &quot;ad_create&quot; |
| CAMPAIGN_CREATE | &quot;campaign_create&quot; |
| AD_SET_CREATE | &quot;ad_set_create&quot; |



