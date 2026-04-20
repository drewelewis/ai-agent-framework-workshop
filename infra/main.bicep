targetScope = 'subscription'

@description('Name of the environment (used for resource naming)')
param environmentName string

@description('Primary location for all resources')
param location string

@description('Model deployment name')
param modelDeploymentName string = 'gpt-4o'

@description('Model version')
param modelVersion string = '2024-11-20'

@description('Model SKU capacity (tokens per minute in thousands)')
param modelCapacity int = 30

var abbrs = loadJsonContent('./abbreviations.json')
var resourceToken = toLower(uniqueString(subscription().id, environmentName, location))
var tags = { 'azd-env-name': environmentName }

// Resource Group
resource rg 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-${environmentName}'
  location: location
  tags: tags
}

// AI Services (Azure OpenAI)
module aiServices 'modules/ai-services.bicep' = {
  name: 'ai-services'
  scope: rg
  params: {
    name: '${abbrs.cognitiveServicesAccounts}${resourceToken}'
    location: location
    tags: tags
    modelDeploymentName: modelDeploymentName
    modelVersion: modelVersion
    modelCapacity: modelCapacity
  }
}

// AI Foundry Hub + Project
module aiFoundry 'modules/ai-foundry.bicep' = {
  name: 'ai-foundry'
  scope: rg
  params: {
    hubName: '${abbrs.aiFoundryHub}${resourceToken}'
    projectName: '${abbrs.aiFoundryProject}${resourceToken}'
    location: location
    tags: tags
    aiServicesId: aiServices.outputs.id
    aiServicesTarget: aiServices.outputs.endpoint
  }
}

// Azure AI Search (for RAG knowledge index)
module search 'modules/ai-search.bicep' = {
  name: 'ai-search'
  scope: rg
  params: {
    name: '${abbrs.searchSearchServices}${resourceToken}'
    location: location
    tags: tags
  }
}

// Azure Container Registry (for agent container images)
module acr 'modules/container-registry.bicep' = {
  name: 'container-registry'
  scope: rg
  params: {
    name: '${abbrs.containerRegistryRegistries}${resourceToken}'
    location: location
    tags: tags
  }
}

// Application Insights (for monitoring)
module monitoring 'modules/monitoring.bicep' = {
  name: 'monitoring'
  scope: rg
  params: {
    logAnalyticsName: '${abbrs.operationalInsightsWorkspaces}${resourceToken}'
    applicationInsightsName: '${abbrs.insightsComponents}${resourceToken}'
    location: location
    tags: tags
  }
}

// Outputs for azd and .env configuration
output AZURE_RESOURCE_GROUP string = rg.name
output AZURE_AI_SERVICES_ENDPOINT string = aiServices.outputs.endpoint
output AZURE_AI_SERVICES_NAME string = aiServices.outputs.name
output AZURE_AI_FOUNDRY_HUB_NAME string = aiFoundry.outputs.hubName
output AZURE_AI_FOUNDRY_PROJECT_NAME string = aiFoundry.outputs.projectName
output AZURE_AI_SEARCH_ENDPOINT string = search.outputs.endpoint
output AZURE_AI_SEARCH_NAME string = search.outputs.name
output AZURE_CONTAINER_REGISTRY_ENDPOINT string = acr.outputs.loginServer
output AZURE_CONTAINER_REGISTRY_NAME string = acr.outputs.name
output APPLICATIONINSIGHTS_CONNECTION_STRING string = monitoring.outputs.applicationInsightsConnectionString
output MODEL_DEPLOYMENT_NAME string = modelDeploymentName
