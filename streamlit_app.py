
import streamlit
import pandas
streamlit.title("MY Mom's New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & blueberry oatmeal')
streamlit.text(' 🥗 kale, spinach & rocket leaves smoothie')
streamlit.text(' 🐔 Hard boiled Free range eggs')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Lime'])
streamlit.dataframe(my_fruit_list)
