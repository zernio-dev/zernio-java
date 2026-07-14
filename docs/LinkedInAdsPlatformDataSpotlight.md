

# LinkedInAdsPlatformDataSpotlight

POST /v1/ads/create only. Dynamic Spotlight Ad personalized with the viewer's profile photo. Supported goals: traffic, awareness. logoUrl and organizationName default to the Company Page's; set them explicitly if LinkedIn rejects the create with a 404. Mutually exclusive with the other creative sources. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headline** | **String** |  |  |
|**description** | **String** | Mutually exclusive with backgroundImageUrl. |  [optional] |
|**callToAction** | **String** | Button label text. |  |
|**landingUrl** | **URI** |  |  |
|**logoUrl** | **URI** |  |  [optional] |
|**organizationName** | **String** |  |  [optional] |
|**showMemberProfilePhoto** | **Boolean** | Defaults to true. |  [optional] |
|**backgroundImageUrl** | **URI** | Custom background. Replaces the description and the profile photo. |  [optional] |



