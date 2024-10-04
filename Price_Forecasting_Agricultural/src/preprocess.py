
import pandas as pd


from config import *

project_path = "C://Users//admin//PycharmProjects//Dacon//Price_Forecasting_Agricultural"
train_raw_csv_path = project_path + "//data//train//train.csv"
train_meta_csv_path1 = project_path + "//data//train//meta//TRAIN_산지공판장_2018-2021.csv"
train_meta_csv_path2 = project_path + "//data//train//meta//TRAIN_전국도매_2018-2021.csv"

pre_train_raw_csv_path = project_path + "//data//train//train_preprocessed.csv"
pre_train_meta_csv_path1 = project_path + "//data//train//meta//TRAIN_산지공판장_preprocessed.csv"
pre_train_meta_csv_path2 = project_path + "//data//train//meta//TRAIN_전국도매_preprocessed.csv"


df_raw = pd.read_csv(train_raw_csv_path)
df_meta1 = pd.read_csv(train_meta_csv_path1)
df_meta2 = pd.read_csv(train_meta_csv_path2)


filtered_raw_df = {}
target_column_name = TEST_TARGET_POOL[0]
for idx in range(1, len(TEST_TARGET_POOL)):    
    condition = TEST_TARGET_POOL[idx]
    name = condition[0]

    
    # 조건에 맞는 데이터프레임 필터링
    filtered_df = df_raw[
        (df_raw[target_column_name[0]] == condition[0]) &
        (df_raw[target_column_name[1]] == condition[1]) &
        (df_raw[target_column_name[2]] == condition[2]) &
        (df_raw[target_column_name[3]] == condition[3])
    ]
    
    # 필터링된 데이터프레임을 딕셔너리에 저장
    
    if name in filtered_raw_df:
        filtered_raw_df[name].concat(filtered_df, inplace=True)
    else:
        filtered_raw_df[name] = filtered_df
    # print(f'품목명(key) = {condition[0]}')
    # print(f'df shape = {filtered_df.shape}')
    # print('\ndf')
    # print(filtered_df)
    # print()


filtered_meta_df = {}
meta1_target = ['총반입량(kg)', '총거래금액(원)', '평균가(원/kg)', '중간가(원/kg)', '최저가(원/kg)',
       '최고가(원/kg)', '경매 건수', '전순 평균가격(원) PreVious SOON',
       '전달 평균가격(원) PreVious MMonth', '전년 평균가격(원) PreVious YeaR',
       '평년 평균가격(원) Common Year SOON']
meta2_target = ['총반입량(kg)',
       '총거래금액(원)', '평균가(원/kg)', '고가(20%) 평균가', '중가(60%) 평균가 ', '저가(20%) 평균가',
       '중간가(원/kg)', '최저가(원/kg)', '최고가(원/kg)', '경매 건수',
       '전순 평균가격(원) PreVious SOON', '전달 평균가격(원) PreVious MMonth',
       '전년 평균가격(원) PreVious YeaR', '평년 평균가격(원) Common Year SOON']


for name, df_temp_raw in filtered_raw_df.items():
    filtered_df1 = df_meta1[
        (df_meta1['품목명'].isin(df_temp_raw['품목명'])) &
        (df_meta1['품종명'].isin(df_temp_raw['품종명']))
    ]
    filtered_df2 = df_meta2[
        (df_meta2['품목명'].isin(df_temp_raw['품목명'])) &
        (df_meta2['품종명'].isin(df_temp_raw['품종명']))
    ]
    filtered_df1 = filtered_df1.groupby('시점')[meta1_target].mean()
    filtered_df2 = filtered_df2.groupby('시점')[meta2_target].mean()

    print('----------------------------------------- meta 1 -----------------------------------------')
    print(f'품목명(key) = {name}')
    print(f'df shape = {filtered_df1.shape}')
    print('\ndf')
    print(filtered_df1)
    print()

    print('----------------------------------------- meta 2 -----------------------------------------')
    print(f'품목명(key) = {name}')
    print(f'df shape = {filtered_df2.shape}')
    print('\ndf')
    print(filtered_df2)
    print()