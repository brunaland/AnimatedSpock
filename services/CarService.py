from repositories.CarRepository import CarRepository
from datetime import datetime, timedelta
from models.Colors import Colors

class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()


    def getCars(self, action, typeAction,dateAvailable):
        return self.__carRepo.getCars(action, typeAction,dateAvailable)

    def addCar(self, newCar):
        self.__carRepo.addCar(newCar)

    def checkValidDate(self):
        while True:
            try:
                rentOutCar = input("Date created in this format DD-MM-YYYY: ").strip() + '-12-00'
                day, month, year, hour, minutes = map(int, rentOutCar.split('-'))
                break
            except:
                print("\nplease input valid date\n")
        return rentOutCar

    def checkCarType(self):
        while True:
            try:
                carTypeInput = int(input("Choose from available car types:  "))
                if 0 < carTypeInput < 6:
                    break
                else:
                    print("Please choose from available types\n")
            except:
                print("Please only insert integer values\n")
        return str(carTypeInput)

    def checkPassengers(self):
        while True:
            try:
                passengers = int(input("Passengers: "))
                break
            except:
                print("\nPlease only insert integer values\n")
        return passengers
        
    def checkTransmission(self):
        print("{}\n{}\n{}".format("Transmission:","1. Auto","2. Manual"))

        while True:
            try:
                transmissionInput = int(input("Choose: "))
                if 0 < transmissionInput < 3:
                    break
                else:
                    print("Please choose from available transmissions\n")
            except:
                print("Please only insert integer values\n")
        return transmissionInput

    def checkLicenseplate(self, newCar=True):
        licensePlate = ''
        booleanCheck = False
        while len(licensePlate) != 6 or not booleanCheck:
            licensePlate = input("\nLicense plate (F.x. LL-L00): ").upper()
            if len(licensePlate) == 6 and newCar == True:
                booleanCheck = self.__carRepo.duplicateLicensePlateCheck(str(licensePlate))
                if booleanCheck == False:
                    print("License plate already registered!")
            elif len(licensePlate) == 6:
                booleanCheck = True
            else:
                print("License plate has to match the format")
        return licensePlate
  
    def returnCar(self, licenseplate, TimeOfOrder):
        theFoundLicenseplate = self.__carRepo.returnCar(licenseplate, TimeOfOrder)
        if theFoundLicenseplate == None:
            return None
        else:
            return theFoundLicenseplate

    def licensePlateCheck(self, licensePlate):
        return self.__carRepo.LicensePlateCheck(licensePlate)
    
    def editCar(self, carType, make,licenseplate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar):
        return self.__carRepo.editCar(carType, make,licenseplate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar)
