from csv import reader
import csv
from datetime import datetime


#time management
time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")



class QuantPlate:

    #plate1of4 = ["A1", "A3", "A5", "A7", "A9", "A11", "A13", "A15", "A17", "A19", "A21", "A23", "C1", "C3", "C5", "C7", "C9", "C11", "C13", "C15", "C17", "C19", "C21", "C23", "E1", "E3", "E5", "E7", "E9", "E11", "E13", "E15", "E17", "E19", "E21", "E23", "G1", "G3", "G5", "G7", "G9", "G11", "G13", "G15", "G17", "G19", "G21", "G23", "I1", "I3", "I5", "I7", "I9", "I11", "I13", "I15", "I17", "I19", "I21", "I23", "K1", "K3", "K5", "K7", "K9", "K11", "K13", "K15", "K17", "K19", "K21", "K23", "M1", "M3", "M5", "M7", "M9", "M11", "M13", "M15", "M17", "M19", "M21", "M23", "O1", "O3", "O5", "O7", "O9", "O11", "O13", "O15", "O17", "O19", "O21", "O23"]
    #plate2of4 = ["A2", "A4", "A6", "A8", "A10", "A12", "A14", "A16", "A18", "A20", "A22", "A24", "C2", "C4", "C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "E2", "E4", "E6", "E8", "E10", "E12", "E14", "E16", "E18", "E20", "E22", "E24", "G2", "G4", "G6", "G8", "G10", "G12", "G14", "G16", "G18", "G20", "G22", "G24", "I2", "I4", "I6", "I8", "I10", "I12", "I14", "I16", "I18", "I20", "I22", "I24", "K2", "K4", "K6", "K8", "K10", "K12", "K14", "K16", "K18", "K20", "K22", "K24", "M2", "M4", "M6", "M8", "M10", "M12", "M14", "M16", "M18", "M20", "M22", "M24", "O2", "O4", "O6", "O8", "O10", "O12", "O14", "O16", "O18", "O20", "O22", "O24"]
    #plate3of4 = ["B1", "B3", "B5", "B7", "B9", "B11", "B13", "B15", "B17", "B19", "B21", "B23", "D1", "D3", "D5", "D7", "D9", "D11", "D13", "D15", "D17", "D19", "D21", "D23", "F1", "F3", "F5", "F7", "F9", "F11", "F13", "F15", "F17", "F19", "F21", "F23", "H1", "H3", "H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "J1", "J3", "J5", "J7", "J9", "J11", "J13", "J15", "J17", "J19", "J21", "J23", "L1", "L3", "L5", "L7", "L9", "L11", "L13", "L15", "L17", "L19", "L21", "L23", "N1", "N3", "N5", "N7", "N9", "N11", "N13", "N15", "N17", "N19", "N21", "N23", "P1", "P3", "P5", "P7", "P9", "P11", "P13", "P15", "P17", "P19", "P21", "P23"]
    #plate4of4 = ["B2", "B4", "B6", "B8", "B10", "B12", "B14", "B16", "B18", "B20", "B22", "B24", "D2", "D4", "D6", "D8", "D10", "D12", "D14", "D16", "D18", "D20", "D22", "D24", "F2", "F4", "F6", "F8", "F10", "F12", "F14", "F16", "F18", "F20", "F22", "F24", "H2", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "J2", "J4", "J6", "J8", "J10", "J12", "J14", "J16", "J18", "J20", "J22", "J24", "L2", "L4", "L6", "L8", "L10", "L12", "L14", "L16", "L18", "L20", "L22", "L24", "N2", "N4", "N6", "N8", "N10", "N12", "N14", "N16", "N18", "N20", "N22", "N24", "P2", "P4", "P6", "P8", "P10", "P12", "P14", "P16", "P18", "P20", "P22", "P24"]

    plate1of4 = ["A1", "C1", "E1", "G1", "I1", "K1", "M1", "O1", "A3", "C3", "E3", "G3", "I3", "K3", "M3", "O3", "A5", "C5", "E5", "G5", "I5", "K5", "M5", "O5", "A7", "C7", "E7", "G7", "I7", "K7", "M7", "O7", "A9", "C9", "E9", "G9", "I9", "K9", "M9", "O9", "A11", "C11", "E11", "G11", "I11", "K11", "M11", "O11", "A13", "C13", "E13", "G13", "I13", "K13", "M13", "O13", "A15", "C15", "E15", "G15", "I15", "K15", "M15", "O15", "A17", "C17", "E17", "G17", "I17", "K17", "M17", "O17", "A19", "C19", "E19", "G19", "I19", "K19", "M19", "O19", "A21", "C21", "E21", "G21", "I21", "K21", "M21", "O21", "A23", "C23", "E23", "G23", "I23", "K23", "M23", "O23"]
    plate2of4 = ["A2", "C2", "E2", "G2", "I2", "K2", "M2", "O2", "A4", "C4", "E4", "G4", "I4", "K4", "M4", "O4", "A6", "C6", "E6", "G6", "I6", "K6", "M6", "O6", "A8", "C8", "E8", "G8", "I8", "K8", "M8", "O8", "A10", "C10", "E10", "G10", "I10", "K10", "M10", "O1", "A12", "C12", "E12", "G12", "I12", "K12", "M12", "O12", "A14", "C14", "E14", "G14", "I14", "K14", "M14", "O14", "A16", "C16", "E16", "G16", "I16", "K16", "M16", "O16", "A18", "C18", "E18", "G18", "I18", "K18", "M18", "O18", "A20", "C20", "E20", "G20", "I20", "K20", "M20", "O20", "A22", "C22", "E22", "G22", "I22", "K22", "M22", "O22", "A24", "C24", "E24", "G24", "I24", "K24", "M24", "O24"]
    plate3of4 = ["B1", "D1", "F1", "H1", "J1", "L1", "N1", "P1", "B3", "D3", "F3", "H3", "J3", "L3", "N3", "P3", "B5", "D5", "F5", "H5", "J5", "L5", "N5", "P5", "B7", "D7", "F7", "H7", "J7", "L7", "N7", "P7", "B9", "D9", "F9", "H9", "J9", "L9", "N9", "P9", "B11", "D11", "F11", "H11", "J11", "L11", "N11", "P11", "B13", "D13", "F13", "H13", "J13", "L13", "N13", "P13", "B15", "D15", "F15", "H15", "J15", "L15", "N15", "P15", "B17", "D17", "F17", "H17", "J17", "L17", "N17", "P17", "B19", "D19", "F19", "H19", "J19", "L19", "N19", "P19", "B21", "D21", "F21", "H21", "J21", "L21", "N21", "P21", "B23", "D23", "F23", "H23", "J23", "L23", "N23", "P23"]
    plate4of4 = ["B2", "D2", "F2", "H2", "J2", "L2", "N2", "P2", "B4", "D4", "F4", "H4", "J4", "L4", "N4", "P4", "B6", "D6", "F6", "H6", "J6", "L6", "N6", "P6", "B8", "D8", "F8", "H8", "J8", "L8", "N8", "P8", "B10", "D10", "F10", "H10", "J10", "L10", "N10", "P1", "B12", "D12", "F12", "H12", "J12", "L12", "N12", "P12", "B14", "D14", "F14", "H14", "J14", "L14", "N14", "P14", "B16", "D16", "F16", "H16", "J16", "L16", "N16", "P16", "B18", "D18", "F18", "H18", "J18", "L18", "N18", "P18", "B20", "D20", "F20", "H20", "J20", "L20", "N20", "P20", "B22", "D22", "F22", "H22", "J22", "L22", "N22", "P22", "B24", "D24", "F24", "H24", "J24", "L24", "N24", "P24"]
    
    def __init__(self, plateNum, octetFilePath):
        self.platenNum = plateNum
        self.octetFilePath = octetFilePath
        self.octetQuantsDict_Quad1 = {}
        self.octetQuantsDict_Quad2 = {}
        self.octetQuantsDict_Quad3 = {}
        self.octetQuantsDict_Quad4 = {}
        self.octetQuants_Quad1 = []
        self.octetQuants_Quad2 = []
        self.octetQuants_Quad3 = []
        self.octetQuants_Quad4 = []


    #reads incoming octet raw file and capture well id and qant value into a dictionary based on the quad of the 384 well plate the well id is in
    def setQuantDictionary(self):
        with open(self.octetFilePath, "r") as f:
            file_reader = reader(f)
            counter = 0
            for i in file_reader:
                if counter != 0: 
                    wellID = i[5]
                    octetConc = i[12]
                    counter = counter + 1
                    if wellID in self.plate1of4:
                        self.octetQuantsDict_Quad1[wellID] = octetConc
                    if wellID in self.plate2of4:
                        self.octetQuantsDict_Quad2[wellID] = octetConc
                    if wellID in self.plate3of4:
                        self.octetQuantsDict_Quad3[wellID] = octetConc
                    if wellID in self.plate4of4:
                        self.octetQuantsDict_Quad4[wellID] = octetConc
                else:
                    counter = counter + 1

    #adds dictoary values quant value) to the octetQuants_Quad list based on strict order of the plate#of# list struct
    def quantListCreator(self, dict, read_lst, write_lst):
        counter = 0
        while counter < 96:
            for key, value in dict.items():
                if counter < 96:
                    if key == read_lst[counter]:
                        write_lst.append(value)
                        counter += 1
                        # print(counter)
                        # print(key)
        return write_lst
    
    def masterQuantParser(self):
        self.setQuantDictionary()
        print("DICT1 ")
        print(self.octetQuantsDict_Quad1)
        print("DICT2 ")
        print(self.octetQuantsDict_Quad2)
        print("DICT3 ")
        print(self.octetQuantsDict_Quad3)
        print("DICT4 ")
        print(self.octetQuantsDict_Quad4)
        self.quantListCreator(self.octetQuantsDict_Quad1, self.plate1of4, self.octetQuants_Quad1)
        self.quantListCreator(self.octetQuantsDict_Quad2, self.plate2of4, self.octetQuants_Quad2)
        self.quantListCreator(self.octetQuantsDict_Quad3, self.plate3of4, self.octetQuants_Quad3)
        self.quantListCreator(self.octetQuantsDict_Quad4, self.plate4of4, self.octetQuants_Quad4)
        print("QUANT LIST 1 ")
        print(self.octetQuants_Quad1)
        print("QUANT LIST 2 ")
        print(self.octetQuants_Quad2)
        print("QUANT LIST 3 ")
        print(self.octetQuants_Quad3)
        print("QUANT LIST 4 ")
        print(self.octetQuants_Quad4)

    def getOctetQuants_Quad1(self):
        return self.octetQuants_Quad1
    def getOctetQuants_Quad2(self):
        return self.octetQuants_Quad2
    def getOctetQuants_Quad3(self):
        return self.octetQuants_Quad3
    def getOctetQuants_Quad4(self):
        return self.octetQuants_Quad4
    


