

# CreateLeadFormRequestContextCard

Intro card shown before the questions page. Omit to skip the intro screen.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | Headline / title of the intro card. |  [optional] |
|**content** | **List&lt;String&gt;** | Body text lines shown on the intro card. |  [optional] |
|**style** | [**StyleEnum**](#StyleEnum) | Visual layout of the intro card. |  [optional] |
|**buttonText** | **String** | CTA button label on the intro card. |  [optional] |
|**coverPhoto** | **String** | Image hash of the cover photo (obtain from the Meta Ad Images API). Omit to show no image. |  [optional] |



## Enum: StyleEnum

| Name | Value |
|---- | -----|
| LIST_STYLE | &quot;LIST_STYLE&quot; |
| PARAGRAPH_STYLE | &quot;PARAGRAPH_STYLE&quot; |



