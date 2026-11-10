

# AutocompleteContacts200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**emails** | **List&lt;String&gt;** |  |  [optional] |
|**phones** | **List&lt;String&gt;** | E.164 numbers only. |  [optional] |
|**company** | **String** |  |  [optional] |
|**jobTitle** | **String** |  |  [optional] |
|**photoUrl** | **String** |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | contacts &#x3D; saved contacts, other &#x3D; people the user mailed, directory &#x3D; the organization. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| CONTACTS | &quot;contacts&quot; |
| OTHER | &quot;other&quot; |
| DIRECTORY | &quot;directory&quot; |



