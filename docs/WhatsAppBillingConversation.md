

# WhatsAppBillingConversation

WhatsApp only. Meta's `conversation` object from the status webhook (the billing window, not the Zernio inbox `conversation`). Same presence rules as `pricing`; from Graph API v24 Meta sends it only inside an open free entry point window. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta&#39;s conversation id. |  |
|**expiresAt** | **OffsetDateTime** | When the window expires. Meta sends it only on the &#x60;sent&#x60; status. |  |
|**originType** | **String** | Meta &#x60;origin.type&#x60;, for example &#x60;marketing&#x60;, &#x60;utility&#x60;, &#x60;service&#x60;, &#x60;referral_conversion&#x60;. |  |



