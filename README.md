# Google_Bard-AI-chat
A simple Python code for sending and receiving data to Google_Bard AI MLL machine

for access to Google_Bard for now you should have proxy from United_state and you should access the site from this country.(use proxy or VPN for this issue).
till the Google expand it's countries to other( not Iran probabely because of the sanctions).

Step 1:

for Accessing the site you need something named __Secure-1PSID that this value as an API KEY for convenience, it is not an officially provided API KEY.
for getting this code.
do this steps:

Authentication
1-Visit https://bard.google.com/
2-F12 for console
3-Session: Application → Cookies → Copy the value of __Secure-1PSID cookie.

Step 2:

We are using the package named bardapi from this repo(https://github.com/dsdanielpark/Bard-API)
for installing this package first do this steps:
Install
The latest stable release (and required dependencies) can be installed from PyPI:

pip install bardapi

You may instead want to use the development version from Github:

pip install git+https://github.com/dsdanielpark/Bard-API.git

Step 3:

replace the code you got in step 1 here in this part in token section:

<< import bardapi
import tkinter as tk

token = 'xxxxxxxxxx.'
...
...
...
>>

finally run the code and enjoy to ask innovative questions from googles(gogolli) AI machine.
