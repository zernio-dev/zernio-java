

# CommentAutomationTemplate

A Meta generic template (product card) sent as the automation's first DM. It REPLACES the plain `dmMessage` bubble: a Meta message carries one body shape, and a comment gets exactly one private reply, so the card and the text cannot both be delivered. Put your selling copy in `subtitle`. Mutually exclusive with `buttons` (sending both is a 400). Works on both the `comment` and `story_reply` triggers. Up to 10 elements, rendered as a horizontally swipeable carousel. Rendering confirmed on the Instagram and Messenger mobile apps. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**elements** | [**List&lt;CommentAutomationTemplateElement&gt;**](CommentAutomationTemplateElement.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GENERIC | &quot;generic&quot; |



