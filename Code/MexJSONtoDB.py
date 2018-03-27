import glob
from datetime import timedelta,datetime
from time import time,mktime,strptime
import numpy as np
import json

def MEP_ParseUpload(report, process):
    from sqlalchemy import create_engine
    usern='root'
    p='MEP2017'
    host='localhost:3306'
    db="sys"
    e_string='mysql+pymysql://'+usern+":"+p+"@"+host+"/"+db
    engine = create_engine(e_string)
    connection = engine.connect()

    from sqlalchemy import insert,MetaData,Table,select
    metadata=MetaData()
    node_table= Table('node',metadata,
                      autoload=True, autoload_with=engine)
    if np.logical_and(report=="PML",process=="DA"):
        dapowerfiles=glob.iglob(
                '/Users/W1/MEP/MEP/CENACEdata/PML*MDA*.json')
        for f in dapowerfiles:
            data=json.load(open(f))
            for r in data['Resultados']:
                code= r['clv_nodo']
                stmnt=select([node_table])
                stmnt=stmnt.where(node_table.columns.node_code==code)
                result_proxy=connection.execute(stmnt)
                results=result_proxy.fetchone()
                node=results[0]
                for v in r['Valores']:
                    d=strptime(v['fecha'],'%Y-%m-%d')
                    d=datetime.fromtimestamp(mktime(d))
                    date_time=d+timedelta(hours=int(v['hora'])-1)
                    price= v['pml']
                    
                    da_table= Table('dapower',metadata,
                                    autoload=True, autoload_with=engine)
                    stmt=insert(da_table).values(dt=date_time,
                                                 country_id=2,
                                                 currency_id=2,
                                                 value=price,
                                                 node_id=node)

                    result_proxy = connection.execute(stmt)
    elif np.logical_and(report=="PML",process=="RT"):
        rtpowerfiles = glob.iglob('/Users/W1/MEP/MEP/CENACEdata/PML*MTR*.json')
        for f in rtpowerfiles:
            data=json.load(open(f))
            for r in data['Resultados']
                code= r['clv_nodo']
                stmnt=select([node_table])
                stmnt=stmnt.where(node_table.columns.node_code==code)
                result_proxy=connection.execute(stmnt)
                results=result_proxy.fetchone()
                node=results[0]
                for v in r['Valores']:
                    d=strptime(v['fecha'],'%Y-%m-%d')
                    d=datetime.fromtimestamp(mktime(d))
                    date_time=d+timedelta(hours=int(v['hora'])-1)
                    price= v['pml']
                    
                    
                    rt_table= Table('rtpower',metadata,
                                    autoload=True, autoload_with=engine)
                    stmt=insert(rt_table).values(dt=date_time,
                                                 country_id=2,
                                                 currency_id=2,
                                                 value=price,
                                                 node_id=node)

                    result_proxy = connection.execute(stmt)
    else:
        raise ValueError('Either the report type is not yet supported or the process was not correctly specified')

