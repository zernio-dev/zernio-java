

# PurchasePhoneNumberRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile to associate the number with |  |
|**country** | **String** | ISO 3166-1 alpha-2 country for the number (default US). International numbers require usage-based billing. Tier 3/4 countries return 202 { status: \&quot;kyc_required\&quot;, kycUrl } — the customer must complete KYC at that URL before the number is ordered. See GET /v1/phone-numbers/countries.  |  [optional] |
|**numberType** | [**NumberTypeEnum**](#NumberTypeEnum) | Which of the country&#39;s offered number types to order (see &#x60;types[]&#x60; on GET /v1/phone-numbers/countries). Omitted &#x3D; the country&#39;s default type, which is always the WhatsApp-safe choice. Capabilities, price, and KYC requirements are per (country, type): toll_free can never connect WhatsApp (400 when combined with connectWhatsapp:true), and wantsSms:true requires an SMS-capable type.  |  [optional] |
|**connectWhatsapp** | **Boolean** | A phone number is the unit; WhatsApp is one optional feature. Pass false to buy a STANDALONE number (Calls/SMS only): provisioning skips the Meta pre-verify/OTP steps and the number activates immediately. Omitted defaults to the WhatsApp provisioning path. WhatsApp can be connected to a standalone number later from the connect flow.  |  [optional] |
|**wantsSms** | **Boolean** | SMS capability is per-number, not per-country. Pass true to provision from the SMS-capable inventory pool so the number can actually text (see also GET /v1/phone-numbers/available with sms&#x3D;true, and smsAvailable on GET /v1/phone-numbers/countries).  |  [optional] |
|**purchaseIntentId** | **String** | Optional idempotency key. Send the same value when retrying a purchase: if a number was already bought under this key, the API returns { status: \&quot;already_purchased\&quot;, numberId, phoneNumber } instead of provisioning a second number. Generate a fresh key for each genuinely new purchase.  |  [optional] |
|**allowMultiple** | **Boolean** | Any second purchase within 10 minutes of a previous one is rejected with 409 code PURCHASE_VELOCITY as duplicate protection. Pass true to confirm the additional purchase is intentional (e.g. bulk provisioning).  |  [optional] |



## Enum: NumberTypeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| MOBILE | &quot;mobile&quot; |
| NATIONAL | &quot;national&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



