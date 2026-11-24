

# GetEvent200ResponseDeliveriesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**destinationId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;dropped&#x60;: not sent because the visitor did not consent; &#x60;errorCode&#x60; says why (&#x60;consent_denied&#x60; or &#x60;consent_missing&#x60;). |  [optional] |
|**attempt** | **Integer** | Send attempt (1 &#x3D; the first). |  [optional] |
|**error** | **String** |  |  [optional] |
|**errorCode** | **String** |  |  [optional] |
|**sentAt** | **OffsetDateTime** |  |  [optional] |
|**valueSent** | **BigDecimal** | The value this destination got, after its forwarding rule&#39;s &#x60;eventValues&#x60; or &#x60;valueOverride&#x60;. Null when it got none, and on sends before 2026-11-24. |  [optional] |
|**currencySent** | **String** | The currency sent with &#x60;valueSent&#x60;. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| METAADS | &quot;metaads&quot; |
| GOOGLEADS | &quot;googleads&quot; |
| LINKEDINADS | &quot;linkedinads&quot; |
| TIKTOKADS | &quot;tiktokads&quot; |
| OPENAIADS | &quot;openaiads&quot; |
| PINTERESTADS | &quot;pinterestads&quot; |
| REDDITADS | &quot;redditads&quot; |
| APPLOVINADS | &quot;applovinads&quot; |
| MICROSOFTADS | &quot;microsoftads&quot; |
| XADS | &quot;xads&quot; |
| SNAPCHATADS | &quot;snapchatads&quot; |
| TABOOLAADS | &quot;taboolaads&quot; |
| OUTBRAINADS | &quot;outbrainads&quot; |
| GOOGLEANALYTICS | &quot;googleanalytics&quot; |
| KLAVIYO | &quot;klaviyo&quot; |
| ATTENTIVE | &quot;attentive&quot; |
| IMPACT | &quot;impact&quot; |
| AWIN | &quot;awin&quot; |
| CAMPAIGNMANAGER360 | &quot;campaignmanager360&quot; |
| TRADEDESKADS | &quot;tradedeskads&quot; |
| AMAZONADS | &quot;amazonads&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| RETRYING | &quot;retrying&quot; |
| FAILED | &quot;failed&quot; |
| DROPPED | &quot;dropped&quot; |



