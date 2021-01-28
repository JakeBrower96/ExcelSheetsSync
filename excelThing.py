#Initial Commit
#excel and sheets syncronization for 552 TRSS
#@author A1C Jake Brower 12/29/2020

#gspread is the pkg I'm using to pull the data from the google sheets doc onto the computer
import gspread
#this verifies that the JSON file in this directory is the one being used no china hacking here
from oauth2client.service_account import ServiceAccountCredentials
#this has my airmen object
import classes
#dates to check leave and stuff
from datetime import datetime, date
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
workingSheet = spreadSheet.worksheet("newForm")

#all of the data that is associated with the airmen
airmenData = workingSheet.get_all_records()

def getLeaveDate(leaveDateStr: str):
    date1 = ""
    date2 = ""
    onDate2 = False
    for i in leaveDateStr:
        if i != "-" and onDate2 == False:
            date1 = date1 + i
        elif i != "-" and onDate2 == True:
            date2 += i
        else:
            onDate2 = True
    date1 = datetime.strptime(date1, "%m/%d/%Y")
    date1 = date1.date()
    date2 = datetime.strptime(date2, "%m/%d/%Y")
    date2 = date2.date()
    return [date1, date2]

def isOnLeaveRN(leaveDates):
    if leaveDates[0] <= date.today() <= leaveDates[1]:
        return True
    else:
        return False

def getAirmenData():
    myData = workingSheet.row_values(18)
    # pprint(myData)
    leaveDatesStr = myData[35]
    leaveDates = None
    isOnLeave = False
    if leaveDatesStr != None:
        leaveDates = getLeaveDate(leaveDatesStr)
        isOnLeave = isOnLeaveRN(leaveDates)
    isoOrRom = False
    if myData[2] != "":
        isoOrRom = True
    print(isoOrRom)
    # a1CBrower = classes.airmen(myData[0], "MSO", isOnLeave, leaveDates, isoOrRom)

#run a for loop through the spreadsheet and make an airmen class with each row being an airmen
# def getAirmenData():
#     # pprint(workingSheet.row_values(19)) #this is me, playing around seeing if i can go cell by cell
#     data = workingSheet.row_values(19)
#     leaveDates = data[1] #the leave colom poses some real problems that are due to inconsistencies in how it is written in the spreadsheet the format should be something like mm/dd/yyyy - mm/dd/yyyy
#     isOnLeave = False
#     isoOrRom = False
#     if data[2] == "T":
#         isoOrRom = True
#     else:
#         isoOrRom = False
#     strDateArrived = data[6]
#     dayArrived = int(strDateArrived[:2])
#     monthArrived = strDateArrived[3:6]
#     yearArrived = int(strDateArrived[7:])
#     dateArrived = date(yearArrived, monthArrived, dayArrived)
#     print(dateArrived)
    # a1cBrower = classes.airmen(data[0], None, MSO, isOnLeave, None, isoOrRom, data[3], data[4], data[5], )

getAirmenData()