import requests
import streamlit as st

def main(search_line,search_station):
    # Step 1: Define the API endpoint
    url = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php"

    # Step 2: Set up the parameters
    params = {
        "line": search_line,  # Parameter 1 - line
        "sta": search_station       # Parameter 2 - sta
    }

    # Step 3: Make the GET request
    response = requests.get(url, params=params)

    # Step 4: Check the response status and parse the data
    if response.status_code == 200:
        try:
            data = response.json()
            # Extract schedules for the specified station    
            schedules = data.get("data", {}).get(params["line"]+"-"+params["sta"], {})
            for direction in ["UP", "DOWN"]:
                trains = schedules.get(direction, [])
                st.write(f"Direction: {direction}")
                for train in trains:
                    time = train.get("time")
                    dest = train.get("dest")
                    plat = train.get("plat")
                    st.write(f"  Next train at {time} to {dest} (Platform {plat})")
        except ValueError:
            st.write("Response is not in JSON format.")
            st.write(f"Response text: {response.text}")
    else:
        st.write(f"Error: {response.status_code} - {response.text}")