

# BlogArticle

An article inside a blog on the connected platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native article/post id: numeric on Shopify and WordPress, a GUID on Wix, a hex item id on Webflow. |  [optional] |
|**blogId** | **String** | Platform-native id of the blog the article belongs to. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**bodyHtml** | **String** | Article body as HTML. Wix stores rich content, converted from and to HTML; Wix lists return null (get the article for its body). |  [optional] |
|**handle** | **String** | URL slug of the article. |  [optional] |
|**tags** | **List&lt;String&gt;** | Tag names. On WordPress and Wix, missing tag names are created and matching is case-insensitive. |  [optional] |
|**author** | **String** | Shopify author display name, numeric WordPress user id serialized as a string, or Wix site member id. Wix posts without one are attributed to the site&#39;s default author. |  [optional] |
|**excerpt** | **String** | Short summary shown in blog listings. |  [optional] |
|**image** | [**BlogArticleImage**](BlogArticleImage.md) |  |  [optional] |
|**isPublished** | **Boolean** | False while the article is a draft or its publish date is still in the future. |  [optional] |
|**publishedAt** | **OffsetDateTime** | Publication time. On WordPress this is present only when status is &#x60;publish&#x60;; null for drafts, pending/private posts, and scheduled posts. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | WordPress and Wix. Post status (&#x60;future&#x60; &#x3D; scheduled, &#x60;pending&#x60; &#x3D; in review on Wix); omitted for Shopify. |  [optional] |
|**publishDate** | **OffsetDateTime** | WordPress and Wix. Scheduled publication time in UTC when status is &#x60;future&#x60;; null for other statuses and omitted for Shopify. |  [optional] |
|**createdAt** | **OffsetDateTime** | Creation time when the platform exposes one. WordPress returns null because its core date is the editable publication date. |  [optional] |
|**updatedAt** | **OffsetDateTime** | Last modification time. WordPress returns modified_gmt as UTC. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WORDPRESS | &quot;wordpress&quot; |
| WIX | &quot;wix&quot; |
| WEBFLOW | &quot;webflow&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PUBLISH | &quot;publish&quot; |
| FUTURE | &quot;future&quot; |
| DRAFT | &quot;draft&quot; |
| PENDING | &quot;pending&quot; |
| PRIVATE | &quot;private&quot; |



