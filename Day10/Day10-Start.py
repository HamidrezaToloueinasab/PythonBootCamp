# Functions with outputs
def format_name(f_name, l_name):
    """ Takes a first and last name and formats them to title case version of the name. """    #Docstring 
    if f_name == "" or l_name == "":
        return "You have provided invalid inputs"
    formated_f_name = f_name.title()
    formated_l_name =l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
print(format_name(input("What is your first name? "), input("What is your last name? ")))