

# AutomationAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**step** | **String** | The id of the step that made it, for example &#x60;budget&#x60;. |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**reason** | **String** | Why it was skipped or failed, such as &#x60;already_paused&#x60;, &#x60;daily_limit_reached&#x60; or &#x60;awaiting_approval&#x60;. |  |
|**previous** | [**AutomationChangedValue**](AutomationChangedValue.md) |  |  |
|**target** | [**AutomationChangedValue**](AutomationChangedValue.md) |  |  |
|**id** | **String** |  |  |
|**automationId** | **String** |  |  |
|**automationName** | **String** |  |  |
|**checkId** | **String** |  |  |
|**subject** | [**AutomationActionAllOfSubject**](AutomationActionAllOfSubject.md) |  |  |
|**platform** | **String** |  |  |
|**adAccount** | [**AutomationActionAllOfAdAccount**](AutomationActionAllOfAdAccount.md) |  |  |
|**currency** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_PAUSE | &quot;ads.pause&quot; |
| ADS_ACTIVATE | &quot;ads.activate&quot; |
| ADS_SET_BUDGET | &quot;ads.set_budget&quot; |
| ADS_DUPLICATE | &quot;ads.duplicate&quot; |
| ADS_EDIT_NAME | &quot;ads.edit_name&quot; |
| ADS_SET_BID | &quot;ads.set_bid&quot; |
| ADS_SET_TARGET | &quot;ads.set_target&quot; |
| ADS_REALLOCATE_BUDGET | &quot;ads.reallocate_budget&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPLIED | &quot;applied&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |



