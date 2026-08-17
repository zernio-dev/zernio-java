

# UpdateAdSetStatus200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | The status written to the ad set. Absent when nothing was written (see message). |  [optional] |
|**updated** | **Integer** | Number of ads whose own stored status changed too. 0 is normal on a resume whose ads are all awaiting the platform. |  [optional] |
|**skipped** | **Integer** | Number of ads whose own status was left as it was |  [optional] |
|**skippedReasons** | **List&lt;String&gt;** | Why each group of ads was skipped |  [optional] |
|**message** | **String** | Present only where the platform has no ad-set switch and no child ad was actionable |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



