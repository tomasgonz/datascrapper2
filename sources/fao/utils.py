from data.Frame import Frame
def json_to_frame(j):
    df = Frame()
    for r in j['data']:
        df.add_row(r)
    
    return df