

# ImessageSenderLifecycle

A provisioned iMessage sender order and its lifecycle. Activation is asynchronous: poll GET /v1/imessage/senders/{senderId} or subscribe to account.connected.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) |  |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) |  |  [optional] |
|**handle** | **String** | The sender handle once activation assigns it |  [optional] |
|**optInLink** | **String** | imessage:// deep link that opens Messages on this sender with a prefilled text. Share it so contacts message you first (Apple only lets a sender reach contacts who wrote to it first); null until the handle is assigned. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**priceCents** | **Integer** | Monthly price billed while the sender is active |  [optional] |
|**provider** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**failureReason** | **String** |  |  [optional] |
|**accountId** | **String** | The messaging account created at activation |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| PHONE | &quot;phone&quot; |
| EMAIL | &quot;email&quot; |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| GB | &quot;GB&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ORDERING | &quot;ordering&quot; |
| ACTIVATING | &quot;activating&quot; |
| ACTIVE | &quot;active&quot; |
| SUSPENDED | &quot;suspended&quot; |
| CANCELED | &quot;canceled&quot; |
| FAILED | &quot;failed&quot; |



