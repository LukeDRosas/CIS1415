#Luke Doughty-Rosas

class CellPhone:

    def __init__(self):
        self.manufact = ''
        self.model = ''
        self.retail_price = 0
        
    def set_manufact(self):
        self.manufact = input('Enter the manufacturer: ')
        return self.manufact

    def set_model(self):
        self.model = input('Enter the model number: ')
        return self.model
    
    def set_retail_price(self):
        self.retail_price = input('Enter the retail price: ')
        return float(self.retail_price)

    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return float(self.retail_price)


phone1 = CellPhone()
phone1.manufact = phone1.set_manufact()
phone1.model = phone1.set_model()
phone1.retail_price = phone1.set_retail_price()
print('Here is the data that you entered:')
print('Manufacturer:', phone1.manufact)
print('Model Number:', phone1.model)
print('Retail Price: $%.2f' % phone1.retail_price)


                                  
                                  
        
        
