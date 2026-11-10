

# ListContactGroups200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Google contactGroups/{id}; Outlook folder:{folderId} (folder:default for the default Contacts folder) or category:{name}. |  [optional] |
|**name** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**system** | **Boolean** | A group the provider defines, such as Google starred or the default Outlook Contacts folder. |  [optional] |
|**memberCount** | **Integer** | Members as Google counts them. Null for Outlook. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |
| FOLDER | &quot;folder&quot; |
| CATEGORY | &quot;category&quot; |



