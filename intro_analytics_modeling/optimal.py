#%%
# install packages
import pandas as pd
from pulp import *
from pprint import pprint

#%%
# class to encapsulate each sub problem
class Problem:

    def __init__(self, df) -> None:
        self.df = df
        self.food = [row for row in self.df['Foods']]
        self.cost = [row for row in self.df['Price/ Serving']]
        self.nutrients = []
        self.nutrients.append([row for row in self.df['Calories']])
        self.nutrients.append([row for row in self.df['Cholesterol mg']])
        self.nutrients.append([row for row in self.df['Total_Fat g']])
        self.nutrients.append([row for row in self.df['Sodium mg']])
        self.nutrients.append([row for row in self.df['Carbohydrates g']])
        self.nutrients.append([row for row in self.df['Dietary_Fiber g']])
        self.nutrients.append([row for row in self.df['Protein g']])
        self.nutrients.append([row for row in self.df['Vit_A IU']])
        self.nutrients.append([row for row in self.df['Vit_C IU']])
        self.nutrients.append([row for row in self.df['Calcium mg']])
        self.nutrients.append([row for row in self.df['Iron mg']])
        self.min = [1500,30,20,800,130,125,60,1000,400,700,10]
        self.max = [2500,240,70,2000,450,250,100,10000,5000,1500,40]
        return

    # no constraint optimization
    def optimize_without_constaint(self) -> bool:
        solution = LpProblem('HW7', LpMinimize)
        amounts = [LpVariable(food_item, 0) for food_item in self.food]
        cols = df.columns[3:]
        solution += lpSum([a*b for a, b in zip(self.cost, amounts)]), 'total_cost'
        for i, col_nm in enumerate(cols):
            solution += lpSum([a*b for a, b in zip(self.nutrients[i], amounts)]) >= self.min[i], f'min_{col_nm}'
            solution += lpSum([a*b for a, b in zip(self.nutrients[i], amounts)]) <= self.max[i], f'max_{col_nm}'
        solution.solve()
        pprint([f'{a} : {b}' for a, b in zip([v.name for v in solution.variables()],[v.varValue for v in solution.variables()])])
        return True

#%%
# assumes xls is in same dir
df = pd.read_excel('diet.xls')
df.dropna(inplace=True)
print(df)
prolem_13_2_1 = Problem(df).optimize_without_constaint()
# %%
