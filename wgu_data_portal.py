import streamlit as st
from PIL import Image
from industry import industry_page
from employment import employment_page
from education import education_page
from institutions import institutions_main, institutions_specific
from ipeds_dictionary import ipeds_dictionary_page

# Page configurations
st.set_page_config(layout="wide")


# Main section of the portal homepage
def home_page():
    st.title("Welcome!")
    st.write("Welcome to the WGU Labs data portal! Select a section on the left to get started.")

    col1, gap, col2, rgap = st.columns([0.7,0.04,0.8, 0.02])

    with col1:
        st.header("Section Overview")
        st.markdown("""
        - **Institutions (Main):** Data about schools, students, and degrees aggregated by region
        - **Institutions (Specific):** Filter schools to create custom lists, view school-specific data
        - **Education:** Educational attainment, educational requirements for different occupations
        - **Employment:** Employment projections, historical employment counts and wage data for different occupations
        - **Industry:** Industry prevalence, trends both nationally and at state level
        - **IPEDS Dictionary:** Quickly look up IPEDS variables and tables using their name, acronym, and other identifying features
        """)

    with col2:
        st.header("Quick Tips")
        st.markdown("""
        - Click the expand button in the corner of graphs to make them bigger
        - Save pictures of visualizations you create using by clicking the camera icon in its top right corner
        - Download buttons throughout the portal allow you to download both original data sets and ones you've generated
        - Dataframes are scrollable!
        """)
        st.header("Feedback or Questions?")
        st.markdown("Have a question about this portal or a suggestion for a feature you'd like to see added? Please let us know!")
        st.markdown("Email: jeremy.hodgson@wgu.edu")


# Sidebar
image = Image.open('WGUlogo2.png')
st.sidebar.image(image, use_column_width=True)

st.sidebar.header("Data Portal")

navigation = st.sidebar.radio(
    "Choose a section to get started",
    ("Home","Institutions (Main)", "Institutions (Specific)", "Education", "Employment", "Industry", "IPEDS Dictionary")
)

if navigation == "Home":
    home_page()
if navigation == "Institutions (Main)":
    institutions_main.display_institutions_page()
if navigation == "Institutions (Specific)":
    institutions_specific.view_page()
if navigation == "Education":
    education_page.view_page()
if navigation == "Employment":
    employment_page.view_employment_page()
if navigation == "Industry":
    industry_page.view_industry_page()
if navigation == "IPEDS Dictionary":
    ipeds_dictionary_page.view_page()


st.write("***")
st.sidebar.header("About")
st.sidebar.write("This portal aggregates data from public educational data sources and allows nontechnical users to explore and interface with it.")
st.sidebar.write("[View this project's source code](https://github.com/emily-erickson/WGU_Data_Portal.git)")
st.sidebar.write("Copyright WGU Labs 2022")



