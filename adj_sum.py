filename = "triangle.txt"

f = open(filename,"r+")

total = 0

#will store the position of the maximum value in the line
index = 0

#get the first pyramid value
total = [int(x) for x in f.readline().split()][0]

#since it's only one value, the position will start with 0
current_index = 0 

# loop through the lines
for line in f:

    # transform the line into a list of integers
    cleaned_list = [int(x) for x in line.split()]

    # get the maxium value between index and index + 1 (adjacent positions)
    maximum_value_now = max(cleaned_list[current_index],cleaned_list[current_index + 1])

    # stores the index to the next iteration        
    future_indexes = [ind for (ind,value) in enumerate(cleaned_list) if value == maximum_value_now]

    # we have more that 2 values in our list with this maximum value
    # must return only that which is greater than our previous index                    
    if (len(future_indexes) > 1):        
        current_index = [i for i in future_indexes if (i >= current_index and i <= current_index + 1)][0]

    else:
        #only one occurence of the maximum value        
        current_index = future_indexes[0]

    # add the value found to the total sum
    total = total + maximum_value_now

print total