import time
import numpy as np

def rng1(c, lower_limit, upper_limit, iteration):     # first Random number Generator model
    #a = 7**5; m = (2**31)-1;       #parameters based on the theory of the minimal standard
    a = 871212; m = (2**31)-1;
    seed = (time.time() * 1000) - 1490342000000  #seed based on time/clock
    x = ( (a * seed) + c) % m    #creates the very first random number
    numbr_list = []    #this stores a list of different random numbers
    while len(numbr_list) < iteration:   #loop generator
        x = ( (a * x) + c) % m  
        numbr_list.append(x)
    for i in range(len(numbr_list)): #transform random numbers into a range of values
        numbr_list[i] /= m
        numbr_list[i] = ((upper_limit-lower_limit)*numbr_list[i]) + lower_limit
    return numbr_list

def rng2(lower_limit, upper_limit, iteration):     # second Random number Generator model
    m = (2**31)-1; 
    seed = (time.time() * 1000) - 1490342000000
    #a1 = 107374182; a2 = 0; a3 = 0; a4 = 0; a5 = 104480;           #parameters based on the theory of the minimal standard
    a1 = 261924; a2 = 444265; a3 = 441900; a4 = 948839; a5 = 363843;#alternative model with arbitrary parameters
    seed1 = ((a1*seed)+(a5*seed)) % m
    seed2 = ((a1*seed1)+(a5*seed1)) % m
    seed3 = ((a1*seed2)+(a5*seed2)) % m
    seed4 = ((a1*seed3)+(a5*seed3)) % m
    seed5 = ((a1*seed4)+(a5*seed4)) % m
    numbr_list = [seed1, seed2, seed3, seed4, seed5]    #this stores a list of different random numbers
    while len(numbr_list) < iteration:
        x = ( (a1*numbr_list[-1])+(a2*numbr_list[-2])+(a3*numbr_list[-3])+(a4*numbr_list[-4])+(a5*numbr_list[-5])) % m
        numbr_list.append(x)
    for i in range(len(numbr_list)):
        numbr_list[i] /= (m+1)
        numbr_list[i] = ((upper_limit-lower_limit)*numbr_list[i]) + lower_limit
    return numbr_list


print("Hello there, you are welcome to try my random number generator")
print("You need to know that the range between 0 and 100 has been set up as default to create the rand numbers")
generator_type = int(input("Select generator type. Enter '1' for LCS, or '2' for MRG: "))

iteration = int(input("Please, type the total number of points for the cube: "))

start = time.time()

if generator_type == 1:
    random_arr1 = rng1(0, 0, 100, iteration)  # X-values
    random_arr2 = rng1(0, 0, 100, iteration)  # Y-values
    random_arr3 = rng1(0, 0, 100, iteration)  # Z-values

if generator_type == 2:
    random_arr1 = rng2(0, 100, iteration)  # X-values
    random_arr2 = rng2(0, 100, iteration)  # Y-values
    random_arr3 = rng2(0, 100, iteration)  # Z-values

#I calculate the distance of the points with respect to the center of the bodies
#I will use these numbers to know how many are outside of the sphere

radius_arr = []

for i in range(iteration):
    radius = ((random_arr1[i]-50)**2 + (random_arr2[i]-50)**2 + (random_arr3[i]-50)**2)**0.5
    radius_arr.append(radius)

####I will keep the numbers in a file for future reference

#Random numbers on axis-X
name = str(iteration)+"RNG"+str(generator_type)+"_X.txt"
f = open(name,"w")
for item in random_arr1:
    f.write(str(item)+"\n")
f.close()

#Random numbers on axis-Y
name = str(iteration)+"RNG"+str(generator_type)+"_Y.txt"
f = open(name,"w")
for item in random_arr2:
    f.write(str(item)+"\n")
f.close()

#Random numbers on axis-Z
name = str(iteration)+"RNG"+str(generator_type)+"_Z.txt"
f = open(name,"w")
for item in random_arr3:
    f.write(str(item)+"\n")
f.close()

#List of the Radius[distance] values
name = str(iteration)+"RNG"+str(generator_type)+"_R.txt"
f = open(name,"w")
for item in radius_arr:
    f.write(str(item)+"\n")
f.close()

#summary file with execution time and proportion of inside of sphere
name = str(iteration)+"RNG"+str(generator_type)+"_SUMMARY.txt"
radius_values = np.array(radius_arr)
f = open(name,"w")
content = str(len(radius_values[radius_values<20])/iteration)+ \
        "% of points are inside of the sphere \n Execution time: " + str(time.time()-start) + " seconds"
f.write(content)
f.close()



