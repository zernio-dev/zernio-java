

# MediaItem

Media referenced in posts. URLs must be publicly reachable over HTTPS. Use POST /v1/media/presign for uploads up to 5GB. Zernio auto-compresses images and videos that exceed platform limits (videos over 200 MB may not be compressed).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Optional when the item names a connected file (&#x60;fileId&#x60;): inferred from the file&#39;s MIME type. |  [optional] |
|**url** | **URI** | A media item with a null, missing or empty url is dropped, unless it names a connected file with &#x60;fileId&#x60; + &#x60;accountId&#x60;. |  [optional] |
|**fileId** | **String** | A file of a connected Google Drive or OneDrive account (see the Files endpoints). Requires &#x60;accountId&#x60;.  The file is copied into Zernio media storage when the post is created, and the item is stored as a plain &#x60;url&#x60;. A folder, an undownloadable file or an unknown id fails the request with a 4xx naming &#x60;mediaItems[i].fileId&#x60;.  |  [optional] |
|**accountId** | **String** | The connected Google or Microsoft account the &#x60;fileId&#x60; belongs to (must have the &#x60;files&#x60; area). Required with &#x60;fileId&#x60;. |  [optional] |
|**title** | **String** | Optional title for the media item. Used as the document title for LinkedIn PDF/carousel posts. If omitted, falls back to the post title, then the filename. |  [optional] |
|**altText** | **String** | Accessibility alternative text for an image. Set once per image; the same value is sent to each selected platform.  - Applied on: Instagram (feed images only, not Reels/Stories), Facebook, Threads, X (max 1000 chars), LinkedIn, Bluesky, Pinterest (max 500 chars). - Ignored on platforms without alt-text support (TikTok, YouTube, Snapchat, Telegram, Reddit, Google Business Profile, WhatsApp) and on video items where the platform does not accept it.  |  [optional] |
|**filename** | **String** |  |  [optional] |
|**size** | **Integer** | Optional file size in bytes |  [optional] |
|**mimeType** | **String** | Optional MIME type (e.g. image/jpeg, video/mp4) |  [optional] |
|**thumbnail** | **URI** | Optional custom thumbnail/cover image URL for videos. Supported for Facebook video posts, Facebook Reels, regular video uploads, and LinkedIn video posts. Max 10MB, JPG/PNG recommended. |  [optional] |
|**instagramThumbnail** | **URI** | Custom cover image URL for Instagram Reels. Can also be set via platformSpecificData.instagramThumbnail or platformSpecificData.reelCover. Resolution order: this field &gt; platformSpecificData.instagramThumbnail &gt; platformSpecificData.reelCover &gt; platformSpecificData.thumbnailUrl (legacy). |  [optional] |
|**subtitles** | [**List&lt;MediaSubtitle&gt;**](MediaSubtitle.md) | Subtitle (closed caption) files for a video item, in SRT or WebVTT. Each language may appear once per video. Zernio downloads each file when the post is created or updated and converts it to the format each platform requires.  Sent to YouTube, Facebook videos, LinkedIn, X and Bluesky; ignored with a warning elsewhere. Per platform:  - YouTube: every track. - Facebook: every track, up to 200 KB each. - Bluesky: every track, up to 20 KB each after conversion to WebVTT. - X: the first track only (one subtitle per video). - LinkedIn: the first English track only.  Tracks a platform cannot take are skipped and reported in the response warnings.  A file that is unreachable, redirects, exceeds 1 MB, is not valid SRT or WebVTT, or is over a platform limit is rejected with a 400 (code INVALID_SUBTITLES). If a platform rejects a file at publish time, the post still publishes, without subtitles.  |  [optional] |
|**tiktokProcessed** | **Boolean** | Internal flag indicating the image was resized for TikTok |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| GIF | &quot;gif&quot; |
| DOCUMENT | &quot;document&quot; |



