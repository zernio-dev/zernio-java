

# ConversionAuditReport

The scored conversion-tracking audit of one page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **String** | The normalized URL that was scanned. |  |
|**domain** | **String** | The scanned host without &#x60;www.&#x60;. |  |
|**score** | **BigDecimal** | Conversion tracking score, 0-100. Higher means a more complete setup and less signal at risk. |  |
|**grade** | [**GradeEnum**](#GradeEnum) | Letter grade for the score. |  |
|**scoreRange** | [**ConversionAuditReportScoreRange**](ConversionAuditReportScoreRange.md) |  |  [optional] |
|**estimatedSignalLossPct** | **BigDecimal** | Average share of conversions at risk on the networks with no visible server-side path, 0-100. |  |
|**platforms** | [**List&lt;ConversionAuditReportPlatformsInner&gt;**](ConversionAuditReportPlatformsInner.md) | One finding per ad platform the scan looked for. |  |
|**browserOnly** | **Boolean** | True when every active platform is tracked browser-only. |  |
|**consentManager** | **String** | Consent manager found on the page, or null. |  |
|**activePlatformCount** | **Integer** | How many ad platforms the scan found any tracking for. |  |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | &#x60;full&#x60; &#x3D; pixels were visible, &#x60;limited&#x60; &#x3D; tags load dynamically so not all are visible, &#x60;none&#x60; &#x3D; nothing found. |  |
|**scannerBlocked** | **Boolean** | Always &#x60;true&#x60; when present: set when the site served our page fetch a bot wall and showed no pixel. The report is a partial, source-only read, so &#x60;score&#x60; and &#x60;grade&#x60; are placeholders, not a verdict, and &#x60;networks&#x60; is empty. |  [optional] |
|**siteSignals** | **List&lt;String&gt;** | Site tech recognized (Shopify, WooCommerce, ...). |  |
|**scanMode** | [**ScanModeEnum**](#ScanModeEnum) | &#x60;rendered&#x60; when a headless browser ran the page and its requests were checked, &#x60;static&#x60; for the page source only. |  [optional] |
|**limitations** | **List&lt;String&gt;** | What this scan could not see. |  [optional] |
|**checks** | [**List&lt;ConversionAuditReportChecksInner&gt;**](ConversionAuditReportChecksInner.md) | The scored checks behind &#x60;score&#x60;. |  [optional] |
|**serverSide** | [**ConversionAuditReportServerSide**](ConversionAuditReportServerSide.md) |  |  [optional] |
|**consent** | [**ConversionAuditReportConsent**](ConversionAuditReportConsent.md) |  |  [optional] |
|**consentScan** | [**ConversionAuditReportConsentScan**](ConversionAuditReportConsentScan.md) |  |  [optional] |
|**tagManagers** | **List&lt;String&gt;** |  |  [optional] |
|**otherNetworks** | [**List&lt;ConversionAuditReportOtherNetworksInner&gt;**](ConversionAuditReportOtherNetworksInner.md) | Ad networks found that the score does not cover. &#x60;relaySupported&#x60; is true when Zernio can send them conversions. |  [optional] |
|**otherNetworksConfigured** | [**List&lt;ConversionAuditReportOtherNetworksInner&gt;**](ConversionAuditReportOtherNetworksInner.md) | Rendered scans: unscored ad networks found only in a Google Tag Manager container that the visit never saw load or send. Not counted in &#x60;otherNetworks&#x60;. |  [optional] |
|**faviconUrl** | **String** | The site&#39;s icon. Absent when the site was unreachable. |  [optional] |
|**summary** | **String** | One-paragraph summary of the audit. |  |



## Enum: GradeEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| B | &quot;B&quot; |
| C | &quot;C&quot; |
| D | &quot;D&quot; |
| F | &quot;F&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| FULL | &quot;full&quot; |
| LIMITED | &quot;limited&quot; |
| NONE | &quot;none&quot; |



## Enum: ScanModeEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;static&quot; |
| RENDERED | &quot;rendered&quot; |



