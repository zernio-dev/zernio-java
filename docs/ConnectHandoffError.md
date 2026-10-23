

# ConnectHandoffError

Set when `status` is `failed`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The &#x60;error&#x60; code the flow ended on, as on a redirect_url. &#x60;connect_incomplete&#x60; when the phone reported no outcome, &#x60;connect_unverified&#x60; when it reported an account Zernio could not match to this connect. |  [optional] |
|**message** | **String** |  |  [optional] |
|**details** | **Map&lt;String, String&gt;** | The other params the redirect flow appends for that error, such as &#x60;is_user_fixable&#x60;, &#x60;reason&#x60;, &#x60;dashboard_url&#x60;, &#x60;request_id&#x60; and &#x60;stage&#x60;. All optional. |  [optional] |



