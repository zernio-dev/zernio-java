

# AutomationPreview

What an ad rule would do if it ran now. Nothing is changed. Cooldowns and daily caps are left out, so a run right after can act on fewer objects. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluatedAt** | **OffsetDateTime** |  |  |
|**today** | **LocalDate** | Today in the ad account timezone. |  |
|**timezone** | **String** |  |  |
|**timezoneAssumed** | **Boolean** | True when the ad account timezone is unknown and UTC was used. |  |
|**currency** | **String** |  |  |
|**hourlyThrough** | **OffsetDateTime** | Where the hourly windows (&#x60;last_complete_hour&#x60;, &#x60;last_3h&#x60;, &#x60;today_so_far&#x60;) ended: the end of the latest hour a sync has settled. Null when the rule has none or they could not be read. |  [optional] |
|**evaluated** | **Integer** |  |  |
|**matched** | **Integer** |  |  |
|**truncated** | **Boolean** | True when more subjects were judged than &#x60;limit&#x60; lists. |  |
|**subjects** | [**List&lt;AutomationPreviewSubjectsInner&gt;**](AutomationPreviewSubjectsInner.md) | Matches first, up to &#x60;limit&#x60;. |  |
|**groups** | [**List&lt;AutomationPreviewGroupsInner&gt;**](AutomationPreviewGroupsInner.md) | Each group&#39;s totals against the conditions, when the rule has &#x60;subjects.groups&#x60;. |  [optional] |



