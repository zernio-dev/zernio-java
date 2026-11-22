

# ConversionAuditReportPlatformsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Stable platform key (meta, google, tiktok, ...). |  |
|**name** | **String** | Human-readable platform name. |  |
|**browserPixel** | **Boolean** | Whether a browser pixel for this platform was found. |  |
|**serverSide** | **Boolean** | True only when a server-side path is proven: visible from the page, or verified through the Zernio account behind the site tag. |  |
|**relayedBy** | [**RelayedByEnum**](#RelayedByEnum) | The only server path seen is the Zernio site tag relay; &#x60;serverSideVerified&#x60; says whether its delivery to this platform is proven. |  [optional] |
|**loadedBy** | [**LoadedByEnum**](#LoadedByEnum) | On a scan that read the page source only: the pixel comes from the Zernio site tag&#39;s settings, which load it after consent, not from the page. Its ids are not reported. |  [optional] |
|**serverSideVerified** | **Boolean** | The Zernio site tag on the page belongs to an account whose destination for this platform accepted the site&#39;s events in the last 7 days. |  [optional] |
|**serverTool** | **String** | A third-party server-side tool installed on the site that may already send this platform&#39;s events (Elevar, Littledata, Stape), when its status is &#x60;likely&#x60;. Which platforms the tool feeds is not visible from the page. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;good&#x60;: server-side. &#x60;warn&#x60;: browser-only (the leak). &#x60;missing&#x60;: not tracked. &#x60;not-firing&#x60;: installed but sent nothing during a full visit. &#x60;configured&#x60;: only in a Google Tag Manager container and not seen firing on a visit where silence proves nothing, so not counted as tracked. |  |
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



## Enum: LoadedByEnum

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
| CONFIGURED | &quot;configured&quot; |



## Enum: FiredEnum

| Name | Value |
|---- | -----|
| BEFORE_CONSENT | &quot;before-consent&quot; |
| AFTER_CONSENT | &quot;after-consent&quot; |



