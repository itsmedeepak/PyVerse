def removeDuplicates(arr): 
    iter_ = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[iter_]:
            arr[iter_+1] = arr[i]
            iter_ += 1
    return iter_+1

        
   
        
# dublicate removal

arr = [2, 3, 3, 3, 6, 9, 9]
print(removeDuplicates(arr))
