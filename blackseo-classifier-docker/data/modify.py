import pandas as pd

# 读取原始的Excel文件
df = pd.read_excel('white_label.xlsx')

# 选择任意10行数据
selected_rows = df.sample(n=10)  # 从数据框中随机选择10行

# 将选定的数据保存为新的Excel文件
selected_rows.to_excel('white_label_2.xlsx', index=False)  # 将数据保存为新的Excel文件，不包括行索引