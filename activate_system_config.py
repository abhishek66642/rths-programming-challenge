import numpy

def activate_system_config(input_integer):
    exponent_list = []
    remainder = int(numpy.log(input_integer)/numpy.log(2))
    exponent_list +=[remainder]
    while (remainder!=0):
        input_integer = input_integer - pow(2,remainder)
        if (input_integer == 2):
            exponent_list+=[1]
            break
        remainder = int(numpy.log(input_integer)/numpy.log(2))
        exponent_list +=[remainder]
    exponent_string=""
    for i in range(len(exponent_list)):
        exponent_string +="2^"+str(exponent_list[i])
        if (i!=len(exponent_list)-1):
            exponent_string+=","

    return exponent_string

print(activate_system_config(22))
print(activate_system_config(31))
print(activate_system_config(15))
