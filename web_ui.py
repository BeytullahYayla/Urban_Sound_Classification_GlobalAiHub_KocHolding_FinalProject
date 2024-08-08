import streamlit as st

# Title and Introduction
st.title('Amon\'s Portfolio')
st.write('Welcome to my portfolio! Here you can find information about me and my projects.')

# About Me Section
st.header('About Me')
st.write('Hi, I\'m Amon, a software developer with a background in computer vision and backend development. I have experience working with various technologies and frameworks. Currently, I\'m doing an internship in the Network Engineering department at Roketsan.')

# Projects Section
st.header('Projects')

# Project 1
st.subheader('Automatic License Plate Recognition')
st.write('This project involves using computer vision techniques to automatically recognize license plates from images. I utilized OpenCV and TensorFlow to develop the recognition model.')

# Project 2
st.subheader('Car Vehicle Quality System')
st.write('A platform aimed at providing quality control and tracking of vehicles for manufacturers and sellers. The system manages vehicles in compliance with quality standards throughout production, delivery, and sales stages.')
st.write('[GitHub Repository](https://github.com/BeytullahYayla/Vehicle-Quality-System-Backend)')

# Project 3
st.subheader('Customer Counting Project')
st.write('This project involves counting customers in retail shops using deep learning models. I used YOLOv8 for detection, DeepSORT for tracking, and MobileNetV2 for classification.')

# Other Links
st.header('Find Me Online')
st.write('[GitHub Profile](https://github.com/BeytullahYayla)')

# Contact Section
st.header('Contact')
st.write('Feel free to reach out to me on LinkedIn or via email for any inquiries or collaborations.')

