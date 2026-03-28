#Formatações de saída no print

var1 = 123
var2 = "Mundo"
print("Hello to the", var2, var1)
print("Hello to the %s %d "%(var2, var1))
print("Hello to the {} {}".format(var2, var1))
print(f"Hello to the {var2} {var1}")