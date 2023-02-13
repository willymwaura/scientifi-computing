import seaborn as sns  
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("VIOLIN PLOT WITH STREAMLIT")
st.subheader("ASSIGNMENT 2")

data = pd.read_csv("gapminder_with_codes.csv")
data_2007 = data[data['year']==2007][['gdpPercap']]
# , 'pop', 'lifeExp'

# Plot the data using a violin plot
fig, ax = plt.subplots()
sns.violinplot(data=data_2007, ax=ax)
plt.title("GDP  in 2007\n", fontweight='bold')

ax.set_xlabel("GDP", fontweight='bold')
ax.set_ylabel("Values", fontweight='bold')


# Display the plot in the Streamlit app
st.pyplot(fig)


# POPULATION 

data_pop = data[data['year'] == 2007][['pop']]

fig2 , ax2 = plt.subplots()

sns.violinplot(data=data_pop , ax=ax2)

ax2.set_xlabel("POPULATION", fontweight='bold')
ax2.set_ylabel("Values", fontweight='bold')

st.pyplot(fig2)

#LIFE EXPECTANCY
data_exp = data[data['year'] == 2007][['lifeExp']]

fig3 , ax3 = plt.subplots()

sns.violinplot(data=data_exp , ax=ax3)

ax3.set_xlabel("LIFE EXPECTANCY", fontweight='bold')
ax3.set_ylabel("Values", fontweight='bold')

st.pyplot(fig3)