

# TrackingTag

A platform measurement tag — the thing you create, install on a website, send events to, and target ads against. On Meta this is a Pixel (`kind: pixel`). The shape is platform-neutral so other platforms (Pinterest Tag, LinkedIn Insight Tag, etc.) can be added without changing the contract; platform-specific fields are simply absent where a platform has no equivalent. Returned by `listTrackingTags`, `createTrackingTag`, `getTrackingTag`, and `updateTrackingTag`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native tag id. Meta: numeric pixel id, as a string. |  |
|**name** | **String** |  |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | Platform-native flavor of the tag (Meta: &#x60;pixel&#x60;). |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;inactive&#x60; when the platform reports the tag as broken/unavailable. |  |
|**code** | **String** | The base-code &#x60;&lt;script&gt;&#x60; snippet to install on the site. Meta only; populated by &#x60;getTrackingTag&#x60;, omitted from the list view.  |  [optional] |
|**lastFiredTime** | **Integer** | Unix seconds of the last event the tag received, or &#x60;null&#x60; if it never fired. The practical \&quot;is it installed and working\&quot; signal.  |  [optional] |
|**isUnavailable** | **Boolean** | Whether the tag is in a broken/unavailable state (Meta &#x60;is_unavailable&#x60;). |  [optional] |
|**installed** | **Boolean** | Convenience flag derived from &#x60;lastFiredTime&#x60; — has the tag ever fired. |  [optional] |
|**creationTime** | **Integer** | Unix seconds the tag was created. |  [optional] |
|**ownerBusinessId** | **String** | Business Manager id that owns the tag, or &#x60;null&#x60; when the tag lives on a personal (non-BM) ad account — such tags can&#39;t be shared with other ad accounts.  |  [optional] |
|**ownerAdAccountId** | **String** | Ad account id (&#x60;act_...&#x60;) that owns the tag, when reported. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| METAADS | &quot;metaads&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| PIXEL | &quot;pixel&quot; |
| TAG | &quot;tag&quot; |
| INSIGHT_TAG | &quot;insight_tag&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



