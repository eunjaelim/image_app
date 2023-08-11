import streamlit as st
from rembg import remove
from PIL import Image
from streamlit_image_comparison import image_comparison
import easyocr as ocr
import numpy as np

# ... (이미 존재하는 코드)

if option == '글자추출':
    image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])
    @st.cache
    def load_model(): 
        reader = ocr.Reader(['ko', 'en'], model_storage_directory='.')
        return reader 
    
    reader = load_model() # load model
    
    if image is not None:
        input_image = Image.open(image) # read image
        st.image(input_image) # display image
    
        with st.spinner("🤖 AI is at Work! "):
            result = reader.readtext(np.array(input_image))
            result_text = [] # empty list for results
            object_names = [] # empty list for object names
            
            for text in result:
                result_text.append(text[1])
                
                # Check if the text represents a plausible object name
                if len(text[1]) > 2:  # Filter out short text
                    object_names.append(text[1])
    
            st.write(result_text)
            
            if object_names:
                st.subheader("추측된 사물 이름:")
                st.write(object_names)
                
        st.balloons()
    else:
        st.write("Upload an Image")

# ... (이미 존재하는 코드)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
