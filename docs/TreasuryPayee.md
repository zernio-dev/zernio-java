

# TreasuryPayee


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**payeeType** | [**PayeeTypeEnum**](#PayeeTypeEnum) |  |  [optional] |
|**payeeRef** | **String** |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**onboardingStatus** | [**OnboardingStatusEnum**](#OnboardingStatusEnum) |  |  [optional] |
|**detailsSubmitted** | **Boolean** |  |  [optional] |
|**payoutsEnabled** | **Boolean** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PayeeTypeEnum

| Name | Value |
|---- | -----|
| CREATOR | &quot;creator&quot; |
| AD_ACCOUNT | &quot;ad_account&quot; |



## Enum: OnboardingStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COMPLETE | &quot;complete&quot; |
| RESTRICTED | &quot;restricted&quot; |



