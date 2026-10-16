# import class from python script
from my_oracle import MyOracleDB

# create an object
my_oracle_object = MyOracleDB()
# open a connection
my_oracle_object.connect()
# print a retrieved datafraame
df = my_oracle_object.query_to_df("SELECT 1 as COLNAME, SYSDATE as datetime FROM dual")
print(df)
print(type(df))
print(df.dtypes)
# close connection
my_oracle_object.close()