import pandas as pd

data=pd.read_csv('customer_accounts.csv')
df=pd.DataFrame(data)
print(df)
print(df.columns)
print(data)
print(data.columns)
# df.dropna(inplace=True)

print(df.head(5))
print(df.tail(5))

print(df['customer_id'].nunique())
print(df['city'].nunique())
print(df.groupby('account_type').count())
print(df.groupby('account_type').size())
print(df.loc[df['city']=='Delhi'])
print(df.loc[df['balance'].isna()])

df['balance']=df['balance'].fillna(0)
df.sort_values(by='balance',ascending=False)

print(df)

print(df.loc[df['balance']>50000])
print(df.loc[df['last_txn_amount']<1000])
print(df.loc[(df['account_status']=='inactive') & (df['balance']!=0)])
print(df.loc[df['created_at']>"2023-01-01"])

print(df.loc[((df['city']=='Delhi')|(df['city']=='Mumbai'))&(df['account_status']=='active')])

print(df.loc[df['email'].isna()])


print(df[(df["account_type"] == "FD") &
   (df["balance"] > df[df["account_type"] == "FD"]["balance"].mean())])


print(df.groupby("customer_id").filter(lambda x: len(x) > 1))


print(df.loc[df['last_txn_amount'].isna()])
print(df.loc[df['account_status'].isna()])

print(df.groupby('customer_id')['balance'].sum())
print(df.groupby('city')['balance'].mean())

print(df.groupby('account_status')['account_status'].count())

print(df.groupby('account_status')['balance'].agg(['mean','max','min']))

print(df.loc[df['balance']>100000])
print(df.groupby('city').size().loc[lambda x: x > 2])
print(df.loc[df['balance'] == df['balance'].max()])
print((df.groupby('city')['balance'].sum()).sort_values().tail(1))
print(df.groupby('account_type')['last_txn_amount'].mean())
print(df['city'])
df['city']=df['city'].fillna('unknown')
print(df['city'])

print(df['account_status'])
df['account_status']=df['account_status'].fillna('inactive')
print(df['account_status'])


print(df['last_txn_amount'])
df['last_txn_amount']=df['last_txn_amount'].fillna(df['last_txn_amount'].median())
print(df['last_txn_amount'])

df['balance'].dropna(inplace=True)
df['last_txn_amount'].dropna(inplace=True)
print(df[df.isna().sum(axis=1) > 1])
df['created_at']=pd.to_datetime(df['created_at'],errors='coerce')