import random
caracteres = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input("¿qué tan grande quisieras que sea tu contraseña: "))

contraseña = ""

for i in range (x):
    contraseña = contraseña + (random.choice(caracteres))

print ("la contraseña segira es", contraseña)
