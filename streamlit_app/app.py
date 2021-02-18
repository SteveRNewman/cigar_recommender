#############version used on heroku###################
import streamlit as st
from PIL import Image
import model_app
import pandas as pd
import random 

st.set_page_config(page_title="Cigars-Rec", page_icon="💨" , layout='centered')

whisky_tbl = pd.read_pickle('w_join2.pkl')
#whisky_tbl = pd.read_pickle('w_join2.pkl')
cigar_tbl = pd.read_pickle('df_desc2.pkl')
def_cigar_tbl = pd.read_pickle('c_def_list.pkl')
wky_to_cgr = pd.read_pickle('wky_to_cgr.pkl')
wky_to_cgr2 = pd.read_pickle('final_pref.pkl')

cigar_lst = list(model_app.df_final_v_3.index)
cigar_lst.append(' ')
whsky_lst = list(whisky_tbl.index)
whsky_lst.append(' ')
whsky_lst2 = list(wky_to_cgr2.index)
whsky_lst2.append(' ')

options = cigar_lst
options0 = whsky_lst2
options1 = whsky_lst
options2 = list(cigar_tbl.columns[:-1])
options3 = list(whisky_tbl.columns[:-1])
options4 = list(wky_to_cgr.columns[:-2])
options5 = list(wky_to_cgr2.columns[:-2])
options10 = list(whisky_tbl.index)
options11 = list(wky_to_cgr2.index)

def get_key2(val):
    for key, value in dict(enumerate(options10)).items():
         if val == value:
            return key

def get_key3(val):
    for key, value in dict(enumerate(options11)).items():
         if val == value:
            return key

st.markdown(
    """<h1 style='display: block; text-align: center;' >Cigar Recommender</h1>
    """,
    unsafe_allow_html=True)
img = Image.open('figures/cigar.jpeg')
img2 = Image.open('figures/img2.jpeg')
col1, col2, col3 = st.beta_columns([1,1,1])
col2.image(img, width= 200)
st.image( img2,  caption='“Smoking cigars is like falling in love. \n First, you are attracted by its shape; you stay for its flavor, and you must always remember never, never to let the flame go out.”\n Winston Churchill')

home_btn = st.radio('',['Instructions','Enter Favorite Cigar Name', 'Enter Favorite Cigar Profile','Match Cigar to Whisky', 'Match Whisky to Cigar'],index=1)

if home_btn == ('Instructions'):

	st.write('There are four ways to search for cigars:')
	st.write('__Enter Favorite Cigar Name__  \n Enter the name of your favorite cigar and a list of ten similar cigars will display.\n   \n There are over 1600 cigars in the list, however, I was not able to capture every one. If your favorite cigar is missing from the list, leave a note in the comments and I will add it in.')	
	st.write('__Enter Favorite Cigar Profile__  \n Enter as many profile notes as you like and matching cigars will be displayed.')
	st.write('__Match Cigar to Whisky__  \n Enter the name of your favorite cigar and a list of ten matching whiskys will display.')
	st.write('__Match Whisky to Cigar__  \n Enter the name of your favorite whisky and a list of ten matching cigars will display.  \n   \n There are over 2400 whiskys in the list, however, I was not able to capture every one. If your favorite whisky is missing from the list, leave a note in the comments and I will add it in.')




if home_btn == ('Enter Favorite Cigar Name'):

	st.subheader('Enter your favorite cigar and autocomplete will provide selection.  \n  \n (If your favorite cigar is missing from the list, leave a note in the comments and I will add it in.)')
	cigar_id = st.selectbox('Start typing cigar name', options, index=1612)
	srch_cigar_btn = st.button('Search Cigars')
	srch_profile_btn = None
	whisky_btn = None
	w_srch_cigar = None
	if srch_cigar_btn:
		if cigar_id == (' '):
			st.error('Please enter a valid cigar')
		else:
			st.success('Distance scores closer to zero are better matches because they have more similar features.')
			query_index = model_app.get_key(val=cigar_id)
			distances, indices = model_app.knn_search.kneighbors(model_app.df_final_v_3.iloc[query_index,:].values.reshape(1,-1), n_neighbors=11)
			for i in range(0,len(distances.flatten())):
				if i == 0:
					st.write('Top Cigar Recommendations for: {}'.format(model_app.df_final_v_3.index[query_index]))
					st.write(' Profile notes: {}'.format(cigar_tbl['New'][query_index][:-1]))
					html_string1 = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>Cigar Info</a>".format(model_app.df_final_v_3.index[query_index].replace("'",""))
					st.markdown(html_string1, unsafe_allow_html=True)
				else:
					p2 = model_app.df_final_v_3.index[indices.flatten()[i]]
					st.write('{}: {} with a Distance Score of: {}'.format(i, model_app.df_final_v_3.index[indices.flatten()[i]],round(distances.flatten()[i],4)))
					st.write(' Profile notes: {}'.format(cigar_tbl['New'][p2][:-1]))
					html_string = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>Cigar Info</a>".format(model_app.df_final_v_3.index[indices.flatten()[i]].replace("'",""),round(distances.flatten()[i],4))
					st.markdown(html_string, unsafe_allow_html=True)
			st.success('Finished')

