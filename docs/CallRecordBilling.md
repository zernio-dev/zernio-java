

# CallRecordBilling


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metaMinutes** | **BigDecimal** |  |  [optional] |
|**telnyxSeconds** | **BigDecimal** |  |  [optional] |
|**transcriptionSeconds** | **BigDecimal** |  |  [optional] |
|**transcriptionCostUSD** | **BigDecimal** |  |  [optional] |
|**metaCostUSD** | **BigDecimal** | WhatsApp channel only. Meta per-minute charge, billed by Meta directly to your WABA. Display only; not billed by Zernio. |  [optional] |
|**telnyxCostUSD** | **BigDecimal** |  |  [optional] |
|**recordingCostUSD** | **BigDecimal** |  |  [optional] |
|**billableCostUSD** | **BigDecimal** | Amount Zernio bills you &#x3D; telephony leg + recording + transcription (excludes any Meta portion). |  [optional] |
|**totalCostUSD** | **BigDecimal** | Full cost incl. any Meta portion you pay directly. Display only. |  [optional] |
|**currency** | **String** |  |  [optional] |



