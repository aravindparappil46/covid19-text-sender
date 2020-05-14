# Coronavirus Stats by US County - Text Message sender
Sends text message of total confirmed cases, total deaths, new deaths & new cases for counties in the US
<br>
Uses https://covid19-us-api.herokuapp.com/county API to get the data. Find their documentation [here](https://covid19-us-api.herokuapp.com/redoc)

# Requirements
- Python 3.x+
- Gmail account
- Enable *Less Secure App* access for that Gmail account. Go [here](https://myaccount.google.com/lesssecureapps) while logged in to the Gmail account
- Receiver phone number in the US (network should be one among AT&T, T-Mobile, Verizon, Sprint or Cricket (or their MVNOs))

# How-to
- Fill the details in ```msg_info.json```
	- ```sendTo```: Which phone number do you want to send the SMS to?
	- ```network```: What is that number's network provider? Enter one of the following: ```ATT, TMobile, Verizon, Sprint or Cricket``` (Enter exactly as given. Case sensitive)
	- You can keep as many entries as you want; the value of X in key ```msgX``` does not matter as long as it is unique
- In ```sender_info```, write your gmail address in the first line & gmail account password in the second line
	- **WARNING**: There is no encryption or other means of security here. Storing plain text passwords is very dangerous and not recommended. **This file's security is your responsibility so don't store it somewhere other's can access.** This goes for the **mobile number** stored in ```msg_info.json``` as well. Since this was for educational purposes, I have kept it as-is. Feel free to raise a PR if you wish to contribute towards a safer approach to storing credentials.
- Run using ```python3 script.py``` or ```python script.py``` depending on your environment setup

<br><br>
*Again, keeping the Gmail account credentials and the phone numbers safe and secure is your responsibility. This script was just for educational purposes.*