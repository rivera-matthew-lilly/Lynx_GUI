from csv import reader
import csv
from datetime import datetime
from testingPlatesAsObjects import NormPlate
from lynxGUIFunctions import userInputForNorm
#time management
time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")


sourceTypeSelected, desTypeSelected, tipTypeSelected, numberOfPlates, bCreateEcho, targetVol, targetConc, neatVol, bMix, intMixHeightOffset, mixVol = userInputForNorm()

#NormPlate Object --->__init__(self, plateNum, targetConc, targetVol, neatVol)
normPlateObjectList = []
for i in range(0, numberOfPlates):
    plateID = "plate" + str(i)
    plate = NormPlate(plateID, targetConc, targetVol, neatVol)
    normPlateObjectList.append(plate)

print(len(normPlateObjectList))

#lynxGUIMasterLogic_v2.0.py
