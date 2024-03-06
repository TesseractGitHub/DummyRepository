import os

path = "C:/Users/chris/OneDrive/Documents/Bumstick/DummyRepository/"
i=0
for element in os.listdir(path) : 
    os.rename(path+element, path+str(i)+".png")
    i = i+1