import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def time_period(hour):
    if 8<hour<18:
        return 'Lunch'
    else:
        return 'Dinner'


st.write("""
# Tips Graphs and Info for a Nameless Diner
         
Shown are the many ways one can observe the tippers HORRID and NIGHTMARISH stinginess!
         
""")

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)
tips['time_order'] = pd.to_datetime(np.random.uniform(pd.to_datetime('2023-01-01').timestamp(), pd.to_datetime('2023-01-31').timestamp(), len(tips)), unit = 's')
tips['day_of_the_week'] = tips['time_order'].dt.day_name()
tips['meal_time'] = (tips['time_order'].dt.hour).apply(time_period)


st.line_chart(tips, x = 'time_order', y = 'tip')


sns.histplot(data = tips['total_bill'])
plt.title('Tips Change Over Time')
plt.xlabel('date')
plt.ylabel('tip')
plt.show()

st.pyplot(plt)


st.scatter_chart(tips, x = 'total_bill', y = 'tip')


st.line_chart(tips[['total_bill', 'tip', 'size']])


st.scatter_chart(tips, x = 'day_of_the_week', y = 'total_bill')


sns.boxplot(data = tips, x = 'day_of_the_week', y = 'total_bill', hue = 'meal_time', palette = 'Set1')
plt.title('Tips Box Plot')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')

st.pyplot(plt)


fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (14,6), sharey = True)

sns.histplot(data = tips[tips['meal_time'] == 'Lunch'], x = 'tip', bins = 20, ax = axes[0], color = 'skyblue', kde = True)
axes[0].set_title('Tips During Lunch')

sns.histplot(data = tips[tips['meal_time'] == 'Dinner'], x = 'tip', bins = 20, ax = axes[1], color = 'salmon', kde = True)
axes[1].set_title('Tips During Dinner')

plt.tight_layout()

st.pyplot(plt)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(data = tips[tips['sex']=='Female'], x = 'sex', y='tip', hue = 'smoker', s = 60, alpha = 0.5)
plt.title('Scatterplot для женщин')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

plt.subplot(1, 2, 2)
sns.scatterplot(data = tips[tips['sex']=='Male'], x = 'sex', y='tip', hue = 'smoker', s = 60, alpha = 0.5)
plt.title('Scatterplot для мужчин')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

st.pyplot(plt)


sns.heatmap(tips[['total_bill', 'tip', 'size']].corr(), annot = True, cmap = 'coolwarm', fmt = ".2f", linewidths = 0.5)

st.pyplot(plt)


