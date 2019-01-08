import requests
import zipfile
import io
from data.Frame import Frame

class Dataset:

    def __init__(self):		
        self.DatasetCode = ""
        self.DatasetName = ""	
        self.Topic = ""
        self.DatasetDescription = ""
        self.Contact = ""
        self.Email = ""
        self.DateUpdate = ""
        self.CompressionFormat = ""
        self.FileType = ""
        self.FileSize = ""
        self.FileRows = ""
        self.FileLocation = ""
        self.data = Frame()

    def __get_zip__(self, url_zip):
        with zipfile.ZipFile(io.BytesIO(requests.get(url_zip).content)) as thezip:                        
            z = thezip.read(thezip.infolist()[0])
            decoded_data = z.decode('latin-1')
            decoded_data = decoded_data.split('\r\n')        
    
        return([d.split(',') for d in decoded_data])

    def __get_zip_as_data_frame__(self, url_zip):
        df = Frame()    
        data = self.__get_zip__(url_zip)
        
        for i in range(len(data)-1):
            row = {}
            for j in range(len(data[0])-1):
                row[data[0][j]] = data[i][j]        
        
            df.add_row(row)
        
        return(df)
    
    def __load_data__(self):
        self.data = self.__get_zip_as_data_frame__(self.FileLocation)