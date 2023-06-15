import pandas as pd
df= pd.read_csv("tweets.txt",
                      delimiter = '\n',names=['tweets'])
d=[]
for i in range(len(df)):

    if df['tweets'][i].find('http')!=-1:
        d=d+[i]
df2=df.drop(df.index[d])
d=[]
df2=df2.reset_index()
for i in range(len(df2)):

    if df2['tweets'][i].find('انتخابات1400#')!=-1:
        d=d+[i]
df3=df2.drop(df2.index[d])
df4=df3.drop(['index'],axis=1)
df4=df4.reset_index()

d=[]

for i in range(len(df4)):
    q=df4['tweets'][i].find('اصلاح')
    q1=df4['tweets'][i].find('اصولگرا')
    q2=df4['tweets'][i].find('رئیسی')
    q3=df4['tweets'][i].find('رضایی')
    q4=df4['tweets'][i].find('هاشمی')
    q5=df4['tweets'][i].find('جلیلی')
    q6=df4['tweets'][i].find('زاکانی')
    q7=df4['tweets'][i].find('علیزاده')
    q8=df4['tweets'][i].find('همتی')
    
    if q !=-1 and q1!=-1 and q2!=-1 and q3!=-1 and q4!=-1 and q5!=-1 and q6!=-1 and q7!=-1 and q8!=-1:
        
        d=d+[i]
        

        
        
labels=[]
d=[]

for i in range(len(df4)):
    q0=df4['tweets'][i].find('اصلاحات')
    q=df4['tweets'][i].find('اصلاح')
    q1=df4['tweets'][i].find('اصولگرا')
    q2=df4['tweets'][i].find('رئیسی')
    q3=df4['tweets'][i].find('رضایی')
    q4=df4['tweets'][i].find('هاشمی')
    q5=df4['tweets'][i].find('جلیلی')
    q6=df4['tweets'][i].find('زاکانی')
    q7=df4['tweets'][i].find('علیزاده')
    q8=df4['tweets'][i].find('همتی')
    
    if q2 !=-1 and q5!=-1 and q3!=-1 and q6!=-1:
        labels=labels+['اصولگرا']
    elif q2 !=-1 and q5!=-1:
        labels=labels+['اصولگرا']
    elif q2 !=-1 and q6!=-1:
        labels=labels+['اصولگرا']
    elif q2 !=-1 and q3!=-1:
        labels=labels+['اصولگرا']
    elif q2 !=-1 and q6!=-1:
        labels=labels+['اصولگرا']
        
        
    elif q !=-1:
        labels=labels+['اصلاح طلب']
    elif q0 !=-1:
        labels=labels+['اصلاحات']
    elif q1 !=-1:
        labels=labels+['اصولگرا']
    
    elif q3 !=-1:
        labels=labels+['رضایی']
    elif q4 !=-1:
        labels=labels+['هاشمی']
    elif q5 !=-1:
        labels=labels+['جلیلی']
    elif q6 !=-1:
        labels=labels+['زاکانی']
    elif q1 !=-1:
        labels=labels+['علیزاده']
    elif q1 !=-1:
        labels=labels+['همتی']
    elif q2 !=-1:
        labels=labels+['رئیسی']
        
    else:
        d=d+[i]
        
        
df5=df4.drop(df4.index[d])
df6=df5.drop(['level_0','index'],axis=1)

df7=df6.reset_index()

df7['labels']=labels
df8=df7.drop(['index'],axis=1)


df8.to_csv('result.csv', encoding='utf-8-sig')


