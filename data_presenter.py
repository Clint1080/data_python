import matplotlib.pyplot as plt
import numpy as np

open_file = open("CupcakeInvoices.csv")

purchase_amounts = []

for row in open_file:
    # print(row) # checking that it works
    row = row.rstrip('/').split(',')
    
    # print(row[2]) # Cupcake type
    
    purchase_total = float(row[3]) * float(row[4]) # row[3] is amount purchased and row[4] is price per each
    # print(purchase_total) # Checking that I was able to get the totals
    
    purchase_amounts.append(purchase_total) # Putting purchase amounts into a new array
    #print(purchase_amounts)
    
    
purchase_total = round(sum(purchase_amounts), 2) # adding all of the individual purches together
print('All the cupcake purchases = $', purchase_total)

open_file.close()