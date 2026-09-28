

# RcsAgentProfile

The agent's public profile. At least one of phone, website or email is required.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  |
|**logoUrl** | **URI** | 224x224, max 50 KB. Upload any image through POST /v1/rcs/assets to get a compliant URL. |  |
|**heroUrl** | **URI** | Banner, 1440x448, max 200 KB. Upload through POST /v1/rcs/assets. |  |
|**brandColor** | **String** | Hex colour, e.g. #1A73E8. Needs 4.5:1 contrast against white. |  |
|**privacyPolicyUrl** | **URI** |  |  |
|**termsUrl** | **URI** |  |  |
|**phone** | [**RcsAgentProfilePhone**](RcsAgentProfilePhone.md) |  |  [optional] |
|**website** | [**RcsAgentProfileWebsite**](RcsAgentProfileWebsite.md) |  |  [optional] |
|**email** | [**RcsAgentProfileEmail**](RcsAgentProfileEmail.md) |  |  [optional] |



