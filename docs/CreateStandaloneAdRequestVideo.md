

# CreateStandaloneAdRequestVideo

Meta (facebook, instagram) and LinkedIn. When set, creates a VIDEO ad on the legacy (or, for Meta, attach) shape. Mutually exclusive with `imageUrl`. For Meta multi-creative, set `video` per entry inside `creatives[]` instead. For LinkedIn the video is uploaded to LinkedIn under the authoring Company Page (see `organizationId`) and the campaign format is set to SINGLE_VIDEO; LinkedIn ignores `thumbnailUrl` (it auto-generates the poster frame) — supply MP4 H.264/AAC, 3s-30min, 75KB-500MB.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** | Public URL of the video. Meta: uploaded via chunked transfer on /act_X/advideos, then the request blocks on Meta&#39;s transcoding until status.video_status &#x3D;&#x3D;&#x3D; &#39;ready&#39;. LinkedIn: uploaded via the Videos API (multipart), then the request blocks until LinkedIn finishes transcoding (status AVAILABLE) — short clips take ~10-30s. |  |
|**thumbnailUrl** | **URI** | Public URL of a still-image thumbnail for the video. Required by Meta on every video creative (uploaded as an ad image and referenced in object_story_spec.video_data). Ignored by LinkedIn (auto-generated poster frame). |  [optional] |



