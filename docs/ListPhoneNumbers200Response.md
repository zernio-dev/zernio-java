

# ListPhoneNumbers200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numbers** | [**List&lt;OwnedPhoneNumber&gt;**](OwnedPhoneNumber.md) |  |  [optional] |
|**connected** | [**List&lt;ListPhoneNumbers200ResponseConnectedInner&gt;**](ListPhoneNumbers200ResponseConnectedInner.md) | Connected (bring-your-own) WhatsApp numbers: your own WABA numbers linked via Embedded Signup. Not provisioned or billed by Zernio, so they are not in &#x60;numbers&#x60;; &#x60;accountId&#x60; is the social-account id used by the messaging and inbox endpoints. Included only on the default and &#x60;status&#x3D;active&#x60; views.  |  [optional] |
|**imessage** | [**List&lt;ImessageSenderLifecycle&gt;**](ImessageSenderLifecycle.md) | iMessage phone senders (see /v1/imessage/senders/order). Hosted by the iMessage provider, not on your Telnyx numbers: SMS and Calls can never be enabled on them, and they bill as iMessage senders. &#x60;handle&#x60; is null until the carrier assigns the number at activation. Included only on the default and &#x60;status&#x3D;active&#x60; views.  |  [optional] |
|**sandbox** | [**ListPhoneNumbers200ResponseSandbox**](ListPhoneNumbers200ResponseSandbox.md) |  |  [optional] |



