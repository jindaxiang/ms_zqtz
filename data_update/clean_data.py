import pandas as pd
import akshare as ak

temp_df = pd.read_csv(r"C:\Users\albert\PycharmProjects\ms_zqtz\data_update\a_updated_stock_with_name.csv", dtype={"symbol": str, "date": str})
temp_df = temp_df[~(temp_df['date']=="2023-02-01")]
# temp_df.to_csv("a_updated_stock_with_name.csv", index=False)
