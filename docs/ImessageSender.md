

# ImessageSender

An iMessage sender registered as an account on a profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Account id (use it with the inbox endpoints&#39; accountId) |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**sender** | **String** | The sender handle (E.164 phone or email) |  [optional] |
|**optInLink** | **String** | imessage:// deep link that opens Messages on this sender with a prefilled text. Share it so contacts message you first (Apple only lets a sender reach contacts who wrote to it first). |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**provider** | **String** | Delivery provider backing this sender (e.g. loopmessage) |  [optional] |
|**senderVerified** | **Boolean** | Whether the provider confirmed the sender as active at registration time |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| IMESSAGE | &quot;imessage&quot; |



