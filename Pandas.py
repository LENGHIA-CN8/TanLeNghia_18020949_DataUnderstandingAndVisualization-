import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Example.csv')
print(df)

def classify(x):
    if "iPhone" in x :
        return "iPhone"
    elif "Samsung" in x :
        return "SamSung"
    elif "Vsmart" in x :
        return "Vsmart"
    elif "Oppo" in x :
        return "Oppo"
    elif "Xiaomi" in x:
        return "Xiaomi"
    elif "Panasonic" in x:
        return "Panasonic"
    else:
        return "Others"


# xử lí phần price
l= df.price.tolist()
for i in range(len(l)):
    l[i]=l[i].replace('đ','')
    l[i]=l[i].replace('.','')
    l[i]=int(l[i])
print(l)
df['price']=l
print(df)

#xử lí phần discount
d = df.discount.tolist()
for i in range(len(d)):
    if d[i] == 'Khong giam':
        d[i]=0
    else:
        d[i]=d[i].strip('-%')
        d[i]=float(d[i])
df['discount']=d
df['origin_price']=df['price']/(100-df['discount'])*100
print(df['origin_price'])
print(d)
#xu li phan brand
df['brand']=df['name'].apply(classify)
print(df['brand'])
brand_count = df['brand'].value_counts()
print(brand_count)



#histogram plot
plt.figure(1)
plt.ylabel('frequency')
hist=sns.distplot(df['price'],bins=50)

#reg plot
plt.figure(2)
scatter = sns.regplot(x='origin_price',y='discount',data=df)

#scatter
plt.figure(3)
# df['brand_color']=df['brand'].apply(recode)
# plt.scatter(x=df['price'],y=df['discount'],c=df['brand_color'],alpha=0.5)
sns.scatterplot(x='price',y='discount',hue='brand',data=df)

#count plot
plt.figure(4)
count=sns.countplot('brand',data=df)

plt.show()










# def recode(br):
#     if br == 'Iphone':
#         return '#31a354'
#     elif br == 'Samsung':
#         return '#e34a33'
#     elif br == 'Panasonic':
#         return '#8856a7'
#     else:
#         return '#dd1c77'

