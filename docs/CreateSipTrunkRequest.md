

# CreateSipTrunkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** | Display name for the trunk. |  |
|**sipHost** | **String** | Fully-qualified hostname inbound calls are delivered to (e.g. sip.rtc.elevenlabs.io, sip.retellai.com). |  |
|**sipPort** | **Integer** | Defaults to 5061 for tls, 5060 otherwise. |  [optional] |
|**transport** | [**TransportEnum**](#TransportEnum) | Signaling transport toward sipHost. Default tls (with SRTP media). |  [optional] |



## Enum: TransportEnum

| Name | Value |
|---- | -----|
| TLS | &quot;tls&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



