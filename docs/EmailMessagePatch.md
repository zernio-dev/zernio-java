

# EmailMessagePatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**unread** | **Boolean** |  |  [optional] |
|**starred** | **Boolean** |  |  [optional] |
|**folder** | **String** | Well-known folder name or folder id to move into. |  [optional] |
|**addLabels** | **List&lt;String&gt;** | Labels to add, by id or name (case-insensitive). The message stays where it is. On Outlook these are category names; a name not yet in the mailbox is created on the message. |  [optional] |
|**removeLabels** | **List&lt;String&gt;** | Labels to remove, by id or name. A label cannot be both added and removed in one request. |  [optional] |



