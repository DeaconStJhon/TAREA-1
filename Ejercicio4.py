# 4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: mayor de edad , tener ruc y tener un nombre comercial ,los inputs son si y /o no . la salida debe ser si esta apto o no para abrir un comercio.
print("FILTRO DE REGISTRO DE NEGOCIOS. PORFAVOR RESPONDER SI/NO A LAS SIGUIENTES PREGUNTAS")
edad=input("Es usted mayor de edad?: ")
ruc=input("Posee usted un RUC?: ")
comercial=input("Posee un nombre comercial?:")

if edad.lower()=="si" and ruc.lower()=="si" and comercial.lower()=="si":
    print("Se encuantra apto para registrar su negocio. Felicidades.")
else:
    print("Lo sentimos, no se encuentra apto.")