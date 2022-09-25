# python-sfdx
In this repo, you will learn how to connect your salesforce account with your python code using SFDX. Salesforce is a powerful CRM tool that allows businesses to track and manage their customer interactions. However, in order to get the most out of salesforce, it is often necessary to connect it with other software applications. Python is a versatile scripting language that can be used for a wide variety of tasks, including data analysis and automation. By connecting salesforce with python using SFDX, you can easily access and manipulate your salesforce data from within python code. In addition, you can use python to automate various salesforce tasks, such as creating new records or updating existing ones. By taking advantage of the powerful combination of salesforce and python, you can streamline your business processes and improve your bottom line.
## Update sfdx
```
sfdx update
```
## Login to Production or Developer edition org
```
sfdx auth:web:login 
```
## Login to Sandbox Org
```
sfdx force:auth:web:login -r https://test.salesforce.com
```
## Get the Access Token and Instance URL
```
sfdx force:org:display --targetusername <username>
```
