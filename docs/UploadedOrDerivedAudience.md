

# UploadedOrDerivedAudience

customer_list, website, or lookalike audience (uploaded or derived from a source).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**adAccountId** | **String** | Platform ad account ID. Must start with act_ for Meta; bare platform id for others (Google customer id, X/TikTok/LinkedIn/Pinterest account id). |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**matchRules** | [**List&lt;UploadedOrDerivedAudienceMatchRulesInner&gt;**](UploadedOrDerivedAudienceMatchRulesInner.md) | Required for website_retargeting audiences (LinkedIn only). Each rule is a URL pattern; a member who visits any matching page enters the segment. Needs the LinkedIn Insight Tag installed on the customer&#39;s site — the segment only starts filling once the tag reports visits.  The response&#39;s &#x60;platformAudienceId&#x60; is the LinkedIn adSegment id, valid for downstream use. These segments appear in GET /v1/ads/audiences with  &#x60;type: website_retargeting&#x60; once LinkedIn has finished building them.  |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Required for engagement audiences (LinkedIn only): what members engaged with — a video/leadgen/single-image ad campaign, a Company Page or an Event page.  |  [optional] |
|**trigger** | **String** | Required for engagement audiences. The action, validated by LinkedIn against &#x60;sourceType&#x60;. Common values: VIDEO_ADS FIRST_QUARTILE / MIDPOINT / THIRD_QUARTILE / FULL_COMPLETE; LEAD_GEN_FORMS VIEW_FORM / LEAD_FORM_SUBMIT; ORGANIZATION_PAGES VIEW / CTA_CLICK; EVENT_PAGES RSVPED / VIDEO_VIEWED / ENGAGEMENT / CLICK.  |  [optional] |
|**lookbackDays** | [**LookbackDaysEnum**](#LookbackDaysEnum) | Required for engagement audiences. Rolling window. |  [optional] |
|**engagementSources** | **List&lt;String&gt;** | Required for engagement audiences. Campaign URNs for the ad source types, organization URNs for pages and events. LinkedIn creates one rule per source, all sharing the same trigger and lookbackDays.  |  [optional] |
|**companies** | [**List&lt;UploadedOrDerivedAudienceCompaniesInner&gt;**](UploadedOrDerivedAudienceCompaniesInner.md) | Required for company_list audiences (LinkedIn only): plain-text company rows for account targeting. Each row needs at least one identifier. LinkedIn recommends 1,000+ companies for a usable match rate and takes up to 48h to process the list.  |  [optional] |
|**pixelId** | **String** | Required for website audiences |  [optional] |
|**retentionDays** | **Integer** | Required for website audiences |  [optional] |
|**sourceAudienceId** | **String** | Required for lookalike audiences |  [optional] |
|**country** | **String** | 2-letter code, required for lookalike audiences |  [optional] |
|**ratio** | **BigDecimal** | Required for lookalike audiences |  [optional] |
|**rule** | **Object** | Pixel event rule for website audiences (optional) |  [optional] |
|**customerFileSource** | **String** | Data source declaration for GDPR compliance (customer_list only) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_LIST | &quot;customer_list&quot; |
| COMPANY_LIST | &quot;company_list&quot; |
| ENGAGEMENT | &quot;engagement&quot; |
| WEBSITE | &quot;website&quot; |
| WEBSITE_RETARGETING | &quot;website_retargeting&quot; |
| LOOKALIKE | &quot;lookalike&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| VIDEO_ADS | &quot;VIDEO_ADS&quot; |
| LEAD_GEN_FORMS | &quot;LEAD_GEN_FORMS&quot; |
| ORGANIZATION_PAGES | &quot;ORGANIZATION_PAGES&quot; |
| EVENT_PAGES | &quot;EVENT_PAGES&quot; |
| SINGLE_IMAGE_ADS | &quot;SINGLE_IMAGE_ADS&quot; |



## Enum: LookbackDaysEnum

| Name | Value |
|---- | -----|
| NUMBER_30 | 30 |
| NUMBER_60 | 60 |
| NUMBER_90 | 90 |
| NUMBER_180 | 180 |
| NUMBER_365 | 365 |



