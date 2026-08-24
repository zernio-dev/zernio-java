

# CreateSipTrunk201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**label** | **String** |  |  [optional] |
|**sipHost** | **String** |  |  [optional] |
|**sipPort** | **Integer** |  |  [optional] |
|**transport** | [**TransportEnum**](#TransportEnum) |  |  [optional] |
|**termination** | [**CreateSipTrunk201ResponseTermination**](CreateSipTrunk201ResponseTermination.md) |  |  [optional] |
|**numbersAttached** | **Integer** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**digestPassword** | **String** | SIP digest password, shown only in this response. |  [optional] |



## Enum: TransportEnum

| Name | Value |
|---- | -----|
| TLS | &quot;tls&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



