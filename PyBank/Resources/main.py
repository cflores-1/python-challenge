#PyBank main
#Python script that analyzes the records to calculate each of the following:

import pathlib
import csv

#The total number of months included in the dataset
#Defining the calculation and printing 
   
        Total_Months = (A2:A87)
        print = ("Total Months: Total_Months ")
       
#The net total amount of "Profit/Losses" over the entire period
#Defining the calculation and printing 

        Total_Amount = sum(B2:B87)
        print = ("Total: Total_Amount")

#The average of the changes in "Profit/Losses" over the entire period
#Defining the calculation and printing 

        output = B3-B2
        output = (B3+1)-(B2+1)
        #and so on...

        outputlist = 

        average_changes = avg(outputlist)
        print = ("Average Change: average_changes")

#The greatest increase in profits (date and amount) over the entire period
#Defining the calculation and printing 



        inc_profit = max(average_changes)
        print = ("Greatest Increase in Profits: inc_profit")

#The greatest decrease in losses (date and amount) over the entire period
#Defining the calculation and printing 

        dec_profit = min(average_changes)
        print = ("Greatest Decrease in Profits: dec_profit")