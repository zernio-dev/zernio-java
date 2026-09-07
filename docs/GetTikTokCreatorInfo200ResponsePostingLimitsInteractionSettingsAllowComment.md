

# GetTikTokCreatorInfo200ResponsePostingLimitsInteractionSettingsAllowComment

Descriptor for the allow_comment toggle.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the creator permits this interaction. False means they disabled it in the TikTok app. This is availability, never the value the user selected. |  [optional] |
|**required** | **Boolean** | Whether tiktokSettings.allow_comment must be supplied when creating a post. Always true, because TikTok forbids defaulting it. |  [optional] |
|**_default** | **Boolean** | Initial value a post composer should render. A UI seed only, never applied server-side when the field is omitted. |  [optional] |
|**label** | **String** | Human-readable toggle label. |  [optional] |



