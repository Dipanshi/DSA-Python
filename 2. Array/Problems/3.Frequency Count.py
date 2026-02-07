# Frequency Count of array

def FrequencyCount(arr):
    fre_dict={}
    for a in arr:
        fre_dict[a]=fre_dict.get(a,0)+1    
    return fre_dict

arr=[1,3,5,2,1,2,3,2,1,5]
print(FrequencyCount(arr))
