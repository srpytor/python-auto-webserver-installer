#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sys

print('------------------------------------------------------')
print('--------------- Auto Web Service Installer -----------')
print('---------------- Autor: Alejandro Lahoz --------------')
print('------------------------------------------------------')
print('- Welcome to the linux services installation program -')
print('------------------------------------------------------')
time.sleep(3)

def main():

    actualizar = input('Before installing anything, it is advisable to update your system! Do you want to update? (y/n) ')
    actualizar.lower()

    if actualizar == 'y':
        print('----- Updating your system -----')
        time.sleep(0.2)
        os.system('sudo apt-get upgrade && apt-get update')
        time.sleep(1)
        os.system('clear')        

    instalacion = True

    while instalacion:

        eleccion = input('\n What do you want to install? (Enter the number corresponding to the desired service) \n 1.- Apache2 \n 2.- PHP \n 3.- MySQL \n 4.- OpenSSH \n Eleccion: ')
        
        if eleccion == '1':
            apache()
            continuar = input('Do you want to install any more services? (y/n) ')

        elif eleccion == '2':
            php()
            continuar = input('Do you want to install any more services? (y/n) ')

        elif eleccion == '3':
            mysql()
            continuar = input('Do you want to install any more services? (y/n) ')

        elif eleccion == '4':
            openssh()
            continuar = input('Do you want to install any more services? (y/n) ')

        else:
            continuar = 's'
            print('\n--- The entered value is not correct ---')
            
        if continuar == 'n':
            instalacion = False

def apache():
    print('--- You have selected Apache2 ---')
    time.sleep(0.5)
    os.system('sudo apt-get install apache2')
    print('--- Instalation complete ---')
    
def php():
    print('--- You have selected PHP ---')
    time.sleep(0.5)
    os.system('sudo apt-get install php libapache2-mod-php')
    os.system('sudo apt-get intall php-cli')
    os.system('sudo apt-get install php-cgi')
    os.system('sudo apt-get install php-mysql')
    print('--- Instalation complete ---')

def mysql():
    print('--- You have selected MySQL ---')
    time.sleep(0.5)
    os.system('sudo apt-get install mysql-server')
    print('--- Instalation complete ---')
    
def openssh():
    print('--- You have selected OpenSSH ---')
    time.sleep(0.5)
    os.system('sudo apt-get install openssh-server')
    print('--- Instalation complete ---')

if __name__ == '__main__':
    os.system('clear')
    main()