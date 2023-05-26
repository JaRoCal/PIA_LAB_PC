#!/bin/bash
#Jaime Ronaldo Calderon Sanchez 1970947
#
# Escaner de red basico en BASH
#
# Determinar el segmento de red
which ifconfig && { echo "Comando ifconfig existe...";
                    direccion_ip=`ifconfig |grep inet |grep -v "127.0.0.1" |awk '{ print $2}'`;
                    echo " Esta es tu direccion ip: "$direccion_ip;
                    subred=`ifconfig |grep inet |grep -v "127.0.0.1" |awk '{ print $2}' |awk -F. '{print $1"."$2"."$3"."}'`;
                    echo " Esta es tu subred: "$subred;
                  }\
               || { echo "No existe el comando ifconfig...usando ip ";
                   direccion_ip=`ip addr show |grep inet | grep -v "127.0.0.1" |awk '{ print $2}'`;
                   echo " Esta es tu direccion ip: "$direccion_ip;
                   subred=`ip addr show |grep inet |grep -v "127.0.0.1" |awk '{ print $2}' |awk -F. '{print $1"."$2"."$3"."}'`;
                   echo " Esta es tu subred: "$subred;
                 }
  for ip in {1..254}
  do
      ping -q -c 4 ${subred}${ip} > /dev/null
      if [ $? -eq 0 ]
      then
          echo "Host responde: " ${subred}${ip}
      fi
  done