

# GetSipTrunk200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**label** | **String** |  |  [optional] |
|**sipHost** | **String** |  |  [optional] |
|**sipPort** | **Integer** |  |  [optional] |
|**transport** | [**TransportEnum**](#TransportEnum) |  |  [optional] |
|**termination** | [**ListSipTrunks200ResponseTrunksInnerTermination**](ListSipTrunks200ResponseTrunksInnerTermination.md) |  |  [optional] |
|**numbersAttached** | **Integer** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**numbers** | [**List&lt;GetSipTrunk200ResponseNumbersInner&gt;**](GetSipTrunk200ResponseNumbersInner.md) |  |  [optional] |



## Enum: TransportEnum

| Name | Value |
|---- | -----|
| TLS | &quot;tls&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



