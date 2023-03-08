import akshare as ak
from loguru import logger
import os

file_name_list_with_suffix = os.listdir(
    r"C:\Users\albert\PycharmProjects\ms_zqtz\data\updated_stock_daily_data"
)
file_name_list = [item.split(".")[0] for item in file_name_list_with_suffix]


logger.add("stock_download_updated_{time}.log")

stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()

stock_code_list = stock_zh_a_spot_em_df["代码"].tolist()

need_stock_list = list(set(stock_code_list) - set(file_name_list))

for stock in need_stock_list:
    logger.info(f"开始下载股票 {stock} 的数据")
    try:
        stock_zh_a_hist_df = ak.stock_zh_a_hist(
            symbol=stock, start_date="20230308", end_date="20230308"
        )
        logger.info(f"下载股票 {stock} 的数据成功")
    except:
        logger.error(f"股票 {stock} 的数据下载失败")
        continue
    stock_zh_a_hist_df.rename(
        columns={
            "日期": "date",
            "开盘": "open",
            "收盘": "close",
            "最高": "high",
            "最低": "low",
            "成交量": "volume",
            "成交额": "amount",
            "振幅": "zf",
            "涨跌幅": "zdf",
            "涨跌额": "zde",
            "换手率": "turnover",
        },
        inplace=True,
    )
    stock_zh_a_hist_df.to_csv(
        rf"C:\Users\albert\PycharmProjects\ms_zqtz\data\updated_stock_daily_data\{stock}.csv",
        index=False,
    )
