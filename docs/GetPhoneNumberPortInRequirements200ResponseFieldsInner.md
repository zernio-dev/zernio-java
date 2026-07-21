

# GetPhoneNumberPortInRequirements200ResponseFieldsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requirementId** | **String** | Pass back as requirements[].requirementTypeId. |  [optional] |
|**label** | **String** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | text/date take a string value; file takes a documentId from the documents endpoint; address is satisfied automatically from the end-user service address. |  [optional] |
|**description** | **String** |  |  [optional] |
|**example** | **String** |  |  [optional] |
|**acceptableValues** | **List&lt;String&gt;** | When present, the value must be one of these. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| DATE | &quot;date&quot; |
| ADDRESS | &quot;address&quot; |
| FILE | &quot;file&quot; |
| ACTION | &quot;action&quot; |



