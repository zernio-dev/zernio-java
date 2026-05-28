

# InitiateWhatsAppCall200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**callId** | **String** | Internal Call doc ID |  [optional] |
|**telnyxCallControlId** | **String** | Telnyx call_control_id of the outbound leg |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**to** | **String** |  |  [optional] |
|**forwardTo** | **String** |  |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DIALING | &quot;dialing&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| OUTBOUND | &quot;outbound&quot; |



