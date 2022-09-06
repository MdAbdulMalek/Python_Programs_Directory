data={'Name':['Karan','Rohit','Sahil','Aryan'],'Age':[23,22,21,24]}

df=pd.DataFrame(data)

#df

data1 ={'Name':['Karan','Rohit','Sahil','Aryan', 'Aryauun', 'ooooryan'],'Age':[28,29,21,20, 24, 55]}

df1=pd.DataFrame(data1)

#df1

for i in range(len(df.index)):
  first = df['Age'][i]
  for j in df1['Age']:
    if first == j:
      ind = df1.index[df1['Age']== first].tolist()
      df1 = df1.drop(ind)

