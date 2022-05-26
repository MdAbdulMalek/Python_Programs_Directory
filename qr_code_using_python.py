### pip install qrcode

import qrcode  
import matplotlib.pyplot as plt

input = 'Hello World !!! and Rion vai'
img = qrcode.make(input)
plt.imshow(img)
plt.show()
