

# GetLeadForm200ResponseForm

Full form config — sufficient to duplicate the form via POST /v1/ads/lead-forms.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | ARCHIVED forms can&#39;t receive new leads. |  [optional] |
|**locale** | **String** |  |  [optional] |
|**createdTime** | **OffsetDateTime** |  |  [optional] |
|**leadsCount** | **Integer** |  |  [optional] |
|**privacyPolicyUrl** | **URI** |  |  [optional] |
|**followUpActionUrl** | **URI** |  |  [optional] |
|**questions** | [**List&lt;GetLeadForm200ResponseFormQuestionsInner&gt;**](GetLeadForm200ResponseFormQuestionsInner.md) |  |  [optional] |
|**thankYouPage** | [**GetLeadForm200ResponseFormThankYouPage**](GetLeadForm200ResponseFormThankYouPage.md) |  |  [optional] |
|**contextCard** | **Object** | Intro card shown before the form questions (title, content, button label). |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



