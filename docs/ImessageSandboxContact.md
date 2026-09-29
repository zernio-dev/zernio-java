

# ImessageSandboxContact


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**handle** | **String** | Phone (E.164) or lowercase Apple ID email |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**joinText** | **String** | Send this from the handle to the sandbox line to activate it |  [optional] |
|**joinLink** | **String** | Opens Messages on the sandbox line with joinText prefilled |  [optional] |
|**activatedAt** | **OffsetDateTime** |  |  [optional] |
|**lastInboundAt** | **OffsetDateTime** | Replies are allowed for 24 hours after this |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACTIVE | &quot;active&quot; |



