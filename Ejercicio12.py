#Hacer un programa para sumar numeros pares dentro de un rango

a = int(input("Digite de donde va a comenzar a sumar -> "))
b = int(input("Digite hasta donde quiere llegar a sumar -> "))
suma = 0

for i in range(a,b+1):
    if i%2==0:
        suma += i

print(f"La suma de los numeros pares dentro del rango es: {suma}")

#Carolina EM
