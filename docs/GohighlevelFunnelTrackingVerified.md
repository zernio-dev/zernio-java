

# GohighlevelFunnelTrackingVerified

The page check, null unless a page was checked.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **String** |  |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | &#x60;tag&#x60;: the page carries the tag. &#x60;tag-manager&#x60;: Google Tag Manager loads on the page, so the tag may come through it. &#x60;missing&#x60;: not on the page. &#x60;unreachable&#x60;: the page did not load. |  [optional] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| TAG | &quot;tag&quot; |
| TAG_MANAGER | &quot;tag-manager&quot; |
| MISSING | &quot;missing&quot; |
| UNREACHABLE | &quot;unreachable&quot; |



