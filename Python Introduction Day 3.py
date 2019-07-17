cadburyType1 = "Milk Chocolate"
cadburyType2 = "Dark Chocolate"
cadburyType3 = "White Chocolate"
print("In the cadbury box, there is", cadburyType1 + ",", cadburyType2 + ", and", cadburyType3)

cadMilk = 5
cadDark = 3
cadWhite = 8
print("There are", cadMilk, cadburyType1, "bars," , cadDark, cadburyType2, "bars, and", 
      cadWhite, cadburyType3, "bars.")

chocolate1 = {"milk":5}
chocolate2 = {"dark":8}
chocolate3 = {"white":3}

chocolateBox = {"milk":5, "dark":8, "white":3}

print(chocolateBox)
print("The number of milk chocolate bars in the chocolate box is", chocolateBox["milk"])
print("The number of white chocolate bars in the chocolate box is", chocolateBox["white"])

#dict data-type pairs
studentAge = {"Steve":32, "Lia":28, "Vin":45, "Katie":38}
studentGender = {"Steve":"Male", "Lia":"Female", "Vin":"Male", "Katie":"Female"}
print(studentAge, studentGender)

print("Lia's age is", studentAge["Lia"], "and gender is", studentGender["Lia"])

import pandas
dir (pandas)

chocolateBox = {"milk":5, "dark":8, "white":3}
chocolateinfo = pandas.Series(chocolateBox)
print(chocolateinfo)

chocolatedata = [chocolateBox] #convert dict to list
print(chocolatedata)

#dataframes
chocolatedf = pandas.DataFrame(chocolatedata, index = ["quantity"]) #convert to columns
print(chocolatedf)

studentInfo = [["steve", 32, "male"], ["Lia", 28, "female"], ["vin", 45, "male"], ["katie", 38, "female"]]
df = pandas.DataFrame(studentInfo)
print(df)

df1 = pandas.DataFrame([studentInfo])
print(df1)

df2 = pandas.DataFrame(studentInfo, columns=["Name","Age","Gender"])
print(df2)