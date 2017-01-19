#!/bin/bash

#--
#-- by Allex Lima
#-- TESTED ONLY IN ** DEBIAN-BASED ** SYSTEMS
#--
#-- This bash script will move the Wava Image Dataset Processing (WADP) files directory to /opt/WADP/
#-- and create a desktop entry in /usr/share/applications/ aiming an Desktop Shortcut
#-- OR
#-- It will remove the Wava Image Dataset Processing (WADP) files from your computer
#--
#-- https://github.com/allexlima/WavaImageDatasetProcessing.git
#--

FILE="/tmp/out.$$"
GREP="/bin/grep"

# Check root

if [ "$(id -u)" != "0" ]; then
   echo -e "\n\e[31m--* You must run this setup as root/sudo *-- \033[0m\n" 1>&2
   exit 1
fi

# Init

read -p "Do you want INSTALL or REMOVE WADP? ([i]nstall | [r]emove) : " answer


if echo "$answer" | grep -iq "^i" ;then
    echo -e "\n\033[1;33mInstalling requirements... \033[0m\n"
    apt-get install python-qt4
    echo -e "\n\033[1;33mInstalling Wava Image Dataset Processing... \033[0m\n"
    echo "Creating files directory..."
    mkdir /opt/WADP
    echo "Copying files..."
    cp -Rf . /opt/WADP
    echo "Creating desktop entry..."
    cp -f WADP.desktop /usr/share/applications/
    echo -e "\n\e[1;34mInstallation done successfully!  \e[0m\n"
    echo -e "\nAccess the README file in https://github.com/allexlima/WavaImageDatasetProcessing :)  \n"
elif echo "$answer" | grep -iq "^r" ;then
    cd ~
    echo -e "\n\033[1;33mRemoving WADP... \033[0m\n"
    echo "Removing desktop entry..."
    rm /usr/share/applications/WADP.desktop
    echo "Removing files..."
    rm -rf /opt/WADP
    echo -e "\n\e[1;34mUninstall done successfully!  \e[0m"
    echo -e "\nThank you so much for use Wava Image Dataset Processing! \nhttps://github.com/allexlima/WavaImageDatasetProcessing \n"
else
    echo "Error: Invalid parameter"
    exit
fi
