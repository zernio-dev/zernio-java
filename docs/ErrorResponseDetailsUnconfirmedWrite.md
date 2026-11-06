

# ErrorResponseDetailsUnconfirmedWrite

Meta ad create failures only, when Meta answered a create with a 5xx or a non-JSON body, or dropped the connection after the request was sent, and reading the parent back by name did not settle it: several objects of the same name, a parent that could not be read, or (after a dropped connection, a non-JSON body, or a 5xx with `retryOnServerError: false`) no such object. Zernio did not retry it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**parentId** | **String** | Where to look for it: the ad set for an ad, the campaign for an ad set, the ad account otherwise. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |
| CREATIVE | &quot;creative&quot; |
| AD | &quot;ad&quot; |



