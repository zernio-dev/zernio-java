

# UpdateGoogleBusinessLocationDetailsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**updateMask** | **String** | Required. Comma-separated fields to update (e.g. &#39;regularHours&#39;, &#39;specialHours&#39;, &#39;profile.description&#39;, &#39;categories&#39;, &#39;serviceItems&#39;). Any valid Google Business Information API updateMask field is supported. |  |
|**regularHours** | [**UpdateGoogleBusinessLocationDetailsRequestRegularHours**](UpdateGoogleBusinessLocationDetailsRequestRegularHours.md) |  |  [optional] |
|**specialHours** | [**GetGoogleBusinessLocationDetails200ResponseSpecialHours**](GetGoogleBusinessLocationDetails200ResponseSpecialHours.md) |  |  [optional] |
|**profile** | [**UpdateGoogleBusinessLocationDetailsRequestProfile**](UpdateGoogleBusinessLocationDetailsRequestProfile.md) |  |  [optional] |
|**websiteUri** | **String** |  |  [optional] |
|**phoneNumbers** | [**GetGoogleBusinessLocationDetails200ResponsePhoneNumbers**](GetGoogleBusinessLocationDetails200ResponsePhoneNumbers.md) |  |  [optional] |
|**categories** | [**UpdateGoogleBusinessLocationDetailsRequestCategories**](UpdateGoogleBusinessLocationDetailsRequestCategories.md) |  |  [optional] |
|**serviceItems** | [**List&lt;UpdateGoogleBusinessLocationDetailsRequestServiceItemsInner&gt;**](UpdateGoogleBusinessLocationDetailsRequestServiceItemsInner.md) | Services offered by the business. Use updateMask&#x3D;&#39;serviceItems&#39; to update. |  [optional] |
|**title** | **String** | Business name. Use updateMask&#x3D;&#39;title&#39;. |  [optional] |
|**storeCode** | **String** | External store identifier, unique within the account. Use updateMask&#x3D;&#39;storeCode&#39;. |  [optional] |
|**labels** | **List&lt;String&gt;** | Free-form, internal-only labels for grouping (1-255 characters each). Use updateMask&#x3D;&#39;labels&#39;. |  [optional] |
|**storefrontAddress** | [**UpdateGoogleBusinessLocationDetailsRequestStorefrontAddress**](UpdateGoogleBusinessLocationDetailsRequestStorefrontAddress.md) |  |  [optional] |
|**serviceArea** | [**UpdateGoogleBusinessLocationDetailsRequestServiceArea**](UpdateGoogleBusinessLocationDetailsRequestServiceArea.md) |  |  [optional] |
|**openInfo** | [**UpdateGoogleBusinessLocationDetailsRequestOpenInfo**](UpdateGoogleBusinessLocationDetailsRequestOpenInfo.md) |  |  [optional] |
|**moreHours** | [**List&lt;UpdateGoogleBusinessLocationDetailsRequestMoreHoursInner&gt;**](UpdateGoogleBusinessLocationDetailsRequestMoreHoursInner.md) | Additional hours for specific services (delivery, drive-through, etc.). Use updateMask&#x3D;&#39;moreHours&#39;. |  [optional] |
|**latlng** | [**UpdateGoogleBusinessLocationDetailsRequestLatlng**](UpdateGoogleBusinessLocationDetailsRequestLatlng.md) |  |  [optional] |
|**adWordsLocationExtensions** | [**UpdateGoogleBusinessLocationDetailsRequestAdWordsLocationExtensions**](UpdateGoogleBusinessLocationDetailsRequestAdWordsLocationExtensions.md) |  |  [optional] |



