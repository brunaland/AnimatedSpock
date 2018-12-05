from services.CustomerService import CustomerService
from models.Customer import Customer


class EmployeeUi():
    def __init__(self):
        self.__customerService = CustomerService()

    def findCustomerMenu(self):
            self.findCustomerMenuPrint()
            findCustomerAction = input('Choose action: ')
            if findCustomerAction == '0':
                self.startPageMenu()
            elif findCustomerAction == '1':
                self.searchCustomerPrintHeader()
            elif findCustomerAction == '2':
                customers = self.__customerService.getAllCustomers()
                customers = self.displayAllCustomersPrint(customers)
                s = input('Customers')

    def startPageMenu(self):
        #employee = EmployeeUi()
        action = True
        while action:
            self.mainMenuPrint()
            action = '5'
            if action == '3':
                name,age,ssn = self.createCustomer()
                newCustomer = Customer(name,age,ssn)
                self.__customerService.addCustomer(newCustomer)
            elif action == '5':
                self.findCustomerMenuPrint()
                self.findCustomerMenu()


    def mainMenuPrint(self):
        print("\nYou can do the following: ")
        print("1. List all available cars")
        print("2. List all unavailable cars")
        print("3. Register customer.")
        print("4. Create car reservation.")
        print("5. Find a customer.")
        print("6. Look up an order.")
        print("7. Show list of orders.")
        print("8. Return a car.")
        print("9. Edit order.")
        print("press q to quit\n")

    def createCustomer(self):
        name = input('Enter name: ')
        age = input('Enter age: ')
        ssn = input('Enter Social-security-nr: ')
        return name,age,ssn

    # Displays options that the user has.
    def findCustomerMenuPrint(self):
        print("0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")

    def displayAllCustomersPrint(self,customers):
        print("{:15} {:15} {:15}".format("Name", "Age", "SSN"))
        print("{:15} {:15} {:15}".format("---------------",\
        "---------------","---------------","---------------","---------------",\
        "---------------","---------------",))
        for customer in customers:
            print(customer)
        

    def searchCustomerPrintHeader(self):
        print("--------------------------------------------Search for customer-------------------------------------------")
