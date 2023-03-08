import pandas as pd
import akshare as ak

temp_df = pd.read_csv(r"C:\Users\albert\PycharmProjects\ms_zqtz\data_update\a_updated_stock_daily.csv", dtype={"symbol": str})
stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
stock_name_list_with_str = stock_zh_a_spot_em_df['名称'].tolist()
stock_code_list_with_str = stock_zh_a_spot_em_df['代码'].tolist()
stock_name_list = [item.replace(" ", "").strip() for item in stock_name_list_with_str]
stock_code_list = [item.strip() for item in stock_code_list_with_str]
code_name_map = dict(zip(stock_code_list, stock_name_list))

temp_df.insert(1, "name", temp_df['symbol'].map(code_name_map))
temp_df.to_csv("a_updated_stock_with_name.csv", index=False)
