

# AutomationTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | A team template&#39;s id (24 hex characters), or the id of one of Zernio&#39;s templates such as &#x60;stop_losers&#x60;. |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  |
|**publisher** | [**AutomationTemplatePublisher**](AutomationTemplatePublisher.md) |  |  |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | &#x60;team&#x60;: your team only. &#x60;link&#x60;: anyone with the share link can read and install it. &#x60;public&#x60;: one of Zernio&#39;s templates. |  |
|**version** | **Integer** | Goes up each time the content changes. Renaming or sharing keeps it. |  |
|**areas** | [**List&lt;AreasEnum&gt;**](#List&lt;AreasEnum&gt;) | What its automations work on. |  |
|**inputs** | [**List&lt;AutomationTemplateInput&gt;**](AutomationTemplateInput.md) |  |  |
|**automations** | [**List&lt;AutomationTemplateAutomation&gt;**](AutomationTemplateAutomation.md) |  |  |
|**installs** | **Integer** | Installs across every team. Always 0 on Zernio&#39;s templates. |  |
|**installedInTeam** | **Integer** | Your team&#39;s automations made from it. Absent on shared and Zernio templates. |  [optional] |
|**share** | [**AutomationTemplateShare**](AutomationTemplateShare.md) |  |  |
|**createdBy** | **String** | The user who saved it. Only on your team&#39;s templates. |  [optional] |
|**createdAt** | **OffsetDateTime** | Absent on Zernio&#39;s templates. |  [optional] |
|**updatedAt** | **OffsetDateTime** | Absent on Zernio&#39;s templates. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| TEAM | &quot;team&quot; |
| LINK | &quot;link&quot; |
| PUBLIC | &quot;public&quot; |



## Enum: List&lt;AreasEnum&gt;

| Name | Value |
|---- | -----|
| ADS | &quot;ads&quot; |
| EVENTS | &quot;events&quot; |
| POSTS | &quot;posts&quot; |
| INBOX | &quot;inbox&quot; |
| COMMENTS | &quot;comments&quot; |



