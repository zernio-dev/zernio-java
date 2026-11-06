

# AutomationApprovalChange


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionId** | **String** |  |  |
|**subject** | [**AutomationApprovalChangeSubject**](AutomationApprovalChangeSubject.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**previous** | [**AutomationApprovalChangePrevious**](AutomationApprovalChangePrevious.md) |  |  |
|**target** | [**AutomationApprovalChangeTarget**](AutomationApprovalChangeTarget.md) |  |  |
|**conditions** | **List&lt;Object&gt;** | Each condition as it was judged when the request was sent, with its actual value. |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;pending&#x60; until the request is decided. |  |
|**reason** | **String** | Why the change was made, skipped or failed, when known. |  |



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
| PENDING | &quot;pending&quot; |
| APPLIED | &quot;applied&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |
| UNKNOWN | &quot;unknown&quot; |



