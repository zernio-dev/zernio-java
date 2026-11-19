

# GetVoiceCallEstimate200ResponseTrunk

Trunk calls only. Whether the trunk's limits would refuse this call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Trunk the limits were read from. Null when none was resolved and the defaults apply. |  [optional] |
|**limitsSource** | [**LimitsSourceEnum**](#LimitsSourceEnum) |  |  [optional] |
|**maxDestinationRateUsd** | **BigDecimal** | Per-minute cap, compared with the carrier&#39;s rate for the route (half the billed rate). Default 0.30, null when the trunk has no cap. |  [optional] |
|**destinationWhitelisted** | **Boolean** | Whether destinationCountry is on the trunk&#39;s whitelist. The default whitelist is every country Zernio sells numbers in. |  [optional] |
|**rateCheck** | [**RateCheckEnum**](#RateCheckEnum) | &#x60;partial&#x60; means some of the destination&#39;s networks are above the cap and calls to them are refused. |  [optional] |
|**outboundEnabled** | **Boolean** | False while outbound is paused for an unfunded balance. Null with default limits. |  [optional] |
|**wouldBlock** | **Boolean** |  |  [optional] |
|**blockReasons** | [**List&lt;BlockReasonsEnum&gt;**](#List&lt;BlockReasonsEnum&gt;) |  |  [optional] |



## Enum: LimitsSourceEnum

| Name | Value |
|---- | -----|
| TRUNK | &quot;trunk&quot; |
| DEFAULT | &quot;default&quot; |



## Enum: RateCheckEnum

| Name | Value |
|---- | -----|
| UNDER | &quot;under&quot; |
| PARTIAL | &quot;partial&quot; |
| OVER | &quot;over&quot; |



## Enum: List&lt;BlockReasonsEnum&gt;

| Name | Value |
|---- | -----|
| DESTINATION_NOT_WHITELISTED | &quot;destination_not_whitelisted&quot; |
| RATE_ABOVE_CAP | &quot;rate_above_cap&quot; |
| OUTBOUND_PAUSED | &quot;outbound_paused&quot; |



