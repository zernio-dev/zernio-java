

# WebhookPayloadWhatsAppTemplateCategoryUpdatedTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**templateId** | **String** | Meta&#39;s &#x60;message_template_id&#x60;, returned as a string. |  |
|**name** | **String** | Meta&#39;s &#x60;message_template_name&#x60;. |  |
|**language** | **String** | Meta&#39;s &#x60;message_template_language&#x60; (e.g. &#x60;en_US&#x60;). |  |
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | &#x60;scheduled&#x60; is Meta&#39;s 24h advance notice of an upcoming reclassification; &#x60;applied&#x60; is the change taking effect.  |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category right now, regardless of changeType. |  |
|**previousCategory** | [**PreviousCategoryEnum**](#PreviousCategoryEnum) | Present only when changeType is &#x60;applied&#x60;. The category before this change. |  [optional] |
|**scheduledCategory** | [**ScheduledCategoryEnum**](#ScheduledCategoryEnum) | Present only when changeType is &#x60;scheduled&#x60;. The category that will take effect at &#x60;effectiveAt&#x60;. |  [optional] |
|**effectiveAt** | **OffsetDateTime** | Present only when changeType is &#x60;scheduled&#x60;. ISO-8601 timestamp when the scheduled category takes effect. |  [optional] |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| SCHEDULED | &quot;scheduled&quot; |
| APPLIED | &quot;applied&quot; |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| UTILITY | &quot;UTILITY&quot; |
| MARKETING | &quot;MARKETING&quot; |
| AUTHENTICATION | &quot;AUTHENTICATION&quot; |



## Enum: PreviousCategoryEnum

| Name | Value |
|---- | -----|
| UTILITY | &quot;UTILITY&quot; |
| MARKETING | &quot;MARKETING&quot; |
| AUTHENTICATION | &quot;AUTHENTICATION&quot; |



## Enum: ScheduledCategoryEnum

| Name | Value |
|---- | -----|
| UTILITY | &quot;UTILITY&quot; |
| MARKETING | &quot;MARKETING&quot; |
| AUTHENTICATION | &quot;AUTHENTICATION&quot; |



