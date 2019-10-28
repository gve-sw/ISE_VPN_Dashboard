
This demo utilizes ISE API to create a customized dashboard that non-technical staff members can navigate.  The dashboard allows IT staff to add users to ISE and assign designated tag group, view all ISE users and status, and edit the status of the users.  For this specific use case, new users are added to the VPN default ISE group and enabling/disabling of users equates to allowing or disallowing VPN access of resources to specific users.

The config.py file contains necessary variables used by the script and needs addressing for demo.  The iseIP variable is the IP address for the desired ISE appliance and the identityGroupId variable is the desired default ISE group that new users will be assigned to.  The USER_PASS variable identifies the authorized user making this request (defined per RFC 2617)

——------ Running Code ------——
1. Make sure Python is installed
2. Make sure pip is installed (https://pip.pypa.io/en/stable/installing/ for more information on pip)
3. Enter 'pip install -r requirements.txt' into command line to download necessary libraries
4. Ensure all elements of the config.py file are completed
5. In command line enter 'python iseApp.py' and navigate to shown URL address
