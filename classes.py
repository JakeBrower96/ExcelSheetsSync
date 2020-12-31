#Initial Commit
#stores all values associated with a particular airmen, as well as
#functions that will be useful for the switch to java after the prototype
#@author A1C Jake Brower 12/29/2020

from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class cbt:
    isDone: bool
    name: str

    def __init__(self, isDone: bool, name: str):
        self.isDone = isDone
        self.name = name

@dataclass
class sere:
    hasPhysical: bool
    isDone: bool
    dateOfSere: date

    def __init__(self, hasPhysical: bool, isDone: bool, dateOfSere: date):
        self.hasPhysical = hasPhysical
        self.isDone = isDone
        self.dateOfSere = dateOfSere

@dataclass
class completionReport:
    hasStartDate: bool
    atSonoran: bool
    isAwaitingFlying: bool
    isFlying: bool
    inMQTorOther: bool
    comments: str

    def __init__(self, hasStartDate: bool, atSonoran: bool, isAwaitingFlying: bool, isFlying: bool, inMQTorOther: bool, comments: str):
        self.hasStartDate = hasStartDate
        self.atSonoran = atSonoran
        self.isAwaitingFlying = isAwaitingFlying
        self.isFlying = isFlying
        self.inMQTorOther = inMQTorOther
        self.comments = comments

#the structure of how every airmen's information will be populated
@dataclass
class airmen:
    name: str
    rank: str
    crewPos: str
    isOnLeave: bool
    scheduledLeave: List[date]
    isoOrRom: bool
    hundredPercentContact: str
    zoom: str
    lineSqd: str
    dateArrived: date
    classNumber: str
    shift: int
    projStartDate: date
    hasPolicyLit: bool
    cbts: List[cbt]
    afe: bool
    crm: bool
    sec: int #0 for bad 1 for s 2 for ts
    hasLineBadge: bool
    hasRedBadge: bool
    hasRips: bool
    ipadStatus: int #0 for not submitted 1 for submitted 2 for has iPad
    hasPHA: bool
    checkedInWithSarm: bool
    checkedInWithHarm: bool
    hasHeadset: bool
    hasPubs: bool
    hasGtc: bool
    updatedDogTags: bool
    hasFlightGear: bool
    completedFTAC: bool
    sereInfo: sere
    hasLOA: bool
    hasAuth: bool
    hasVoucher: bool
    obCBTestStatus: int #not sure what this is
    completionRep: completionReport
    remarks: str

    def __init__(self, name: str, rank: str, crewPos: str, isoOrRom: bool, hundredPercentContact: str, dateArrived: str, sec: int, sereInfo: sere, remarks: str):
        self.name = name
        self.rank = rank
        self.crewPos = crewPos
        self.isOnLeave = False
        self.scheduledLeave = None
        self.isoOrRom = isoOrRom
        self.hundredPercentContact = hundredPercentContact
        self.zoom = ""
        self.lineSqd = ""
        self.dateArrived = dateArrived
        self.classNumber = ""
        self.shift = 0
        self.projStartDate = None
        self.hasPolicyLit = False
        self.cbts = None #I want to make this the list on the inprocessing list of cbts
        self.afe = False
        self.crm = False
        self.sec = sec
        self.hasLineBadge = False
        self.hasRedBadge = False
        self.hasRips = False
        self.ipadStatus = 0
        self.hasPHA = False
        self.checkedInWithSarm = False
        self.checkedInWithHarm = False
        self.hasHeadset = False
        self.hasPubs = False
        self.hasGtc = False
        self.updatedDogTags = False
        self.hasFlightGear = False
        self.completedFTAC = False
        self.sereInfo = sereInfo
        self.hasLOA = False
        self.hasAuth = False
        self.hasVoucher = False
        self.obCBTestStatus = 0
        self.completionRep = completionReport(False, False, False, False, False, "") #make completion report from the goodies
        self.remarks = remarks