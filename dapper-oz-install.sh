#!/bin/bash
#Oz sandbox profile setup for Dapper Linux

#------------------------------
# Document and Image viewing
#------------------------------
oz-install /usr/bin/eog
oz-install /usr/bin/evince

#------------------------------
# Image Editing
#------------------------------
oz-install /usr/bin/gimp-2.8
oz-install /usr/bin/inkscape

#------------------------------
# Media Programs
#------------------------------
oz-install /usr/bin/totem
oz-install /usr/bin/vlc


#------------------------------
# Document Editing
#------------------------------
oz-install /usr/bin/lyx
oz-install /usr/bin/libreoffice
oz-install /usr/bin/soffice

#------------------------------
# Web Browsers and Email
#------------------------------
oz-install /usr/bin/firefox
oz-install /usr/bin/firefox-hardened
oz-install /usr/bin/thunderbird

#------------------------------
# Internet enabled programs
#------------------------------
oz-install /usr/bin/liferea
oz-install /usr/bin/polari
oz-install /usr/bin/transmission-gtk
