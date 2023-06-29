def outer_function(x):
    def inner_function(factor):
        return x * factor

    result = inner_function(15) 
    print(result)
    
outer_function(30)