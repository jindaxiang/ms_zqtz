import os
from datetime import datetime
import pandas as pd
from loguru import logger

logger.add('stock_merge_{time}.log')

file_name_list = os.listdir(r"C:\Users\albert\PycharmProjects\ms_zqtz\data\updated_stock_daily_data")
created_time_var = datetime.now().isoformat()
big_df = pd.DataFrame()

for file_name in file_name_list:
    logger.info(f"开始合并股票 {file_name.split('.')[0]} 的数据")
    try:
        temp_df = pd.read_csv(fr"C:\Users\albert\PycharmProjects\ms_zqtz\data\updated_stock_daily_data\{file_name}")
    except pd.errors.EmptyDataError as e:
        logger.info(f"股票 {file_name.split('.')[0]} 的数据为空")
        continue
    temp_df['created_time'] = created_time_var
    temp_df.insert(0, "symbol", file_name.split(".")[0])
    big_df = pd.concat([big_df, temp_df], ignore_index=True)

big_df.to_csv("a_stock_daily.csv", index=False)
