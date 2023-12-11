# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:54:33 2023

@author: iyino
"""

import pandas as pd
data1 = pd.read_csv("STEG_BILLING_HISTORY.csv",low_memory=False)
#check data type
data_type = data1.dtypes
print(data1)



#display information about dataframe
datax = data1.info()
print(data1)

#display the front rows of the datframe
data1_head = data1.head()

#display the laat few rows of dataframe
data1_tail = data1.tail()

data1_first_10 = data1.head(10)
print(data1_first_10 )

client_0_bils = data1.iloc[:10, :10]
print(client_0_bils)


client_0_bils_nullcount = client_0_bils.isnull().sum()
client_0_bils_total_null_count = client_0_bils.isnull().sum().sum
data1_total_null_account = data1.isnull().sum().sum

catergorical_features = data1.select_dtypes(include = ["object"]).columns
num_categorical_features= len(catergorical_features)
print(f"number of catergorical features:{num_categorical_features}")

memory_consumption = data1.memory_usage(deep = True).sum()
print(f"memory_consumption: {memory_consumption} bytes")

missing_values = data1.isnull().sum()
print(missing_values)

numeric_descriptive = data1.describe()
print(numeric_descriptive)

select_bill1 = data1[data1["client_id"]== "train_client_0"]
select_bill2 =data1.loc[data1["client_id"]=="train_client_0"]

from sklearn.preprocessing import LabelEncoder
counter_type_column = data1["counter_type"]
label_encoder = data1()
numeric_counter_type = label_encoder.fit_transform(counter_type_column)
data1["object"] = numeric_counter_type
data1 = data1.drop("counter_statue", axis =1 )
