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

studentInfo = [["steve", 32, "male"], ["Lia", 28, "female"], ["vin", 45, "male"],
               ["katie", 38, "female"]]
df = pandas.DataFrame(studentInfo)
print(df)

df1 = pandas.DataFrame([studentInfo])
print(df1)

df2 = pandas.DataFrame(studentInfo, columns=["Name","Age","Gender"])
print(df2)






# DAY 4 DATA VISUALIZATION

import pandas
import plotly

studentInfo = [["Steve", 32, "male"], ["Lia", 28, "female"], ["Vin", 45, "male"],
               ["Katie", 38, "female"]]
print(studentInfo)

df2 = pandas.DataFrame(studentInfo, columns=["name","age","gender"])
print(df2)

#graphing our data
dir (plotly)
from plotly.offline import plot
import plotly.graph_objs as go



agename = go.Bar(x=df2["name"], y = df2["age"])
plot([agename])

#Pandas analysis of excel
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

#we read the data into a dataset or data frame called df
df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")

#we usenthe Bar graph option of the graph_objs from the plotly library
womenoccupation = go.Bar(x = df["occupation"], y=df["women"], 
                         marker = {"color": df["women"], "colorscale" : "Blackbody"})
#we call the plot function from the plotly.offline library
plot([womenoccupation])

#OR we use figure optionof the graph_objs function from the plotly library
fig = go.Figure(data=[womenoccupation])
plot (fig)

titles = go.Layout(
        #Define title of the graph
        title = "Percentage of Women Employed by Occupation",
        
        #Define title for x-axis
        xaxis = go.layout.XAxis(
                title = go.layout.xaxis.Title(
                text = "Occupation",
            )
        ),

        #Define title for y-axis
        yaxis = go.layout.YAxis(
                title = go.layout.yaxis.Title(
                text = "Percentage",
                )
            )
        )

fig = go.Figure(data=[womenoccupation], layout = titles)

plot(fig)
        
#Coding project code: Women CEOS

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

#we read the data into a dataset or data frame called df
df = pd.read_excel("GISdata.xlsx", sheet_name = "womenCEOs")

womenoccupation = go.Bar(x = df["Year"], y=df["CEOs"], 
                         marker = {"color": df["CEOs"], "colorscale" : "jet"})

plot([womenoccupation])

#OR we use figure optionof the graph_objs function from the plotly library
fig = go.Figure(data=[womenoccupation])
plot (fig)

titles = go.Layout(
        #Define title of the graph
        title = "Percentage of Women Employed by Occupation",
        
        #Define title for x-axis
        xaxis = go.layout.XAxis(
                title = go.layout.xaxis.Title(
                text = "Occupation",
            )
        ),

        #Define title for y-axis
        yaxis = go.layout.YAxis(
                title = go.layout.yaxis.Title(
                text = "Percentage",
                )
            )
        )

fig = go.Figure(data=[womenoccupation], layout = titles)

plot(fig)



















