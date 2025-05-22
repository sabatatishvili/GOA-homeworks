#def print_based_on_type(arg):
    #if isinstance(arg, str):
        #print("Literature")
    #elif isinstance(arg, (int, float)):
        #print("Math")
    #elif isinstance(arg, bool):
        #print("Science")
#-----------------------------------------------
#from collections import Counter
#def most_common_type(lst):
    #types = [type(item) for item in lst]
    #count = Counter(types)
    #most_common = count.most_common(1)
    #if most_common:
     #   return most_common[0][0]
    #return None
#--------------------------------------------
#def remove_non_integers(lst):
    #return [x for x in lst if isinstance(x, int)]
#-------------------------------------------------------------
#def result_type(expression: str):
    #try:
        #result = eval(expression)
        #return type(result)
    #except Exception as a:
        #return f"Error: {a}"
#-------------------------------------------------------------
#