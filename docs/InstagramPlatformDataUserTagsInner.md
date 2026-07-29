

# InstagramPlatformDataUserTagsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**username** | **String** | Instagram username (@ symbol is optional and will be removed automatically) |  |
|**x** | **BigDecimal** | X coordinate position from left edge (0.0 &#x3D; left, 0.5 &#x3D; center, 1.0 &#x3D; right). Required for photos, ignored for Reels/videos, optional for stories. |  [optional] |
|**y** | **BigDecimal** | Y coordinate position from top edge (0.0 &#x3D; top, 0.5 &#x3D; center, 1.0 &#x3D; bottom). Required for photos, ignored for Reels/videos, optional for stories. |  [optional] |
|**mediaIndex** | **Integer** | Zero-based index of the carousel item to tag. Defaults to 0. Tags on out-of-range indices are ignored. |  [optional] |



