

# CreateStandaloneAdRequestVideo

Meta (facebook, instagram) and LinkedIn. Creates a single VIDEO ad. Mutually exclusive with `imageUrl`. Supply `url` to upload a file, or `id` to reuse a video already on the ad account (list them with GET /v1/ads/videos). Works on the single-ad and attach (`adSetId`) shapes; for Meta multi-creative, set `video` per entry inside `creatives[]` instead. For LinkedIn the video is uploaded to LinkedIn under the authoring Company Page (see `organizationId`) and the campaign format is set to SINGLE_VIDEO; LinkedIn ignores `thumbnailUrl` (it auto-generates the poster frame) — supply MP4 H.264/AAC, 3s-30min, 75KB-500MB.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** | Public URL of the video. Meta: uploaded via chunked transfer on /act_X/advideos, then the request blocks on Meta&#39;s transcoding until status.video_status &#x3D;&#x3D;&#x3D; &#39;ready&#39;. LinkedIn: uploaded via the Videos API (multipart), then the request blocks until LinkedIn finishes transcoding (status AVAILABLE) — short clips take ~10-30s. Provide either &#x60;url&#x60; or &#x60;id&#x60;. |  [optional] |
|**id** | **String** | Meta only. Reuse a video ALREADY uploaded to this ad account instead of re-uploading the file: pass the &#x60;videoId&#x60; returned by a previous create. Wins over &#x60;url&#x60;, so N ads that differ only in copy share one upload (&#x60;existingCreativeId&#x60; only covers the identical-copy case). Provide either &#x60;url&#x60; or &#x60;id&#x60;. |  [optional] |
|**thumbnailUrl** | **URI** | Public URL of a still-image thumbnail for the video. OPTIONAL: when omitted on Meta, the poster is auto-generated from Meta&#39;s own preferred video thumbnail (the same candidates Ads Manager shows), so video ads usually publish without supplying one. When Meta produces no candidate the request fails with a 502 platform_error (reason: video_thumbnail_unavailable) — retry, or supply this field. Provide it to control the poster frame exactly (uploaded as an ad image and referenced in object_story_spec.video_data). Ignored by LinkedIn (auto-generated poster frame). |  [optional] |



