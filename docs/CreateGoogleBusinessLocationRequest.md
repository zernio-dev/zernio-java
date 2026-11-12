

# CreateGoogleBusinessLocationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | Business name as shown on Google. |  |
|**languageCode** | **String** | BCP-47 language of the listing (e.g. \&quot;es\&quot;). Immutable after creation. |  |
|**primaryCategory** | **String** | Category name from GET gmb-categories (e.g. \&quot;categories/gcid:cafe\&quot;). A bare \&quot;gcid:cafe\&quot; is also accepted. |  |
|**additionalCategories** | **List&lt;String&gt;** | Further category names, same format as primaryCategory. |  [optional] |
|**storefrontAddress** | [**CreateGoogleBusinessLocationRequestStorefrontAddress**](CreateGoogleBusinessLocationRequestStorefrontAddress.md) |  |  [optional] |
|**serviceArea** | [**CreateGoogleBusinessLocationRequestServiceArea**](CreateGoogleBusinessLocationRequestServiceArea.md) |  |  [optional] |
|**phone** | **String** | Primary phone number. Required when storefrontAddress is absent and websiteUri is not set. |  [optional] |
|**websiteUri** | **String** | Website URL. Required when storefrontAddress is absent and phone is not set. |  [optional] |
|**description** | **String** | Business description (Google profile.description). |  [optional] |
|**regularHours** | **Map&lt;String, Object&gt;** | Google &#x60;regularHours&#x60; object (periods with openDay, openTime, closeDay, closeTime). |  [optional] |
|**validateOnly** | **Boolean** | Validate with Google without creating the listing or attaching anything. |  [optional] |



