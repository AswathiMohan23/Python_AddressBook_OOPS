class Details:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.phn = None
        self.email = None

    def getFirst_name(self):
        return self.first_name

    def setFirst_name(self, first_name):
        self.first_name = first_name

    def getLast_name(self):
        return self.last_name

    def setLast_name(self, last_name):
        self.last_name = last_name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getZip_code(self):
        return self.zip_code

    def setZip_code(self, zip_code):
        self.zip_code = zip_code

    def getPhn(self):
        return self.phn

    def setPhn(self, phn):
        self.phn = phn

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email
