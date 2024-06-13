#declarar variables
user1="pedro";
contra1="1234";
user2="angel";
contra2="a4s1";



user=input("Ingrese su usuario: ").lower();
contraseña=input("Ingrese su contraseña: ");

if (user==user1) and (contraseña==contra1):
        print("Bienvenido a la EMPRESA XY");
elif (user==user2) and (contraseña==contra2):
        print("Bienvenido a la EMPRESA XY");
else:
  print("ERROR 404!!");

# de una sola linea, se ahorra un elif

if (user.lower==user1 and contraseña==contra1) or (user.lower==user2 and contraseña==contra2):
        print("Bienvenido a la EMPRESA XY");
else:
  print("ERROR 404!!");
 
