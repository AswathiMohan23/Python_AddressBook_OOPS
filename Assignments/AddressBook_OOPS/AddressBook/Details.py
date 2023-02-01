class Details:
    def __init__(self):
        self.__first_name = None
        self.__last_name = None
        self.__address = None
        self.__city = None
        self.__state = None
        self.__zip_code = None
        self.__phn = None
        self.__email = None

    def getFirst_name(self):
        return self.__first_name

    def setFirst_name(self, first_name):
        self.__first_name = first_name

    def getLast_name(self):
        return self.__last_name

    def setLast_name(self, last_name):
        self.__last_name = last_name

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getCity(self):
        return self.__city

    def setCity(self, city):
        self.__city = city

    def getState(self):
        return self.__state

    def setState(self, state):
        self.__state = state

    def getZip_code(self):
        return self.__zip_code

    def setZip_code(self, zip_code):
        self.__zip_code = zip_code

    def getPhn(self):
        return self.__phn

    def setPhn(self, phn):
        self.__phn = phn

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email
