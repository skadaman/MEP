#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:02:41 2018

@author: SKadamany
"""

import pandas as pd

raw_data=pd.read_excel('/Users/W1/MEP/MEP/Docs/Node_Catalog.xlsx',header=1,
                       usecols=[0,3,4,5,14,15])
raw_data['node_details']=raw_data['SISTEMA']+','+raw_data['ESTADO']+','+raw_data['LOCALIDAD']
raw_data['node_details']=raw_data['node_details'].apply(lambda x: x.strip())
raw_data['kv']=raw_data['NIVEL DE TENSION (kV)'].apply(lambda x:str(x))
raw_data['desc']=raw_data['NOMBRE']+","+raw_data['kv']

from sqlalchemy import create_engine

usern='root'
p='MEP2017'
host='localhost:3306'
db="sys"
e_string='mysql+pymysql://'+usern+":"+p+"@"+host+"/"+db
engine = create_engine(e_string)
connection = engine.connect()

from sqlalchemy import insert, Table,MetaData
meta=MetaData()
node=Table('node',meta,autoload=True,autoload_with=engine)
for i in raw_data.index:
    stmt=insert(node).values(node_code=raw_data['CLAVE'][i],
                 country_id=2,
                 Description=raw_data['desc'][i],
                 zone=raw_data['ESTADO'][i],
                 node_details=raw_data['node_details'][i])
    result_proxy = connection.execute(stmt) 
    print(raw_data['CLAVE'][i])

