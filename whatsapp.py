"""
This script sends WhatsApp message (via Twilio) of
Paderborn Coronavirus numbers to Twilio registered
WhatsApp number 
"""
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import date

options = Options()
options.add_argument('--headless')
driver_path = "C:\\Program Files\\chromedriver.exe"
driver = webdriver.Chrome(driver_path, options=options)

driver.get("https://www.kreis-paderborn.de/kreis_paderborn/aktuelles/pressemitteilungen/Informationen-zu-Coronaviren.php")

# Finding table of all details
table = driver.find_element_by_xpath('//*[@id="anchorContent"]/div[8]/table')

# Getting to Paderborn's row
row = table.find_elements(By.TAG_NAME, "tr")[10]
col = row.find_elements(By.TAG_NAME, "td")

curr_confirmed = int(col[1].text)
yest_confirmed = int(col[2].text)
curr_deaths = int(col[3].text)
yest_death= int(col[4].text)
curr_recover = int(col[5].text)
yest_recover = int(col[6].text)
driver.close()

today = str(date.today())

msg = "*📈 Coronavirus stats for Paderborn*\n📅 "+today+"\n\n💡 Total Confirmed Cases: "+str(curr_confirmed)+\
	  "\n💀 Total Deaths: "+ str(curr_deaths)+"\n🏥 Total Recovered: "+str(curr_recover)+ \
	  "\n\n⬆ New Cases Today: "+ str(curr_confirmed-yest_confirmed) + \
	  "\n⛅ New Deaths Today: "+ str(curr_deaths-yest_death) + \
	  "\n🌟 New Recoveries Today: "+ str(curr_recover-yest_recover)

# Reading from a file twilio_creds which has
# Twilio Account ID and Auth token in 2 separate lines
f = open("twilio_creds", "r")
account = f.readline()
token = f.readline()
client = Client(account, token)

from_whatsapp_number ='whatsapp:+14155238886' # Twilio ph.num
to_whatsapp_number= 'EnterTwilioRegisteredWhatsAppNumHere'
client.messages.create(body=msg,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

print("Sent to:", to_whatsapp_number)
