import requests
import json
from config import iseIP, identityGroupId

ip = iseIP + ":9060"

# create new users in ISE with given credentials
def createNewUser(name,password,enable,description):
    print(name+' - '+password+' - '+enable+' - '+description)
    url = "https://"+ip+"/ers/config/internaluser"
    payload = "        {\r\n    \"InternalUser\": {\r\n    \"name\": \""+name+"\",\r\n    \"password\" : \""+password+"\",\r\n    \"enabled\" : \""+enable+"\",\r\n    \"changePassword\" : \"false\",\r\n    \"identityGroups\" : \""+identityGroupId+"\",\r\n    \"description\" : \""+description+"\"\r\n    }\r\n    }\r\n    \r\n    \r\n    "
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "Basic "+USER_PASS,
        'Host': ip,
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "281",
        'Connection': "keep-alive",
        }
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    print(response)
    print(response.text)
    return response

# returns list of internal users in ISE
def getUsers():
    url = "https://"+ip+"/ers/config/internaluser"
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "Basic "+USER_PASS,
        'Host': ip,
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        }
    response = requests.request("GET", url, headers=headers,verify=False)
    return response


# modify user to enable/disable in ISE
def modifyUser(user,idvar,enable):
    print(user+" "+enable+" "+idvar)
    url = "https://"+ip+"/ers/config/internaluser/"+idvar
    payload = "    {\r\n    \"InternalUser\": {\r\n    \"name\": \""+user+"\",\r\n    \"id\":\""+idvar+"\",\r\n    \"enabled\" : \""+enable+"\"\r\n    }\r\n    }\r\n    "
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'ERS-Media-Type': "identity.internaluser.1.2",
        'Authorization': "Basic "+USER_PASS,
        'Host': ip,
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "150",
        'Connection': "keep-alive",
        }
    response = requests.request("PUT", url, data=payload, headers=headers, verify=False)
    print(response.text)
    return response

# return a single user to get more information
def getSingleUser(idvar):
    url = "https://"+ip+"/ers/config/internaluser/"+idvar
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "Basic "+USER_PASS,
        'Host': ip,
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        }
    response = requests.request("GET", url, headers=headers, verify=False)
    print(response.text)
    return response
