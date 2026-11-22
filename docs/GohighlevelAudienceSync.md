

# GohighlevelAudienceSync


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**tag** | **String** | The HighLevel tag, lowercased. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**memberCount** | **Integer** | Contacts with the tag uploaded to the audiences so far. |  |
|**lastError** | **String** |  |  |
|**audiences** | [**List&lt;GohighlevelAudienceSyncAudiencesInner&gt;**](GohighlevelAudienceSyncAudiencesInner.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SYNCING | &quot;syncing&quot; |
| READY | &quot;ready&quot; |
| ERROR | &quot;error&quot; |



