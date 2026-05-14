

# WebhookPayloadAdStatusChangedAdObject

The ad-platform object the status change applies to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | [**LevelEnum**](#LevelEnum) | Hierarchy level the status applies to. Mirrors Meta&#39;s &#x60;level&#x60;. Creative-level events are not forwarded. |  |
|**platformId** | **String** | Platform-native ID of the campaign / ad set / ad. For Meta this is the bare numeric ID (e.g. &#x60;120244894077860689&#x60;).  |  |
|**platformAdAccountId** | **String** | Platform-native ad-account ID. For Meta this uses the &#x60;act_&lt;id&gt;&#x60; shape.  |  |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;CAMPAIGN&quot; |
| AD_SET | &quot;AD_SET&quot; |
| AD | &quot;AD&quot; |



