

# GetGmbAttributeMetadata200ResponseAttributeMetadataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parent** | **String** | Resource name of the attribute (e.g. \&quot;attributes/has_delivery\&quot;). |  [optional] |
|**valueType** | **String** | Value type (e.g. BOOL, ENUM, URL, REPEATED_ENUM). |  [optional] |
|**displayName** | **String** | Localized human-readable attribute name. |  [optional] |
|**groupDisplayName** | **String** | Display name of the attribute group. |  [optional] |
|**repeatable** | **Boolean** | True if multiple values can be set simultaneously. |  [optional] |
|**deprecated** | **Boolean** | True if this attribute should no longer be used. |  [optional] |
|**valueMetadata** | [**List&lt;GetGmbAttributeMetadata200ResponseAttributeMetadataInnerValueMetadataInner&gt;**](GetGmbAttributeMetadata200ResponseAttributeMetadataInnerValueMetadataInner.md) | Possible enum values (for ENUM / REPEATED_ENUM types). |  [optional] |



