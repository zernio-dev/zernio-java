

# ReplyToInboxPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**message** | **String** | Reply text. On LinkedIn, mention with @[https://www.linkedin.com/in/vanity] (resolved to LinkedIn&#39;s live name, same rules and errors as post content) or @[Name](urn:li:person|organization:ID); a hand-written name must match LinkedIn&#39;s exactly or it renders as plain text. |  |
|**attachmentUrl** | **URI** | (Facebook only) URL of an image to attach, publishing a photo comment alongside the text. The URL must be publicly accessible so Meta can fetch it. Returns 400 for other platforms. |  [optional] |
|**commentId** | **String** | Reply to specific comment (optional) |  [optional] |
|**parentCid** | **String** | (Bluesky only) Parent content identifier |  [optional] |
|**rootUri** | **String** | (Bluesky only) Root post URI |  [optional] |
|**rootCid** | **String** | (Bluesky only) Root post CID |  [optional] |



