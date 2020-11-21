#############version used on heroku###################
import streamlit as st
from PIL import Image
#import models_app
import pandas as pd 


#default_range =20

#sidebars
# st.sidebar.header('Info')
# st.sidebar.text('subsection')

#test/title
st.title("Cigar Recommender")

img = Image.open('figures/cigar.jpeg')
st.image(img, caption='“Smoking cigars is like falling in love. First, you are attracted by its shape; you stay for its flavor, and you must always remember never, never to let the flame go out.” - Winston Churchill')

#header
st.header('Input your favorite cigar.')
st.subheader('You can search any cigars listed here, \n https://www.cigarsinternational.com/shop/big-list-of-cigars-brands/1803000/ ')

#ask user for input
cigar_id = st.text_input('Enter cigar name.')

#zip_code = st.text_input('Enter zip code to search for similar climbs in that area:', '92008')
st.info('Or search by profile notes')
profile = st.text_input('Enter profile keyword:', '')
#state = st.text_input('Enter state to search in that area:', '')

#st.text('Lastly, enter the search radius (defaults to 20 miles)')
#radius_range = st.number_input('Enter radius to search in specified area:', default_range)


#once button pressed we check for input errors and start search
test = st.button('Search for recommended cigars')
# pd.set_option('max_colwidth', 100)

#run recommender
# if test:
# 	if climb_id:
# 		#spinner
# 		#below lines show we are done
# 		if len(climb_id)>10:
# 			climb_id = climb_id.split('/')[-2]
# 		#else we have climb id lets look it up
# 		st.success('Searching for similar climbs in that area')
# 		#call function and pass id, city, state, zip and radius
# 		#fxn returns df of 10 most similar climbs in search range
# 		st.dataframe(models_app.get_wrecked(target_id=climb_id, target_state=state,target_city=city,
# 			target_zipcode=zip_code,target_radius_range=radius_range,star_limit=3.5))
# 		st.success('Finished')
# 		st.balloons()
# 		#RUN recommender
# 	else:
# 		st.error('Please enter a valid ID/url into the climb id box')
# 		#ERROR please input a target climb


# img2 = Image.open('figures/09A21D41-981D-4FC1-A359-74653420A488_1_105_c.jpeg')
# st.image(img2, caption='View of the Witch in the Needles, CA')























