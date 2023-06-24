import os
from dotenv import load_dotenv
import requests

load_dotenv ()
WEBSHARE_TOKEN = os.getenv ("WEBSHARE_TOKEN")

def main (): 
    
    # get current ip
    res = requests.get ("https://api.ipify.org?format=json")
    if res.status_code != 200:
        print ("Error getting ip: API request unsuccessful.")
        quit ()
    json_response = res.json ()
    ip = json_response["ip"]
    
    # Update ip
    res = requests.post (
        "https://proxy.webshare.io/api/v2/proxy/ipauthorization/", 
        json={"ip_address": ip},
        headers={"Authorization": f"Token {WEBSHARE_TOKEN}"}
    )
    
    # Catch invalid token
    if res.status_code == 401:
        print ("Error: Invalid token.\n")
    
    # Catch ip already authorized
    if res.status_code == 400:
        print ("Done: IP already authorized.\n")
        quit ()
        
    # Ok response
    if res.status_code == 201:
        print ("Done: IP authorized.")
        quit () 
    
    # Catch error details
    print ("Error: API request unsuccessful.")
    print (f"Status code: {res.status_code}")
    print (f"Response: {res.text}")
    


if __name__ == "__main__":
    main()