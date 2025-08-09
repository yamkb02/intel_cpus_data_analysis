import streamlit as st
from PIL import Image

def run():
    st.title('Cookbook')
    if st.button("Return to Dashboard"):
        st.session_state.runpage = 'dashboard'
        st.rerun()

    st.write('## What is your data set?')
    st.write('**Intel Processors**')
    # image = Image.open('correlation_matrix.png')
    # st.image(image, caption='Intel Processors', use_column_width=True)

    st.write('## Where did you acquire your data set?')
    st.write('The dataset was acquired from Kaggle. It was originally scraped from Intel\'s website by the author.')

    st.write('## Why did you choose this particular dataset?')
    st.write('The choice to use a dataset of Intel processors is based on several factors:')
    st.write('**Industry Relevance:** Intel is one of the leading manufacturers of processors in the world. Their products are used in a wide range of devices, from personal computers to servers. Analyzing Intel\'s processors can provide valuable insights into current industry standards and trends.')
    st.write('**Diversity of Data:** Intel\'s product line is diverse, ranging from budget-friendly processors for everyday use to high-performance processors for gaming and professional work. This diversity allows for a more comprehensive analysis as it covers a wide spectrum of the market.')
    st.write('**Technical Specifications:** The dataset includes detailed technical specifications of the processors such as \'Model\', \'Price\', \'MarketSegment\', \'Lithography\', \'CoreCount\', \'ThreadCount\', \'ClockSpeedMax\', \'TurboBoostMaxTechMaxFreq\', \'ClockSpeed\', \'Cache\', \'Bus\', \'MaxTDP\', and \'BornOnDate\'. These attributes can provide insights into the design philosophy, performance characteristics, and pricing strategy of Intel processors.')
    st.write('**Benchmarking and Comparison:** By analyzing Intel\'s processors, we can establish a benchmark against which other manufacturers\' products can be compared. This can be particularly useful when studying market competition and technological advancements in the industry.')
    st.write('However, it\'s important to note that while this dataset provides valuable insights into Intel\'s processors, it does not represent the entire processor market. For a more comprehensive analysis, it would be beneficial to include data from other manufacturers as well.')
    
    st.write('## What are the variables in your dataset?')
    st.write('The variables in the dataset of Intel processors are:')
    st.write('**Model:** The specific model of the processor.')
    st.write('**Price:** The price of the processor.')
    st.write('**MarketSegment:** The market segment that the processor is targeted towards, such as consumer, enterprise, etc.')
    st.write('**Lithography:** The size of the transistors in the processor, measured in nanometers.')
    st.write('**CoreCount:** The number of cores in the processor.')
    st.write('**ThreadCount:** The number of threads that the processor can handle simultaneously.')
    st.write('**ClockSpeedMax:** The maximum clock speed of the processor under normal conditions.')
    st.write('**TurboBoostMaxTechMaxFreq:** The maximum frequency achievable using Intel\'s Turbo Boost Max Technology.')
    st.write('**ClockSpeed:** The base clock speed of the processor.')
    st.write('**Cache:** The size of the processor\'s cache memory.')
    st.write('**Bus:** The bus speed of the processor.')
    st.write('**MaxTDP:** The maximum Thermal Design Power (TDP) that the cooling system needs to dissipate.')
    st.write('**BornOnDate:** The release date of the processor.')
    st.write('Each of these variables provides a different piece of information about the processors and can be used to analyze and compare their performance, cost, and other characteristics.')
    
    st.write('## What is the size of your dataset (number of observations and variables)?')
    st.write('1076 rows × 14 columns before cleaning')
    st.write('595 rows × 11 columns after cleaning')

    st.write('## Are there any missing values or outliers in your data?')
    st.write('Yes there were. The process on how we cleaned the data can be found in the next section.')

    st.write('## How did you clean and process the data?')
    st.write('Initially there were 14 columns in this dataset and 1076 records.')
    st.write('Since most of almost all values under the TurboBoost column is null, we dropped it.')
    image = Image.open('./images/1.png')
    st.image(image, use_column_width=True)

    st.write('All rows that had missing prices were dropped as well because they were too many for an imputation.')
    st.write('12 out of 14 variables were classified as object types to we converted them into numerical values.')
    image = Image.open('./images/2.png')
    st.image(image, use_column_width=True)

    st.write('The variable MarketSegment was converted has three values namely, Desktop, Embedded and Mobile so we used Dummy encoding to convert them.')
    image = Image.open('./images/3.png')
    st.image(image, use_column_width=True)

    st.write('Based on the Intel Website, Intel 7 is 10nm, so we will used this to fill in the missing data')
    image = Image.open('./images/4.png')
    st.image(image, use_column_width=True)
    st.write('ClockSpeedMax and ClockSpeed were converted into numerical types.')
    image = Image.open('./images/5.png')
    st.image(image, use_column_width=True)  

    st.write('In terms of Cache, there are four types: basic, L2, L3, and Intel® Smart Cache. As technology advances, their performance improves. Labels were assigned to them using a label encoder, with higher labels for more recent technologies.')
    image = Image.open('./images/6.png')
    st.image(image, use_column_width=True)  

    st.write('The \'Bus\' variable is difficult to standardize because Gigatransfers and Megahertz can\'t be converted into each other. This column was dropped.')
    image = Image.open('./images/7.png')
    st.image(image, use_column_width=True)

    st.write('MaxTDP is also converted into an int data type.')
    image = Image.open('./images/8.png')
    st.image(image, use_column_width=True)
    st.write('With the case of MaxTDP and ClockSpeed, there were a lot of null values under this column.')
    st.write('Based on the descriptive statistics, the standard deviation of the ClockSpeed isnt as high compared to its mean, we can substitute the null values with the median without losing too much information.')
    st.write('MaxTDP on the other hand is the opposite, thus it would be risky to make substitutions with the null values. So we dropped this column.')
    st.write('All other columns with very little null values were substituted with their median.')
    image = Image.open('./images/9.png')
    st.image(image, use_column_width=True)