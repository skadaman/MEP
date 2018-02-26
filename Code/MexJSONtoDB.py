import glob
import pandas as pd
#import numpy as np
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

    from sqlalchemy import insert,MetaData,Table

    if np.logical_and(report=="PML",process=="DA"):
        dapowerfiles=glob.iglob('/Users/W1/MEP/MEP/CENACEdata/PML*MDA*.json')
        for f in dapowerfiles:
            data=jason.load(f)
            for r in data['Resultados']
                nodecode= {r['clv_nodo']}
                qstmnt='Select node_id from node where node_code='+nodecode
                result_proxy=connection.execute(qstmnt)
                results=result_proxy.fetchone()
                nodeid=results[0].node_id
            for r in data['Resultados']:
                for v in r['Valores']:
                    d=datetime.strptime(v['fecha'],'%Y-%m-%d')
                    dt=d+timedelta(hours=int(v['hora'])-1)
                    price= v['pml']
                    
                    metadata=MetaData()
                    da_table= Table('dapower',metadata, autoload=True, autoload_with=engine)
                    stmt=insert(da_table)
                    harvested_vlist=[{'dt':dt,
                                      'country_id':2,
                                      'currency_id':2,
                                      'value':price,
                                      'node_id':nodeid}
                                    ]
    elif np.logical_and(report=="PML",process=="RT"):
        rtpowerfiles=glob.iglob('/Users/W1/MEP/MEP/CENACEdata/PML*MTR*.json')
        rt_list = []
        for f in rtpowerfiles:
            df = pd.read_json(f,orient='split')
            rt_list.append(df)
            rt_power=pd.concat(rt_list)
        return rt_power
    else:
        raise ValueError('Either the report type is not yet supported or the process was not correctly specified')

