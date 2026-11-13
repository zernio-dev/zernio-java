

# EmailCapabilitiesSentItems

Outlook only: how mail sent from the user's own mail client reaches you (`message.sent`). `poll` while Microsoft will not give Zernio a Sent Items subscription for this mailbox; it switches back to `push` by itself.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) |  |  [optional] |
|**typicalDelaySeconds** | **Integer** |  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| PUSH | &quot;push&quot; |
| POLL | &quot;poll&quot; |



