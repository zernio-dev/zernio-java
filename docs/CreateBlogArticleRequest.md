

# CreateBlogArticleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  |
|**bodyHtml** | **String** | Article body as HTML. |  [optional] |
|**handle** | **String** | URL slug. Generated from the title when omitted. |  [optional] |
|**tags** | **List&lt;String&gt;** | Tag names. WordPress and Wix resolve existing names case-insensitively and create missing tags (Wix allows up to 30). |  [optional] |
|**author** | **String** | Shopify author display name, numeric WordPress user id serialized as a string, or Wix site member id. Assigning another WordPress user may require elevated capability. Wix posts without one go to the site&#39;s default author. |  [optional] |
|**excerpt** | **String** | Short summary shown in blog listings. |  [optional] |
|**image** | [**CreateBlogArticleRequestImage**](CreateBlogArticleRequestImage.md) |  |  [optional] |
|**seo** | [**CreateBlogArticleRequestSeo**](CreateBlogArticleRequestSeo.md) |  |  [optional] |
|**isPublished** | **Boolean** | Set false for a draft or true to publish. On WordPress and Wix false takes priority over a future publishDate; omission with no date defaults to draft. |  [optional] |
|**publishDate** | **OffsetDateTime** | ISO 8601 datetime with offset (or Z). A future date schedules publication natively on the platform. |  [optional] |



