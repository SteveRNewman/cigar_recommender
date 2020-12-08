###########version used on heroku############
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from sklearn.neighbors import kneighbors_graph
import warnings
warnings.filterwarnings("ignore")

df_final_v_3 = pd.read_pickle('df_final_v_3.pkl')


knn_search = NearestNeighbors(metric='wminkowski', p=2, metric_params={'w': [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 2., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1, 1, 1, 1, 1, 1., 1, 1, 1, 1, 2, 1,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,
        1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ]})

knn_search.fit(df_final_v_3)

# import autoFill as af
# from ipywidgets import HTML, HBox

# def auto(value):
#     show.value=value.new

options = list(df_final_v_3.index)
# autofill = af.autoFill(options,callback=open)

# show = HTML('Result will be displayed here!')

# display(HBox([autofill,show]))

def get_key(val):
    for key, value in dict(enumerate(options)).items():
         if val == value:
            return key
