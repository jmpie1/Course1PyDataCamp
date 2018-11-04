a="a"
print(type(a))

# Create a variable savings
savings = 100

# Create a variable factor
factor = 1.1

# Calculate result
result = savings*factor**7

# Print out result
print(result)

# créer une liste
maList=[2,5,5,"toto"]
print(type((maList)))

# Info  malist[start:end]   end:not in the extract

round(1.78)
print(maList.index("toto"),maList.count(5))

#NumPy
#Can't calculate li1/lis2**2
import numpy as np

np_height=[1.45,1.8,2.0,1.65]
np_height=np.array(np_height)
np_weight=[65,-45,46,67]
np_weight = np.array(np_weight)

np_2d=np.array([np_height,np_weight])
print("type np_2d ",type(np_2d))
print(np_2d)
print("dim: ", np_2d.shape)
print(np_2d[0,1])
print(np_2d[0][1])
np_2d[:,1:3]
BMI= np_weight/np_height**2
print(BMI.round(1))
print(np_weight[np_weight>50])

print(np.mean(np_2d[0,:]))
print(np.mean(np_2d[1,:]))
print(np.median(np_2d[0,:]))

print(np.corrcoef(np_2d[0,:],np_2d[1,:]))

height=np.round(np.random.normal(1.75,0.2,5000),2)
print(height)
weight=np.round(np.random.normal(60.32,15,5000),2)

np_city=np.column_stack((height,weight))
print(np_city, np_city.shape)

#Fin






