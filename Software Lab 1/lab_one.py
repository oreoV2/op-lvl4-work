#This program calculates the amont of litres and cost for those litres of petrol up to 100km 

print("Cost of Litres per Kilometre for Open Roads & City Roads \n ")
#this will print a short sentence so the user knows what the program is and its purpose

print("Km:  | \t\t Open Road Litres:  | \t\t Open Road Cost:  | \t\t   City Litres:  |\t\tCity Cost:  \n")
#this prints out the headings to align with the calculations so the user knows what each calculation is.

open_road_litres = 8.08 #this is a variable and stores what the cost of one litre of petrol is on open roads and stores it for later use
city_litres = 5.95 #this is a variable and stores what the cost of one litre of petrol is on city roads and stores it for later use
base_price = 1.949 #this is the base price for the petrol


for km in range(5, 101, 5): #this is the start of the for loop, it creates "km" as a variable and says that in the range of 5 to 100 go up in fives
    open_road_litres_calc = km / open_road_litres #this variable calculates litres for km needed 
    city_litres_calc = km / city_litres #this variable calculates litres for km needed 
    open_road_cost = open_road_litres_calc * base_price #this variable calculates the cost for km needed 
    city_road_cost = city_litres_calc * base_price #this variable calculates the cost for km needed 
    print(f"{km:2d} \t \t \t {open_road_litres_calc:0.2f} \t \t \t \t {open_road_cost:0.2f} \t \t \t \t {city_litres_calc:0.2f} \t \t \t {city_road_cost:0.2f}") 
    #the print statement above will print the results/calculations for each the cost and litres needed per km, \t spaces it out {} calls a function  
    #0.2f rounds to two decimal places


