

# GohighlevelSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**locationId** | **String** | The GoHighLevel sub-account (location) id. |  |
|**companyId** | **String** | The agency that owns the sub-account, null for a sub-account under no agency. |  |
|**locationName** | **String** |  |  |
|**installedBy** | **String** | The GoHighLevel user who installed the app. |  |
|**relayConversions** | **Boolean** | CRM events are relayed as conversions. Default true. |  |
|**writeBackAttribution** | **Boolean** | Relayed conversions are written back onto the GoHighLevel contact. Default true. |  |
|**reportToAds** | **Boolean** | Relayed conversions are forwarded to the profile&#39;s ad platforms. Default false. |  |
|**syncContacts** | **Boolean** | Inbox contacts are matched to HighLevel contacts by phone, then email, and created there when none matches. Default true. |  |
|**logMessages** | **Boolean** | Inbox messages from every channel (both directions) are logged on the HighLevel contact as one note per channel and day. Default true. |  |
|**logDeliveryStatus** | **Boolean** | Logged outgoing messages show their delivery status (sent, delivered, read, failed) on their note line. Default true. |  |
|**syncAdLeads** | **Boolean** | Leads from the profile&#39;s ad network lead forms become HighLevel contacts, deduplicated by email, then phone. Default true. |  |
|**mirrorConversations** | **Boolean** | Telegram, LINE, WeChat, iMessage and RCS messages go into the contact&#39;s Conversations thread under the Zernio channel (answerable from HighLevel) instead of a note. Default true. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOHIGHLEVEL | &quot;gohighlevel&quot; |



