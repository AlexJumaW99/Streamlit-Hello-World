#Make necessary imports
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st

select = st.sidebar.selectbox('Page', ['Home', 'About Me'], key='1')

if select == 'Home':

    #create our df object 
    df = pd.read_csv('fandango_scrape.csv')

    #let's carry out some EDA
    df = df[(df['STARS']!=0) | (df['VOTES']!=0) | (df['RATING']!=0)]
    df['YEAR'] = df['FILM'].str.split(' ').str[-1].str[1:-1]
    df['YEAR'] = df['YEAR'].apply(lambda x: int(x))
    #aggr df
    aggr = df.describe() #aggr of each column 

    #corr df
    corr_df = df.drop('YEAR', axis=1).corr()

    #movies with highest number of votes
    high_votes = df.nlargest(10,'VOTES')

    #add a title to the webpage
    st.title('FANDANGO DATA ANALYSIS PROJECT')
    st.header('Is there a conflict of interest for a company that both sells movie tickets and reviews movies?')
    st.write('The company in question here is Fandango (raw data can be toggled off from the sidebar).')

    #creation of a side-bar and checkbox to display df
    sidebar = st.sidebar
    sidebar.title('Sidebar')
    sidebar.header('Toggle Plots ON/OFF')
    df_display = sidebar.checkbox('Display Raw Data', value=True)
    aggr_display = sidebar.checkbox('Display Column Aggregates', value=True)
    scatt_display = sidebar.checkbox('Show Scatter Plot: Rating vs Votes', value=True)
    corr_display = sidebar.checkbox('Show the Correlation Matrix for the numerical columns', value=True)
    count_display = sidebar.checkbox('Show the number of movies released each year', value=True)
    highest_votes = sidebar.checkbox('Show the movies with the highest number of votes', value=True)
    kde_display = sidebar.checkbox('Show KDE Distribution plot for num and star ratings', value=True)

    if df_display:
        st.write(df)

    st.subheader('Let us take a look at the statistical aggregates')

    if aggr_display:
        st.write(aggr)

    def plot_scatt(data):
        fig, ax = plt.subplots()
        ax = sns.scatterplot(data=data, x='RATING', y='VOTES', hue='YEAR')
        ax.set_title('RATING VS NO. OF VOTES', color='#b11e31', fontweight=600)
        ax.set_xlabel('Numerical Rating')
        ax.set_ylabel('Number of Votes')
        st.pyplot(fig)

    st.subheader('Scatter Plot')
    st.write('That shows the number of votes for each movie rating.')

    if scatt_display:
        plot_scatt(df)

    if corr_display:
        st.subheader('Let us look at the Correlation between the various columns')
        st.write(corr_df, 'We can clearly see that most of the columns are directly proportional from the +ve values.')

    def plot_yrcount(data):
        fig, axes = plt.subplots()
        axes = sns.countplot(data=data, x='YEAR')
        st.pyplot(fig)

    if count_display:
        st.subheader('Let us look at the distribution of movies by year')
        plot_yrcount(df)

    if highest_votes:
        st.subheader('These are the 10 movies with the highest number of votes')
        st.write(high_votes)


    def kde_pl(data):
        fig, ax = plt.subplots()
        sns.kdeplot(ax=ax, data=data, x='RATING', shade=True, color='#00e1d9', label='Numerical Rating')
        sns.kdeplot(ax=ax, data=data, x='STARS', shade=True, color='#5e001f', label='Stars')
        ax.legend(loc=(1.1,0.5))

        st.pyplot(fig)

    if kde_display:
        st.subheader('KDE plot showing distributions for Star and Numerical Ratings')
        st.write('From this plot we can clearly see that they round up their numerical ratings to achieve higher star ratings for each movie.')
        st.write('This deceives the client as it gives them the impression that the movie is better than it actually is.')
        kde_pl(df)
    
elif select == 'About Me':
    st.title('Who is Alex Juma?')
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quam lacus, laoreet eget euismod id, tristique sed sapien. In elementum nulla non scelerisque posuere. Vestibulum sagittis ex placerat arcu pellentesque commodo. In finibus tortor at convallis pretium. Etiam libero nisi, tempus ac dignissim vitae, tristique eget massa. Fusce gravida a risus at cursus. Etiam sollicitudin porta neque non semper. In sit amet enim quis ligula placerat tincidunt. Phasellus nec mi eleifend sem finibus accumsan. Nulla facilisi. Vivamus nec consequat enim.')
    st.write('Duis augue nisl, sodales nec tincidunt vel, condimentum sit amet ipsum. Donec ac placerat metus. Nunc viverra non nibh porta facilisis. Quisque id viverra arcu, quis varius lacus. Cras lobortis vestibulum dolor pellentesque suscipit. Nullam urna orci, vulputate vel ligula non, placerat porttitor lorem. Sed blandit eros ex. Aliquam diam dolor, euismod feugiat condimentum in, facilisis eu ligula. Phasellus aliquet massa eu tristique ullamcorper. Phasellus vulputate neque sit amet condimentum lobortis.')
