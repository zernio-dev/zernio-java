

# ReplyToInboxPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**message** | **String** |  |  |
|**attachmentUrl** | **URI** | (Facebook only) URL of an image to attach, publishing a photo comment alongside the text. The URL must be publicly accessible so Meta can fetch it. Returns 400 for other platforms. |  [optional] |
|**commentId** | **String** | Reply to specific comment (optional) |  [optional] |
|**parentCid** | **String** | (Bluesky only) Parent content identifier |  [optional] |
|**rootUri** | **String** | (Bluesky only) Root post URI |  [optional] |
|**rootCid** | **String** | (Bluesky only) Root post CID |  [optional] |



