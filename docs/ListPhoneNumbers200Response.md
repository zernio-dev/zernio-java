

# ListPhoneNumbers200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numbers** | [**List&lt;ListPhoneNumbers200ResponseNumbersInner&gt;**](ListPhoneNumbers200ResponseNumbersInner.md) |  |  [optional] |
|**connected** | [**List&lt;ListPhoneNumbers200ResponseConnectedInner&gt;**](ListPhoneNumbers200ResponseConnectedInner.md) | Connected (bring-your-own) WhatsApp numbers — your own WABA numbers linked via Embedded Signup. Not provisioned or billed by Zernio, so they are not in &#x60;numbers&#x60;; &#x60;accountId&#x60; is the social-account id used by the messaging and inbox endpoints. Included only on the default and &#x60;status&#x3D;active&#x60; views.  |  [optional] |
|**sandbox** | [**ListPhoneNumbers200ResponseSandbox**](ListPhoneNumbers200ResponseSandbox.md) |  |  [optional] |



