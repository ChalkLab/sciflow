from .ingestion import*
import os
import json
from .logwriter import logwrite

normcheck = {}

def normalize(path, loginfo):
    try:
        compound, target = getsystem(path)
        logwrite("act", loginfo, "System:\n\t- Compound: " + str(compound))
        logwrite("act", loginfo, "\t- Target: " + str(target))
        findprofile(path, compound)
        normalizationcheck(path, loginfo)
    except:
        pass

    i = 0
    for value in normcheck.values():
        if value is False:
            i += 1

    if i == 0:
        return True
    else:
        return False


#gets the compound and target within the scidata file
#sddir = '/Users/n01448636/Documents/PycharmProjects/chembl_django/scidata/JSON_dumps/'
def getsystem(path):
    compound = {}
    target = {}
    try:
        x = json.loads(open(path).read())
        for k,v in x.items():
            if k == '@graph':
                for a in x['@graph']['scidata']['system']['facets']:
                    for b,c in a.items():
                        if b == '@id' and c.startswith('target'):
                            target.update({'targetchembl':(a['chembl_id'])})
                        if b == '@id' and c.startswith('compound'):
                            compound.update({'inchi':(a['identifiers']['standard_inchi'])})
        if compound:
            return compound, target

    except:
        pass

#for sdfile in os.listdir(sddir):
    #print(findcomp(sdfile))


#searches the database for a profile matching the found inchi key
def findprofile(path, compound):
    inchi = compound.get("inchi")
    if "exists" == True:
        getprofile(inchi)
    else:
        makeprofile(inchi)
    addprofile(inchi)

#if the profile is found, this pulls it
def getprofile(inchi):
    print("")

#if the profile is not found, this creates it
def makeprofile(inchi):
    print("")

#once the profile has been created or obtained, this integrates it to the main file
def addprofile(inchi):
    print("")


#checks to make sure the file has been correctly normalized
def normalizationcheck(path, loginfo):
    normalized = True
    if normalized == True:
        logwrite("act", loginfo, "Normalization: Valid")
    else:
        logwrite("act", loginfo, "Normalization: Invalid!")
        logwrite("err", loginfo, "- File was not properly normalized!")

