import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static01.nyt.com/images/2019/10/07/nyregion/07nytoday/merlin_161095017_2e602694-a94f-4afc-a664-05c69e327571-superJumbo.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.markdown("<h1 style='text-align: center;'>Impact of Uber on NYC Taxi Ridership</h1>", unsafe_allow_html=True)

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
st.write('Using pandas and matplotlib, we illustrated the trend of ridership over the month of June for both Uber and NYC TLC (Taxi and Limousine Commission).')
st.markdown("<h4 style='text-align: center;'>Figure 1</h4>", unsafe_allow_html=True)
st.image('https://i.imgur.com/NxTeoSF.png')
st.markdown("<h4 style='text-align: center;'>Figure 2</h4>", unsafe_allow_html=True)
st.image('https://i.imgur.com/BBcZWwb.png')
st.markdown("<h4 style='text-align: center;'>Figure 3</h4>", unsafe_allow_html=True)
st.image('https://i.imgur.com/ggPYbFo.png')
st.markdown("<h4 style='text-align: center;'>Figure 4</h4>", unsafe_allow_html=True)
st.image('https://www.calendarpedia.com/images-large/months/june-2014-calendar.png')



st.header('Summary')

st.write('In conclusion, we can see from our bar charts that Uber has significantly altered the pickups of yellow cab and green cab taxis in New York City.')
st.write('In figure 3, the majority of Taxi pickups in June 2009 exceeds past 500,000 pickups. In figure 2, the taxi pickups in June 2014 has decreased significantly. Where only a few days in June 2014 does the taxi pickup exceed 500,000.')
st.write('We can also note that when Uber rideshare is available, the taxi pickups become stagnant. In figure 2, the taxi pickups stays relatively the same throughout the month unlike how it is in figure 1.')
st.write('From our analysis of the two datasets, we can conclude Uber has caused a decline in rides among the cabs throughout New York City.')

