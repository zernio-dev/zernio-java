

# ConversionAuditReportPlatformsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Stable platform key (meta, google, tiktok, ...). |  |
|**name** | **String** | Human-readable platform name. |  |
|**browserPixel** | **Boolean** | Whether a browser pixel for this platform was found. |  |
|**serverSide** | **Boolean** | True only when a server-side path is proven: visible from the page, or verified through the Zernio account behind the site tag. |  |
|**relayedBy** | [**RelayedByEnum**](#RelayedByEnum) | The only server path seen is the Zernio site tag relay; &#x60;serverSideVerified&#x60; says whether its delivery to this platform is proven. |  [optional] |
|**serverSideVerified** | **Boolean** | The Zernio site tag on the page belongs to an account whose destination for this platform accepted the site&#39;s events in the last 7 days. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;good&#x60; &#x3D; server-side, &#x60;warn&#x60; &#x3D; browser-only (the leak), &#x60;missing&#x60; &#x3D; not tracked, &#x60;not-firing&#x60; &#x3D; the tag is installed but sent nothing during a full visit. |  |
|**estimatedLossBrowserOnly** | **BigDecimal** | Share of conversions typically lost when this platform runs browser-only, 0-1. |  |
|**note** | **String** | Short explanation of the finding. |  |
|**ids** | **List&lt;String&gt;** | Pixel or tag ids found for this platform. |  [optional] |
|**events** | **List&lt;String&gt;** | Standard events called in the page or its tag-manager containers. |  [optional] |
|**fixSteps** | **List&lt;String&gt;** | Steps to fix this platform&#39;s tracking. |  [optional] |
|**fired** | [**FiredEnum**](#FiredEnum) | Rendered scans: &#x60;after-consent&#x60; when the pixel fired only once the scan accepted the cookie banner. |  [optional] |



## Enum: RelayedByEnum

| Name | Value |
|---- | -----|
| ZERNIO_TAG | &quot;zernio-tag&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| GOOD | &quot;good&quot; |
| WARN | &quot;warn&quot; |
| MISSING | &quot;missing&quot; |
| NOT_FIRING | &quot;not-firing&quot; |



## Enum: FiredEnum

| Name | Value |
|---- | -----|
| BEFORE_CONSENT | &quot;before-consent&quot; |
| AFTER_CONSENT | &quot;after-consent&quot; |



