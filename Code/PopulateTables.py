'''Creating db connection'''
from sqlalchemy import create_engine
usern='root'
p='MEP2017'
host='localhost:3306'
db="sys"
e_string='mysql+pymysql://'+usern+":"+p+"@"+host+"/"+db
engine = create_engine(e_string)
connection = engine.connect()

from sqlalchemy import insert,MetaData,Table

metadata=MetaData()
country_table= Table('country',metadata, autoload=True, autoload_with=engine)
stmt=insert(country_table)
country_vlist=[{'c_code':'COL','description':'Colombia'},
               {'c_code':'MEX','description':'Mexico'},
               {'c_code':'USA','description':'Unites States'},
               {'c_code':'BRZ','description':'Brazil'},
               {'c_code':'PAN','description':'Panama'},
               {'c_code':'DOM','description':'Dominican Republic'},
               {'c_code':'CHL','description':'Chile'}
               ]
result_proxy=connection.execute(stmt,country_vlist)

currency_table=Table('currency',metadata, autoload=True, autoload_with=engine)
stmt2=insert(currency_table)
currency_vlist=[{'currency_code':'COP','country_id':1},
                {'currency_code':'MXN','country_id':2},
                {'currency_code':'USD','country_id':3},
                {'currency_code':'BRL','country_id':4},
                {'currency_code':'PAB','country_id':5},
                {'currency_code':'DOP','country_id':6},
                {'currency_code':'CLP','country_id':7}
                ]
result_proxy2=connection.execute(stmt2,currency_vlist)