if home_btn == ('Enter Favorite Cigar Profile'):

		st.info('Select any number of profile keywords. Then select "Search Cigars" for new matches.')
		profile = st.multiselect('Select only one strength option (all capitalized) for best results:', options2)
		srch_profile_btn = st.button('Search Cigars')
		srch_cigar_btn = None
		whisky_btn = None
		w_srch_cigar = None
		if srch_profile_btn:
			if profile:
				st.success('Select "Search Cigars" again for new options if more than 10 matches are available.')
				targets = profile
				cigar_tbl['pro'] = pd.DataFrame(cigar_tbl.New.apply(lambda sentence: all(word in sentence for word in targets)))
				df = pd.DataFrame(cigar_tbl['New'][cigar_tbl['pro']==True])
				if len(df)>10:
					df=df.sample(n=10)
				for i in range(len(df)):
					st.write('{}: {}'.format(i+1,df.index[i]))
					st.write('---Profile notes: {}'.format(df["New"][i][:-1]))
					html_string = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>Cigar Info</a>".format(df.index[i].replace("'",""))
					st.markdown(html_string, unsafe_allow_html=True)

if home_btn == ('Match Cigar to Whisky'):

		#st.info('Enter your favorite cigar and autocomplete will provide selection.')
		pck_cigar = st.selectbox('Enter your favorite cigar for profile notes.', options, index=1612)
		#w_srch_cigar = st.button('Search Cigar')
		
		if pck_cigar:
			if pck_cigar == (' '):
				st.error('Please enter a valid cigar')
			else:
				#st.success('Enter cigar profile notes in whisky selection box.')
				query_index = model_app.get_key(val=pck_cigar)
				# distances, indices = model_app.knn_search.kneighbors(model_app.df_final_v_3.iloc[query_index,:].values.reshape(1,-1), n_neighbors=11)
				# for i in range(0,len(distances.flatten())):
				# 	if i == 0:
				st.write('Cigar profile to match to whisky: {}'.format(model_app.df_final_v_3.index[query_index]))
				st.write(' Profile notes: {}'.format(cigar_tbl['New'][query_index][:-1]))
				html_string1 = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>Cigar Info</a>".format(model_app.df_final_v_3.index[query_index].replace("'",""))
				st.markdown(html_string1, unsafe_allow_html=True)
				cig_list = def_cigar_tbl['c_targ_l'][query_index]
				if cig_list == ['']:
					st.error('No Matches')
					w_profile = None
				else:
					cig_list = cig_list
					w_profile = st.multiselect('Select whisky profile notes', options3, default=cig_list)
				#whisky_btn = st.button('Search Whisky')
				srch_cigar_btn = None
				st.experimental_set_query_params(my_saved_result=w_profile)
				
				app_state = st.experimental_get_query_params()  
						
				w_profile2 = app_state["my_saved_result"]
				#st.write(f'{w_profile2}')		
				whisky_btn2 = st.button('Search Whiskys')		
				if whisky_btn2:
					if w_profile2:
						st.success('Select "Search Whisky" again for new options if more than 10 matches are available.')
						st.success('Add or delete profile notes for more whisky options. Coffee, Espresso, and Cedar are limiting profile notes in whisky, consider removing them.')
						w_targets = w_profile2
						whisky_tbl['pro'] = pd.DataFrame(whisky_tbl.new.apply(lambda sentence: all(word in sentence for word in w_targets)))
						w_df = pd.DataFrame(whisky_tbl['new'][whisky_tbl['pro']==True])
						if len(w_df)>10:
							w_df=w_df.sample(n=10)
						for i in range(len(w_df)):
							st.write('{}: {}'.format(i+1,w_df.index[i]))
							st.write('---Profile notes: {}'.format(w_df["new"][i][:-1]))
							html_string = "<a target='_blank' href='http://google.com/search?q={}+distiller.com&rlz'>whisky info</a>".format(w_df.index[i].replace("'",""))
							st.markdown(html_string, unsafe_allow_html=True)
						
				srch_profile_btn = None
				srch_cigar_btn = None

