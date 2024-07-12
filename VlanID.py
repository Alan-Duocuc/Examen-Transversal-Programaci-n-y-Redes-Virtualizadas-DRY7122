id_vlan = int(input("Ingrese el ID de la VLAN: "))

if 1 <= id_vlan <= 1005:
    print("VLAN de rango Normal")
elif 1006 <= id_vlan <= 4095:
    print("VLAN de rango Extendido")
else:
    print("El número de VLAN ingresado es desconocido")