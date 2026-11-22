

# AudienceUploadUser

One person. Each key is plaintext or its SHA-256 hash (64 hex characters). At least one key is required; see the endpoint description for which keys each platform uses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Email, or SHA-256 of it trimmed and lowercased. |  [optional] |
|**phone** | **String** | Phone with country code. Plaintext matches on Meta and Google; see the endpoint description before sending it hashed. |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**birthYear** | **String** | YYYY. Meta only. |  [optional] |
|**birthMonth** | **String** | MM (01-12). Meta only. |  [optional] |
|**birthDay** | **String** | DD (01-31). Meta only. |  [optional] |
|**gender** | **String** | m or f. Meta only. |  [optional] |
|**city** | **String** | Meta only. |  [optional] |
|**state** | **String** | Meta only. |  [optional] |
|**zip** | **String** |  |  [optional] |
|**country** | **String** | ISO 3166-1 alpha-2 code. |  [optional] |
|**externalId** | **String** | Your own id for the person. Meta only. |  [optional] |
|**region** | **String** | Where the person is (ISO country, or US-CA). With no granted consent, EEA, UK and CH people are dropped before upload. |  [optional] |
|**consent** | [**AudienceUploadUserConsent**](AudienceUploadUserConsent.md) |  |  [optional] |



