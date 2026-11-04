

# ListWhatsAppCalls200ResponseCallsInnerBilling


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metaCostUSD** | **BigDecimal** | Meta per-minute charge, billed by Meta directly to your WABA. Display only; not billed by Zernio. |  [optional] |
|**telnyxCostUSD** | **BigDecimal** |  |  [optional] |
|**recordingSeconds** | **BigDecimal** | Seconds of the call that were recorded and billed as recording. |  [optional] |
|**recordingCostUSD** | **BigDecimal** |  |  [optional] |
|**billableCostUSD** | **BigDecimal** | Amount Zernio bills you &#x3D; Telnyx leg + recording (excludes Meta). |  [optional] |
|**totalCostUSD** | **BigDecimal** | Full cost incl. the Meta portion you pay directly. Display only. |  [optional] |
|**currency** | **String** |  |  [optional] |



