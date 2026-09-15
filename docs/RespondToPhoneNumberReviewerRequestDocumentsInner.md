

# RespondToPhoneNumberReviewerRequestDocumentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requirementId** | **String** |  |  |
|**filename** | **String** |  |  [optional] |
|**base64** | **String** | Base64-encoded file bytes (or supply documentId instead). |  [optional] |
|**documentId** | **String** | Id of a document already uploaded out-of-band. |  [optional] |
|**issuedAt** | **LocalDate** | Date printed on the document (YYYY-MM-DD), for slots the regulator windows such as proof of address. The pre-submit review trusts it over its own read of the PDF. |  [optional] |



