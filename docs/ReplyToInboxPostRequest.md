

# ReplyToInboxPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**message** | **String** | Reply text. On LinkedIn, mention with @[https://www.linkedin.com/in/vanity] (resolved to LinkedIn&#39;s live name, same rules and errors as post content) or @[Name](urn:li:person|organization:ID); a hand-written name must match LinkedIn&#39;s exactly or it renders as plain text. |  |
|**attachmentUrl** | **URI** | (Facebook only) URL of an image to attach, publishing a photo comment alongside the text. The URL must be publicly accessible so Meta can fetch it. Returns 400 for other platforms. |  [optional] |
|**commentId** | **String** | Reply to specific comment (optional) |  [optional] |
|**mentionAuthor** | **Boolean** | (LinkedIn only) When true, the reply starts with an @mention of the author of &#x60;commentId&#x60; (a member or a page), tagged with their URN and the name LinkedIn returns for them. Requires &#x60;commentId&#x60;. Returns 400 &#x60;platform_not_supported&#x60; on other platforms, and 400 &#x60;linkedin_mention_name_unavailable&#x60; with &#x60;details.authorUrn&#x60; when LinkedIn does not return the author&#39;s name (for example a page the account does not administer); mention them in &#x60;message&#x60; as @[Name](urn) instead. If LinkedIn rejects any mention in the reply, it is posted once more with every mention as plain text. |  [optional] |
|**parentCid** | **String** | (Bluesky only) Parent content identifier |  [optional] |
|**rootUri** | **String** | (Bluesky only) Root post URI |  [optional] |
|**rootCid** | **String** | (Bluesky only) Root post CID |  [optional] |



