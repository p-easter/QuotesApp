import streamlit as st
import pandas as pd
import random as ran

st.title('Find Your Perfect Quote!')
st.markdown('### You can either get a random quote:')
file = 'https://github.com/p-easter/QuotesApp/blob/main/Quotes_lg.csv'

@st.cache
def getData(file):
	df = pd.read_csv(file)
	df.drop('Unnamed: 0', axis=1, inplace=True)
	return df

def randomQuote(df):
	x = ran.randint(0,len(df))
	quote = df.iloc[x]
	return "{} \n\n ~ {}".format(quote['Quote'],quote['Author'])

def getQuotes(df, option):
	quotes = df[df['Author'] == option]['Quote']
	for q in quotes:
		st.write(q)

df = getData(file)

st.button('Get Random Quote', on_click=st.write(randomQuote(df)))

st.markdown('### Or you can select based on the author:')
option = st.selectbox(label = '',
	options = pd.Series(df['Author'].unique()))

st.write(getQuotes(df, option))
