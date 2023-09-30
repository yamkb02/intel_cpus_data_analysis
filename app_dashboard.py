import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('Intel_CPUs_cleaned.csv')

# Title
st.title("Intel CPUs Dashboard")

# Create a pie chart with custom colors
desktop_count = df['Desktop'].sum()
embedded_count = df['Embedded'].sum()
mobile_count = df['Mobile'].sum()

data = pd.DataFrame({
    'Type': ['Desktop', 'Embedded', 'Mobile'],
    'Count': [desktop_count, embedded_count, mobile_count]
})

# Define custom colors
colors = ['#FF5733', '#33FFC7', '#FF33F9']

st.plotly_chart(px.pie(data, values='Count', names='Type', title='Market Segmentation of Intel CPUs',
                      color_discrete_sequence=colors))

# Create a slider for CoreCount filter
core_count_slider = st.slider("Select a range for Core Count", 0, int(df['CoreCount'].max()), (0, int(df['CoreCount'].max())))

# Filter the data based on the slider value
filtered_df = df[(df['CoreCount'] >= core_count_slider[0]) & (df['CoreCount'] <= core_count_slider[1])]

# Create a bar chart for filtered data with a custom color
st.plotly_chart(px.histogram(filtered_df, x='CoreCount', title='Distribution of Core Counts in Intel CPUs',
                             color_discrete_sequence=['#FF5733']))

# Create a scatter plot with custom color
st.plotly_chart(px.scatter(df, x='ClockSpeedMax', y='Price', title='Maximum Clock Speed vs Price',
                            color_discrete_sequence=['#33FFC7']))

# Create another scatter plot with custom color
st.plotly_chart(px.scatter(df, x='CoreCount', y='Price', title='Core Count vs Price',
                            color_discrete_sequence=['#FF33F9']))

# Create a correlation matrix heatmap with a custom color
correlation_data = df.iloc[:, 1:].corr()
st.plotly_chart(px.imshow(correlation_data, title='Correlation Matrix', color_continuous_scale='Viridis'))

# Create a heatmap with a custom color
heatmap_data = df[['Price', 'CoreCount', 'ThreadCount']].corr()
st.plotly_chart(px.imshow(heatmap_data, title='Heatmap of Price vs CoreCount and ThreadCount', color_continuous_scale='Viridis'))

# Create a box plot with custom color
st.plotly_chart(px.box(df, x="Lithography", y="ClockSpeedMax", title='Distribution of Clock Speed Max by Lithography',
                       color_discrete_sequence=['#FF5733']))

# Add a button to reset the CoreCount filter
if st.button("Reset Filter"):
    core_count_slider = (0, int(df['CoreCount'].max()))

# You can add more 3D-style effects to other plots as needed

# Run the Streamlit app
if __name__ == '__main__':
    st.title('Intel CPUs Dashboard')
    st.sidebar.title('Filter Options')



