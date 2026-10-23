

# GetLinkedInMentions200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**urn** | **String** | The LinkedIn URN (person or organization) |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of entity (person or organization) |  [optional] |
|**displayName** | **String** | Display name (provided, from API, or derived from vanity URL) |  [optional] |
|**mentionFormat** | **String** | Ready-to-use mention format for post content |  [optional] |
|**vanityName** | **String** | The vanity name/slug (only for organization mentions) |  [optional] |
|**warning** | **String** | Only present for person mentions when displayName was not provided and the real name could not be resolved from LinkedIn |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PERSON | &quot;person&quot; |
| ORGANIZATION | &quot;organization&quot; |



