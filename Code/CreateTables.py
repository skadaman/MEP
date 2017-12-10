'''Creating db connection'''
from sqlalchemy import create_engine

usern='root'
p='MEP2017'
host='localhost:3306'
db="sys"
e_string='mysql+pymysql://'+usern+":"+p+"@"+host+"/"+db
engine = create_engine(e_string)
connection = engine.connect()
''' creating tables '''
from sqlalchemy import (Table, MetaData,Column, TEXT, INTEGER,DATETIME,VARCHAR, ForeignKey,func)

metadata=MetaData()

country_table=Table("country", metadata,
                    Column('country_id',INTEGER(),primary_key=True,unique=True),
                    Column('c_code',VARCHAR(length=3),unique=True),
                    Column('description',TEXT())
                    )

zone_table=Table("zone",metadata,
                 Column('zone_id',INTEGER(),primary_key=True,unique=True),
                 Column('country_id',None,ForeignKey('country.country_id')),
                 Column('zonelabel_1',TEXT()),
                 Column('zonelabel_2',TEXT()),
                 Column('zonelabel_3',TEXT()),
                 Column('lattitude',INTEGER()),
                 Column('longitude',INTEGER())
                 )

node_table=Table("node", metadata,
                 Column('node_id',INTEGER(),primary_key=True,unique=True),
                 Column('country_id',None,ForeignKey('country.country_id')),
                 Column('node_code',VARCHAR(length=15),nullable=False),
                 Column('Description',TEXT()),
                 Column('zone',None,ForeignKey('zone.zone_id')),
                 Column('node_details',TEXT())
                 )
currency_table=Table("currency", metadata,
                     Column('currency_id',INTEGER(),primary_key=True,unique=True),
                     Column('currency_code',VARCHAR(length=3)),
                     Column('country_id',None,ForeignKey('country.country_id'))
                     )

load_table=Table('loadid', metadata,
                 Column('load_id',INTEGER(),primary_key=True,unique=True),
                 Column('node_id',None,ForeignKey('node.node_id')),
                 Column('description',TEXT())
                 )
loaddata_table=Table('loaddata',metadata,
                     Column('lkey',INTEGER(),index=True,unique=True),
                     Column('dt',DATETIME(),nullable=False),
                     Column('value',INTEGER(),nullable=False),
                     Column('created',DATETIME),
                     Column('updated',DATETIME,onupdate=func.NOW())
                     )

anciid_table=Table('ancitype',metadata,
                   Column('anci_id',INTEGER(),primary_key=True,unique=True),
                   Column('country_id',None,ForeignKey('country.country_id')),
                   Column('description',TEXT()),
                   Column('details',TEXT())
                   )
ancidata_table=Table('ancidata',metadata,
                     Column('akey',INTEGER(),index=True,unique=True),
                     Column('dt',DATETIME(),nullable=False),
                     Column('zone_id',None,ForeignKey('zone.zone_id')),
                     Column('country_id',None,ForeignKey('country.country_id')),
                     Column('currency_id',None,ForeignKey('currency.currency_id')),
                     Column('value', INTEGER(), nullable=False),
                     Column('created', DATETIME),
                     Column('updated', DATETIME, onupdate=func.NOW())
                    )
da_data = Table('dapower', metadata,
                Column('dapkey', INTEGER(), index=True),
                Column('dt', DATETIME(), nullable=False),
                Column('zone_id', None, ForeignKey('zone.zone_id')),
                Column('country_id', None, ForeignKey('country.country_id')),
                Column('currency_id', None, ForeignKey('currency.currency_id')),
                Column('value', INTEGER(), nullable=False),
                Column('created', DATETIME),
                Column('updated', DATETIME, onupdate=func.NOW())
                )
rt_data = Table('rtpower', metadata,
                Column('dtpkey', INTEGER(), index=True),
                Column('dt', DATETIME(), nullable=False),
                Column('zone_id', None, ForeignKey('zone.zone_id')),
                Column('country_id', None, ForeignKey('country.country_id')),
                Column('currency_id', None, ForeignKey('currency.currency_id')),
                Column('value', INTEGER(), nullable=False),
                Column('created', DATETIME),
                Column('updated', DATETIME, onupdate=func.NOW())
                )
metadata.create_all(engine)

