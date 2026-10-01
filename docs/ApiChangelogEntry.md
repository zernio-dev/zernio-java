

# ApiChangelogEntry

One API changelog entry, as shown on https://docs.zernio.com/changelog.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable entry id; the same entry is never published twice. |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**platforms** | **List&lt;String&gt;** | Platform and area slugs the entry is about: a platform (&#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;threads&#x60;, &#x60;tiktok&#x60;, &#x60;x&#x60;, &#x60;linkedin&#x60;, &#x60;youtube&#x60;, &#x60;pinterest&#x60;, &#x60;reddit&#x60;, &#x60;bluesky&#x60;, &#x60;telegram&#x60;, &#x60;snapchat&#x60;, &#x60;whatsapp&#x60;, &#x60;discord&#x60;, &#x60;slack&#x60;, &#x60;google-business&#x60;, &#x60;imessage&#x60;), an ads platform (&#x60;meta-ads&#x60;, &#x60;google-ads&#x60;, &#x60;tiktok-ads&#x60;, &#x60;linkedin-ads&#x60;, &#x60;pinterest-ads&#x60;, &#x60;x-ads&#x60;) or an area (&#x60;ads&#x60;, &#x60;publishing&#x60;, &#x60;inbox&#x60;, &#x60;telephony&#x60;, &#x60;commerce&#x60;, &#x60;analytics&#x60;, &#x60;webhooks&#x60;, &#x60;general&#x60;). Filter with the &#x60;platform&#x60; query parameter. |  |
|**message** | **String** | The announcement, in Markdown. |  |
|**publishedAt** | **OffsetDateTime** |  |  |
|**specVersion** | **String** | The &#x60;info.version&#x60; of the OpenAPI spec the entry describes, when known. |  |
|**url** | **URI** | The entry on the docs changelog. |  |
|**changes** | [**ApiChangelogEntryChanges**](ApiChangelogEntryChanges.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NEW_FEATURE | &quot;new_feature&quot; |
| BREAKING_CHANGE | &quot;breaking_change&quot; |
| IMPROVEMENT | &quot;improvement&quot; |
| DEPRECATION | &quot;deprecation&quot; |
| MINOR | &quot;minor&quot; |



