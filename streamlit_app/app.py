#############version used on heroku###################
import streamlit as st
from PIL import Image
import model_app
import pandas as pd

st.set_page_config(page_title="Cigars-Rec", page_icon="💨" , layout="centered")

df_desc2 = pd.read_pickle('df_desc2.pkl')
options5 = list(model_app.df_final_v_3.index)
options5.append(' ')
options = options5
options2 = list(df_desc2.columns[:-1])
st.markdown(
    """<h1 style='display: block; text-align: center;' >Cigar Recommender</h1>
    """,
    unsafe_allow_html=True)
col1, col2, col3 = st.beta_columns([1,1,1])
img = Image.open('figures/cigar.jpeg')
img2 = Image.open('figures/img2.jpeg')
col2.image(img, use_column_width=True)
st.image(img2, caption='“Smoking cigars is like falling in love. First, you are attracted by its shape; you stay for its flavor, and you must always remember never, never to let the flame go out.” Winston Churchill')
test3 = st.radio('Choose how to get cigar recommendations:',['Enter Favorite Cigar Name', 'Enter Favorite Cigar Profile'])
# if test3 == ('About'):
# 	st.header('Info about the model - working on it. Will have features by type in sidebar with buttons to expand and displayed as graphs in the main section.')
# 	wrapper = st.sidebar.button('View Wrapper Types')
# 	filler = st.sidebar.button('View Filler Types')
# 	strength = st.sidebar.button('View Strength Types')
# 	st.sidebar.write('etc.')
# 	test = None
# 	test2 = None
# 	html_string1 = "<a target='_blank' href = 'mailto: stevernewman@gmail.com'>Contact Steve</a>"
# 	st.markdown(html_string1, unsafe_allow_html=True)
if test3 == ('Enter Favorite Cigar Profile'):

		st.info('Select any number of profile keywords. Then select "Search Cigars" for new matches.')
		profile = st.multiselect('Select only one strength option (all capitalized) for best results:', options2)
		test2 = st.button('Search Cigars')
		test = None
else:
	st.subheader('Enter your favorite cigar and autocomplete will provide selection.')
	cigar_id = st.selectbox('Start typing cigar name', options, index=1612)
	test = st.button('Search Cigars')
	test2 = None

# else:
# 	st.error('Please enter a valid cigar')

if test:
	if cigar_id == (' '):
		st.error('Please enter a valid cigar')
	else:
		st.success('Distance scores closer to zero are better matches because they have more similar features.')
		query_index = model_app.get_key(val=cigar_id)
		distances, indices = model_app.knn_search.kneighbors(model_app.df_final_v_3.iloc[query_index,:].values.reshape(1,-1), n_neighbors=11)
		for i in range(0,len(distances.flatten())):
			if i == 0:
				st.write('Top Cigar Recommendations for: {}'.format(model_app.df_final_v_3.index[query_index]))
				st.write(' Profile notes: {}'.format(df_desc2['New'][query_index][:-1]))
				html_string1 = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>more info</a>".format(model_app.df_final_v_3.index[query_index].replace("'",""))
				st.markdown(html_string1, unsafe_allow_html=True)
			else:
				p2 = model_app.df_final_v_3.index[indices.flatten()[i]]
				st.write('{}: {} with a Distance Score of: {}'.format(i, model_app.df_final_v_3.index[indices.flatten()[i]],round(distances.flatten()[i],4)))
				st.write(' Profile notes: {}'.format(df_desc2['New'][p2][:-1]))
				html_string = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>more info</a>".format(model_app.df_final_v_3.index[indices.flatten()[i]].replace("'",""),round(distances.flatten()[i],4))
				st.markdown(html_string, unsafe_allow_html=True)
		st.success('Finished')

	# else:
	# 	st.error('Please enter a valid cigar')

if test2:
	if profile:
		st.success('Select "Search Cigars" again for new options if more than 10 matches are available.')
		targets = profile
		df_desc2['pro'] = pd.DataFrame(df_desc2.New.apply(lambda sentence: all(word in sentence for word in targets)))
		df = pd.DataFrame(df_desc2['New'][df_desc2['pro']==True])
		if len(df)>10:
			df=df.sample(n=10)
		for i in range(len(df)):
			st.write('{}: {}'.format(i+1,df.index[i]))
			st.write('---Profile notes: {}'.format(df["New"][i][:-1]))
			html_string = "<a target='_blank' href='http://google.com/search?q={}+cigar&rlz'>more info</a>".format(df.index[i].replace("'",""))
			st.markdown(html_string, unsafe_allow_html=True)
html_stringp = "<a target='_blank' href='https://chefnewman.github.io/'>About</a>"
st.markdown(
    """<a target='_blank;' style='display: block; text-align: center;' href="https://chefnewman.github.io/">About</a>
    """,
    unsafe_allow_html=True)
fb = st.checkbox("Comments", value=False)
if fb:
    st.components.v1.iframe("https://s3.us-east-2.amazonaws.com/cigars-rec.com/discuss.html", height=400, scrolling=True)
    st.components.v1.iframe("https://s3.us-east-2.amazonaws.com/cigars-rec.com/disqus.html",height=400, scrolling=True)
