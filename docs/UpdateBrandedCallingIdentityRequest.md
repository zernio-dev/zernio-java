

# UpdateBrandedCallingIdentityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Shown on the callee&#39;s screen. No emoji. |  [optional] |
|**callReasons** | **List&lt;String&gt;** | 1 to 10 reasons you call, each up to 64 characters. Pick from GET /v1/branded-calling/call-reasons to skip manual vetting. |  [optional] |
|**logoUrl** | **String** | HTTPS URL of a PNG, JPEG, WebP or SVG logo. Zernio converts it to the 256x256 BMP the carriers require and hosts it. |  [optional] |
|**authorizer** | [**CreateBrandedCallingIdentityRequestAuthorizer**](CreateBrandedCallingIdentityRequestAuthorizer.md) |  |  [optional] |
|**references** | [**BrandedCallingReferences**](BrandedCallingReferences.md) |  |  [optional] |
|**reviewAnswers** | [**Map&lt;String, UpdateBrandedCallingIdentityRequestReviewAnswersValue&gt;**](UpdateBrandedCallingIdentityRequestReviewAnswersValue.md) | One entry per point id of the open reviewRequest. A text point takes text; a link point takes url; file and link_or_file points take url set to the URL of a file you uploaded first (POST /v1/media/upload). A point id that is not on the open request is a 422. |  [optional] |
|**reviewNote** | **String** |  |  [optional] |



