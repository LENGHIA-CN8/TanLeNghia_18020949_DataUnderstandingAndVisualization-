import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def handle(x):
    for i in x:
        if 'covid-19' in i:
            return 'Thời sự'
    return 'Others'


df=pd.read_json('/Users/user/Downloads/ExampleCode/output/vnexpress/VN1.json',lines=True)


#handle tags to have category (dealing with category='')
df=df.replace({'':'Others'})
c=df['category'].tolist()
t=df['tags'].tolist()
print(c)
for i in range(len(t)):
    if c[i]=='Others':
        c[i]=handle(t[i])
print(c)
#df['category']=df.loc[(df.category=='Others'),'tags'].apply(handle)

#aggregated category
print(df['category'])
df.loc[(df.category == 'Dịch viêm phổi virus corona' )| (df.category == 'Vaccine'),'category']='Thời sự'
df.loc[df.category == '\nThượng đỉnh Mỹ - Triều\n','category']='Thế giới'
df.loc[df.category == 'Kinh tế cho tương lai','category']='Kinh doanh'
print(df['category'].value_counts())
print(df[df['category']=='Dịch viêm phổi virus corona']['category'])
print(df.loc[df.category=='Thời sự'])
#handle tags
li_tags=list()
for tag in df["tags"]:
    if '' in tag:
        tag.remove('')
    li_tags+=tag
Tag=pd.Series(li_tags).value_counts().iloc[0:10]


#countplot
plt.figure(1)
plt.xticks(rotation=45)
plt.ylabel('NumsOfArticles')
count=sns.countplot('category',data=df)
# count.set_width(10)
#bar plot
plt.figure(2)
Tag.plot.bar(x='tags',y='tags_num',rot=45)
#count=sns.countplot(data=Tag.iloc[0:10])


#print(li_tags)

plt.show()