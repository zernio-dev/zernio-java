

# AutomationStepOneOf10

Tags the object's name: `add` puts text at the start (or the end), `remove` takes every copy of it out. Send one of them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**add** | **String** |  |  [optional] |
|**remove** | **String** |  |  [optional] |
|**at** | [**AtEnum**](#AtEnum) |  |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| EDIT_NAME | &quot;edit_name&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_EDIT_NAME | &quot;ads.edit_name&quot; |



## Enum: AtEnum

| Name | Value |
|---- | -----|
| START | &quot;start&quot; |
| END | &quot;end&quot; |



