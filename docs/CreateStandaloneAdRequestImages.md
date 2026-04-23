

# CreateStandaloneAdRequestImages

Google Display (Responsive Display Ads) only. Google RDA requires both a landscape (1.91:1) and a square (1:1) marketing image; sending only one is rejected upstream as 'Too few.' (NOT_ENOUGH_*_MARKETING_IMAGE_ASSET). Supply both URLs here. Either this field or the legacy `imageUrl` can provide the landscape, but `square` has no legacy counterpart so it must be set here for Display.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**landscape** | **URI** | Landscape 1.91:1 marketing image URL (e.g. 1200x628). Also accepted via the top-level &#x60;imageUrl&#x60; for backward compatibility. |  [optional] |
|**square** | **URI** | Square 1:1 marketing image URL (e.g. 1080x1080). Required for Google Display. |  [optional] |



