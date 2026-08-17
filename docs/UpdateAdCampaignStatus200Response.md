

# UpdateAdCampaignStatus200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | The status written to the campaign |  [optional] |
|**updated** | **Integer** | Number of ads whose own stored status changed too. 0 is normal on a resume whose ads are all awaiting the platform. |  [optional] |
|**skipped** | **Integer** | Number of ads whose own status was left as it was |  [optional] |
|**skippedReasons** | **List&lt;String&gt;** | Why each group of ads was skipped |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



