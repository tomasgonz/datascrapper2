import random

colors =[    
'#FA1857',
'#5430F1',
'#2CC775',
'#F4CA04',
'#ABFF3F',
'#491238',
'#C726AD',
'#774502',
'#15F736',
'#C662C2',
'#C36697',
'#CA062D',
'#C0BE0C',
'#9C74BC',
'#3A5B15',
'#BDC335',
'#2BE34B',
'#F05B5A',
'#E2E9C0',
'#FEC401',
'#364C02',
'#7E7D1C',
'#A903A3',
'#0D289B',
'#B05BA5',
'#571203',
'#907902',
'#C01C65',
'#80640E',
'#D8B2AA',
'#00BDFB',
'#2BE380',
'#C90EFF',
'#238103',
'#1A6ED8',
'#577752',
'#71D824',
'#F31E28',
'#DD7CF7',
'#1B59B3',
'#0AE607',
'#E528C3',
'#B7CCD5',
'#538314',
'#62B8C3',
'#B4266D',
'#A55583',
'#941CA5',
'#D460F3',
'#BEC935',
'#1BFAD7',
'#7413E8',
'#C552C2',
'#463EAE',
'#E8E363',
'#A5677A',
'#D2E2D6',
'#745690',
'#E4F1CE',
'#8860DD',
'#F3FA7F',
'#4D1A61',
'#04F61C',
'#2602E4',
'#AC1012',
'#484601',
'#8547ED',
'#19DCF0',
'#DD7B36',
'#EA6144',
'#6C10F1',
'#F066C1',
'#EB1A73',
'#B60863',
'#29A7C1',
'#05AF25',
'#A24157',
'#5F4210',
'#C7C760',
'#B84190',
'#84EAB3',
'#AB6F14',
'#C0BB39',
'#135EF0',
'#6A6205',
'#3CEEE4',
'#05AE87',
'#B5365F',
'#257E6E',
'#031D8E',
'#31FDFC',
'#3BE1B5',
'#B3D9EC',
'#86A0AA',
'#D1E432',
'#051682',
'#61BFE4',
'#69B27B',
'#EB4528'
]


def color_generator():    
    print ("[")

    for i in range(1,100):
        r = lambda: random.randint(0,255)
        print("'#%02X%02X%02X,'" % (r(),r(),r()))
    print ("]")