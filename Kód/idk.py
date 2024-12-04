import pandas as pd

df=pd.read_csv("C:\\Users\\Andris\\Documents\\Szakdoga\\scaled\\incm.csv")

incm=df


def hatar(inc):
    cla=[]
    a=0
    b=0
    k=[]


    inc2=pd.DataFrame()
    inc2['k']=k
    print(inc2.head())
    hat= inc.mean()
 
    print(hat)
    for x in inc['incidents_per_month']:

        if x<hat:
            cla.append(0)
            a+=1

        else:
            cla.append(1)
            b+=1
   
            

    print(a)
    print(b)
    print(len(inc))
    return cla



h=int(len(incm)/2)
incm=incm.sort_values(by="incidents_per_month")
print(incm)
incml=incm.iloc[:h]
incml["kat"]=1

incmh=incm.iloc[h:]
incmh["kat"]=0

inc2=pd.concat([incml, incmh], axis=0)
inc2.index=pd.to_datetime(inc2['Unnamed: 0'])
inc2.sort_index()
print(inc2)
