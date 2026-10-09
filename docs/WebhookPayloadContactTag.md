

# WebhookPayloadContactTag


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Event id, the dedupe key. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**contact** | [**WebhookPayloadContactTagContact**](WebhookPayloadContactTagContact.md) |  |  |
|**tag** | **String** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | Who wrote the tag: the API or dashboard, a workflow add_tag / remove_tag node, or a comment-automation link click. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CONTACT_TAG_ADDED | &quot;contact.tag_added&quot; |
| CONTACT_TAG_REMOVED | &quot;contact.tag_removed&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| WORKFLOW | &quot;workflow&quot; |
| AUTOMATION | &quot;automation&quot; |



