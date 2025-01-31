import streamlit as st

@st.dialog("Contact Me")
def show_contact_form():
    # Input fields
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    email = st.text_input("E-mail")
    message = st.text_area("Your message")
    
    # Submit button
    if st.button("Submit"):
        # Validation
        if not first_name:
            st.error("Please provide your first name. 🧑")
            return
        if not last_name:
            st.error("Please provide your last name. 🧑")
            return
        if not email:
            st.error("Please provide your email address. 📧")
            return
        if "@" not in email or "." not in email:
            st.error("Please provide a valid email address. 📧")
            return
        if not message:
            st.error("Please provide a message. 💬")
            return
        
        # Success message if all validations pass
        st.success("Message successfully sent! ✅")


col1,col2= st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image(r"C:\Users\jaydeb chakraborty\OneDrive\Desktop\Gen-Ai\image\Anik.png")
with col2:
    st.title("Anik Chakraborty")
    st.write("""
    I am Anik Chakraborty, a passionate Computer Science and Engineering (CSE) student at Netaji Subhash Engineering College (NSEC), Kolkata.  
    Aspiring to become a skilled software developer, I actively engage in coding and open-source contributions.  

    As a Hacktoberfest contributor and a participant in Smart India Hackathon (SIH), I strive to tackle real-world problems through innovative solutions.  
    Currently, I am diving into the fascinating world of Generative AI, expanding my knowledge and sharpening my skills in cutting-edge technologies.
    """)
    if(st.button("Contact me")):
        show_contact_form()

# Experience and Qualification
st.write("\n")
st.header("Experience & Qualification")
st.write("""
I am an enthusiastic Computer Science and Technology student at Netaji Subhash Engineering College, passionate about web development and innovative technologies.  

### Academic Qualifications:
- Class 10: Scored 87%
- Class 12: Scored 90%
- Current CGPA: 8.75  

### Experience:
- **Internship:** Completed a 4-week internship at Cipher Byte Technology, gaining valuable hands-on experience in web development.

### Key Projects:
- **Portfolio Website:** Designed and developed a responsive portfolio website showcasing my technical skills and creativity.
- **Todolist Application:** Built a dynamic task management application using HTML, CSS, and JavaScript.

### Achievements:
- Contributed to Hacktoberfest, enhancing my experience in open-source collaboration.
- Participated in the Smart India Hackathon, applying my skills to solve real-world problems.

### Career Goals:
I aim to continuously learn and grow in the field of web development, explore the potential of Generative AI, and contribute to impactful projects that drive innovation.
""")

# Skills
st.write("\n")
st.subheader("Skills")
st.write("""
- **Programming Languages**: C++, Python  
- **Web Development**: HTML, CSS, JavaScript  
- **Databases**: MySQL  
- **Technologies**: Microsoft Power BI  
- **Frameworks/Technologies**: MERN Stack (ongoing)  
- **Soft Skills**: Communication, Collaboration  
""")

st.write("\n")

# certificates
st.subheader("Certificate")
# Display certificate as an image
st.image(
    r"C:\Users\jaydeb chakraborty\OneDrive\Desktop\Gen-Ai\image\web dev certificate 2.png", 
    caption="Certificate of Completion - Web Development Internship",
)
st.write("\n")

st.caption( "#IBM Developer Skills Network")
st.image(
    r"C:\Users\jaydeb chakraborty\OneDrive\Desktop\Gen-Ai\image\IBM.png",
    caption="""
    Certificate of completion - Prompt Engineering
  
    """,
)
st.write("\n")



st.image(
    r"C:\Users\jaydeb chakraborty\OneDrive\Desktop\Gen-Ai\image\learntube.png",
    caption="Certificate of completion - Data Analytics Assessment"
)
