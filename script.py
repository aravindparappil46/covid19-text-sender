import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

carrier_gateways = {
	"ATT": "@txt.att.net",
	"TMobile": "@tmomail.net",
	"Verizon": "@vtext.com",
	"Sprint": "@messaging.sprintpcs.com",
	"Cricket" : "@mms.cricketwireless.net",
	"Vodafone": "@vodafone-sms.de"
}

# Connecting to GMail SMTP Server
f = open("sender_info", "r")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
gmail_address = f.readline()
gmail_password = f.readline()
server.login(gmail_address, gmail_password)

with open("msg_info.json", "r") as input_file:
	all_input = json.load(input_file)

	for v in all_input.values():
		to_number = v["sendTo"]
		state = v["state"]
		county = v["county"]
		cell_network = v["network"]
		data = '{"state":\"'+state+'\","county":\"'+county+'\"}'

		# Hitting the API to get stats
		response = requests.post('https://covid19-us-api.herokuapp.com/county', data=data)
		m = response.json()['message'][0]
		confirmed = str(m['confirmed'])
		deaths = str(m['death'])
		new = str(m['new'])
		new_death = str(m['new_death'])

		# Forming SMS body
		body = "-\nTotal Cases: "+confirmed+"\nTotal Deaths: "+deaths+"\nNew Cases: "+new + "\nNew Deaths: "+ new_death+"\n-------"

		msg = MIMEMultipart()
		msg['Subject'] = "COVID-19 at "+county+" County, "+state
		msg.attach(MIMEText(body, 'plain'))
		sms = msg.as_string()

		to = to_number + carrier_gateways[cell_network]
		print("Sent to", to)
		server.sendmail(gmail_address, to, sms)

server.close()