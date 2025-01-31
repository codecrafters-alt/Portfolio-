import streamlit as st
import pandas as pd

# Sidebar content

st.title("Hey Connections! :wave:")
st.sidebar.image(r"C:\Users\jaydeb chakraborty\OneDrive\Desktop\Gen-Ai\image\Round.png")
about_page = st.Page(
    page="Views/About.py",
    title="About me",
    icon=":material/account_circle:",
    default=True
)

project_page = st.Page(
    page="Views/Project.py",
    title="Projects",
    icon=":material/smart_toy:"
)

pg=st.navigation(pages=[about_page, project_page])

social_icons_data = {
    "LinkedIn": ["https://www.linkedin.com/in/anik-chakraborty-5b4103275", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
    "GitHub": ["https://github.com/codecrafters-alt/CBTCIP", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    "Instagram":["https://www.instagram.com/anikc13/","https://cdn-icons-png.flaticon.com/128/15713/15713420.png"]
}

social_icons_html = [
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f" style='width: 40px; height: 40px;'></a>"
    for platform in social_icons_data
]

st.sidebar.write("\n")

st.sidebar.write("\n")

st.sidebar.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px; gap: 20px">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

pg.run()



