import pandas as pd
import matplotlib.pyplot as plt

class GraphThings:

    dfother03 = pd.read_excel('Project_File.xlsx', sheet_name='International Monthly Visitor A')
    pd.set_option("display.max_columns", None)


    first_col = dfother03.iloc[:, 0]
    new_col = first_col.str.split()
    date = ''
    data1 = []
    data2 = []

    for i in range(len(new_col)):
        date = new_col[i]
        year = date[0]
        month = date[1]
        data1.append(year)
        data2.append(month)

    dfother03.insert(0, "Year", data1)
    dfother03.insert(1, "Month", data2)

    dfother03.drop(dfother03.columns[2], inplace=True, axis=1)
    another = dfother03[dfother03["Year"] >= "2008"]
    another.drop(another.iloc[:, 2:20], inplace=True, axis=1)
    another.drop(another.iloc[:, 13:18], inplace=True, axis=1)
    another1 = dfother03[dfother03["Year"] == "2008"]

    another1.plot.bar()
    plt.xlabel("Year")
    plt.ylabel("Number of Visitors")
    plt.title("Total Visitor")

    another1.plot.line()
    plt.xlabel("Year")
    plt.ylabel("Number of Visitors")
    plt.title("Total Visitor")

    another1.plot.barh()
    plt.xlabel("Year")
    plt.ylabel("Number of Visitors")
    plt.title("Total Visitor")

    def viewVisitorByYear(self, year):
        yearStats = self.another[self.another["Year"] == str(year)]
        print(yearStats)

    def viewTotalVisitorByYear(self, year):
        yearStats = self.another[self.another["Year"] == str(year)].groupby("Year").sum().reset_index()
        print(yearStats)

    def viewMedianTotalVisitorByYear(self, year):
        yearStats = self.another[self.another["Year"] == str(year)].median()
        print(yearStats)

    def test1(self, year):
        yearStats = self.another[self.another["Year"] == str(year)].sum().reset_index()
        print(yearStats)

    def viewSumTotalVisitorByYear(self, year):
        yearStats = self.another[self.another["Year"] == str(year)].sum()
        print(yearStats)




gts = GraphThings()
gts.viewVisitorByYear(2017)
gts.viewTotalVisitorByYear(2017)
gts.viewMedianTotalVisitorByYear(2009)
gts.test1(2008)
gts.viewSumTotalVisitorByYear(2011)
plt.show()
