@description('Name of the AI Foundry Hub')
param hubName string

@description('Name of the AI Foundry Project')
param projectName string

@description('Location for the resources')
param location string

@description('Tags for the resources')
param tags object = {}

@description('Resource ID of the AI Services account')
param aiServicesId string

@description('Endpoint of the AI Services account')
param aiServicesTarget string

resource hub 'Microsoft.MachineLearningServices/workspaces@2024-10-01' = {
  name: hubName
  location: location
  tags: tags
  kind: 'Hub'
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: hubName
    publicNetworkAccess: 'Enabled'
  }
}

resource aiServicesConnection 'Microsoft.MachineLearningServices/workspaces/connections@2024-10-01' = {
  parent: hub
  name: 'ai-services-connection'
  properties: {
    category: 'AIServices'
    target: aiServicesTarget
    authType: 'AAD'
    metadata: {
      ApiType: 'Azure'
      ResourceId: aiServicesId
    }
  }
}

resource project 'Microsoft.MachineLearningServices/workspaces@2024-10-01' = {
  name: projectName
  location: location
  tags: tags
  kind: 'Project'
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: projectName
    hubResourceId: hub.id
    publicNetworkAccess: 'Enabled'
  }
}

output hubName string = hub.name
output projectName string = project.name
output hubId string = hub.id
output projectId string = project.id
