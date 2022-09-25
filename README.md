# python-sfdx
## Update sfdx
sfdx update
## Login to Production or Developer edition org
sfdx auth:web:login 
## Login to Sandbox Org
sfdx force:auth:web:login -r https://test.salesforce.com
## Get the Access Token and Instance URL
sfdx force:org:display --targetusername <username>
