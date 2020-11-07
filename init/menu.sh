#!/bin/bash
function Log_in() {
    echo ""
	echo "Heading to kitchen !!"
	python3 auth.py
	echo ""
}
function Co_lab() {
    echo ""
	echo "Cooking Shakaal special XC"
	python3 run.py
	echo ""
}
menu(){
green='\e[32m'
blue='\e[34m'
clear='\e[0m'
ColorGreen(){
	echo -ne $green$1$clear
}
ColorBlue(){
	echo -ne $blue$1$clear
}
echo -ne "
ShaKaaL Restaurants
$(ColorGreen '1)') Login In Google
$(ColorGreen '2)') Run Colaboratory
$(ColorGreen '0)') Exit
$(ColorBlue 'What do you want to order?:') "
        read a
        case $a in
	        1) Log_in ; menu ;;
	        2) Co_lab ; menu ;;
			0) exit 0 ;;
			*) echo -e $red"Wrong option."$clear; WrongCommand;;
        esac
}
menu
