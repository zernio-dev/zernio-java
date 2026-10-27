

# AdLeadConsent

One custom disclaimer checkbox on a Meta lead form (for example a TCPA call or SMS consent), as Meta returns it in custom_disclaimer_responses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkboxKey** | **String** | The checkbox key as Meta returns it: the one set in platformSpecificData.customDisclaimer.checkboxes[].key on POST /v1/ads/lead-forms, or otherwise a key Meta derives from the checkbox text, which can be long and contain spaces and punctuation. |  |
|**isChecked** | **Boolean** |  |  |



