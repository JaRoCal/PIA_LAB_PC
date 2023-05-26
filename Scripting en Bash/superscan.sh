#!/bin/bash
#
#Jaime Ronaldo Calderon Sanchez
# 
date
echo "---------------------------"
echo "----------Menu-------------"
echo "---------------------------"
echo "1. NetDiscover."
echo "2. PortScanv1."
echo "3. Welcome."
echo "4. Salir."
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) bash ./netdiscover.sh;;
        2) read -p "Escribe tu IP: " IP; bash ./portscanv1.sh $IP;;
        3) bash ./welcome.sh;;
        4) echo "Saliendo..."; exit 0;;
esac
