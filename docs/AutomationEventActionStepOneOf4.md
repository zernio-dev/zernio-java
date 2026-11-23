

# AutomationEventActionStepOneOf4

Adds a tag to the person's contact, or removes it. Skipped when the person is not a contact yet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**action** | [**ActionEnum**](#ActionEnum) |  |  |
|**tag** | **String** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CONTACTS_TAG | &quot;contacts.tag&quot; |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ADD | &quot;add&quot; |
| REMOVE | &quot;remove&quot; |



