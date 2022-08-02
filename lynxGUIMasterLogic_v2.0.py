from csv import reader
import csv
from datetime import datetime
from testingPlatesAsObjects import NormPlate, QuantPlate
from lynxGUIFunctions import userInputForNorm, userInputForQuant
#time management
time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")

octetPlateCount, octetFilePath1, octetFilePath2, octetFilePath3 = userInputForQuant()
sourceTypeSelected, desTypeSelected, tipTypeSelected, numberOfPlates, bCreateEcho, targetVol, targetConc, neatVol, bMix, intMixHeightOffset, mixVol = userInputForNorm()

#QuantPlate Object --->__init__(self, plateNum, octetFilePath):
quantPlateObjectList = []
normPlateObjectList = []
if octetPlateCount >= 1:
    quantPlate1 = QuantPlate("QuantPlate1", octetFilePath1)
    quantPlateObjectList.append(quantPlate1)
    quantPlate1.masterQuantParser()

    #quant plat 1 & norm plate 1
    quantsPlate1_Quad1 = quantPlate1.getOctetQuants_Quad1()
    normPlate1 = NormPlate("NormPlate1", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate1)
    #normPlate1.setQuantData()
    normPlate1.volListCreation(quantsPlate1_Quad1)
    normPlate1_supVol = normPlate1.getSupVolList()
    normPlate1_dilVol = normPlate1.getDilVolList()
    normPlate1.inputCSVFileWriter()

    #quant plat 1 & norm plate 2
    quantsPlate1_Quad2 = quantPlate1.getOctetQuants_Quad2()
    normPlate2 = NormPlate("NormPlate2", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate2)
    #normPlate2.setQuantData()
    normPlate2.volListCreation(quantsPlate1_Quad2)
    normPlate2_supVol = normPlate2.getSupVolList()
    normPlate2_dilVol = normPlate2.getDilVolList()
    normPlate2.inputCSVFileWriter()
    
    #quant plat 1 & norm plate 3
    quantsPlate1_Quad3 = quantPlate1.getOctetQuants_Quad3()
    normPlate3 = NormPlate("NormPlate3", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate3)
    #normPlate3.setQuantData()
    normPlate3.volListCreation(quantsPlate1_Quad3)
    normPlate3_supVol = normPlate3.getSupVolList()
    normPlate3_dilVol = normPlate3.getDilVolList()
    normPlate3.inputCSVFileWriter()

    #quant plat 1 & norm plate 4
    quantsPlate1_Quad4 = quantPlate1.getOctetQuants_Quad4()
    normPlate4 = NormPlate("NormPlate4", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate4)
    #normPlate4.setQuantData()
    normPlate4.volListCreation(quantsPlate1_Quad4)
    normPlate4_supVol = normPlate4.getSupVolList()
    normPlate4_dilVol = normPlate4.getDilVolList()
    normPlate4.inputCSVFileWriter()
 
    # print("Norm Sup List 1")
    # print(normPlate1_supVol)
    # print("Norm Sup List 2")
    # print(normPlate2_supVol)
    # print("Norm Sup List 3")
    # print(normPlate3_supVol)
    # print("Norm Sup List 4")
    # print(normPlate4_supVol)

if octetPlateCount >= 2:
    plate2 = QuantPlate("QuantPlate2", octetFilePath2)
    quantPlateObjectList.append(plate2)
    plate2.masterQuantParser()
    quantsPlate2_Quad1 = plate2.getOctetQuants_Quad1()
    quantsPlate2_Quad2 = plate2.getOctetQuants_Quad2()
    quantsPlate2_Quad3 = plate2.getOctetQuants_Quad3()
    quantsPlate2_Quad4 = plate2.getOctetQuants_Quad4()
    
    

if octetPlateCount >=3:
    plate3 = QuantPlate("QuantPlate3", octetFilePath3)
    quantPlateObjectList.append(plate3)
    plate3.masterQuantParser()
    quantsPlate3_Quad1 = plate3.getOctetQuants_Quad1()
    quantsPlate3_Quad2 = plate3.getOctetQuants_Quad2()
    quantsPlate3_Quad3 = plate3.getOctetQuants_Quad3()
    quantsPlate3_Quad4 = plate3.getOctetQuants_Quad4()
   


#NormPlate Object --->__init__(self, plateNum, targetConc, targetVol, neatVol)



print(len(normPlateObjectList))

#"C:\codeBASE\Lynx\octet_results_sheet_4plate_testable.csv"
#lynxGUIMasterLogic_v2.0.py
