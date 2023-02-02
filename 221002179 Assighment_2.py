#!/usr/bin/env python
# coding: utf-8

# # Name: Rawan Osama Baker 
# ID: 221002179

# In[56]:


import numpy as np
import matplotlib.pyplot as plt
import random


# In[52]:


rate = 0.25
#Population mean is going to be
mu = 1/rate

Avrage = []
def simulate_central_limit(random_samples,sample_size):
    Avrage = []
    for i in range(random_samples):
        Each_Thorw = []

        random_sample=(np.random.exponential((1 / rate), sample_size))

        Avrage.append(np.mean(random_sample))
        
    avg_each_roll = Avrage
    mean = np.mean(Avrage)
    var = np.var(Avrage)
    return avg_each_roll, mean, var


# In[53]:


avgs1, mean1, var1 = simulate_central_limit(50,2)


#Second exp
# use another 5000 random samples ,sample size= 500
avgs2, mean2, var2 = simulate_central_limit(5000,500)

print("First 50 random samples: ")
print("Mean = {0:f}, Variance = {1:f}".format(mean1, var1))
print("Average of outcomes in each case: ", avgs1, "\n")

print("Another 50 random samples: ")
print("Mean = {0:f}, Variance = {1:f}".format(mean2, var2))
print("Average of outcomes in each case: ", avgs2, "\n")


# In[54]:


plt.hist(avgs1, bins=100);
# plt.title('Histogram of first random 50 samples');


# In[55]:


# use another 5000 random samples ,sample size= 500  (Secand exp)
plt.hist(avgs2, bins=100);
plt.title('Histogram of another 50 random samples: ' );


# In[ ]:





# In[ ]:




