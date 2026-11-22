

# ConversionAuditAnswerNetworksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Stable platform key (meta, google, tiktok, ...), as in &#x60;report.platforms&#x60;. |  |
|**name** | **String** | Short network name (Meta, Google, TikTok, ...). |  |
|**setup** | [**SetupEnum**](#SetupEnum) | How the network gets its conversions: &#x60;verified&#x60;, &#x60;likely&#x60; or &#x60;possible&#x60; server path, &#x60;not-visible&#x60; (browser pixel, no server path visible), &#x60;not-firing&#x60; (installed, sent nothing), &#x60;configured&#x60; (tag manager only, never seen firing, not at risk) or &#x60;missing&#x60;. |  |
|**leakPct** | **Integer** | Share of this network&#39;s conversions at risk, 0-100 (0 once a server path is verified). Null when the network has no working browser pixel to measure. |  |
|**loadedBy** | [**LoadedByEnum**](#LoadedByEnum) | &#x60;zernio-tag&#x60; when the pixel comes from the Zernio site tag&#39;s settings (it loads the pixel after consent) rather than from the page itself, on a scan that read the page source only. |  |



## Enum: SetupEnum

| Name | Value |
|---- | -----|
| VERIFIED | &quot;verified&quot; |
| LIKELY | &quot;likely&quot; |
| POSSIBLE | &quot;possible&quot; |
| NOT_VISIBLE | &quot;not-visible&quot; |
| NOT_FIRING | &quot;not-firing&quot; |
| CONFIGURED | &quot;configured&quot; |
| MISSING | &quot;missing&quot; |



## Enum: LoadedByEnum

| Name | Value |
|---- | -----|
| ZERNIO_TAG | &quot;zernio-tag&quot; |



