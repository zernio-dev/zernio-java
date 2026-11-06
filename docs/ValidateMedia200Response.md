

# ValidateMedia200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**valid** | **Boolean** |  |  [optional] |
|**url** | **URI** |  |  [optional] |
|**error** | **String** | Error message if valid is false |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) | Stable reason when valid is false. MEDIA_UNDECODABLE: the bytes are not a valid image, video or PDF. MEDIA_URL_UNREACHABLE: HTTP error, timeout, network failure, or a web page served instead of the file. MEDIA_URL_NOT_ALLOWED: not a public HTTP(S) URL. |  [optional] |
|**contentType** | **String** | Content-Type header the server sent (may disagree with the detected format) |  [optional] |
|**size** | **Integer** | File size in bytes |  [optional] |
|**sizeFormatted** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Detected from the file bytes |  [optional] |
|**format** | **String** | Detected format (jpeg, png, webp, gif, heif, mp4, mov, webm, pdf, ...) |  [optional] |
|**width** | **Integer** | Image width in pixels (images only) |  [optional] |
|**height** | **Integer** | Image height in pixels (images only) |  [optional] |
|**inspection** | [**InspectionEnum**](#InspectionEnum) | How deeply the content was verified. decoded: every pixel decoded. header: file signature and header verified (videos, PDFs, HEIC/AVIF, images over 32 MB). |  [optional] |
|**platformLimits** | [**Map&lt;String, ValidateMedia200ResponsePlatformLimitsValue&gt;**](ValidateMedia200ResponsePlatformLimitsValue.md) | Per-platform size limit comparison (only present when size and type are known) |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| MEDIA_UNDECODABLE | &quot;MEDIA_UNDECODABLE&quot; |
| MEDIA_URL_UNREACHABLE | &quot;MEDIA_URL_UNREACHABLE&quot; |
| MEDIA_URL_NOT_ALLOWED | &quot;MEDIA_URL_NOT_ALLOWED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| DOCUMENT | &quot;document&quot; |



## Enum: InspectionEnum

| Name | Value |
|---- | -----|
| DECODED | &quot;decoded&quot; |
| HEADER | &quot;header&quot; |



