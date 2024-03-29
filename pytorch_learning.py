# -*- coding: utf-8 -*-
"""Pytorch Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sw1ymfdLNQEhJ0xUiZl_SLZh10YlI75h
"""

!pip3 install torch torchvision torchaudio
!pip install pandas
!pip install matplotlib
!pip install pillow
!pip install scikit-learn
!pip install seaborn
# !pip install pytorch

import torch
import pandas as pd
import seaborn as sns
import numpy as np

#### Libraries From Pytorch
import torch
import torch.nn as nn
import torch.nn.functional as F

torch.__version__

df=pd.read_csv('diabetes.csv')
df.head()

# df['Outcome']=np.where(df['Outcome']==1,"Diabetic","No Diabetic")

sns.pairplot(df,hue="Outcome")

X = df.drop('Outcome',axis=1).values    ### independent features
y = df['Outcome'].values                ###dependent features

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=0)

##### Creating Tensors
X_train = torch.FloatTensor(X_train)
X_test = torch.FloatTensor(X_test)
y_train = torch.LongTensor(y_train)
y_test = torch.LongTensor(y_test)

#### Creating Modelwith Pytorch

class ANN_Model(nn.Module):
    def __init__(self, input_features=8, hidden1=32, hidden2=16, out_features=2):
        super().__init__()
        self.f_connected1=nn.Linear(input_features,hidden1)
        self.f_connected2=nn.Linear(hidden1,hidden2)
        self.out=nn.Linear(hidden2,out_features)

    def forward(self, x):
        x=F.relu(self.f_connected1(x))
        x=F.relu(self.f_connected2(x))
        x=self.out(x)
        return x

####instantiate my ANN_model
torch.manual_seed(32)
model=ANN_Model()

model.parameters

###Backward Propogation-- Define the loss_function,define the optimizer
loss_function=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),lr=0.01)

epochs=800
final_losses=[]
for i in range(epochs):
    i=i+1
    y_pred=model.forward(X_train)
    loss=loss_function(y_pred,y_train)
    final_losses.append(loss)
    if i%10==1:
        print("Epoch number: {} and the loss : {}".format(i,loss.item()))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Commented out IPython magic to ensure Python compatibility.
### plot the loss function
import matplotlib.pyplot as plt
# %matplotlib inline

final_losses_ten =torch.tensor(final_losses)

plt.plot(range(epochs), final_losses_ten)
plt.ylabel('Loss')
plt.xlabel('Epoch')

#### Prediction In X_test data
predictions=[]
with torch.no_grad():
    for i,data in enumerate(X_test):
        y_pred=model(data)
        predictions.append(y_pred.argmax().item())
        print(y_pred.argmax().item())

from sklearn.metrics import confusion_matrix
cmx = confusion_matrix(y_test,predictions)
cmx

plt.figure(figsize=(10,6))
sns.heatmap(cmx,annot=True)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')

from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,predictions)
score

#### Save the model
torch.save(model,'diabetes.pt')

#### Save And Load the model
model=torch.load('diabetes.pt')

model.eval()

### Predcition of new data point
list(df.iloc[0,:-1])
#### New Data
lst1=[6.0, 130.0, 72.0, 40.0, 0.0, 25.6, 0.627, 45.0]

new_data=torch.tensor(lst1)

#### Predict new data using Pytorch
with torch.no_grad():
    print(model(new_data))
    print(model(new_data).argmax().item())