'''add more consert'''
from fastapi import FastAPI, Form
from src.consert import Consert
from datetime import datetime
@app.get("/add_consert", respons_model=Consert)
def add_consert(kname: str = Form(...),
                c_date: datetime = datetime.strptime(Form(...)),
                comment: str = Form(...),
                location: int = Form(...),
                orgnizer: int = Form(...),
                price_str: str = Form(...),
                time_str: str = Form(...), # irregular time
                type: int = Form(...)):
    #create the consert object
    Consert(kname, c_date, comment, location, orgnizer, price_str, time_str, type)
    #add to the database and add ID
    return  Consert
