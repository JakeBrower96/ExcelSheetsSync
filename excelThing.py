#Initial Commit
#excel and sheets syncronization for 552 TRSS
#@author A1C Jake Brower 12/29/2020

#gspread is the pkg I'm using to pull the data from the google sheets doc onto the computer
import gspread
#this verifies that the JSON file in this directory is the one being used no china hacking here
from oauth2client.service_account import ServiceAccountCredentials
#useful for testing
from pprint import pprint

#this is the google sheets document referenced in the google cloud console
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#this logs the code into the google sheets document
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

#opens the whole spreadsheet
spreadSheet = client.open("testing")
#pulls the particular spreadsheet that Capt. Wright uses to track airmen
workingSheet = spreadSheet.worksheet("Airmen Directory")

#all of the data that is associated with the airmen
airmenData = workingSheet.get_all_records()