class NormPlate:
    numInstances = 0
    

    def __init__(self, plateNum, targetConc, targetVol, neatVol):
        self.plateNum = plateNum
        self.targetConc = targetConc
        self.targetVol = targetVol
        self.neatVol = neatVol
        self.supVolList = []
        self.dilVolList = []
        NormPlate.numInstances += 1 #numInstance is the total count of class instances created
        self.count = NormPlate.numInstances #count is the object instance number
        self.SupCSVInput = "C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time + "\SupCSVInput_" + str(self.count) + "_" + time + ".csv"
        self.DilCSVInput =  "C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time + "\DilCSVInput_" + str(self.count) + "_" + time + ".csv"

    #will accept a list of quantData already parsed into 96 indexs
    # def setQuantData(self, quantDatalst):
    #     #self.quantDatalst = quantDatalst
    #     quantDatalst = quantDatalst

    #gets parsed quant data list
    def getQuantData(self):
        return self.quantDatalst
    
    #method used locally by other methods in class only
    def supCalc(self, quantConc):
        # supVol = (self.targetConc/quantConc) * self.targetVol
        # if supVol > self.targetVol:
        #     finalSupVol = self.neatVol
        # else:
        #     finalSupVol = supVol
        # finalSupVol = round(finalSupVol, 2)
        finalSupVol = quantConc
        return finalSupVol


    def volListCreation(self, quantDatalst):
        for i in quantDatalst:
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

    def inputCSVFileWriter(self):
        with open(self.SupCSVInput, "w") as SUP:
            writer = SUP.write
            self.plateFormatFileWriter(writer, self.supVolList)

        with open(self.DilCSVInput, "w") as DIL:
            writer = DIL.write
            self.plateFormatFileWriter(writer, self.dilVolList)



