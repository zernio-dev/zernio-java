

# GetVoiceCallEstimate200ResponseBreakdown


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**telnyxCostUSD** | **BigDecimal** |  |  [optional] |
|**recordingCostUSD** | **BigDecimal** |  |  [optional] |
|**transcriptionCostUSD** | **BigDecimal** |  |  [optional] |
|**brandedCallUSD** | **BigDecimal** | Branded Calling surcharge, 0 unless &#x60;from&#x60; is a verified branded number calling a US destination. |  [optional] |
|**billableCostUSD** | **BigDecimal** | What Zernio bills for the call. |  [optional] |
|**totalCostUSD** | **BigDecimal** | Equals billableCostUSD (no separate Meta bill on PSTN); kept for shape parity with the WhatsApp estimate. |  [optional] |



