

# BusinessAgentStatus

Where the merchant is in the Meta Business Agent setup for this number.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eligible** | **Boolean** | Whether the number can run the agent; null when the terms are not accepted yet (Meta refuses the check). |  |
|**termsAccepted** | **Boolean** | False when Meta rejects calls because the merchant has not accepted the terms in WhatsApp Manager. |  |
|**onboarded** | **Boolean** | An agent exists on the number (onboard was called). |  |
|**enabled** | **Boolean** | The agent answers live conversations. |  |
|**agentId** | **String** |  |  |
|**settings** | [**BusinessAgentSettings**](BusinessAgentSettings.md) |  |  |
|**manualSteps** | [**List&lt;BusinessAgentStatusManualStepsInner&gt;**](BusinessAgentStatusManualStepsInner.md) | Steps Meta keeps outside the API that Zernio can verify are still pending. |  |
|**unverifiedSteps** | [**List&lt;BusinessAgentStatusUnverifiedStepsInner&gt;**](BusinessAgentStatusUnverifiedStepsInner.md) | Steps Meta keeps outside the API and exposes no state for, listed once an agent exists. Informational: Zernio cannot tell whether the merchant already did them. |  |



