# # A. Daily attendance of bike tracks
# every row contains the number of bicycles on every track of the city(montreal), 
# for every day of the year.
# Can you infer anything from the attendence record?

# url = "https://raw.githubusercontent.com/ndas1971/Misc/master/bikes.csv"

# 1. Read 

import pandas as pd
url=r"C:\Users\Harshika\handson\code\data\bikes.csv"
df = pd.read_csv(url)
print(df)

# 2. Check head 

df.head()

# 3. Check summary statistics 

df.describe()

# 4. plot the daily attendance of two tracks, 'Berri1', 'PierDup'

import matplotlib.pyplot as plt
df.plot(x='Date', y=['Berri1','PierDup'], kind= 'line')
plt.title("Berri1 & PierDup based on Date")
plt.ylabel("daily attendance")
plt.grid(True)
plt.show()

# 5. Check index , explore weekday_name attributes 

df.index
df['weekday']=pd.to_datetime(df['Date'], dayfirst=True).dt.day_name()
df

# 6. Get sum of all attendance as a function of the weekday

#total
df['total'] = df.loc[:,['Berri1','CSC','Mais1','Mais2','Parc','PierDup','Rachel1','Totem_Laurier']].sum(axis=1)
df

#aggregating
attendence=df.groupby('weekday').agg({'total':'sum'})
attendance


# 7. Display this in figure , what is the inference?
#plotting
plt.plot(attendence.index,attendence.total,color='red')