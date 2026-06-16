

# LinkedInPlatformData

Up to 20 images, no multi-video. Single PDF supported (max 100MB). Link previews auto-generated when no media attached. Use organizationUrn for multi-org posting. Geo-restriction only works for organization pages (not personal profiles) and requires the targeted audience to exceed 300 followers. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentTitle** | **String** | Title displayed on LinkedIn document (PDF/carousel) posts. Required by LinkedIn for document posts. If omitted, falls back to the media item title, then the filename. |  [optional] |
|**organizationUrn** | **String** | Target LinkedIn Organization URN (e.g. \&quot;urn:li:organization:123456789\&quot;). If omitted, uses the default org. Use GET /v1/accounts/{id}/linkedin-organizations to list orgs. |  [optional] |
|**firstComment** | **String** | Optional first comment to add after the post is created |  [optional] |
|**disableLinkPreview** | **Boolean** | Set to true to disable automatic link previews for URLs in the post content (default is false) |  [optional] |
|**reshareUrl** | **String** | LinkedIn post link to repost (use the post&#39;s \&quot;Copy link to post\&quot; action), or a urn:li:share / urn:li:ugcPost / urn:li:groupPost URN. The published post becomes a quote-reshare: your content is shown as the commentary and the original post is embedded underneath (LinkedIn&#39;s \&quot;repost with your thoughts\&quot;). Mutually exclusive with media. Works on personal profiles and organization pages. |  [optional] |
|**geoRestriction** | [**GeoRestriction**](GeoRestriction.md) |  |  [optional] |



