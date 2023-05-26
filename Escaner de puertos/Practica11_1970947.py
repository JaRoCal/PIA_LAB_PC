#Jaime Ronaldo Calderon Sanchez 1970947
import nmap

# Función para realizar el escaneo UDP
def scan_udp():
    scanner = nmap.PortScanner()
    ip = input("Introduce una IP válida a analizar: ")
    # Realizar el escaneo UDP en el rango de puertos 1-1024
    result = scanner.scan(ip, '1-1024', '-v -sU')
    print("Resultado del escaneo UDP:")
    print(result)

# Función para realizar el escaneo completo (TCP y UDP)
def scan_complete():
    scanner = nmap.PortScanner()
    ip = input("Introduce una IP válida a analizar: ")
    print("Escaneo de TCP:")
    # Realizar el escaneo TCP en el rango de puertos 1-1024
    result_tcp = scanner.scan(ip, '1-1024', '-v -sS')
    print(result_tcp)
    print("\nEscaneo de UDP:")
    # Realizar el escaneo UDP en el rango de puertos 1-1024
    result_udp = scanner.scan(ip, '1-1024', '-v -sU')
    print(result_udp)

# Función para realizar la detección del sistema operativo
def detect_os():
    scanner = nmap.PortScanner()
    ip = input("Introduce una IP válida a analizar: ")
    # Realizar el escaneo con detección del sistema operativo
    result = scanner.scan(ip, '1-1024', '-A')
    print("Detección del sistema operativo:")
    print(result)

# Función para realizar el escaneo de red con ping
def scan_ping():
    scanner = nmap.PortScanner()
    ip = input("Introduce una IP válida a analizar: ")
    # Realizar el escaneo de red utilizando ping y paquetes ACK
    result = scanner.scan(ip, arguments='-sP -PA')
    print("Escaneo de red con ping:")
    print(result)

# Función para mostrar el menú y recibir la opción del usuario
def menu():
    while True:
        print("==============> Menu <==============")
        print("1. Escaneo UDP")
        print("2. Escaneo completo")
        print("3. Detección de sistema operativo")
        print("4. Escaneo de red con ping")
        print("5. Salir")
        option = input("Selecciona una opción: ")

        if option == '1':
            scan_udp()
        elif option == '2':
            scan_complete()
        elif option == '3':
            detect_os()
        elif option == '4':
            scan_ping()
        elif option == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

        print("====================================\n")

# Llamamos a la función del menú para comenzar el programa
menu()

