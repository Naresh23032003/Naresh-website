import streamlit as st

# Personal information
name = "Naresh R"
email_id = "rnaresh23r@gmail.com"
phone = "+91 8610790485"
education = ['''Indian institute of Technology Madras\n
Inter disciplinary dual degree, TechMBA, 2023 - 2025 (expected)''',

'''Indian institute of Technology Madras\n
Bachelor of Technology, Mechanical engineering, 2020 - 2024 (expected)\n
CGPA: 7.76''',

'''Maharishi Vidya Mandir, 2019 - 2020\n
Percentage obtained: 94.6
''']
experience = ['''Razorpay (June 2023 - August 2023)\n
Software Development Intern\n
Tech stack: MS Excel, Excel VBA (Visual basic for application), Google Suite, Google Apps Script, JavaScript\n
•	Achieved a 95%+ reduction in data errors for a 1000+ entry Excel file by leveraging innovative VBA scripting, surpassing competitor performance. This led to slashing weekly error rates from 20-25% to under 5%, significantly elevating data accuracy and computational efficiency\n
•	Saved 2-3 hours per on-call report for engineers by automating report generation, ensuring heightened precision. Expanded this automation across diverse teams using various reporting tools as a stretch goal\n
•	Reduced average resolution time by 30% and optimized on-call bandwidth by developing a Call-to-Action feature within the dashboard''',
'''Royal Enfield (May 2022 - July 2022)\n
Summer Intern\n
Tech stack: MS Office, AutoCAD\n
•	Achieved cost savings of 10 Lakhs per annum by proposing process streamlining and space optimization ideas through data analysis and insights gained from hands-on experience with various business systems and data extraction
''']
leadership = ['Core, Saathi\n\n • Led a 33-member team focused on mental health and student wellbeing, impacting over 11,000 students, by revamping team structure for improved delegation, accountability, and responsibility, while expanding academic programs to benefit 2nd and 3rd-year students. Organized diverse events aimed at promoting mental wellness','Executive, Fitness Club\n\n• Planned and organized sports events while managing the club\'s social media presence, resulting in a 40% growth in followers','SMC Mentor, Saathi\n\n• Mentored and supported 6 incoming freshmen during their initial days at IITM, providing guidance and assistance throughout their transition']
projects = ['''Document Summarization and Reporting\n	             
•	Designed and implemented a comprehensive data processing system utilizing the Langchain framework and GPT-3.5 for extracting structured information from unstructured data. Implemented a user-friendly Streamlit frontend to facilitate seamless user interaction. This end-to-end solution highlights my proficiency in data processing, frontend development, and API integration.''',
'''Surface defects detection using image processing\n	            
Detected surface defects via image processing techniques got an accuracy of 98 - 99%. Enhanced quality control, reducing flaws and integrating solutions for efficient, accurate defect identification in manufacturing''',
'''Sales Dashboard using Power BI\n
•	Presented complex sales data in an accessible and interactive format, enabling better- informed decision making''',
'''Gender detection using Images\n	         
•	Created CNN model which recognises an image and predicts a label that the image corresponds to a Male or a Female with an accuracy of 96.1%''',
'''Spam Detection\n	         
•	Classified messages as spam or not with accuracy up to 98.85% using ML Algorithms like SVC, CountVectorizer and MultinomialNB
''']
certifications = '''
    Gen AI Pinnacle Program - Analytics Vidhya (Ongoing)\n
    AWS Certified Cloud Practitioner\n
    PostgreSQL - Simplilearn\n
    Data Analysis with Python - IBM, Coursera\n
    Deep Learning with PyTorch: Zero to GANs - Jovian\n
    Machine Learning with Python - IBM, Verzeo\n
    Introduction to Git and GitHub - Google, Coursera
'''

skills = ['Programming & Skills: Amazon web services, Machine Learning, NLP, Deep Learning, Python, Langchain, C++, SQL, C',
'Software & Tools: MS Excel, PowerBI, GitHub',
'Interests: Data science, Data analysis, Software development, Finance, Product development']

# Streamlit app layout
st.title(f"Welcome to {name}'s Website!")
st.markdown("A tech enthusiast who has a deep-seated passion for building real-world solutions that use current technological advancements to solve problems in the realm of business")
# Information sections
st.header("What would you like to know about me?")
option = st.selectbox("", ["Choose an option","Education", "Experience", "Projects", "Leadership & Activities", "Skills & Interests"])
answer = ''
if option == "Projects":
    answer = projects
elif option == "Education":
    answer = education
elif option == "Experience":
    answer = experience
elif option == "Leadership & Activities":
    answer = leadership
elif option == "Skills & Interests":
    answer = skills
if option != "Choose an option":
     with st.chat_message("Assistant"):
            st.markdown("Let's know more about Naresh's " + option.lower())
     for ans in answer:
          with st.chat_message("Naresh"):
            st.markdown(ans)
# Create main content container
main_content = st.container()

# Create sidebar container
sidebar = st.sidebar.container()

# About Me section
with sidebar:
    about_me_section = st.expander("About Me", expanded=True)
    with about_me_section:
        st.markdown(f"Hey, I'm {name}!")
        st.markdown("I'm a passionate individual with a strong interest in technology and innovation.")

# Contact section
with sidebar:
    contact_section = st.expander("Contact")
    with contact_section:
        st.markdown("Get in touch! I'd love to hear from you.")

        # Contact form
        with st.form(key="contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message")
            submit_button = st.form_submit_button("Send Message")

            if submit_button:
                # Replace with your secure email API integration and error handling
                st.error("This functionality is currently not implemented.")
