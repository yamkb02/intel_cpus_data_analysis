import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('Intel_CPUs_cleaned.csv')

# Title
st.title("Intel CPUs Dashboard")

# Create a pie chart
desktop_count = df['Desktop'].sum()
embedded_count = df['Embedded'].sum()
mobile_count = df['Mobile'].sum()

data = pd.DataFrame({
    'Type': ['Desktop', 'Embedded', 'Mobile'],
    'Count': [desktop_count, embedded_count, mobile_count]
})

st.plotly_chart(px.pie(data, values='Count', names='Type', title='Market Segmentation of Intel CPUs'))

# Create a bar chart
st.plotly_chart(px.histogram(df, x='CoreCount', title='Distribution of Core Counts in Intel CPUs'))

# Create a scatter plot
st.plotly_chart(px.scatter(df, x='ClockSpeedMax', y='Price', title='Maximum Clock Speed vs Price'))

# Create another scatter plot
st.plotly_chart(px.scatter(df, x='CoreCount', y='Price', title='Core Count vs Price'))

# Create a correlation matrix heatmap
correlation_data = df.iloc[:, 1:].corr()
st.plotly_chart(px.imshow(correlation_data, title='Correlation Matrix'))

# Create a heatmap
heatmap_data = df[['Price', 'CoreCount', 'ThreadCount']].corr()
st.plotly_chart(px.imshow(heatmap_data, title='Heatmap of Price vs CoreCount and ThreadCount'))

# Create a box plot
st.plotly_chart(px.box(df, x="Lithography", y="ClockSpeedMax", title='Distribution of Clock Speed Max by Lithography'))


# You can add more 3D-style effects to other plots as needed

# Run the Streamlit app
if __name__ == '__main__':
    st.title('Intel CPUs Dashboard')
    st.sidebar.title('Filter Options')


