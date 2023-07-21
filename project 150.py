from tkinter import *
import random

root=Tk()
root.title("Random Countries and Capitals")
root.geometry("400x400")

enter_name = Entry(root)
enter_input = Entry(root)

country_list = Label(root)
capital_list = Label(root)
country_random_number = Label(root)
city_random_number = Label(root)

list1 = []
list2 = []
def country_and_capital():
    country_name = enter_name.get()
    list1.append(country_name)
    country_name["text"] = "Country Name :  " + str(list1)
    
    capital_name = enter_name.get()
    list1.append(capital_name)
    capital_name["text"] = "City Name :  " + str(list2)
    
def random_number():
    length1 = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    country_random_number["text"] = "Random Country: " + str(generated_random_number)
    
    length2 = len(list2)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    country_random_number["text"] = "Random Country: " + str(generated_random_number)
    