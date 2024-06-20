import pandas as pd

# 讀取CSV文件
df = pd.read_csv('TJ_emotion_data_2013_2023_04_30_2024.csv')

# 將date列轉換為datetime格式
df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')

# 過濾出date是2018年的數據
df_2018 = df[df['date'].dt.year == 2018]

# 將篩選後的數據保存到新的CSV文件中
df_2018.to_csv('2018_hiker_journal.csv', index=False)

print("篩選和保存完成！")
