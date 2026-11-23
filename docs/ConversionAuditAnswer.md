

# ConversionAuditAnswer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**report** | [**ConversionAuditReport**](ConversionAuditReport.md) |  |  |
|**networks** | [**List&lt;ConversionAuditAnswerNetworksInner&gt;**](ConversionAuditAnswerNetworksInner.md) | Each ad network with its final setup and leak, computed exactly as the public report page shows them, best setup first. Empty when &#x60;report.scannerBlocked&#x60; is set: the scan could not see any network. |  |
|**topFixes** | [**List&lt;ConversionAuditAnswerTopFixesInner&gt;**](ConversionAuditAnswerTopFixesInner.md) | The few fixes that matter most, in the order the public report page lists them. |  |
|**fixPrompt** | **String** | A prompt to paste into a coding agent. It lists the report&#39;s findings, then connecting Zernio, sending conversions server-side and verifying them. |  |
|**publicReport** | [**ConversionAuditAnswerPublicReport**](ConversionAuditAnswerPublicReport.md) |  |  |



