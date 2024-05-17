import pandas as pd


# 读取两个Excel文件
df_medical_directory = pd.read_excel(r'D:\BaiduSyncdisk\产品项目单据\医保目录\药品目录20220623\药品目录20220623.xls')
df_national_directory = pd.read_excel(r'D:\BaiduSyncdisk\产品项目单据\医保目录\药品目录20220623\中成药.xlsx')

# 假设'医保编码'列在df_medical_directory中对应于'药品代码'列在df_national_directory中
# 首先确保两者的列名一致以便于匹配
df_medical_directory.rename(columns={'医保编码': '药品代码'}, inplace=True)

# 进行左连接，以确保西药国家目录中的所有记录都被保留
merged_df = pd.merge(df_national_directory, df_medical_directory[['药品代码', '支付标准']], on='药品代码', how='left')

# 更新支付价列，注意如果支付标准存在空值，这一步可能需要额外处理
merged_df['支付价'] = merged_df['支付标准']

# 如果有需要，可以删除合并后多余的列，比如'支付标准'，这里假设保留原表结构，不删除
# merged_df.drop(columns=['支付标准'], inplace=True)

# 将结果保存回西药国家目录表
merged_df.to_excel('D:\BaiduSyncdisk\产品项目单据\医保目录\药品目录20220623\更新支付价后的中成药国家目录.xlsx', index=False)