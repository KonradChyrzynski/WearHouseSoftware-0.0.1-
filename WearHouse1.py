import os

x = 0

def loop():
    question = input("What you want to do?: ")
    while question != "quit":
        if question == "search":
            Article.searching()
            question
        elif question == "quit":
            quit()


class Article:

    def __init__(self,name,num,location,quantity,lenght,width):
        self.name = name
        self.num = num
        self.location = location
        self.quantity = quantity
        self.lenght = lenght
        self.widht = width


    def print_article(self):
        print("Name: " + self.name)
        print("Number: " + str(self.num))
        print("Location: " + self.location)
        print("Quantity: " + str(self.quantity))
        print("Lenght: " + str(self.lenght))
        print("Width: " + str(self.widht))

    def quit(self=2):
        quit


    def Upgraded_searching(self,name):
        in_put = input("Enter the name of article, or type quit to exit: ")
        if in_put == self.name:
            print(Article.print_article)


    def searching(self=1):
        in_put = input("Enter the name of article, or type quit to exit: ")
        while in_put != "quit":
            if in_put.upper() == "WOOD":
                print_wood = Wood.print_article()
                break
            elif in_put.upper() == "STEEL":
                print_steel = Steel.print_article()
                break
            elif in_put.upper() == "PICTURE":
                print_Picture = Picture.print_article()
                break
            elif in_put.upper() == "CD":
                print_CD = CD.print_article()
                break
            else: 
                loop()
                



Wood = Article("Wood","2","M1",20,2000,3000)
Steel = Article("Stell","2","M2",150,200,300)
Picture = Article("Picture", "3", "M3", 5,300,300)
CD = Article("CD-01","4","M4",20,20,20)


loop()
print("Test")


















