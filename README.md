# 证券投资系统开发

## 数据更新

通过 `C:\Users\albert\PycharmProjects\ms_zqtz\data_update` 来进行数据的更新
1. `update_data.py` 来进行增量数据的更新，需要设置好日期
2. `merge_data.py` 来进行增量数据的更新，需要设置好日期
3. `merge_name.py` 来进行增量数据的更新，需要设置好日期
4. 如果有重复数据，则使用 `clean_data`

## 环境准备

```
fastapi[all]  # 后续需要精简
redis
akshare
```

## 数据准备

### 下载数据

利用 AKShare 下载数据到本地，并存储到数据库（确定数据库的版本，由于数据量比较大，需要考虑分表）中，在
测试开发中，只考虑少量股票。

1. 只考虑未复权数据
2. 只考虑日频率数据
3. 分钟数据实时采集及模拟

### 更新数据

对数据做定时更新功能，此部分考虑用 celery 做异步及定时任务，消息队列选择 redis

### 

定时获取数据利用 airflow 来做