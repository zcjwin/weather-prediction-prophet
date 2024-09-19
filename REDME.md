# 数据预测项目 - 使用Prophet进行时间序列分析

## 项目简介
该项目旨在使用Facebook的Prophet库对给定的数据集进行时间序列分析和预测。主要目标是基于历史数据对未来一段时间内的趋势进行预测。

## 技术栈
- Python
- Pandas: 用于数据处理
- Prophet: 时间序列预测库

## 数据准备
1. 数据集存储在`data.csv`文件中。
2. 数据集包含两列：
   - `date`: 日期
   - `cases`: 需要预测的目标值

## 步骤说明
1. **读取数据**
   - 使用Pandas读取CSV文件，并将日期列解析为日期格式。
   - 将列名调整为Prophet所需的格式`"ds"`和`"y"`。

2. **模型训练**
   - 创建一个Prophet模型实例。
   - 使用调整后的数据拟合模型。

3. **未来预测**
   - 生成未来365天的数据框。
   - 对未来数据进行预测，并输出预测结果。

## 运行示例
```python
# !pip install pandas prophet
```

```python
import pandas as pd
from prophet import Prophet
```
### 读取数据
```python
path = 'data.csv'
data = pd.read_csv(path, parse_dates=["ds"])
data_new = data.rename(columns={"date": "ds", "cases": "y"})
```
### 创建并训练模型
```python
m = Prophet() 
m.fit(data_new)
```
### 生成未来数据框
```python
future = m.make_future_dataframe(periods=365)
```
### 进行预测
```python
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
```

## 注意事项
- 确保`data.csv`文件存在于指定路径下。
- 根据实际需求调整预测周期（`periods=365`）。


