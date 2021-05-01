import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

#Objektbild Spalt
spalt=np.zeros((512,512))  #schwarzes Bild
spalt[200:312,253:259]=1         #weisser Spalt in der Mitte

#Beugungsbild
#FFT=Fast Fourier Transformation
f = np.fft.fft2(spalt)      #Fouriertransformation
fshift = np.fft.fftshift(f) #Umsortieren (Butterfly algorithm)
#beugung = (np.abs(fshift))**2
beugung = (np.abs(fshift))**1.1 # !!!!!Potenz dient zum Anheben des Kontrasts. Physikalisch richtig ist die Potenz 2!

fig = plt.figure(figsize=(12, 12))
plt.subplot(121)
plt.xticks([]), plt.yticks([])
plt.imshow(spalt, cmap = 'gray')
plt.title('Objektbild')

plt.subplot(122)
plt.xticks([]), plt.yticks([])
plt.imshow(beugung, cmap=plt.cm.gray)
plt.title('Beugungsbild')

beugung = (np.abs(fshift))**2
plt.plot(beugung[256])
plt.xlim([0,512]) #Intensit

     
imgdata = StringIO()
fig.savefig(imgdata, format='svg')
imgdata.seek(0)
data = imgdata.getvalue()

print(imgdata)



def return_graph():
    
    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

return_graph()