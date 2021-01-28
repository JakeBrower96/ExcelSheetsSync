#Initial Commit
#This creates a base object of each class using my own information and
#will use that to test all of the functionallity
#@author A1C Jake Brower 12/31/2020

#this allows me to reference the objects made in classes.py
import classes
#A premade object that represents dates, used in some of my made classes
from datetime import date
#So i can make a list of every object ill be utilizing
from typing import List

#all of this information is from the excel sheet, DOES NOT PULL FROM THE GOOGLE SHEET
name = "Jake Brower"
rank = "A1C"
crewPos = "MSO"
isOnLeave = False
scheduledLeave = None 
isoOrRom = False
hundredPercentContact = "Capt Wright"
zoom = "jacobbrower96@gmail.com"
lineSqd = None
dateArrived = date(2020, 7, 13)
classNumber = "20 LAT"
shift = 8
projStartDate = date(2020, 9, 24)
hasPolicyLit = True
cbts = [classes.cbt(True, "CBT 1"), classes.cbt(False, "CBT 2")]
afe = True
crm = True
sec = 2 #0 for bad 1 for s 2 for ts
hasLineBadge = True
hasRedBadge = True
hasRips = True
ipadStatus = 1 #0 for not submitted 1 for submitted 2 for has iPad
hasPHA = True
checkedInWithSarm = True
checkedInWithHarm = True
hasHeadset = True
hasPubs = True
hasGtc = True
updatedDogTags = True
hasFlightGear = True
completedFTAC = True
sereInfo = classes.sere(True, True, date(2020, 8, 31))
hasLOA = True
hasAuth = True
hasVoucher = True
obCBTestStatus = 0 #not sure what this is
completionRep = classes.completionReport(True, False, True, False, False, "This is a comment for A1C Jake Brower")
remarks = "This is a remark for A1C Jake Brower :) ME!!!"
#End of the variables to make 1 airmen object then I get to run tests :)

#This very long line is the test for making the airmen object
a1cJakeBrower = classes.airmen(name, rank, crewPos, isoOrRom, hundredPercentContact, dateArrived, sec, sereInfo, remarks)