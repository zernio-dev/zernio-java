

# SyncExternalPosts200ResponseSynced


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postsFound** | **Integer** | Posts returned by the platform listing during the on-demand sync |  [optional] |
|**postsSynced** | **Integer** | Stored records this call wrote: new posts and posts whose metadata changed. On LinkedIn personal profiles and the X fallback sync, posts whose metrics were refreshed are counted too. |  [optional] |
|**skipped** | **Boolean** | True when the account was synced within the debounce window and no live fetch ran. |  [optional] |



