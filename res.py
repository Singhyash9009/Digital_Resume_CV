from pathlib import Path
import streamlit as st
from PIL import Image

current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file= current_dir/"styles"/"main.css"
resume_file=current_dir/"assets"/"Yash Singh Resume.pdf"
profile_pic=current_dir/"assets"/"IMG_20230926_200253-fotor-202309270811.png"
GitHub=current_dir/"assets"/"GitHub.png"
LinkedIn=current_dir/"assets"/"LinkedIn.png"
Gmail=current_dir/"assets"/"Gmail.png"

#-----general setting----#
PAGE_TITLE ="Digital CV | Yash Singh"
PAGE_ICON  =":wave:"
NAME      ="Yash Singh"
DESCRIPTION="""
I am a skilled and certified Data Scientist proficient in statistical modeling, data mining, and data extraction. I am actively seeking a fulltime
career opportunity in a reputable organization where I can collaborate with experienced professionals and realize my full
potential.
"""

EMAIL  ="singhyash9009@gmail.com"
SOCIAL_MEDIA={
    'LinkedIn':"https://www.linkedin.com/in/yash-singh-02b7341a3/",
    'GitHub'  :"https://github.com/Singhyash9009/GIT-HUB",
    'Gmail'   :"sinyash9009@gmail.com"
}

PROJECTS ={
    "🏆 Capstone_Amazon_Project":"https://github.com/Singhyash9009/GIT-HUB/tree/main/Capstone%20Amazon%20Project",
    "🏆 Kaggle_Walmart_Project" :"https://github.com/Singhyash9009/GIT-HUB/tree/main/Kaggle%20dataset",
    "🏆Classification_model_mini_project":"https://github.com/Singhyash9009/GIT-HUB/blob/main/MINI%20PROJECT/MINI%20PROJECT%20%202%20(CLASSIFICATION%20MODEL)%20YASH%20SINGH.ipynb",
    "🏆 Clustering_model_mini_project"    :"https://github.com/Singhyash9009/GIT-HUB/blob/main/MINI%20PROJECT/MINI%20PROJECT%203%20(CLUSTERING%20MODEL)%20YASH%20SINGH.ipynb",
    "🏆 Summary_app_tool":"https://github.com/Singhyash9009/GIT-HUB/tree/main/Summary%20App%20Tool",
    "🏆 Digital Resume creation using Streamlit.":"https://github.com/Singhyash9009/GIT-HUB/tree/main/Resume%20Builder%20Using%20Streamlit"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

<<<<<<< HEAD
=======


# --- EXPERIENCE & QUALIFICATIONS ---
>>>>>>> da6fc01d41adb8bf5900c7aa6c8037a054a4dbf3
st.write("---")

st.write('\n')
st.subheader("Qualifications")
st.write("""

-      🎓 Advanced PGP in Data Science and Machine Learning 
-   NIIT  Sep-2022 to Mar-2023
-         🎓 Civil Engineering
-   Shri Ramdeobaba College of Engineering & Management 2016-2020 

-      🎓 Higher Secondary Certificate
-   Macro Vision Academy 2015-2016

"""
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience")
st.write(
    """  
- ✔️ Strong hands on experience and knowledge in Python,MySQL and Excel
- ✔️ Having good experience on visualization software such as Tableau and PowerBI
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Having 3 months internships experience at Bugendaitech
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), SQL
- 📊 Data Visulization: Tableau,PowerBi, MS Excel, Plotly
- 📚 Supervised Models: Logistic and Linear regression, Decision tree, Naive Bayes,Stacking Models
- 📚 Unsupervised Models: K-Means Clustering , DBSCAN , Hierarchical Clustering
- 🗄️ Databases: Postgres, MongoDB, MySQL
- 📊 UI : StreamLit, Django, Flasks
"""
)

st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Science Intern | Bugendaitech**")
st.write("05/2023 - 09/2023")
st.markdown(
    """
- ► Worked on Machine Learning Models created model for AirBnB Dataset
- ► Used Tableau and PowerBI  to redeﬁne and track KPIs on sales of superstore and  recommendations to boost their sales in future
- ► Done LDA on Speech of Narendra Modi
- ► Build a Web Summary Application Tool and made it interactive with help of StreamLit
"""
)


st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

<<<<<<< HEAD
st.write('\n')
st.write('---')
st.write('\n')

GitHub= Image.open(GitHub)
LinkedIn=Image.open(LinkedIn)
Gmail=Image.open(Gmail)
col1, col2, col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
with st.container():
    col1.image(LinkedIn, width=50)
    col3.image(GitHub, width=50)
    col5.image(Gmail,width=50)
# --- SOCIAL LINKS ---


cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write('---')
=======

GitHub= Image.open(GitHub)
LinkedIn=Image.open(LinkedIn)
col1, col2, col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
with st.container():
    col1.image(LinkedIn, width=50)
    col4.image(GitHub, width=50)
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
>>>>>>> da6fc01d41adb8bf5900c7aa6c8037a054a4dbf3
