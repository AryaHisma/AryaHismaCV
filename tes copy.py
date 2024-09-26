import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Aplikasi Saya",
    page_icon="https://example.com/icon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

    
    
st.markdown(
    """
    <style>
    .st-emotion-cache-isgwfk.e1f1d6gn0 {
        background-color: #d88787;
        border: 2px solid #443b3b;
        padding: 5% 5% 5% 5%;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Create columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    
    with st.container(height=300, border=True):
        with open('assets/style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        # --- IMAGE ---
        image = Image.open("assets/pemandangan_alam.jpg")
        st.image(image, width=100)
        # st.markdown('<div class="yellow-bg"><img src="assets/pemandangan_alam.jpg" alt="Pemandangan Alam"></div>', unsafe_allow_html=True)
        # # st.markdown('<div class="yellow-bg"><img src="data:image/png;base64,{}" width="100"></div>'.format(image_to_base64(image)), unsafe_allow_html=True)
    
    with st.container(height=1000, border=True):
        st.header("Data 1")
        st.write("Data 3")
    
        st.header("Data 2")
        # st.write("Data 3")
        st.markdown('<p class="p-hapus">Test</p>', unsafe_allow_html=True)
    
        st.header("Data 3")
        st.write("Data 3")
    
        st.header("Data 3")
        st.write("Data 3")
    
with col2:
    # Apply custom CSS to align the header to the left
    st.markdown("""
    <style>
    .left-aligned-header {
        text-align: left;
        font-size: 2em;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="left-aligned-header">alamamamamma</h1>', unsafe_allow_html=True)

    st.header("Data 1")
    st.write("Data 1")

    st.header("Data 2")
    st.write("Data 2")
    
    st.write("Data 3")
    
    st.header("Data 3")
    st.write("Data 3")
    
    st.header("Data 3")
    st.write("Data 3")
