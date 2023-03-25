names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
## CREATE YOUR FUNCTION HERE
def sort_names(arrayFunct):    
    names = []
    for i in arrayFunct:
        names.append(i)
    names.sort()
    return names 
    

print(sort_names(names))
