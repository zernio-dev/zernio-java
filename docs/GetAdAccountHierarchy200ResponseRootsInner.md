

# GetAdAccountHierarchy200ResponseRootsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** | Native Google Ads customer id, digits only. |  [optional] |
|**name** | **String** |  |  [optional] |
|**currency** | **String** | ISO 4217 code. |  [optional] |
|**timeZone** | **String** | IANA time zone, e.g. Europe/Madrid. |  [optional] |
|**manager** | **Boolean** | True for a manager (MCC) account. |  [optional] |
|**testAccount** | **Boolean** |  |  [optional] |
|**status** | **String** | Google customer status: ENABLED, CANCELED, SUSPENDED or CLOSED. |  [optional] |
|**managerLinks** | [**List&lt;GetAdAccountHierarchy200ResponseRootsInnerManagerLinksInner&gt;**](GetAdAccountHierarchy200ResponseRootsInnerManagerLinksInner.md) | Managers linked to this account, ACTIVE or PENDING. |  [optional] |
|**clients** | [**List&lt;GoogleAdsHierarchyClient&gt;**](GoogleAdsHierarchyClient.md) | Every account under this root at any depth, in Google&#39;s order, followed by pending invitations. |  [optional] |



