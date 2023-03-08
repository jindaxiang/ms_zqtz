import pandas as pd
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import text, insert, Table, delete

metadata_obj = MetaData()

engine = create_engine("mysql+pymysql://root:king@localhost/zqtz_stock")

some_table = Table("a_stock_with_name", metadata_obj, autoload_with=engine)



with engine.connect() as conn:
    result = conn.execute(text("select * from a_stock_with_name where symbol=000001"))
    temp_data = result.fetchall()
    print(temp_data)

temp_df = pd.DataFrame(temp_data)

local_temp_df = pd.read_csv(r"C:\Users\albert\PycharmProjects\ms_zqtz\data_update\a_updated_stock_with_name.csv",
                            dtype={"symbol": str})
local_temp_df['date'] = pd.to_datetime(local_temp_df['date']).dt.date
local_temp_df['created_time'] = pd.to_datetime(local_temp_df['created_time'])

tuple(local_temp_df.to_dict(orient="records")[0].values())

with engine.connect() as conn:
    result = conn.execute(
        insert(some_table),
        local_temp_df.to_dict(orient="records"),
    )
    conn.commit()

with engine.connect() as conn:
    result = conn.execute(
        delete(some_table).
        where(some_table.c.date == pd.Timestamp("20230202")),
    )
    conn.commit()
