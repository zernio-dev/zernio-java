

# ChangeCommerceProductState200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  [optional] |
|**succeeded** | **List&lt;String&gt;** |  |  [optional] |
|**failed** | [**List&lt;ChangeCommerceProductState200ResponseFailedInner&gt;**](ChangeCommerceProductState200ResponseFailedInner.md) |  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACTIVATE | &quot;activate&quot; |
| DEACTIVATE | &quot;deactivate&quot; |
| ARCHIVE | &quot;archive&quot; |
| DELETE | &quot;delete&quot; |



