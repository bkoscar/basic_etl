import requests



class Extract():
    """ This class extractsgit  data from an API where the data cames from a sensor.  
    """
    def __init__(self):
        """ Constructor of the Extract class
        
        Args: 
            url (str): The API url
        """
        self.url =  "http://127.0.0.1:8000/data"
        
    def get_data(self):
        """ Request the data from the API 
        
        Returns:
                raw_data (dictionary): Dictionary for sensor data.
        
        """
        req = requests.get(self.url)
        raw_data = req.json()
        return raw_data

class Transform():
    
    def __init__(self):
        pass
    
class Load():
    
    def __init__(self):
        pass 


