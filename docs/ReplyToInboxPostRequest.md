

# ReplyToInboxPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**message** | **String** | Reply text. On LinkedIn, mention with @[Name](urn:li:person:ID) or @[Org](urn:li:organization:ID); the name must match LinkedIn&#39;s exactly (case-sensitive) or it renders as plain text. The profile-URL form is not resolved in comments, and an unknown person URN posts the plain name. |  |
|**attachmentUrl** | **URI** | (Facebook only) URL of an image to attach, publishing a photo comment alongside the text. The URL must be publicly accessible so Meta can fetch it. Returns 400 for other platforms. |  [optional] |
|**commentId** | **String** | Reply to specific comment (optional) |  [optional] |
|**parentCid** | **String** | (Bluesky only) Parent content identifier |  [optional] |
|**rootUri** | **String** | (Bluesky only) Root post URI |  [optional] |
|**rootCid** | **String** | (Bluesky only) Root post CID |  [optional] |



