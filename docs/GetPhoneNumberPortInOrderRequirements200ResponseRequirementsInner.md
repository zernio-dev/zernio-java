

# GetPhoneNumberPortInOrderRequirements200ResponseRequirementsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requirementId** | **String** |  |  [optional] |
|**label** | **String** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**example** | **String** |  |  [optional] |
|**acceptableValues** | **List&lt;String&gt;** |  |  [optional] |
|**status** | **String** | requirement-info-pending | requirement-info-under-review | requirement-info-exception | approved |  [optional] |
|**filled** | **Boolean** |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| DATE | &quot;date&quot; |
| ADDRESS | &quot;address&quot; |
| FILE | &quot;file&quot; |
| ACTION | &quot;action&quot; |



