

# ListConversionDestinations200ResponseDestinationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Destination identifier. Meta: pixel ID. Google: conversion action resource name. LinkedIn: numeric conversion rule ID.  |  [optional] |
|**name** | **String** |  |  [optional] |
|**type** | **String** | Present when the platform locks event type to the destination (Google conversion actions, LinkedIn conversion rules).  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**adAccountId** | **String** | Set by adapters whose destinations are scoped to a specific ad account (LinkedIn). Pass back on subsequent CRUD calls.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



