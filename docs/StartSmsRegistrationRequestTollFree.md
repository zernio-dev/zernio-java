

# StartSmsRegistrationRequestTollFree

Required for toll_free.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessName** | **String** |  |  |
|**corporateWebsite** | **URI** |  |  |
|**phoneNumbers** | **List&lt;String&gt;** |  |  |
|**useCase** | **String** |  |  |
|**useCaseSummary** | **String** |  |  |
|**productionMessageContent** | **String** |  |  |
|**optInWorkflow** | **String** | How recipients opt in to your messages. |  |
|**optInWorkflowImageUrls** | **List&lt;URI&gt;** | Screenshot URL(s) showing the opt-in flow (at least one). |  |
|**messageVolume** | [**MessageVolumeEnum**](#MessageVolumeEnum) | Expected monthly message volume tier. |  |
|**additionalInformation** | **String** |  |  |
|**businessAddr1** | **String** |  |  |
|**businessAddr2** | **String** |  |  [optional] |
|**businessCity** | **String** |  |  |
|**businessState** | **String** |  |  |
|**businessZip** | **String** |  |  |
|**businessContactFirstName** | **String** |  |  |
|**businessContactLastName** | **String** |  |  |
|**businessContactEmail** | **String** |  |  |
|**businessContactPhone** | **String** |  |  |
|**businessRegistrationNumber** | **String** |  |  |
|**businessRegistrationType** | **String** | e.g. EIN (US), Companies House (UK), ABN (AU). |  |
|**businessRegistrationCountry** | **String** | ISO 3166-1 alpha-2. |  |



## Enum: MessageVolumeEnum

| Name | Value |
|---- | -----|
| _10 | &quot;10&quot; |
| _100 | &quot;100&quot; |
| _1_000 | &quot;1,000&quot; |
| _10_000 | &quot;10,000&quot; |
| _100_000 | &quot;100,000&quot; |
| _250_000 | &quot;250,000&quot; |
| _500_000 | &quot;500,000&quot; |
| _750_000 | &quot;750,000&quot; |
| _1_000_000 | &quot;1,000,000&quot; |
| _5_000_000 | &quot;5,000,000&quot; |
| _10_000_000_ | &quot;10,000,000+&quot; |



