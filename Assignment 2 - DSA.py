#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Name : Saaketh Potluri , Student Number : 100876538


# In[ ]:


import winsound
import time

#Method for Sorting the array in ascending order
def mergesort(garr):
    if len(garr) > 1:
        mid_point = len(garr) // 2
        LS = garr[:mid_point]
        RS = garr[mid_point:]
    
        #Printing Left and Right sides of the divided array
        print("Dividing -> Left:", LS,"Right:",RS)

        #Dividing the array into left and right sides
        mergesort(LS)
        mergesort(RS)
        
        #Initialzing counters
        i = j = k = 0
            
        #Merging left and right sides
        print("Merging:", LS, "and", RS)
        while i < len(LS) and j < len(RS):
            if LS[i] < RS[j]:  
                garr[k] = LS[i]
                i += 1
            else:
                garr[k] = RS[j]
                j += 1
            k += 1
            swap_sound()
            
        
        #Adding remaining elements in the LS to the array
        while i < len(LS):
            garr[k] = LS[i]
            i += 1
            k += 1
            swap_sound()
            
            
        #Adding remaining elements in the RS to the array
        while j < len(RS):  
            garr[k] = RS[j]
            j += 1
            k += 1
            swap_sound()
            
        
        #Printing current iteration
        print("Current Iteration:", garr)
        

#Method for implementing sound while swapping elements
def swap_sound():
    frequency = 2500
    duration = 100
    winsound.Beep(frequency,duration)

    
while True:
    #Initial Array
    garr = [int(x) for x in input("Enter the array to sort (space-separated): ").split()]
    
    #Printing Given Array
    print("Given Array :", garr)
    
    #Calling mergesort method
    mergesort(garr)
    
    #Printing Sorted Array
    print("Sorted Array:", garr)
    
   # Asking the user if they want to continue or implementing break condition
    user_input = input("Would you like to sort another array (Yes/No)? ").strip().lower()
    if user_input == "no":
        break  

