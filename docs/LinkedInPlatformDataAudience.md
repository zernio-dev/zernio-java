

# LinkedInPlatformDataAudience

Organization pages only. Audience targeting for the post (Ads Manager's \"Targeted audience\"), sent as LinkedIn's distribution.targetEntities: OR inside a facet, AND across facets. LinkedIn rejects the post when the targeted audience is under 300 members, and Zernio rejects it on a personal profile. URN facets accept a full urn:li:<type>:<id> or the bare numeric id; find ids with GET /v1/ads/targeting/search?platform=linkedin (types country, region, industry, jobFunction, seniority, companySize).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countries** | **List&lt;String&gt;** | ISO 3166-1 alpha-2 codes with a built-in LinkedIn geo URN (same list as geoRestriction.countries, merged with it). Other countries and sub-country regions go in geoLocations. |  [optional] |
|**geoLocations** | **List&lt;String&gt;** | LinkedIn geo URNs or ids (urn:li:geo:103644278 or 103644278): countries, states, regions, cities. |  [optional] |
|**interfaceLocales** | [**List&lt;LinkedInPlatformDataAudienceInterfaceLocalesInner&gt;**](LinkedInPlatformDataAudienceInterfaceLocalesInner.md) | Members&#39; LinkedIn interface locale, e.g. { language: es, country: ES }. |  [optional] |
|**industries** | **List&lt;String&gt;** | urn:li:industry:&lt;id&gt; or id. |  [optional] |
|**jobFunctions** | **List&lt;String&gt;** | urn:li:function:&lt;id&gt; or id. |  [optional] |
|**seniorities** | **List&lt;String&gt;** | urn:li:seniority:&lt;id&gt; or id. |  [optional] |
|**staffCountRanges** | [**List&lt;StaffCountRangesEnum&gt;**](#List&lt;StaffCountRangesEnum&gt;) | Company size of the member&#39;s current employer. |  [optional] |
|**degrees** | **List&lt;String&gt;** | urn:li:degree:&lt;id&gt; or id (LinkedIn standardized degrees). |  [optional] |
|**fieldsOfStudy** | **List&lt;String&gt;** | urn:li:fieldOfStudy:&lt;id&gt; or id (LinkedIn standardized fields of study). |  [optional] |
|**organizations** | **List&lt;String&gt;** | Schools, as urn:li:organization:&lt;id&gt; or id (LinkedIn&#39;s Organization Lookup). |  [optional] |



## Enum: List&lt;StaffCountRangesEnum&gt;

| Name | Value |
|---- | -----|
| SIZE_1 | &quot;SIZE_1&quot; |
| SIZE_2_TO_10 | &quot;SIZE_2_TO_10&quot; |
| SIZE_11_TO_50 | &quot;SIZE_11_TO_50&quot; |
| SIZE_51_TO_200 | &quot;SIZE_51_TO_200&quot; |
| SIZE_201_TO_500 | &quot;SIZE_201_TO_500&quot; |
| SIZE_501_TO_1000 | &quot;SIZE_501_TO_1000&quot; |
| SIZE_1001_TO_5000 | &quot;SIZE_1001_TO_5000&quot; |
| SIZE_5001_TO_10000 | &quot;SIZE_5001_TO_10000&quot; |
| SIZE_10001_OR_MORE | &quot;SIZE_10001_OR_MORE&quot; |



