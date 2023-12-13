from pystyle import Center, Anime, Colors, 

from datastructure.ListNumbers import *
from datastructure.PhoneBook import *

def menu():
    menu = """
┌───────────────────────────┐
│            Menu           │
│1. Tilføj Kontakt          │
│2. Rediger kontakt         │
│3. Slet kontakt            │
│4. Søg efter kontakt       │
│5. Vis alle kontakter      │                           
│6. Afslut                  │        
└───────────────────────────┘
"""
    centered_text = Center.XCenter(menu)
    Anime.Fade(centered_text)


def main():
    while True:
        menu()
        choice = input("Indtast valg: ")
        if choice == "1":
            addContact()
        elif choice == "2":
            editContact()
        elif choice == "3":
            deleteContact()
        elif choice == "4":
            searchContact()
        elif choice == "5":
            showAllContacts()
        elif choice == "6":
            return
        else:
            print("Ugyldigt valg")


def addContact():
    root = BST("Contacts:")
    root.Insert(input("Navn: "))

def editContact():
    pass

def deleteContact():
    pass

def searchContact():
    pass

def showAllContacts():
    root = BST
    root.PrintTree()

main()