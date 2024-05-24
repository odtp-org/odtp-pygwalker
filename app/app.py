from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import os
import io 

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="ODTP PyGWalker",
    layout="wide"
)

st.sidebar.title('ODTP PyGWalker')
st.sidebar.write('Please select a file from the sidebar to start exploring the data. These are the csv files located on `/odtp/odtp-input`.')

# Credit: https://discuss.streamlit.io/t/server-side-file-select/60704/2
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.sidebar.selectbox('Select a file', filenames)

    if len(filenames) == 0:
        st.sidebar.error('No files found in the selected folder. Please upload a file.')
        return None
    else:
        output_path = os.path.join(folder_path, selected_filename)
        st.sidebar.write('You selected `%s`' % output_path)
        return output_path


filename = file_selector("/odtp/odtp-input")

# Upload from local
# filename = st.sidebar.file_uploader("Upload a CSV file", type="csv")
# st.sidebar.write('You selected `%s`' % filename)

if st.sidebar.button('Load CSV'):
    df = pd.read_csv(filename)
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()