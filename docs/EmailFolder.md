

# EmailFolder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**wellKnown** | [**WellKnownEnum**](#WellKnownEnum) |  |  [optional] |
|**unreadCount** | **Integer** |  |  [optional] |
|**totalCount** | **Integer** |  |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



## Enum: WellKnownEnum

| Name | Value |
|---- | -----|
| INBOX | &quot;inbox&quot; |
| SENT | &quot;sent&quot; |
| DRAFTS | &quot;drafts&quot; |
| TRASH | &quot;trash&quot; |
| SPAM | &quot;spam&quot; |
| ARCHIVE | &quot;archive&quot; |



