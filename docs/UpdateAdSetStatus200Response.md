

# UpdateAdSetStatus200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | The ad set&#39;s delivery status derived from the switches read back: &#x60;paused&#x60; when its own switch or its campaign&#39;s switch is off. Echoes the request when the platform could not be read. |  [optional] |
|**platformAdSetStatus** | **String** | The ad set&#39;s own switch as read back from the platform, in the raw platform vocabulary (Meta effective_status, TikTok ENABLE / DISABLE, Google ENABLED / PAUSED, LinkedIn and Pinterest ACTIVE / PAUSED, ChatGPT (OpenAI) status). Null when the platform could not be read, which is always the case on X. |  [optional] |
|**platformCampaignStatus** | **String** | The parent campaign&#39;s switch, read in the same call where the platform returns it, otherwise the stored value. |  [optional] |
|**statusReadAt** | **OffsetDateTime** | When the ad set switch was read back. Null when it could not be read. |  [optional] |
|**updated** | [**UpdatedEnum**](#UpdatedEnum) | 1 when the ad set&#39;s switch was written. |  [optional] |
|**skipped** | [**SkippedEnum**](#SkippedEnum) | 1 when a live read showed the ad set already in the requested state, so nothing was written. |  [optional] |
|**skippedReasons** | **List&lt;String&gt;** | Why the write was skipped, for example \&quot;Ad set already switched off\&quot;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: UpdatedEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



## Enum: SkippedEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