if home_btn == ('Match Whisky to Cigar'):
	prefer = st.checkbox('Preferred Whisky Only')
	if prefer:
		st.subheader('Enter your favorite whisky and autocomplete will provide selection.  \n (If your favorite whisky is missing from the list, leave a note in the comments and I will add it in.)')
		whisky_id = st.selectbox('Start typing whisky name', options0, index=1593)
		srch_profile_btn = None
		whisky_btn = None
		w_srch_cigar = None
		if whisky_id:
			if whisky_id == (' '):
				st.error('Please enter a valid whisky')
			else:
				#st.success('Distance scores closer to zero are better matches because they have more similar features.')
				query_index = get_key3(val=whisky_id)
				st.write('Whisky to match to cigar: {}'.format(wky_to_cgr2.index[query_index]))
				st.write(' Profile notes: {}'.format(wky_to_cgr2['wky_to_cgr2'][query_index][:-1]))
				html_string1 = "<a target='_blank' href='http://google.com/search?q={}+distiller.com&rlz'>Whisky Info</a>".format(wky_to_cgr2.index[query_index].replace("'",""))
				st.markdown(html_string1, unsafe_allow_html=True)
				cig_list= wky_to_cgr2['w_targ_l'][query_index]
				if cig_list == ['']:
					st.error('No Matches')
					c_profile = None
				else:
					cig_list = cig_list
					c_profile = st.multiselect('Select cigar profile notes', options4, default=cig_list)

				srch_cigar_btn = None

				st.experimental_set_query_params(my_saved_result=c_profile)
				app_state = st.experimental_get_query_params()  
				#st.write(f'{w_profile2}')		
				w_profile2 = app_state["my_saved_result"]
				#st.write(f'{w_profile2}')
				whky_cgr_btn = st.button('Search Cigars')		
				if whky_cgr_btn:
					if w_profile2:
						st.success('Select "Search Cigars" again for new options if more than 10 matches are available.')
						st.success('Whiskys have more profile notes than cigars. Delete down to your top 4 profile notes for more cigar selections.')
						w_targets = w_profile2
						cigar_tbl['pro'] = pd.DataFrame(cigar_tbl.New.apply(lambda sentence: all(word in sentence for word in w_targets)))
						c_df = pd.DataFrame(cigar_tbl['New'][cigar_tbl['pro']==True])
						if len(c_df)>10:
							c_df=c_df.sample(n=10)
						for i in range(len(c_df)):
							st.write('{}: {}'.format(i+1,c_df.index[i]))
							st.write('---Profile notes: {}'.format(c_df["New"][i][:-1]))
							html_string = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>Cigar Info</a>".format(c_df.index[i].replace("'",""))
							st.markdown(html_string, unsafe_allow_html=True)
						
				srch_profile_btn = None
				srch_cigar_btn = None
	else:		
		st.subheader('Enter your favorite whisky and autocomplete will provide selection.  \n (If your favorite whisky is missing from the list, leave a note in the comments and I will add it in.)')
		whisky_id = st.selectbox('Start typing whisky name', options1, index=2404)
		srch_profile_btn = None
		whisky_btn = None
		w_srch_cigar = None
		if whisky_id:
			if whisky_id == (' '):
				st.error('Please enter a valid whisky')
			else:
				#st.success('Distance scores closer to zero are better matches because they have more similar features.')
				query_index = get_key2(val=whisky_id)
				st.write('Whisky to match to cigar: {}'.format(whisky_tbl.index[query_index]))
				st.write(' Profile notes: {}'.format(whisky_tbl['new'][query_index][:-1]))
				html_string1 = "<a target='_blank' href='http://google.com/search?q={}+distiller.com&rlz'>Whisky Info</a>".format(whisky_tbl.index[query_index].replace("'",""))
				st.markdown(html_string1, unsafe_allow_html=True)
				cig_list= wky_to_cgr['w_targ_l'][query_index]
				if cig_list == ['']:
					st.error('No Matches')
					c_profile = None
				else:
					cig_list = cig_list
					c_profile = st.multiselect('Select cigar profile notes', options4, default=cig_list)

				srch_cigar_btn = None

				st.experimental_set_query_params(my_saved_result=c_profile)
				app_state = st.experimental_get_query_params()  
				#st.write(f'{w_profile2}')		
				w_profile2 = app_state["my_saved_result"]
				#st.write(f'{w_profile2}')
				whky_cgr_btn = st.button('Search Cigars')		
				if whky_cgr_btn:
					if w_profile2:
						st.success('Select "Search Cigars" again for new options if more than 10 matches are available.')
						st.success('Whiskys have more profile notes than cigars. Delete down to your top 4 profile notes for more cigar selections.')
						w_targets = w_profile2
						cigar_tbl['pro'] = pd.DataFrame(cigar_tbl.New.apply(lambda sentence: all(word in sentence for word in w_targets)))
						c_df = pd.DataFrame(cigar_tbl['New'][cigar_tbl['pro']==True])
						if len(c_df)>10:
							c_df=c_df.sample(n=10)
						for i in range(len(c_df)):
							st.write('{}: {}'.format(i+1,c_df.index[i]))
							st.write('---Profile notes: {}'.format(c_df["New"][i][:-1]))
							html_string = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>Cigar Info</a>".format(c_df.index[i].replace("'",""))
							st.markdown(html_string, unsafe_allow_html=True)
						
				srch_profile_btn = None
				srch_cigar_btn = None

html_stringp = "<a target='_blank' href='https://stevernewman.github.io/'>About</a>"
st.markdown(
    """<a target='_blank;' style='display: block; text-align: center;' href="https://chefnewman.github.io/">About</a>
    """,
    unsafe_allow_html=True)
fb = st.checkbox("Comments", value=False)
if fb:
    st.components.v1.iframe("https://s3.us-east-2.amazonaws.com/cigars-rec.com/discuss.html", height=400, scrolling=True)
    st.components.v1.iframe("https://s3.us-east-2.amazonaws.com/cigars-rec.com/disqus.html",height=400, scrolling=True)