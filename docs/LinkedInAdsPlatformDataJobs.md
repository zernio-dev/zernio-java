

# LinkedInAdsPlatformDataJobs

POST /v1/ads/create only. Dynamic Jobs Ad promoting your open roles, personalized with the viewer's profile photo. Requires goal job_applicants and a Company Page with active job postings. headline and buttonLabel take exactly one of preApproved or custom. logoUrl and organizationName default to the Company Page's. Mutually exclusive with the other creative sources. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headline** | [**LinkedInAdsPlatformDataJobsHeadline**](LinkedInAdsPlatformDataJobsHeadline.md) |  |  |
|**buttonLabel** | [**LinkedInAdsPlatformDataJobsButtonLabel**](LinkedInAdsPlatformDataJobsButtonLabel.md) |  |  |
|**logoUrl** | **URI** |  |  [optional] |
|**organizationName** | **String** |  |  [optional] |
|**showMemberProfilePhoto** | **Boolean** | Defaults to true. |  [optional] |



