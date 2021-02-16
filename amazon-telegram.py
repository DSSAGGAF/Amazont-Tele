
import re
from telethon.sync import TelegramClient 
from telethon import TelegramClient,events
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 

api_id = ''
api_hash = ''

# your phone number
phone = ""
client = TelegramClient('session', api_id, api_hash) 
   
client.connect() 
    
if not client.is_user_authorized(): 
   
    client.send_code_request(phone) 
      
    # signing in the client 
    client.sign_in(phone, input('Enter the code: '))     

@client.on(events.NewMessage)
async def my_event_handler(event):
    channelID = str(event.message.chat_id)
    if  ""== channelID:
        try:
            link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
            url = re.findall(link_regex, event.message.message)
            for lnk in url:
                
                chrome_options = Options()
                chrome_options.add_argument("--user-data-dir=chrome-data")
                driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
                driver.get(lnk[0]) 
                element = driver.find_element_by_id("placeYourOrder")
                element.click()
                driver.quit()
                print(element)
            print("Done ")     
        except :
            driver.quit()
            print("somthing wrong ")     
client.start()
client.run_until_disconnected()
    



