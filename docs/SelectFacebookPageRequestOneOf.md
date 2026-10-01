

# SelectFacebookPageRequestOneOf


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile ID from your classic connection flow. |  |
|**pageId** | **String** | The Facebook Page ID selected by the user. Send this or pageIds, not both. |  [optional] |
|**pageIds** | **List&lt;String&gt;** | Several Page IDs to connect from one sign-in, each as its own account. With two or more distinct IDs the response lists &#x60;accounts&#x60; and &#x60;failed&#x60; instead of &#x60;account&#x60;, and the request is refused with 400 while a profile holds one Facebook account and on a reconnect or an ads connect, which pick exactly one Page. A single distinct ID behaves exactly like pageId. |  [optional] |
|**tempToken** | **String** | Temporary Facebook access token from OAuth. |  |
|**userProfile** | [**SelectFacebookPageRequestOneOfUserProfile**](SelectFacebookPageRequestOneOfUserProfile.md) |  |  |
|**redirectUrl** | **URI** | Optional custom redirect URL to return to after selection. |  [optional] |



