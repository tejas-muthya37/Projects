import json
import tkinter.font as font
from gtts import gTTS
import os
from random import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *
root = Tk()
root.title("easyBuy")
root.iconbitmap('c:/Python/shopping-cart.ico')
canvas = Canvas(root, height = 500, width = 800)
canvas.pack()

cart1 = []

with open('easyBuy.json') as file:
    cart1 = json.load(file)

def open_inventory():

    '''
    This top level function open_inventory, upon invoking opens 
    the easyBuy inventory making it available for the user to browse.

    It is passed as a command to the button -> inventoryButton
    '''


    myFont = font.Font(family = 'Courier', weight = 'bold', size = 25)

    inventoryFrame = Frame(root, bg = "Black")
    inventoryFrame.place(relheight = 1, relwidth = 1)

    categoryLabel = Label(inventoryFrame, text = "Which category would you like to browse? :)", bg = "#deb8ff", fg = "black")
    categoryLabel.place(relx = 0.125, rely = 0.1, relheight = 0.1, relwidth = 0.75)
    categoryLabel['font'] = myFont

    homeButton = Button(inventoryFrame, text = "Home", bg = "gray", fg = "black", command = homescreen)
    homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
    homeButton['font'] = myFont

    def accessories():

        '''
        This sublevel function accessories() upon invoking opens
        the accessories category in the inventory.

        It is passed as a command to the button -> accessoriesButton
        '''

        myFont = font.Font(family = 'Courier', weight = 'bold', size = 25)

        accessoriesFrame = Frame(root, bg = "Black")
        accessoriesFrame.place(relheight = 1, relwidth = 1)

        accessoryLabel = Label(accessoriesFrame, text = "Accessories", bg = "#deb8ff", fg = "black")
        accessoryLabel.place(relx = 0.125, rely = 0.05, relheight = 0.1, relwidth = 0.75)
        accessoryLabel['font'] = myFont

        accessorycartLabel = Label(accessoriesFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        accessorycartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        accessorycartLabel['font'] = myFont

        homeButton = Button(accessoriesFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        backButton = Button(accessoriesFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont

        product01Price = "1499"
        product01Name = "Casio Men's Watch"


        def button01():
            '''
        This sublevel function button01() upon invoking selects
        the first product in the accessories category to be added onto the cart

        NAMING CONVENTION = button(i)(j), where i is the category number
                                                j is the product number

        ____________________________________________________________________

        SIMILAR CONVENTIONS AND FUNCTIONALITIES ASSIGNED TO THE NEXT 31 BUTTONS
        ____________________________________________________________________

        button01 is a function assigned to add the 
        1st product of the 1st category to the cart.

        It is passed as a command to the button -> product01button
        '''
            cart1.append([product01Name, product01Price])
        
        product01Button = Button(accessoriesFrame, text = product01Name + " : ₹ " + product01Price , bg = "#dcc90a", fg = "black", command = button01)
        product01Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product01Button['font'] = myFont

        product02Price = "2599"
        product02Name = "Titan Ladies Watch"


        def button02():
            cart1.append([product02Name, product02Price])

        product02Button = Button(accessoriesFrame, text = product02Name + " : ₹ " + product02Price , bg = "#dcc90a", fg = "black", command = button02)
        product02Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product02Button['font'] = myFont

        product03Price = "17599"
        product03Name = "Joyalukkas Necklace"


        def button03():
            cart1.append([product03Name, product03Price])

        product03Button = Button(accessoriesFrame, text = product03Name + " : ₹ " + product03Price , bg = "#dcc90a", fg = "black", command = button03)
        product03Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product03Button['font'] = myFont

        product04Price = "5999"
        product04Name = "Wildcraft Backpack"

        def button04():
            cart1.append([product04Name, product04Price])

        product04Button = Button(accessoriesFrame, text = product04Name + " : ₹ " + product04Price , bg = "#dcc90a", fg = "black", command = button04)
        product04Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product04Button['font'] = myFont


    def apparels():

        '''
        This sublevel function apparels() upon invoking opens
        the apparels category in the inventory.

        It is passed as a command to the button -> apparelsButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        apparelsFrame = Frame(root, bg = "Black")
        apparelsFrame.place(relheight = 1, relwidth =1)

        apparelLabel = Label(apparelsFrame, text = "Apparels", bg = "#deb8ff", fg = "black")
        apparelLabel.place(relx = 0.125, rely = 0.05, relheight = 0.1, relwidth = 0.75)
        apparelLabel['font'] = myFont

        apparelcartLabel = Label(apparelsFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        apparelcartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        apparelcartLabel['font'] = myFont

        homeButton = Button(apparelsFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        backButton = Button(apparelsFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont

        product11Price = "599"
        product11Name = "Blue Jeans"


        def button11():
            cart1.append([product11Name, product11Price])

        product11Button = Button(apparelsFrame, text = product11Name + " : ₹ " + product11Price , bg = "#dcc90a", fg = "black", command = button11)
        product11Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product11Button['font'] = myFont

        product12Price = "399"
        product12Name = "Yoga Pants"


        def button12():
            cart1.append([product12Name, product12Price])

        product12Button = Button(apparelsFrame, text = product12Name + " : ₹ " + product12Price , bg = "#dcc90a", fg = "black", command = button12)
        product12Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product12Button['font'] = myFont

        product13Price = "999"
        product13Name = "Nike Shorts"


        def button13():
            cart1.append([product13Name, product13Price])

        product13Button = Button(apparelsFrame, text = product13Name + " : ₹ " + product13Price , bg = "#dcc90a", fg = "black", command = button13)
        product13Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product13Button['font'] = myFont

        product14Price = "1999"
        product14Name = "Adidas Jersey"


        def button14():
            cart1.append([product14Name, product14Price])

        product14Button = Button(apparelsFrame, text = product14Name + " : ₹ " + product14Price , bg = "#dcc90a", fg = "black", command = button14)
        product14Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product14Button['font'] = myFont


    def baby():

        '''
        This sublevel function baby() upon invoking opens
        the baby products category in the inventory.

        It is passed as a command to the button -> babyButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        babyFrame = Frame(root, bg = "Black")
        babyFrame.place(relheight = 1, relwidth = 1)

        babyLabel = Label(babyFrame, text = "Baby Products", bg = "#deb8ff", fg = "black")
        babyLabel.place(relx = 0.125, rely = 0.05, relheight = 0.1, relwidth = 0.75)
        babyLabel['font'] = myFont

        babycartLabel = Label(babyFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        babycartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        babycartLabel['font'] = myFont

        homeButton = Button(babyFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        backButton = Button(babyFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont

        product21Price = "590"
        product21Name = "Diapers - XXL * 28"


        def button21():
            cart1.append([product21Name, product21Price])

        product21Button = Button(babyFrame, text = product21Name + " : ₹ " + product21Price , bg = "#dcc90a", fg = "black", command = button21)
        product21Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product21Button['font'] = myFont

        product22Price = "225"
        product22Name = "Moms Co. Shampoo"


        def button22():
            cart1.append([product22Name, product22Price])

        product22Button = Button(babyFrame, text = product22Name + " : ₹ " + product22Price , bg = "#dcc90a", fg = "black", command = button22)
        product22Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product22Button['font'] = myFont

        product23Price = "299"
        product23Name = "Wet Wipes - 72*3"


        def button23():
            cart1.append([product23Name, product23Price])

        product23Button = Button(babyFrame, text = product23Name + " : ₹ " + product23Price , bg = "#dcc90a", fg = "black", command =button23)
        product23Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product23Button['font'] = myFont

        product24Price = "485"
        product24Name = "Muslin Wash Cloth * 5"


        def button24():
            cart1.append([product24Name, product24Price])

        product24Button = Button(babyFrame, text = product24Name + " : ₹ " + product24Price , bg = "#dcc90a", fg = "black", command = button24)
        product24Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product24Button['font'] = myFont


    def beauty():

        '''
        This sublevel function beauty() upon invoking opens
        the beauty products category in the inventory.

        It is passed as a command to the button -> beautyButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        beautyFrame = Frame(root, bg = "Black")
        beautyFrame.place(relheight = 1, relwidth = 1)

        beautyLabel = Label(beautyFrame, text = "Beauty Products", bg = "#deb8ff", fg = "black")
        beautyLabel.place(relx = 0.125, rely = 0.05, relheight = 0.1, relwidth = 0.75)
        beautyLabel['font'] = myFont

        beautycartLabel = Label(beautyFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        beautycartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        beautycartLabel['font'] = myFont

        homeButton = Button(beautyFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        backButton = Button(beautyFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont

        product31Price = "3899"
        product31Name = "MAC Make-Up Set"


        def button31():
            cart1.append([product31Name, product31Price])

        product31Button = Button(beautyFrame, text = product31Name + " : ₹ " + product31Price , bg = "#dcc90a", fg = "black", command = button31)
        product31Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product31Button['font'] = myFont

        product32Price = "1359"
        product32Name = "Olay Moisturiser"


        def button32():
            cart1.append([product32Name, product32Price])

        product32Button = Button(beautyFrame, text = product32Name + " : ₹ " + product32Price , bg = "#dcc90a", fg = "black", command = button32)
        product32Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product32Button['font'] = myFont

        product33Price = "5499"
        product33Name = "Nykaa Lipstick Set * 10"


        def button33():
            cart1.append([product33Name, product33Price])

        product33Button = Button(beautyFrame, text = product33Name + " : ₹ " + product33Price , bg = "#dcc90a", fg = "black", command = button33)
        product33Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product33Button['font'] = myFont

        product34Price = "199"
        product34Name = "Make Up Brush Set * 10"


        def button34():
            cart1.append([product34Name, product34Price])

        product34Button = Button(beautyFrame, text = product34Name + " : ₹ " + product34Price , bg = "#dcc90a", fg = "black", command = button34)
        product34Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product34Button['font'] = myFont


    def books():

        '''
        This sublevel function accessories() upon invoking opens
        the books category in the inventory.

        It is passed as a command to the button -> booksButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        booksFrame = Frame(root, bg = "Black")
        booksFrame.place(relheight=1, relwidth=1)

        booksLabel = Label(booksFrame, text = "Books", bg = "#deb8ff", fg = "black")
        booksLabel.place(relx = 0.125, rely = 0.05, relheight = 0.1, relwidth = 0.75)
        booksLabel['font'] = myFont

        bookcartLabel = Label(booksFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        bookcartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        bookcartLabel['font'] = myFont

        homeButton = Button(booksFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        backButton = Button(booksFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont

        product41Price = "799"
        product41Name = "Introduction to C++"


        def button41():
            cart1.append([product41Name, product41Price])


        product41Button = Button(booksFrame, text = product41Name + " : ₹ " + product41Price , bg = "#dcc90a", fg = "black", command = button41)
        product41Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product41Button['font'] = myFont

        product42Price = "459"
        product42Name = "Personal Branding"


        def button42():
            cart1.append([product42Name, product42Price])

        product42Button = Button(booksFrame, text = product42Name + " : ₹ " + product42Price , bg = "#dcc90a", fg = "black", command = button42)
        product42Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product42Button['font'] = myFont

        homeButton = Button(booksFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        product43Price = "299"
        product43Name = "Learn Cooking In 10 Days"


        def button43():
            cart1.append([product43Name, product43Price])

        product43Button = Button(booksFrame, text = product43Name + " : ₹ " + product43Price , bg = "#dcc90a", fg = "black", command = button43)
        product43Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product43Button['font'] = myFont

        product44Price = "99"
        product44Name = "Colouring For Children"


        def button44():
            cart1.append([product44Name, product44Price])

        product44Button = Button(booksFrame, text = product44Name + " : ₹ " + product44Price , bg = "#dcc90a", fg = "black", command = button44)
        product44Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product44Button['font'] = myFont



    def cellphones():

        '''
        This sublevel function accessories() upon invoking opens
        the cellphones category in the inventory.

        It is passed as a command to the button -> cellphonesButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        cellphonesFrame = Frame(root, bg = "Black")
        cellphonesFrame.place(relheight = 1, relwidth = 1)

        cellphonesLabel = Label(cellphonesFrame, text = "Cellphones", bg = "#deb8ff", fg = "black")
        cellphonesLabel.place(relx = 0.125, rely = 0.05, relheight = 0.1, relwidth = 0.75)
        cellphonesLabel['font'] = myFont

        homeButton = Button(cellphonesFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        cellphonecartLabel = Label(cellphonesFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        cellphonecartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        cellphonecartLabel['font'] = myFont

        backButton = Button(cellphonesFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont

        product51Price = "21999"
        product51Name = "Samsung M31"


        def button51():
            cart1.append([product51Name, product51Price])

        product51Button = Button(cellphonesFrame, text = product51Name + " : ₹ " + product51Price , bg = "#dcc90a", fg = "black", command = button51)
        product51Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product51Button['font'] = myFont

        product52Price = "45999"
        product52Name = "Apple iPhone XR"


        def button52():
            cart1.append([product52Name, product52Price])

        product52Button = Button(cellphonesFrame, text = product52Name + " : ₹ " + product52Price , bg = "#dcc90a", fg = "black", command = button52)
        product52Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product52Button['font'] = myFont

        product53Price = "29999"
        product53Name = "Samsung Galaxy S9+"


        def button53():
            cart1.append([product53Name, product53Price])

        product53Button = Button(cellphonesFrame, text = product53Name + " : ₹ " + product53Price , bg = "#dcc90a", fg = "black", command = button53)
        product53Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product53Button['font'] = myFont

        product54Price = "32999"
        product54Name = "OnePlus 7T"


        def button54():
            cart1.append([product54Name, product54Price])

        product54Button = Button(cellphonesFrame, text = product54Name + " : ₹ " + product54Price , bg = "#dcc90a", fg = "black", command = button54)
        product54Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product54Button['font'] = myFont



    def sports():

        '''
        This sublevel function accessories() upon invoking opens
        the sports category in the inventory.

        It is passed as a command to the button -> sportsButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        sportsFrame = Frame(root, bg = "Black")
        sportsFrame.place(relheight = 1, relwidth = 1)

        sportsLabel = Label(sportsFrame, text = "Sports", bg = "#deb8ff", fg = "black")
        sportsLabel.place(relx = 0.125, rely = 0.1, relheight = 0.1, relwidth = 0.75)
        sportsLabel['font'] = myFont

        sportscartLabel = Label(sportsFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        sportscartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        sportscartLabel['font'] = myFont

        product61Price = "2999"
        product61Name = "GM Classic Bat"

        homeButton = Button(sportsFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        backButton = Button(sportsFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont


        def button61():
            cart1.append([product61Name, product61Price])

        product61Button = Button(sportsFrame, text = product61Name + " : ₹ " + product61Price , bg = "#dcc90a", fg = "black", command = button61)
        product61Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product61Button['font'] = myFont

        product62Price = "299"
        product62Name = "Kookaburra Ball"


        def button62():
            cart1.append([product62Name, product62Price])

        product62Button = Button(sportsFrame, text = product62Name + " : ₹ " + product62Price , bg = "#dcc90a", fg = "black", command = button62)
        product62Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product62Button['font'] = myFont

        product63Price = "999"
        product63Name = "Puma Gloves"


        def button63():
            cart1.append([product63Name, product63Price])

        product63Button = Button(sportsFrame, text = product63Name + " : ₹ " + product63Price , bg = "#dcc90a", fg = "black", command = button63)
        product63Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product63Button['font'] = myFont

        product64Price = "8999"
        product64Name = "New Ballance Bat"


        def button64():
            cart1.append([product64Name, product64Price])

        product64Button = Button(sportsFrame, text = product64Name + " : ₹ " + product64Price , bg = "#dcc90a", fg = "black", command = button64)
        product64Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product64Button['font'] = myFont



    def videogames():

        '''
        This sublevel function videogames() upon invoking opens
        the accessories category in the inventory.

        It is passed as a command to the button -> videogamesButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        videogamesFrame = Frame(root, bg = "Black")
        videogamesFrame.place(relheight = 1, relwidth = 1)

        videogamesLabel = Label(videogamesFrame, text = "Video Games", bg = "#deb8ff", fg = "black")
        videogamesLabel.place(relx = 0.125, rely = 0.05, relheight = 0.1, relwidth = 0.75)
        videogamesLabel['font'] = myFont

        videogamecartLabel = Label(videogamesFrame, text = "Click on an item to add it to your cart :)", bg = "Black", fg = "white")
        videogamecartLabel.place(relx = 0.15, rely = 0.25, relheight = 0.1, relwidth = 0.7)
        videogamecartLabel['font'] = myFont

        homeButton = Button(videogamesFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        backButton = Button(videogamesFrame, text = "Back" , bg = "gray", fg = "black", command = open_inventory)
        backButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        backButton['font'] = myFont

        product71Price = "5999"
        product71Name = "FIFA 19 - PS4"


        def button71():
            cart1.append([product71Name, product71Price])

        product71Button = Button(videogamesFrame, text = product71Name + " : ₹ " + product71Price , bg = "#dcc90a", fg = "black", command = button71)
        product71Button.place(relx = 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.5)
        product71Button['font'] = myFont

        product72Price = "4599"
        product72Name = "Cricket 19 - Xbox"


        def button72():
            cart1.append([product72Name, product72Price])

        product72Button = Button(videogamesFrame, text = product72Name + " : ₹ " + product72Price , bg = "#dcc90a", fg = "black", command = button72)
        product72Button.place(relx = 0.25, rely = 0.55, relheight = 0.1, relwidth = 0.5)
        product72Button['font'] = myFont

        product73Price = "1999"
        product73Name = "WWE 19 - PC"


        def button73():
            cart1.append([product73Name, product73Price])

        product73Button = Button(videogamesFrame, text = product73Name + " : ₹ " + product73Price , bg = "#dcc90a", fg = "black", command = button73)
        product73Button.place(relx = 0.25, rely = 0.7, relheight = 0.1, relwidth = 0.5)
        product73Button['font'] = myFont

        product74Price = "2999"
        product74Name = "Assassin's Creed - PS4"


        def button74():
            cart1.append([product74Name, product74Price])

        product74Button = Button(videogamesFrame, text = product74Name + " : ₹ " + product74Price , bg = "#dcc90a", fg = "black", command = button74)
        product74Button.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.5)
        product74Button['font'] = myFont

    '''
    Following are the 8 buttons for selecting a particular
    category in the inventory for shopping/browsing.
    '''



    accessoriesButton = Button(inventoryFrame, text = "Accessories", bg="#dcc90a", fg = "black", command = accessories)
    accessoriesButton['font'] = myFont
    accessoriesButton.place(relx = 0.2, rely = 0.4, relheight = 0.1, relwidth = 0.2)

    apparelButton = Button(inventoryFrame, text = "Apparels", bg="#dcc90a", fg = "black", command = apparels)
    apparelButton['font'] = myFont
    apparelButton.place(relx = 0.2, rely = 0.55, relheight = 0.1, relwidth = 0.2)

    babyButton = Button(inventoryFrame, text = "Baby Products", bg="#dcc90a", fg = "black", command = baby)
    babyButton['font'] = myFont
    babyButton.place(relx = 0.2, rely = 0.7, relheight = 0.1, relwidth = 0.2)

    beautyButton = Button(inventoryFrame, text = "Beauty", bg="#dcc90a", fg = "black", command = beauty)
    beautyButton['font'] = myFont
    beautyButton.place(relx = 0.2, rely = 0.85, relheight = 0.1, relwidth = 0.2)

    bookButton = Button(inventoryFrame, text = "Books", bg="#dcc90a", fg = "black", command = books)
    bookButton['font'] = myFont
    bookButton.place(relx = 0.6, rely = 0.4, relheight = 0.1, relwidth = 0.2)

    phoneButton = Button(inventoryFrame, text = "Cell Phones", bg="#dcc90a", fg = "black", command = cellphones)
    phoneButton['font'] = myFont
    phoneButton.place(relx = 0.6, rely = 0.55, relheight = 0.1, relwidth = 0.2)

    sportsButton = Button(inventoryFrame, text = "Sports", bg="#dcc90a", fg = "black", command = sports)
    sportsButton['font'] = myFont
    sportsButton.place(relx = 0.6, rely = 0.7, relheight = 0.1, relwidth = 0.2)

    videogamesButton = Button(inventoryFrame, text = "Video Games", bg="#dcc90a", fg = "black", command = videogames)
    videogamesButton['font'] = myFont
    videogamesButton.place(relx = 0.6, rely = 0.85, relheight = 0.1, relwidth = 0.2)
    


def homescreen():

    with open('easyBuy.json', 'w') as file:
        json.dump(cart1, file)

    '''
    This top level function homescreen() upon invoking
    brings the user back to the homescreen'

    It is passed as a command to the button -> homeButton
    '''
    homePage = Frame(root, bg = "Black")
    homePage.place(relheight = 1, relwidth = 1)

    myFont = font.Font(family='Courier', weight = 'bold', size = 25)

    inventoryButton = Button(homePage, text = "Browse Inventory", bg="#dcc90a", fg = "black", command = open_inventory)
    inventoryButton['font'] = myFont
    inventoryButton.place(relx = 0.35, rely = 0.1, relheight = 0.2, relwidth = 0.3)



    def viewcart():

        global cart1


        '''
        This sub level function viewcart() upon invoking
        allows the user to look at the products in his/her cart.

        It is passed as a command to the button -> cartButton
        '''

        myFont = font.Font(family='Courier', weight = 'bold', size = 25)

        cartFrame = Frame(homePage, bg = "Black")
        cartFrame.place(relheight = 1, relwidth = 1)

        cartLabel = Label(cartFrame, text = "My Cart", bg = "#deb8ff", fg = "black")
        cartLabel.place(relx = 0.35, rely = 0.05, relheight = 0.05, relwidth = 0.3)
        cartLabel['font'] = myFont

        homeButton = Button(cartFrame, text = "Home" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.9, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        dictCart = {"cart1" : 1, "cart2" : 1, "cart3" : 1, "cart4" : 1, "cart5" : 1, "cart6" : 1, "cart7" : 1, "cart8" : 1, "cart9" : 1, "cart10" : 1, "cart11" : 1, "cart12" : 1, "cart13" : 1, "cart14" : 1, "cart15" : 1, "cart16" : 1}

        enumList = list(enumerate(cart1))
        

        def delete():

            '''
            This sub level function delete() upon invoking allows 
            the user to delete a recently added item from his/her cart

            It is passed as a command to the button -> delCart
            '''

            try:
                del cart1[k]
            except:
                print("Cart Empty! :( ")

            viewcart()

        delCart = Button(cartFrame, text = "Delete Recent Item", bg = "grey", fg = "black", command = delete)
        delCart.place(relx = 0, rely = 0.9, relheight = 0.1, relwidth = 0.45)
        delCart['font'] = myFont

        x = 0.15
        y = 0.25
        height = 0.05
        width = 0.7

        dictCart9 = {"cart91" : 1, "cart92" : 1, "cart93" : 1, "cart94" : 1, "cart95" : 1, "cart96" : 1, "cart97" : 1, "cart98" : 1, 
        "cart99" : 1, "cart910" : 1, "cart911" : 1, "cart912" : 1, "cart913" : 1, "cart914" : 1, "cart915" : 1, "cart916" : 1}

        for k, l in list(enumerate(cart1)):

            myFont = font.Font(family='Courier', weight = 'bold', size = 25)

            dictCart9[k] = Label(cartFrame, text = l[0] + ": ₹ " + l[1], bg = "#dcc90a", fg = "black")
            dictCart9[k].place(relx = x, rely = y, relheight = height, relwidth = width)
            dictCart9[k]['font'] = myFont

            y = y + 0.075

    cartButton = Button(homePage, text = "View Cart", bg="#dcc90a", fg = "black", command = viewcart)
    cartButton['font'] = myFont
    cartButton.place(relx = 0.35, rely = 0.4, relheight = 0.2, relwidth = 0.3)

    def checkout():

        '''
        This sub level function allows the user to checkout after
        the desired products have been added to the cart.

        It is passed as a command to the button -> checkoutButton
        '''
        checkoutFrame = Frame(homePage, bg = "Black")
        checkoutFrame.place(relheight = 1, relwidth = 1)

        homeButton = Button(checkoutFrame, text = "Back" , bg = "gray", fg = "black", command = homescreen)
        homeButton.place(relx = 0.7, rely = 0.9, relheight = 0.1, relwidth = 0.1)
        homeButton['font'] = myFont

        myFont1 = font.Font(family='Courier', weight = 'bold', size = 35)

        logoButton = Button(checkoutFrame, text = "easyBuy", bg="#dcc90a", fg = "black", command = homescreen)
        logoButton['font'] = myFont
        logoButton.place(relx = 0.35, rely = 0.5, relheight = 0.2, relwidth = 0.3)

        nameLabel = Label(checkoutFrame, bd = 4, text = "Enter your Name  ", bg = "white", fg = "black", anchor = W)
        nameLabel.place(relx = 0.2, rely = 0.1, relheight = 0.05, relwidth = 0.2)

        ph_noLabel = Label(checkoutFrame, bd = 4, text = "Enter your Contact Number  ", bg = "white", fg = "black", anchor = W)
        ph_noLabel.place(relx = 0.2, rely = 0.2, relheight = 0.05, relwidth = 0.2)

        addressLabel = Label(checkoutFrame, bd = 4, text = "Enter your Address  ", bg = "white", fg = "black", anchor = W)
        addressLabel.place(relx = 0.2, rely = 0.3, relheight = 0.05, relwidth = 0.2)

        nameEntry = Entry(checkoutFrame, bd = 4, selectbackground = "gray", fg = "black")
        nameEntry.place(relx = 0.4, rely = 0.1, relheight = 0.05, relwidth = 0.4)

        ph_noEntry = Entry(checkoutFrame, bd = 4, selectbackground = "gray", fg = "black")
        ph_noEntry.place(relx = 0.4, rely = 0.2, relheight = 0.05, relwidth = 0.4)

        addressEntry = Entry(checkoutFrame, bd = 4, selectbackground = "gray", fg = "black")
        addressEntry.place(relx = 0.4, rely = 0.3, relheight = 0.05, relwidth = 0.4)

        def placeorder():

            '''
            This sub level function allows the user to place his/her 
            final order after the neccesary details have been submitted.

            It is passed as a command to the button -> placeorderButton
            '''

            if (len(nameEntry.get()) == 0) or (len(addressEntry.get()) == 0) or (len(ph_noEntry.get()) == 0):
                messagebox.showinfo("easyBuy", "Please Enter Your Details!")
                checkout()

            if len(cart1) == 0:
                messagebox.showinfo("easyBuy", "Cart Empty!")
                homescreen()
        

            myFont1 = font.Font(family='Courier', weight = 'bold', size = 35)

            if (len(nameEntry.get()) != 0) and (len(addressEntry.get()) != 0) and (len(ph_noEntry.get()) != 0) and (len(cart1) != 0):
                

                billFrame = Frame(root, bg = "white")
                billFrame.place(relheight = 1, relwidth = 1)

                logoButton = Button(billFrame, text = "easyBuy", bg="#dcc90a", fg = "black", command = homescreen)
                logoButton['font'] = myFont1
                logoButton.place(relx = 0.375, rely = 0.05, relheight = 0.2, relwidth = 0.25)

                dictBill = {"cart01" : 1, "cart02" : 2, "cart03" : 3, "cart04" : 4, "cart05" : 5, "cart06" : 6, "cart07" : 7, "cart08" : 8,
                            "cart09" : 9, "cart010" : 9, "cart011" : 10, "cart012" : 11, "cart013" : 12, "cart014" : 13, "cart015" : 14, "cart016" : 15}

                dictBill1 = {"cart11" : 1, "cart12" : 2, "cart13" : 3, "cart14" : 4, "cart15" : 5, "cart16" : 6, "cart17" : 7, "cart18" : 8,
                            "cart19" : 9, "cart110" : 9, "cart111" : 10, "cart112" : 11, "cart113" : 12, "cart114" : 13, "cart115" : 14, "cart116" : 15}

                dictBill2 = {"cart21" : 1, "cart22" : 2, "cart23" : 3, "cart24" : 4, "cart25" : 5, "cart26" : 6, "cart27" : 7, "cart28" : 8,
                            "cart29" : 9, "cart210" : 9, "cart211" : 10, "cart212" : 11, "cart213" : 12, "cart214" : 13, "cart215" : 14, "cart216" : 15}

                invoiceFont = font.Font(family='Arial', weight = 'bold', size = 30)
                billFont = font.Font(family='System', weight = 'bold', size = 15)

                invoiceLabel = Label(billFrame, bg = "white", fg = "black", text = "INVOICE NO", anchor = W)
                invoiceLabel.place(relx = 0.05, rely = 0.05, relheight = 0.2, relwidth = 0.2)
                invoiceLabel['font'] = invoiceFont

                billedToLabel = Label(billFrame, bg = "white", fg = "black", text = "BILLED TO", anchor = W)
                billedToLabel.place(relx = 0.7, rely = 0.05, relheight = 0.2, relwidth = 0.2)
                billedToLabel['font'] = invoiceFont

                dateLabel = Label(billFrame, bg = "white", fg = "black", text = "Date Of Issue : " + str(datetime.now()), anchor = W)
                dateLabel.place(relx = 0.05, rely = 0.27, relheight = 0.05, relwidth = 0.3)
                dateLabel['font'] = billFont

                invoiceIDLabel = Label(billFrame, bg = "white", fg = "black", text = randint(4000, 5000), anchor = W)
                invoiceIDLabel.place(relx = 0.05, rely = 0.20, relheight = 0.05, relwidth = 0.3)
                invoiceIDLabel['font'] = billFont

                customerLabel = Label(billFrame, bg = "white", fg = "black", text = nameEntry.get(), anchor = W)
                customerLabel.place(relx = 0.7, rely = 0.27, relheight = 0.05, relwidth = 0.3)
                customerLabel['font'] = billFont

                idLabel = Label(billFrame, bg = "white", fg = "black", text = "S.No", anchor = W)
                idLabel.place(relx = 0.05, rely = 0.45, relheight = 0.05, relwidth = 0.1)
                idLabel['font'] = invoiceFont

                productLabel = Label(billFrame, bg = "white", fg = "black", text = "Product", anchor = W)
                productLabel.place(relx = 0.3, rely = 0.45, relheight = 0.05, relwidth = 0.1)
                productLabel['font'] = invoiceFont

                amountLabel = Label(billFrame, bg = "white", fg = "black", text = "Amount", anchor = W)
                amountLabel.place(relx = 0.7, rely = 0.45, relheight = 0.05, relwidth = 0.1)
                amountLabel['font'] = invoiceFont

                invoicetotalLabel = Label(billFrame, bg = "white", fg = "black", text = "GRAND TOTAL", anchor = W)
                invoicetotalLabel.place(relx = 0.7, rely = 0.75, relheight = 0.2, relwidth = 0.2)
                invoicetotalLabel['font'] = invoiceFont

                orderconfirmedLabel = Label(billFrame, bg = "white", fg = "black", text = "ORDER CONFIRMED!", anchor = W)
                orderconfirmedLabel.place(relx = 0.05, rely = 0.75, relheight = 0.2, relwidth = 0.5)
                orderconfirmedLabel['font'] = invoiceFont

                grandTotalLabel = Label(billFrame, bg = "white", fg = "black", text = "₹ " + str(sum(cartList)) , anchor = W)
                grandTotalLabel.place(relx = 0.7, rely = 0.9, relheight = 0.05, relwidth = 0.5)
                grandTotalLabel['font'] = invoiceFont

                lineLabel = Label(billFrame, bg = "white", fg = "black", text ="_"*200)
                lineLabel.place(relx = 0, rely = 0.35, relheight = 0.05, relwidth = 1)
                lineLabel['font'] = invoiceFont

                lineLabel1 = Label(billFrame, bg = "white", fg = "black", text ="_"*200)
                lineLabel1.place(relx = 0, rely = 0.55, relheight = 0.05, relwidth = 1)
                lineLabel1['font'] = invoiceFont

                x = 0.05
                y = 0.65
                height = 0.02
                width = 0.4
                j = 0
                k = 0

                myFont2 = font.Font(family='Courier', weight = 'bold', size = 10)

                for i in range(len(dictBill)):

                    if j == len(cart1):
                        break

                    for k in range(len(cart1)):

                        if k == len(cart1):
                            break

                        dictBill1[i] = Label(billFrame, text = k + 1, bg = "white", fg = "black", anchor = W)
                        dictBill1[i].place(relx = x, rely = y, relheight = height, relwidth = width)
                        dictBill1[i]['font'] = myFont2

                        dictBill[i] = Label(billFrame, text = cart1[k][0], bg = "white", fg = "black", anchor = W)
                        dictBill[i].place(relx = 0.3, rely = y, relheight = height, relwidth = width)
                        dictBill[i]['font'] = myFont2

                        dictBill2[i] = Label(billFrame, text = "₹" + cart1[k][1], bg = "white", fg = "black", anchor = W)
                        dictBill2[i].place(relx = 0.7, rely = y, relheight = height, relwidth = width)
                        dictBill2[i]['font'] = myFont2

                        y = y + 0.03
                        j = j + 1
                        k = k + 1






        cartList1 = []
        cartList = []

        for i in range(len(cart1)):
            cartList1.append(cart1[i][1])

        cartList = list(map(int, cartList1))


        placeorderButton = Button(checkoutFrame, text = "Place Order" , bg = "green", fg = "black", command = placeorder )
        placeorderButton.place(relx = 0.8, rely = 0.9, relheight = 0.1, relwidth = 0.2)
        placeorderButton['font'] = myFont



    checkoutButton = Button(homePage, text = "Checkout", bg="#dcc90a", fg = "black", command = checkout)
    checkoutButton['font'] = myFont
    checkoutButton.place(relx = 0.35, rely = 0.7, relheight = 0.2, relwidth = 0.3)


homeFrame = Frame(root, bg = "Black")
homeFrame.place(relheight = 1, relwidth = 1)

text = "Welcome to Easy Buy! Click on the logo to get started!"
language = 'en'
speech = gTTS(text = text, lang = language, slow = False)
speech.save('test.mp3')
os.system('start test.mp3')

myFont3 = font.Font(family='Courier', weight = 'bold', size = 25)

introLabel = Label(homeFrame, text = "Developed in Bengaluru by Texx and Co.", bg = "Black", fg = "white")
introLabel.place(relx = 0, rely = 0.5, relheight = 0.2, relwidth = 1)
introLabel['font'] = myFont3

myFont = font.Font(family='Courier', weight = 'bold', size = 35)

logoButton = Button(homeFrame, text = "easyBuy", bg="#dcc90a", fg = "black", command = homescreen)
logoButton['font'] = myFont
logoButton.place(relx = 0.35, rely = 0.25, relheight = 0.2, relwidth = 0.3)

root.mainloop()