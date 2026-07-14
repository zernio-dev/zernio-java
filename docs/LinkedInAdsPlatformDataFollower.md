

# LinkedInAdsPlatformDataFollower

POST /v1/ads/create only. Dynamic Follower Ad promoting the Company Page. Supported goals: engagement, awareness. headline and description take exactly one of preApproved or custom. Mutually exclusive with the other creative sources. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headline** | [**LinkedInAdsPlatformDataFollowerHeadline**](LinkedInAdsPlatformDataFollowerHeadline.md) |  |  |
|**description** | [**LinkedInAdsPlatformDataFollowerDescription**](LinkedInAdsPlatformDataFollowerDescription.md) |  |  |
|**callToAction** | [**CallToActionEnum**](#CallToActionEnum) |  |  |
|**logoUrl** | **URI** |  |  [optional] |
|**organizationName** | **String** |  |  [optional] |
|**showMemberProfilePhoto** | **Boolean** | Defaults to true. |  [optional] |



## Enum: CallToActionEnum

| Name | Value |
|---- | -----|
| VISIT_ORGANIZATION_COMPANY_PAGE | &quot;VISIT_ORGANIZATION_COMPANY_PAGE&quot; |
| VISIT_ORGANIZATION_LIFE_PAGE | &quot;VISIT_ORGANIZATION_LIFE_PAGE&quot; |
| VISIT_ORGANIZATION_JOBS_PAGE | &quot;VISIT_ORGANIZATION_JOBS_PAGE&quot; |
| VISIT_ORGANIZATION_CAREERS_PAGE | &quot;VISIT_ORGANIZATION_CAREERS_PAGE&quot; |



