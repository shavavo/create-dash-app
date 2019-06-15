# Create Dash App
create-dash-app creates a dash development environment, which includes scripts to deploy to a docker container via SSH. 

# Setup
1. Clone create-dash-app
2. cd create-dash-app
3. python create-dash-app.py
4. Follow prompts

create-dash-app will create two directories, DEV and DEPLOY. The DEPLOY folder's purpose is to make it easier to see what is getting deployed without SSH. Use sync_ignore.txt to ignore files that aren't meant for the deployment environment (credentials, test files, etc.)

# sync.sh
Inside the DEV folder is a script that syncs the DEV to the DEPLOY folder, then uses SSH to deploy the application. The script will ask for SSH credentials twice, which can be resolved by setting up a SSH key.

Run "bash sync.sh" to deploy changes.

# App Credentials 
Change username and password in appCredentials.py


