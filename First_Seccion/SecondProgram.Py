Student_grade=[9.2,9.8,9.9]
Student_grade2=[9,"9.8",1.9]
Student_grade3=[1,"a","1",[1,2,3]]
print(Student_grade)
print(Student_grade2)
print(Student_grade3)
print(Student_grade*2)
#imposible concatenar de esta manera en un areglo 
#print(Student_grade+1)
#Creamos una lista con un rango de 00 al 11 sin tocar el 11
StudentGradeRange=list(range(0,11))
print(StudentGradeRange)
#creamos la lista nuevamente pero sumando 2 en 2  
StudentGradeRange2=list(range(0,11,2))
print(StudentGradeRange2)

Cadena1="help"
#lower() contraparte
print("Canviar la cadena "+Cadena1 +" a mayuscula "+Cadena1.upper())

print("Canviar la cadena "+Cadena1 +" a mayuscula la primera "+Cadena1.title())

# para ver mas propiedades usa la siguiente linea de codigo 
# print(dir (Cadena1)) 

#Ejemplo para calcular promedio

mySum=sum(Student_grade)
Length=len(Student_grade)
mean=mySum/Length

print(mean)
print("--------------------------------------------")
lista={"Marry":9.1,"Sim":8.8,"John": 7.5}
mySum2=sum(lista.values())
length=len(lista)
mean2=mySum2/length
print(mean2)