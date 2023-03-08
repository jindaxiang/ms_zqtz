"""
创建股票板块分类
"""
import akshare as ak
import pandas as pd
import redis

# 链接服务器 Redis
# r = redis.Redis(host='101.201.107.239', port=6379, db=0, password="mssdk@028", decode_responses=True)

# 链接本地 Redis
r = redis.Redis(host='localhost', port=6379, db=5, decode_responses=True)

# 全部
stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
print(stock_zh_a_spot_em_df)

stock_zh_a_spot_em_df['代码'].tolist()
board_qb_map = dict(zip(stock_zh_a_spot_em_df['代码'].tolist(), [0]*len(stock_zh_a_spot_em_df)))
board_qb_df = pd.DataFrame.from_dict(board_qb_map, orient="index")
board_qb_df.reset_index(inplace=True)
board_qb_df.columns = [
    "symbol",
    "code"
]
board_qb_df['board'] = '全部'
board_qb_df.to_csv("board_qb.csv", index=False)

temp_list = board_qb_df['symbol'].tolist()
r.lpush('board:0', *temp_list)
t = r.lrange("board:0", 0, -1)
print(t)


# 上证A股
stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
print(stock_sh_a_spot_em_df)

stock_sh_a_spot_em_df['代码'].tolist()
board_sh_map = dict(zip(stock_sh_a_spot_em_df['代码'].tolist(), [1]*len(stock_sh_a_spot_em_df)))
board_sh_df = pd.DataFrame.from_dict(board_sh_map, orient="index")
board_sh_df.reset_index(inplace=True)
board_sh_df.columns = [
    "symbol",
    "code"
]
board_sh_df['board'] = '上证A股'
board_sh_df.to_csv("board_sh.csv", index=False)

temp_list = board_sh_df['symbol'].tolist()
r.lpush('board:1', *temp_list)
t = r.lrange("board:1", 0, -1)
print(t)


# 深证A股
stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
print(stock_sz_a_spot_em_df)

stock_sz_a_spot_em_df['代码'].tolist()
board_sz_map = dict(zip(stock_sz_a_spot_em_df['代码'].tolist(), [2]*len(stock_sz_a_spot_em_df)))
board_sz_df = pd.DataFrame.from_dict(board_sz_map, orient="index")
board_sz_df.reset_index(inplace=True)
board_sz_df.columns = [
    "symbol",
    "code"
]
board_sz_df['board'] = '深证A股'
board_sz_df.to_csv("board_sz.csv", index=False)

temp_list = board_sz_df['symbol'].tolist()
r.lpush('board:2', *temp_list)
t = r.lrange("board:2", 0, -1)
print(t)

# 北证A股
stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
print(stock_bj_a_spot_em_df)

stock_bj_a_spot_em_df['代码'].tolist()
board_bj_map = dict(zip(stock_bj_a_spot_em_df['代码'].tolist(), [3]*len(stock_bj_a_spot_em_df)))
board_bj_df = pd.DataFrame.from_dict(board_bj_map, orient="index")
board_bj_df.reset_index(inplace=True)
board_bj_df.columns = [
    "symbol",
    "code"
]
board_bj_df['board'] = '北证A股'
board_bj_df.to_csv("board_bj.csv", index=False)

temp_list = board_bj_df['symbol'].tolist()
r.lpush('board:3', *temp_list)
t = r.lrange("board:3", 0, -1)
print(t)

# 创业板
stock_cy_a_spot_em_df = ak.stock_cy_a_spot_em()
print(stock_cy_a_spot_em_df)

stock_cy_a_spot_em_df['代码'].tolist()
board_cyb_map = dict(zip(stock_cy_a_spot_em_df['代码'].tolist(), [4]*len(stock_cy_a_spot_em_df)))
board_cyb_df = pd.DataFrame.from_dict(board_cyb_map, orient="index")
board_cyb_df.reset_index(inplace=True)
board_cyb_df.columns = [
    "symbol",
    "code"
]
board_cyb_df['board'] = '创业板'
board_cyb_df.to_csv("board_cyb.csv", index=False)

temp_list = board_cyb_df['symbol'].tolist()
r.lpush('board:4', *temp_list)
t = r.lrange("board:4", 0, -1)
print(t)

# 科创板
stock_kc_a_spot_em_df = ak.stock_kc_a_spot_em()
print(stock_kc_a_spot_em_df)

stock_kc_a_spot_em_df['代码'].tolist()
board_kcb_map = dict(zip(stock_kc_a_spot_em_df['代码'].tolist(), [5]*len(stock_kc_a_spot_em_df)))
board_kcb_df = pd.DataFrame.from_dict(board_kcb_map, orient="index")
board_kcb_df.reset_index(inplace=True)
board_kcb_df.columns = [
    "symbol",
    "code"
]
board_kcb_df['board'] = '科创板'
board_kcb_df.to_csv("board_kcb.csv", index=False)

temp_list = board_kcb_df['symbol'].tolist()
r.lpush('board:5', *temp_list)
t = r.lrange("board:5", 0, -1)
print(t)
