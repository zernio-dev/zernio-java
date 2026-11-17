

# HubSpotSettingsSyncIssue

Set while the portal refuses to create contacts because it requires properties Zernio does not fill. People already in HubSpot are still matched and their messages logged. Cleared by the next created contact or a change to `contactDefaults`. The account's health shows it too.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) |  |  |
|**properties** | **List&lt;String&gt;** | The required contact properties HubSpot named. |  |
|**message** | **String** |  |  |
|**at** | **OffsetDateTime** |  |  |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| REQUIRED_CONTACT_PROPERTIES | &quot;REQUIRED_CONTACT_PROPERTIES&quot; |



