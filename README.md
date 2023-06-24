<div><a href='https://github.com/darideveloper/ip-updater-webshare/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/ip-updater-webshare.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/ip-updater-webshare/blob/master/logo.png?raw=true' alt='ip-updater-webshare' height='80px'/>

# ip-updater-webshare

IP updater for web service [webshare.io](https://www.webshare.io/)

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://requests.readthedocs.io/en/latest/' target='_blank'> <img src='https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png' alt='Requests' title='Requests' height='50px'/> </a></div>

# Details

Script for get your current proxy and save it with the proxy provider [webshare.io](https://www.webshare.io/)

## Terminal outputs:

a. Error: Invalid token.
b. Done: IP already authorized.
c. Done: IP authorized.

# Install

## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

# Settings

## Enviroment variables

1. Create and get token from [/proxy2.webshare.io/userapi/keys](https://proxy2.webshare.io/userapi/keys)

2. Save the token in this file **.env** (create if if not exists), like:
  
```bash
WEBSHARE_TOKEN = YOUR_TOKEN
```

# Run

Run the project folder with python: 
```sh
python .
```

Or run the main file:
```sh
python __main__.py
```

## Run in loop

If you want to tun the bot in loop (one or multiple times each day), I suggest you to use tools to run the script all days at specific time, like [Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) for windows, [Cron](https://www.google.com/search?q=linux+cronjobs&oq=linux+cronjobs&aqs=chrome..69i57.3719j0j1&sourceid=chrome&ie=UTF-8) for Linux or [Jenkins](https://www.jenkins.io/) for both systems

# Roadmap

* [X] Get current IP
* [X] Read token from .env
* [X] Submit current IP to webshare

****