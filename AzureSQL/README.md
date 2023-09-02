# Introduction 
Sample code to connect to a Azure SQL database using different credentials. 

# Getting Started
Credentials types demoed:
1.	Azure CLI
2.	Service Principal
3.	SQL User

# Build and Test
Change the .env.example file and change to .env

Alter the .env file for the following values:
- Azure SQL Server Name (FQDN)
- Database Name

For Azure CLI credentials:
- No other changes (use 'az login' at command prompt)

For Service Principal credentials:
- Tenant Id
- Client Id
- Client Secret

For SQL login credentials:
- User Name
- Password
