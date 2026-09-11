

# MetaLeadForm

A Meta Lead Gen form as Graph returns it, in Meta's own snake_case. Read through GET /v1/ads/lead-forms/{formId}. Every setting POST /v1/ads/lead-forms writes is present here, so a form can be diffed against what was created and drift from edits made in Meta's form builder is detectable. A compound field is omitted entirely when the form has no value for it, and `fields` narrows the selection. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | **String** | One of ACTIVE, ARCHIVED, DELETED or DRAFT. |  [optional] |
|**locale** | **String** |  |  [optional] |
|**createdTime** | **OffsetDateTime** |  |  [optional] |
|**pageId** | **String** | Owning Facebook Page. A form on any other Page is a 404, whether read or archived. |  [optional] |
|**leadsCount** | **Integer** |  |  [optional] |
|**organicLeadsCount** | **Integer** |  |  [optional] |
|**expiredLeadsCount** | **Integer** | Leads Meta has aged out of the retention window. |  [optional] |
|**privacyPolicyUrl** | **URI** |  |  [optional] |
|**followUpActionUrl** | **URI** |  |  [optional] |
|**followUpActionText** | **String** |  |  [optional] |
|**questionPageCustomHeadline** | **String** |  |  [optional] |
|**isOptimizedForQuality** | **Boolean** |  |  [optional] |
|**blockDisplayForNonTargetedViewer** | **Boolean** |  |  [optional] |
|**allowOrganicLead** | **Boolean** | Whether the form can also be submitted from an organic Page post. |  [optional] |
|**trackingParameters** | [**List&lt;BoostPostRequestTrackingUrlTagsInner&gt;**](BoostPostRequestTrackingUrlTagsInner.md) | Custom key/value pairs attached to every lead of this form. |  [optional] |
|**legalContent** | [**MetaLeadFormLegalContent**](MetaLeadFormLegalContent.md) |  |  [optional] |
|**contextCard** | [**MetaLeadFormContextCard**](MetaLeadFormContextCard.md) |  |  [optional] |
|**thankYouPage** | [**MetaLeadFormThankYouPage**](MetaLeadFormThankYouPage.md) |  |  [optional] |
|**questions** | [**List&lt;MetaLeadFormQuestionsInner&gt;**](MetaLeadFormQuestionsInner.md) |  |  [optional] |



