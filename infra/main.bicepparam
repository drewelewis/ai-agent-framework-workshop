using './main.bicep'

param environmentName = readEnvironmentVariable('AZURE_ENV_NAME', 'contoso-travel')
param location = readEnvironmentVariable('AZURE_LOCATION', 'eastus2')
param modelDeploymentName = readEnvironmentVariable('MODEL_DEPLOYMENT_NAME', 'gpt-4o')
