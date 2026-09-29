

# UpdateAdCampaignStatus200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | The campaign&#39;s delivery status derived from its switch as read back (&#x60;paused&#x60; when the switch is off). Echoes the request when the platform could not be read. |  [optional] |
|**platformCampaignStatus** | **String** | The campaign&#39;s own switch as read back from the platform, in the raw platform vocabulary (Meta effective_status, TikTok ENABLE / DISABLE, Google ENABLED / PAUSED, ChatGPT (OpenAI) status). Null when the platform could not be read, which is always the case on Pinterest, LinkedIn and X (no single-campaign read). |  [optional] |
|**statusReadAt** | **OffsetDateTime** | When the switch was read back. Null when it could not be read. |  [optional] |
|**updated** | [**UpdatedEnum**](#UpdatedEnum) | 1 when the campaign&#39;s switch was written. |  [optional] |
|**skipped** | [**SkippedEnum**](#SkippedEnum) | 1 when a live read showed the campaign already in the requested state, so nothing was written. |  [optional] |
|**skippedReasons** | **List&lt;String&gt;** | Why the write was skipped, for example \&quot;Campaign already switched off\&quot;. |  [optional] |



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



