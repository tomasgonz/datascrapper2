import requests
import zipfile
import io
import csv
from data.Frame import Frame
import re

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
            
            
        #return([d.split(',') for d in decoded_data])
        data = []        
        data.append(decoded_data[0].split(","))
        for d in decoded_data:         
            if(len(re.findall(r'"(.*?)"', d))) > 0:            
                data.append(re.findall(r'"(.*?)"', d))

        return(data)

    def __get_zip_as_data_frame__(self, url_zip, _print = False):
        df = Frame()    

        if _print == True:
            print("Downloading from %s" % (url_zip))

        data = self.__get_zip__(url_zip)
        
        for i in range(len(data)-1):
            row = {}
            for j in range(len(data[i])-1):
                
                      
                row[data[0][j]] = data[i][j]
                if _print == True:
                    print ("Position (%s:%s)" % (i, j))
            df.add_row(row)
        
        return(df)
    
    def __load_data__(self, _print = False):
        self.data = self.__get_zip_as_data_frame__(self.FileLocation, _print=_print)

    def get_data(self, _print = False):
        self.__load_data__(_print = _print)
        return self.data

    def print(self):
        print("----- \n %s - %s \n\n %s \n\n %s \n\n %s -----" % (self.DatasetCode, self.DatasetName, self.DatasetDescription, self.DateUpdate, self.FileRows))