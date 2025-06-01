# Build a website with python
# cmd - streamlit run streamlit_mtrapp.py
# pip freeze > requirements.txt

import time
import streamlit as st
import numpy as np
import pandas as pd
import requests

# Import the main function from mtr_api.py
from mtr_api import main

# Website config
st.set_page_config(
   page_title="MTR Next Train App",
   page_icon="🚆",
   layout="centered",
   initial_sidebar_state="expanded",
   menu_items={}
)

# Website title
st.title('🚇MTR Next Train information:')

# Time progress bar
bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1, f'In progress... {i+1} %')
    time.sleep(0.05)

bar.progress(100, 'Completed！')

# Display welcome message as a user
with st.chat_message("assistant"):
    st.write("Hi 👋, I am Jen Bot 🤖")
    st.write("You can search MTR next train infomration here.🚉")
    st.write("Have a nice day! 😁")

# User input for ine 
userinput_line = st.selectbox(
    "Which route you want to search for?",
    options=("KTL - Kwun Tong Line", "ISL - Island Line", "TKL - Tseung Kwan O Line", "TML - Tuen Ma Line", "EAL - East Rail Line", "TWL - Tsuen Wan Line"),
    index=0,
    placeholder="Select the route ...",
)

st.write("You selected:", userinput_line)

search_line = userinput_line.split(" - ")[0]  # Extract the line code from the selection

# Mapping of stations based on the selected line
station_list = []

if search_line == "KTL":
    station_list = ['WHA - Whampoa', 'HOM - Ho Man Tin', 'YMT - Yau Ma Tei', 'MOK - Mong Kok', 'PRE - Prince Edward', 'SKM - Shek Kip Mei', 'KOT - Kowloon Tong', 'LOF - Lok Fu', 'WTS - Wong Tai Sin', 'DIH - Diamond Hill', 'CHH - Choi Hung', 'KOB - Kowloon Bay', 'NTK - Ngau Tau Kok', 'KWT - Kwun Tong', 'LAT - Lam Tin', 'YAT - Yau Tong', 'TIK - Tiu Keng Leng']
elif search_line == "ISL":
    station_list = ['KET - Kennedy Town', 'HKU - HKU', 'SYP - Sai Ying Pun', 'SHW - Sheung Wan', 'CEN - Central', 'ADM - Admiralty', 'WAC - Wan Chai', 'CAB - Causeway Bay', 'TIH - Tin Hau', 'FOH - Fortress Hill', 'NOP - North Point', 'QUB - Quarry Bay', 'TAK - Tai Koo', 'SWH - Sai Wan Ho', 'SKW - Shau Kei Wan', 'HFC - Heng Fa Chuen', 'CHW - Chai Wan']
elif search_line == "TKL":
    station_list = ['NOP - North Point', 'QUB - Quarry Bay', 'YAT - Yau Tong', 'TIK - Tiu Keng Leng', 'TKO - Tseung Kwan O', 'LHP - LOHAS Park', 'HAH - Hang Hau', 'POA - Po Lam']  
elif search_line == "TML":
    station_list = ['WKS - Wu Kai Sha', 'MOS - Ma On Shan', 'HEO - Heng On', 'TSH - Tai Shui Hang', 'SHM - Shek Mun', 'CIO - City One', 'STW - Sha Tin Wai', 'CKT - Che Kung Temple', 'TAW - Tai Wai', 'HIK - Hin Keng', 'DIH - Diamond Hill', 'KAT - Kai Tak', 'SUW - Sung Wong Toi', 'TKW - To Kwa Wan', 'HOM - Ho Man Tin', 'HUH - Hung Hom', 'ETS - East Tsim Sha Tsui', 'AUS - Austin', 'NAC - Nam Cheong', 'MEF - Mei Foo', 'TWW - Tsuen Wan West', 'KSR - Kam Sheung Road', 'YUL - Yuen Long', 'LOP - Long Ping', 'TIS - Tin Shui Wai', 'SIH - Siu Hong', 'TUM - Tuen Mun'] 
elif search_line == "EAL":
    station_list = ['ADM - Admiralty', 'EXC - Exhibition Centre', 'HUH - Hung Hom', 'MKK - Mong Kok East', 'KOT - Kowloon Tong', 'TAW - Tai Wai', 'SHT - Sha Tin', 'FOT - Fo Tan', 'RAC - Racecourse', 'UNI - University', 'TAP - Tai Po Market', 'TWO - Tai Wo', 'FAN - Fanling', 'SHS - Sheung Shui', 'LOW - Lo Wu', 'LMC - Lok Ma Chau'] 
elif search_line == "TWL":
    station_list = ['CEN - Central', 'ADM - Admiralty', 'TST - Tsim Sha Tsui', 'JOR - Jordan', 'YMT - Yau Ma Tei', 'MOK - Mong Kok', 'PRE - Price Edward', 'SSP - Sham Shui Po', 'CSW - Cheung Sha Wan', 'LCK - Lai Chi Kok', 'MEF - Mei Foo', 'LAK - Lai King', 'KWF - Kwai Fong', 'KWH - Kwai Hing', 'TWH - Tai Wo Hau', 'TSW - Tsuen Wan'] 
else:
    station_list = ['No stations available for this line']

# User input for station
userinput_station = st.selectbox(
    "Which station you want to search for?",
    options=(station_list),
    index=0,
    placeholder="Select the station ...",
)

st.write("You selected:", userinput_station)

search_station = userinput_station.split(" - ")[0]  # Extract the line code from the selection

# Submit the search
if st.button("Submit"):
    st.write("🤖 Output : ")
    main(search_line,search_station)