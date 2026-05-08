

# ConversionEventUserClickIds

Platform click identifiers captured from the originating ad click.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fbc** | **String** | Meta click ID (from fbclid URL param). |  [optional] |
|**fbp** | **String** | Meta browser ID (_fbp cookie). |  [optional] |
|**gclid** | **String** | Google click ID (from gclid URL param). |  [optional] |
|**gbraid** | **String** | Google iOS 14.5+ app attribution ID. |  [optional] |
|**wbraid** | **String** | Google iOS 14.5+ web-to-app attribution ID. |  [optional] |
|**liFatId** | **String** | LinkedIn first-party ad tracking click ID. Captured by parsing &#x60;li_fat_id&#x60; from landing-page URLs after the advertiser enables enhanced conversion tracking on the LinkedIn Insight Tag. Sent to LinkedIn as the LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID userId. Opaque token, not hashed.  |  [optional] |



