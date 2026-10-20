

# ListAdAccountUserInvitations200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** |  |  [optional] |
|**invitations** | [**List&lt;GoogleAdsUserAccessInvitation&gt;**](GoogleAdsUserAccessInvitation.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this data was fetched from Google. Null on a live read. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s quota was exhausted and this is the last successful fetch. |  [optional] |



