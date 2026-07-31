

# BulkCreateContactsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**accountId** | **String** | Required when contacts carry channel data (platformIdentifier or a row-level accountId). Omit for a plain CRM import with no channels. |  [optional] |
|**platform** | **String** | Ignored when accountId is set: the platform is derived from the resolved account. Only relevant to disambiguate accountId lookup; a mismatch 404s. |  [optional] |
|**contacts** | [**List&lt;BulkCreateContactsRequestContactsInner&gt;**](BulkCreateContactsRequestContactsInner.md) |  |  |



