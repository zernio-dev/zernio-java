

# DiscordRole

A Discord guild role, returned verbatim from Discord's API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Role snowflake ID |  [optional] |
|**name** | **String** |  |  [optional] |
|**color** | **Integer** | Decimal color (0 &#x3D; no color). Convert to hex via .toString(16). |  [optional] |
|**position** | **Integer** | Position in role hierarchy (higher &#x3D; more authority) |  [optional] |
|**permissions** | **String** | Permissions bitfield as a stringified integer |  [optional] |
|**managed** | **Boolean** | True for integration-managed roles (bot roles) |  [optional] |
|**mentionable** | **Boolean** |  |  [optional] |
|**hoist** | **Boolean** | True if role is displayed separately in member list |  [optional] |



