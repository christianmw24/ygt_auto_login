#!/bin/bash


# abfrage paketmanager, funktioniert atm nur mit apt/dpgk-based distro, noch nicht mit yum/pacman/rpm-based distros

echo 'Auto-Installer for Python3 inkl. selenium, firefox and geckodriver for webautomatisation.'
echo 'This script was only written for a study project by Christian Morgenstern 2019-03-15 '
echo 'For questions or suggestions you can contact me via github "christianmw24". '
echo '.' 
echo 'Note: sudo privileges are required during installation process '
echo 'Please select your package manager:' 
echo 'apt = 1 (for debian, ubuntu, mint, kali, etc)' 
echo 'yum = 2 (for arch, suse, etc)'
echo 'WARNING: YUM INSTALLATION DOES NOT WORK YET. PLEASE CANCEL AND INSTALL MANUAL'										#entfernen wenn yum/pacman eingebaut
read -p '1 or 2: ' packagemanager
echo 'selected packagemanager: ' $packagemanager		

packagemanager1=1				
packagemanager2=2				


# prüfung auf gültige eingabe

if [ $packagemanager -eq $packagemanager1 ]
	then 
		pmrun='apt'
		echo 'packagemanager: ' $pmrun
	elif [ $packagemanager -eq $packagemanager2 ]
		then		
			pmrun='yum'
			echo 'packagemanager: WARNING: YUM INSTALLATION DOES NOT WORK YET. PLEASE CANCEL AND INSTALL MANUAL ' $pmrun		#yum/pacman noch einbauen
	else
		echo 'what is so hard to select 1 or 2? Run script again!'
fi


# apt update and apt upgrade auswahl

echo 'Befor installation you shoud upgrade your system: yes or no?'
read -p 'select y/n : ' upgrade

upgradey='y'
upgraden='n'


# prüfung auf gültige eingabe, AUSFÜHREN VON APT, NOCH KEIN YUM!!!!

if [ $upgrade = $upgradey ]
	then
		echo 'upgrade will be executed'
		sudo apt update
		sudo apt upgrade
	elif [ $upgrade = $upgraden ]
		then
			echo 'upgrade not be executed'
	else
		echo 'what is so hard to type y or n? Run script again!'
fi


# firefox, python3 und selenium installation, AUSFÜHREN VON APT, NOCH KEIN YUM!!!!

echo 'Installation of Firefox-Browser and Python3 incl. selenium: yes or no? '	
read -p 'select y/n : ' instfps

instfpsy='y'
instfpsn='n'

if [ $instfps = $instfpsy ]
	then
		echo 'Installation will be executed'
		sudo apt install python3
		sudo apt install python3-selenium
		sudo apt install firefox
		sudo apt install firefoxdriver
	elif [ $instfps = $instfpsn ]
		then
			echo 'Installation not be executed'
	else
		echo 'what is so hard to type y or n? Run script again!'
fi


# geckodriver herunterladen und entpacken

echo 'Download geckodriver, unpack and copy to user-path and /usr/local/bin/: yes or no? '	
read -p 'select y/n : ' gecko

geckoy='y'
geckon='n'

if [ $gecko = $geckoy ]
	then
		echo 'Installation will be executed'
		wget -t 5 https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
		gunzip geckodriver-v0.24.0-linux64.tar.gz
		tar -x -f geckodriver-v0.24.0-linux64.tar
		sudo cp -u geckodriver /usr/local/bin/geckodriver
	elif [ $gecko = $geckon ]
		then
			echo 'Installation not be executed'
	else
		echo 'what is so hard to type y or n? Run script again!'
fi








echo 'finish'



































