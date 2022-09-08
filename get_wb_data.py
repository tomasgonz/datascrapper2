import sys
sys.path.append("../..")
from sources import *
from data.Frame import Frame
from data.Stats import calculate_weighted_average as wa
from geo.countries import Countries
from geo.data import world
from pymongo import MongoClient
client = MongoClient('stats.whereistomas.org', username='root', password='Root!0676')
db = client["stats"]
import time
c = Countries()
c.load_wb()
from sources import worldbank as wb
# wb.indicators.load_all()

indicators_to_retrieve = [{"indicator": "SP.POP.TOTL", "aggregation": True, "weight": "None"},
                          {"indicator": "SP.RUR.TOTL", "aggregation": True, "weight": "None" },
                          {"indicator": "AG.LND.TOTL.K2", "aggregation": True, "weight": "None" },
                         {"indicator": "NY.GDP.MKTP.CD", "aggregation": True, "weight": "None" },
                         {"indicator": "SP.RUR.TOTL.ZS", "aggregation": True, "weight": "SPPOPTOTL" },
                          {"indicator": "AG.LND.ARBL.ZS", "aggregation": True, "weight": "AGLNDTOTLK2" },
                          {"indicator": "SH.DYN.MORT", "aggregation": False, "weight": "SPPOPTOTL"}, 
                          {"indicator":"EN.ATM.CO2E.KT", "aggregation": False, "weight": "None"}, 
                          {"indicator":"EN.ATM.CO2E.PC", "aggregation": False, "weight": "SPPOPTOTL"}, 
                          {"indicator": "EG.ELC.ACCS.ZS", "aggregation": False, "weight": "SPPOPTOTL"} , 
                          {"indicator": "DT.ODA.ODAT.GN.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "DT.ODA.ODAT.GI.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "DT.ODA.ODAT.PC.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "GC.XPN.TOTL.GD.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "GC.REV.XGRT.GD.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "BN.CAB.XOKA.CD", "aggregation": True, "weight": "None"},
                          {"indicator": "BX.KLT.DINV.CD.WD", "aggregation": True, "weight": "None"}, 
                          {"indicator": "DT.DOD.DIMF.CD", "aggregation": True, "weight": "None"}, 
                          {"indicator": "FB.ATM.TOTL.P5", "aggregation": False, "weight": "SPPOPTOTL"}, 
                          {"indicator": "FB.BNK.CAPA.ZS", "aggregation": False, "weight": "None"}, 
                          {"indicator": "FB.AST.NPER.ZS", "aggregation": False, "weight": "None"}, 
                          {"indicator": "FB.CBK.BRCH.P5", "aggregation": False, "weight": "SPPOPTOTL"}, 
                          {"indicator": "FS.AST.DOMS.GD.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"}, 
                          {"indicator": "CM.MKT.LCAP.GD.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"}, 
                          {"indicator": "CM.MKT.LCAP.CD", "aggregation": False, "weight": "None"}, 
                          {"indicator": "SE.ENR.PRSC.FM.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "NV.IND.MANF.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "NV.SRV.TOTL.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "NV.AGR.TOTL.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "NY.GDP.MKTP.KD.ZG", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "NY.GDP.PCAP.KD.ZG", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "DT.DOD.DECT.GN.ZS", "aggregation": True, "weight": "NYGDPMKTPCD"},
                          {"indicator": "NE.EXP.GNFS.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "NE.EXP.GNFS.CD", "aggregation": True, "weight": "None"},
                          {"indicator": "NE.IMP.GNFS.CD", "aggregation": True, "weight": "None"},
                          {"indicator": "FP.CPI.TOTL.ZG", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "SL.TLF.TOTL.IN", "aggregation": True, "weight": "None"},
                          {"indicator": "FP.CPI.TOTL.ZG", "aggregation": True, "weight": "NYGDPMKTPCD"},
                          {"indicator": "EG.ELC.RNEW.ZS", "aggregation": False, "weight": "EGELCRNWXKH"},
                          {"indicator": "EG.ELC.RNWX.KH", "aggregation": True, "weight": "None"},
                          {"indicator": "NY.GDP.TOTL.RT.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "EN.ATM.GHGT.KT.CE", "aggregation": True, "weight": "None"},
                          {"indicator": "BX.GRT.TECH.CD.WD", "aggregation": True, "weight": "None"},
                          {"indicator": "FM.LBL.BMNY.GD.ZS", "aggregation": False, "weight": "None"},
                          {"indicator": "FS.AST.PRVT.GD.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "BX.TRF.PWKR.CD.DT", "aggregation": True, "weight": "None"},
                          {"indicator": "FI.RES.TOTL.CD", "aggregation": True, "weight": "None"},
                          {"indicator": "SP.ADO.TFRT", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "SP.ADO.TFRT", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "SE.PRM.UNER.MA", "aggregation": False, "weight": "None"},
                          {"indicator": "SE.PRM.UNER.FE", "aggregation": False, "weight": "None"},
                          {"indicator": "SP.POP.DPND", "aggregation": False, "weight": "None"},
                          {"indicator": "EG.USE.ELEC.KH.PC", "aggregation": False, "weight": "None"},
                          {"indicator": "EN.POP.SLUM.UR.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "TX.VAL.FUEL.ZS.UN", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "TX.VAL.MRCH.CD.WT", "aggregation": True, "weight": "None"},
                          {"indicator": "ST.INT.RCPT.XP.ZS", "aggregation": False, "weight": "TXVALMRCHCDWT"},
                          {"indicator": "TG.VAL.TOTL.GD.ZS", "aggregation": False, "weight": "NYGDPMKTPCD"},
                          {"indicator": "MS.MIL.XPND.ZS", "aggregation": False, "weight": "NECONGOVTCD"},
                          {"indicator": "NE.CON.GOVT.CD", "aggregation": False, "weight": "None"},
                          {"indicator": "SG.GEN.PARL.ZS", "aggregation": False, "weight": "None"},
                          {"indicator": "IP.JRN.ARTC.SC", "aggregation": True, "weight": "None"},
                          {"indicator": "SP.URB.TOTL.IN.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "SH.STA.MMRT", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "SE.SEC.PROG.FE.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "SH.XPD.CHEX.GD.ZS", "aggregation": True, "weight": "SPPOPTOTL"},
                          {"indicator": "SH.XPD.CHEX.PC.CD", "aggregation": True, "weight": "SPPOPTOTL"},
                          {"indicator": "SH.XPD.EHEX.PC.CD", "aggregation": True, "weight": "SPPOPTOTL"},
                          {"indicator": "SN.ITK.DEFC.ZS", "aggregation": False, "weight": "SPPOPTOTL"},
                          {"indicator": "SP.DYN.LE00.FE.IN", "aggregation": True, "weight": "SPPOPTOTL"}]

def process_wb_data(data):
    new_data =[];
    
    for dp in data:
        if dp['entity'] in world:
            new_data.append({'entity':dp['entity'].lower(), 'date': dp['date'], 'value': dp['value']})
        else:
            pass
        
    return new_data

def get_wb_data():
    years= list(map(str, list(range(1960,2021))))

    for ind in indicators_to_retrieve:    
        try:
            data = wb.indicators.get(name=ind['indicator'], 
                                    years=years, 
                                    countries=world)

            ddata = process_wb_data(data['data'])
            time.sleep(1)        

            db["indicators"].update_one({ "name" : data['name']}, 
                        {"$set":{"name" : data['name'],
                                    "aggregation": ind["aggregation"],
                                    "weight": ind["weight"],
                                    "description" : data['description'], 
                                    "years" : years, 
                                    "sourceNote" : data['sourcenote'],
                                    "connector" : data['connector'],
                                    "source" : data['source'],
                                    "sourceurl" : data['sourceurl'], 
                                    "keyField" : "entity",
                                    "pivotField" : "date",
                                    "valueField" : "value",
                                    'data' : ddata}}, True)
            print(ind['indicator'] + " processed.")
            
        except ValueError:
            print("error in " + ind.name )
            print(ValueError)