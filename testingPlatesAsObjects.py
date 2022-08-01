from csv import reader
import csv
from datetime import datetime

#time management
time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")



class QuantPlate:
    def __init__(self, plateNum, quadsOfData):
        self.platenNum = plateNum
        self.quadsOfData = quadsOfData

     # def someName(plateNum):
    #     plateWellRange = [0, 96, 192, 288, 384]
    #     for i in range(plateWellRange[0], plateWellRange[1]):
    #         myQuant = octetQuants[i]
    #         plateNum.append(myQuant)

    # plate1 = []
    # for i in range(0,96):
    #     myQuant = octetQuants[i]
    #     plate1.append(myQuant)


class NormPlate:
    supVolList = []
    dilVolList = []
    numInstances = 0
    

    def __init__(self, plateNum, targetConc, targetVol, neatVol):
        self.plateNum = plateNum
        self.targetConc = targetConc
        self.targetVol = targetVol
        self.neatVol = neatVol
        NormPlate.numInstances += 1 #numInstance is the total count of class instances created
        self.count = NormPlate.numInstances #count is the object instance number

    #will accept a list of quantData already parsed into 96 indexs
    def setQuantData(self, quantDatalst):
        self.quantDatalst = quantDatalst

    #gets parsed quant data list
    def getQuantData(self):
        return self.quantDatalst
    
    #method used locally by other methods in class only
    def supCalc(self, quantConc):
        supVol = (self.targetConc/quantConc) * self.targetVol
        if supVol > self.targetVol:
            finalSupVol = self.neatVol
        else:
            finalSupVol = supVol
        finalSupVol = round(finalSupVol, 2)
        return finalSupVol


    def volListCreation(self):
        for i in self.quantDatalst:
            quantConc = i
            quantConc = float(quantConc)
            supVol = self.supCalc(quantConc)
            dilVol = self.targetVol - supVol
            dilVol = round(dilVol, 2)
            self.supVolList.append(str(supVol))
            self.dilVolList.append(str(dilVol))

    def getSupVolList(self):
        return(self.supVolList)

    def getDilVolList(self):
        return(self.dilVolList)



    def plateFormatFileWriter(self, writer, lst):
        writer("VI;12;8")
        for i in range(1, 13):
                writer("," + str(i))
        aplhaList = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(0, 8):
            writer("\n")
            writer(aplhaList[i])
            for j in range(i, 96, 8):
                writer("," + lst[j])

    def inputCSVFileWriter(self, supWriteToLocation, dilWriteToLocation):
        with open(supWriteToLocation, "w") as SUP:
            writer = SUP.write
            self.plateFormatFileWriter(writer, self.supVolList)

        with open(dilWriteToLocation, "w") as DIL:
            writer = DIL.write
            self.plateFormatFileWriter(writer, self.dilVolList)



SupCSVInputP1 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP1_" + time + ".csv"
DilCSVInputP1 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP1_" + time + ".csv"




mylst = ['709.1', '629.1', '943.8', '444.8', '129.6', '205.4', '153.2', '252.3', '1.64', '1.46', '1.7', '1.49', '1.48', '1.29', '96.4', '100.3', '630.6', '615.9', '492.5', '492.9', '192.5', '188.4', '181.7', '202.2', '1.49', '13.1', '1.61', '1.54', '1.45', '1.38', '233.2', '79.1', '133.3', '2.4', '76.1', '4.03', '84.9', '9.8', '75.4', '11.9', '83.7', '19.5', '106.3', '30.9', '101.6', '22.9', '88.4', '26.1', '2.9', '56.1', '27', '23.8', '2.74', '195.7', '30.4', '138.1', '126', '228', '6.64', '141', '3.16', '76.2', '15.7', '65.9', '123.1', '40.3', '134.9', '28.7', '107.2', '16.3', '2.72', '22.5', '104.2', '28.9', '106.4', '3.91', '148.9', '16', '192.6', '27.7', '2.34', '135.5', '18.2', '226', '19.2', '2.26', '68.2', '133.2', '1.35', '200.5', '2.44', '166.8', '72.1', '211.1', '1.67', '95.5', '117.9', '36', '143', '36.2', '94.4', '14.4', '82', '10.6', '1.74', '17.4', '1.72', '14.9', '8.36', '9.23', '65.4', '6.64', '1.87', '176.8', '4.16', '226.4', '32.3', '324.1', '6.47', '64', '5.26', '1.98', '7.09', '169.4', '11.2', '10.6', '3.46', '121.3', '2.36', '18.1', '65.2', '33.6', '1.41', '11', '35.3', '41.4', '20.1', '56.4', '3.92', '18.6', '62.2', '35.8', '3.35', '18.8', '15.4', '132.6', '2.09', '174', '5.7', '15.4', '7.65', '190.3', '33.8', '32.3', '13.7', '5.74', '35.3', '13', '1.77', '25.1', '2.64', '4.24', '141', '17.2', '69.5', '28.8', '52.3', '1.23', '2.23', '16.1', '2.06', '16.7', '119.7', '11.8', '151.4', '7.74', '3.03', '6.04', '9.51', '45.9', '4.24', '6.68', '17.4', '0.804', '53.7', '4.28', '13.4', '11.1', '63', '23', '59.4', '8.5', '21.9', '1.31', '63.7', '14.1', '106.4', '11.5', '77.9', '19.6', '36', '8.03', '74.6', '19.5', '54.7', '52.5', '79.8', '52.9', '1.12', '1.17', '48.3', '67.4', '100.7', '37.9', '36.8', '8.85', '2.94', '4.32', '44.1', '2.56', '61.8', '5.84', '57.4', '40.5', '161.4', '50.9', '49.5', '15', '80.1', '46', '62.6', '16.3', '222.6', '26.3', '1.84', '55.2', '57.5', '23', '42.6', '45', '27.6', '8.72', '47.2', '8.84', '41', '66.7', '100.3', '48.3', '130.2', '79.5', '135.7', '23.7', '87.8', '30.9', '43.4', '70.7', '32.4', '16.5', '210.8', '9.96', '155', '17.6', '200', '85.1', '136.3', '60.1', '170.5', '73.1', '129.9', '48.3', '140.8', '7.04', '61.6', '27.1', '92.9', '22.7', '16.2', '30.1', '81.4', '13.9', '53.4', '50', '90.9', '23.3', '139.3', '42.1', '2.52', '53.2']

# plate1 = NormPlate("plate1", 36, 100, 100)
# plate1.setQuantData(mylst)
# plate1.volListCreation()
# print(plate1.getSupVolList)
# x = plate1.getDilVolList()
# print(x)
# plate1.inputCSVFileWriter(SupCSVInputP1, DilCSVInputP1)


# plate1_quant_Data = plate1.getQuantData()
# print(plate1_quant_Data)
# print(plate1.count)


# plate2 = NormPlate("plate2", 36, 100, 100)
# plate3 = NormPlate("plate3", 36, 100, 100)
# plate4 = NormPlate("plate4", 36, 100, 100)
# print(plate2.count)
# print(plate3.count)
# print(plate4.count)

# print(plate1.numInstances)
#testingPlatesAsObjects.py