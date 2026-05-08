

# SendConversionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | SocialAccount ID (metaads, googleads, or linkedinads). |  |
|**destinationId** | **String** | Platform destination identifier. For Meta, the pixel/dataset ID. For Google, the conversion action resource name. For LinkedIn, the conversion rule ID or full &#x60;urn:lla:llaPartnerConversion:{id}&#x60; URN.  |  |
|**events** | [**List&lt;ConversionEvent&gt;**](ConversionEvent.md) |  |  |
|**testCode** | **String** | Meta &#x60;test_event_code&#x60; passthrough. Ignored by Google and LinkedIn. |  [optional] |
|**consent** | [**SendConversionsRequestConsent**](SendConversionsRequestConsent.md) |  |  [optional] |



