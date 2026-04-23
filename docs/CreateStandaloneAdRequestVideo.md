

# CreateStandaloneAdRequestVideo

Meta only (facebook, instagram). When set, creates a VIDEO ad on the legacy or attach shape. Mutually exclusive with `imageUrl`. For multi-creative, set `video` per entry inside `creatives[]` instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** | Public URL of the video. Uploaded to Meta via chunked transfer on /act_X/advideos; then the request blocks on Meta&#39;s transcoding until status.video_status &#x3D;&#x3D;&#x3D; &#39;ready&#39;. |  |
|**thumbnailUrl** | **URI** | Public URL of a still-image thumbnail for the video. Required by Meta on every video creative. Uploaded to Meta as an ad image and referenced as the thumbnail in object_story_spec.video_data. |  |



