# Importing all required packages
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Configuring the page
st.set_page_config(page_title="Sudheer Bachina's", page_icon=":tada:", layout="wide")

# Function definition
def loadlottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Variables
lottie_coding = loadlottie_url("https://lottie.host/55927ba1-585e-4ea6-8b4d-78761b905d3c/Wk57FSjytO.json")
img_first = Image.open("D:/Own-Projects/Streamlit/images/first.jpeg")
img_second = Image.open("D:\Own-Projects\Streamlit\images\second.jpeg")

# Header Section
with st.container():
    st.subheader("Hello there :wave: I am Sudheer Bachina")
    st.title("I have developed this website using Streamlit in Python")
    st.write("Media Solutions & Automation - Senior Associate at Dentsu")
    st.write("[Learn More > ](https://www.linkedin.com/in/sudheer-bachina/)")

# About Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me :")
        st.write("##")
        st.write("Started opening the CPU lids in my 6th grade to look up what's sitting inside. Heavily interested in Computers & their communication. Always keen to know how the information moves from one system to other. My ultimate curiosity at that age was to know how a movement in my keyboard/mouse makes a movement in the avatar of the game I play. Started researching since then and haven't stopped it even after my Master's degree.")
    
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")

# Projects Section
with st.container():
    st.write("---")
    st.header("My Projects :")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_first)
    with text_column:
        st.subheader("My work as a Data Analyst at Bhuvan Softwares")
        st.write("Analyzing the current and past datasets alongside analyzing the performance of the company in various departments and timeframes. Visualizing the data using Power BI to the core team during the regular meetings for better performance of the company. Exploring investment opportunities and demonstrated the profit plans to identify the financial performance trends. Provided the financial models using Machine Learning algorithms to the Management team for proper analysis of the organization's performance. ")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_second)
    with text_column:
        st.subheader("My work as a Lead Python Developer at Datamavic")
        st.write("Worked by leading a Python based application development team. Project was to develop a software which tracks the attendance of the employees whoever logs into the system and also monitors the exact number of hours each employee works. All the data will be converted as a report on a daily basis and shall be submitted automatically to the Director by the end of day. I have divided the work as per the ability of my team members and distributed the work accordingly and have been a team member. I got the best intern award during my internship and was rewarded with a laptop.")

# Contact Me
with st.container():
    st.write("---")
    st.subheader("Get in touch with me :")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/sudheer.ajay66@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value = "false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name="message" placeholder = "Your Message here" required></textarea>
        <button type="submit">Send</button>
    </form> """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()