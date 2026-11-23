

# ConnectWordPressWithApplicationPasswordRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Your Zernio profile ID (get from /v1/profiles). |  |
|**siteUrl** | **URI** | HTTPS base URL of the WordPress installation, including a subdirectory path when applicable. |  |
|**username** | **String** | WordPress login name. A colon is not allowed. |  |
|**applicationPassword** | **String** | Application password created for the WordPress user. Spaces in WordPress display formatting are accepted. |  |
|**reconnectAccountId** | **String** | The WordPress site connection being reconnected. In a workspace with no billing set up, the connect is allowed only when it returns to that same site. |  [optional] |



