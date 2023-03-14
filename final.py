import streamlit as st


st.title('Impact of Uber on NYC Taxi Ridership')

st.header('Background and Motivation')
st.write('Our project focuses on analyzing the ridership volume change over time for both Uber and traditional taxi services in New York City.') 
st.write('We chose this topic because of the growing popularity of rideshare services like Uber and Lyft and their impact on the traditional taxi industry.')
st.write('While rideshare services have been around for several years now, the extent of their impact on traditional taxis is still a topic of much debate.')
st.image("https://spectrum.ieee.org/media-library/taxis-in-new-york-city.jpg?id=25582245&width=1200&height=900")

st.header('Dataset and Data Management Plan')

st.subheader('-Working with raw data')
st.write('We chose two main datasets for our project: June 2014 Uber Pickups in New York City dataset and the New York City Taxi and Limousine Commission (TLC) Trip Record Data for 2009 and 2014 dataset.')
st.write('The Uber dataset includes information about the date and time of each pickup, latitude and longitude coordinates of the pickup location, and the base name of the affiliated Uber dispatch company.')
st.write('TLC dataset includes information about pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts.')
        
st.subheader('-Limitations')
st.write('Our analysis only covers the month of June in 2009 and 2014, which may not be representative of broader trends over time.')
st.write('Uber dataset did not include other factors, such as surge pricing and availability of other transportation options.')
st.write('Did not include the impact of other rideshare companies, like Lyft and Juno, which may have influenced observed ridership trends.')
             
st.subheader('-Design of E/R diagram')
st.write('Both Uber and NYC taxis are the entities. The shared attributes from the two datasets that we utilized to perform our analysis are date/time and trips.')
             
st.header('Analysis')

st.header('Summary')
