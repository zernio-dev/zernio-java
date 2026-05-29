

# WebhookPayloadCallEndedCallBilling


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metaCostUSD** | **BigDecimal** | Meta per-minute charge. Billed by Meta DIRECTLY to your WhatsApp Business Account payment method (your separate Meta invoice). Zernio does NOT charge this. Display only. |  [optional] |
|**telnyxCostUSD** | **BigDecimal** |  |  [optional] |
|**recordingCostUSD** | **BigDecimal** |  |  [optional] |
|**billableCostUSD** | **BigDecimal** | The amount Zernio bills you &#x3D; Telnyx leg + recording. Excludes Meta (billed by Meta directly). |  [optional] |
|**totalCostUSD** | **BigDecimal** | Full economic cost incl. the Meta portion you pay directly (Meta + Telnyx + recording). Display only, not the Zernio-billed amount. |  [optional] |