# SupCSVInputP1 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP1_" + time + ".csv"
# DilCSVInputP1 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP1_" + time + ".csv"




# mylst = ['709.1', '629.1', '943.8', '444.8', '129.6', '205.4', '153.2', '252.3', '1.64', '1.46', '1.7', '1.49', '1.48', '1.29', '96.4', '100.3', '630.6', '615.9', '492.5', '492.9', '192.5', '188.4', '181.7', '202.2', '1.49', '13.1', '1.61', '1.54', '1.45', '1.38', '233.2', '79.1', '133.3', '2.4', '76.1', '4.03', '84.9', '9.8', '75.4', '11.9', '83.7', '19.5', '106.3', '30.9', '101.6', '22.9', '88.4', '26.1', '2.9', '56.1', '27', '23.8', '2.74', '195.7', '30.4', '138.1', '126', '228', '6.64', '141', '3.16', '76.2', '15.7', '65.9', '123.1', '40.3', '134.9', '28.7', '107.2', '16.3', '2.72', '22.5', '104.2', '28.9', '106.4', '3.91', '148.9', '16', '192.6', '27.7', '2.34', '135.5', '18.2', '226', '19.2', '2.26', '68.2', '133.2', '1.35', '200.5', '2.44', '166.8', '72.1', '211.1', '1.67', '95.5', '117.9', '36', '143', '36.2', '94.4', '14.4', '82', '10.6', '1.74', '17.4', '1.72', '14.9', '8.36', '9.23', '65.4', '6.64', '1.87', '176.8', '4.16', '226.4', '32.3', '324.1', '6.47', '64', '5.26', '1.98', '7.09', '169.4', '11.2', '10.6', '3.46', '121.3', '2.36', '18.1', '65.2', '33.6', '1.41', '11', '35.3', '41.4', '20.1', '56.4', '3.92', '18.6', '62.2', '35.8', '3.35', '18.8', '15.4', '132.6', '2.09', '174', '5.7', '15.4', '7.65', '190.3', '33.8', '32.3', '13.7', '5.74', '35.3', '13', '1.77', '25.1', '2.64', '4.24', '141', '17.2', '69.5', '28.8', '52.3', '1.23', '2.23', '16.1', '2.06', '16.7', '119.7', '11.8', '151.4', '7.74', '3.03', '6.04', '9.51', '45.9', '4.24', '6.68', '17.4', '0.804', '53.7', '4.28', '13.4', '11.1', '63', '23', '59.4', '8.5', '21.9', '1.31', '63.7', '14.1', '106.4', '11.5', '77.9', '19.6', '36', '8.03', '74.6', '19.5', '54.7', '52.5', '79.8', '52.9', '1.12', '1.17', '48.3', '67.4', '100.7', '37.9', '36.8', '8.85', '2.94', '4.32', '44.1', '2.56', '61.8', '5.84', '57.4', '40.5', '161.4', '50.9', '49.5', '15', '80.1', '46', '62.6', '16.3', '222.6', '26.3', '1.84', '55.2', '57.5', '23', '42.6', '45', '27.6', '8.72', '47.2', '8.84', '41', '66.7', '100.3', '48.3', '130.2', '79.5', '135.7', '23.7', '87.8', '30.9', '43.4', '70.7', '32.4', '16.5', '210.8', '9.96', '155', '17.6', '200', '85.1', '136.3', '60.1', '170.5', '73.1', '129.9', '48.3', '140.8', '7.04', '61.6', '27.1', '92.9', '22.7', '16.2', '30.1', '81.4', '13.9', '53.4', '50', '90.9', '23.3', '139.3', '42.1', '2.52', '53.2']

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