@description('Name of the AI Search service')
param name string

@description('Location for the resource')
param location string

@description('Tags for the resource')
param tags object = {}

resource search 'Microsoft.Search/searchServices@2024-06-01-preview' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: 'basic'
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
    publicNetworkAccess: 'enabled'
    semanticSearch: 'free'
  }
}

output id string = search.id
output name string = search.name
output endpoint string = 'https://${name}.search.windows.net'
