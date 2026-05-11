

# UpdateTrackingTagRequest

At least one field is required; the route returns 400 if the body is empty.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**enableAutomaticMatching** | **Boolean** | Meta Advanced Matching toggle (&#x60;enable_automatic_matching&#x60;). |  [optional] |
|**automaticMatchingFields** | [**List&lt;AutomaticMatchingFieldsEnum&gt;**](#List&lt;AutomaticMatchingFieldsEnum&gt;) | Which user fields Advanced Matching may collect. Meta&#39;s terse codes: em&#x3D;email, ph&#x3D;phone, fn&#x3D;first name, ln&#x3D;last name, ge&#x3D;gender, db&#x3D;date of birth, ct&#x3D;city, st&#x3D;state, zp&#x3D;zip.  |  [optional] |
|**firstPartyCookieStatus** | [**FirstPartyCookieStatusEnum**](#FirstPartyCookieStatusEnum) |  |  [optional] |
|**dataUseSetting** | [**DataUseSettingEnum**](#DataUseSettingEnum) |  |  [optional] |



## Enum: List&lt;AutomaticMatchingFieldsEnum&gt;

| Name | Value |
|---- | -----|
| EM | &quot;em&quot; |
| PH | &quot;ph&quot; |
| FN | &quot;fn&quot; |
| LN | &quot;ln&quot; |
| GE | &quot;ge&quot; |
| DB | &quot;db&quot; |
| CT | &quot;ct&quot; |
| ST | &quot;st&quot; |
| ZP | &quot;zp&quot; |
| COUNTRY | &quot;country&quot; |
| EXTERNAL_ID | &quot;external_id&quot; |



## Enum: FirstPartyCookieStatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;empty&quot; |
| FIRST_PARTY_COOKIE_DISABLED | &quot;first_party_cookie_disabled&quot; |
| FIRST_PARTY_COOKIE_ENABLED | &quot;first_party_cookie_enabled&quot; |



## Enum: DataUseSettingEnum

| Name | Value |
|---- | -----|
| ADVERTISING_AND_ANALYTICS | &quot;advertising_and_analytics&quot; |
| ANALYTICS_ONLY | &quot;analytics_only&quot; |
| EMPTY | &quot;empty&quot; |



