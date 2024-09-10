import streamlit as st
from PIL import Image

st.title('File Uploading')

# Image
st.subheader('1. Uploading an Image')
file = st.file_uploader('Upload image', type=['png','jpeg','jpg'])
if file is not None:
    file_details = {'file_name':file.name,
                   'file_type':file.type,
                   'file_size':file.size}
    st.write(file_details)
    st.image(Image.open(file))

# Video
st.subheader('2. Uploading Video')
file = st.file_uploader('Upload video', type=['mov', 'mp4', 'mkv'])
if file is not None:
    file_details = {'file_name':file.name,
                   'file_type':file.type,
                   'file_size':file.size}
    st.write(file_details)
    st.video(file)

# Audio
st.subheader('3. Uploading Audio')
file = st.file_uploader('Upload Audio', type=['mav', 'mp3'])
if file is not None:
    file_details = {'file_name':file.name,
                   'file_type':file.type,
                   'file_size':file.size}
    st.write(file_details)
    st.audio(file)

# CSV
st.subheader('4. Uploading CSV File')
file = st.file_uploader('Upload CSV', type=['csv', 'xlsx'])
if file is not None:
    file_details = {'file_name':file.name,
                   'file_type':file.type,
                   'file_size':file.size}
    st.write(file_details)
    st.dataframe(file)

st.subheader('5. Image Converter')

def convert_image(img_path, new_format):
    with Image.open(img_path) as img:
        new_name = img_path.name.split('.')[0] + '.' + new_format
        new_path = 'D:/GFG Data Science & Machine Learning/Python/Streamlit/Working with Data/' + new_name

        img = img.convert('RGB')
        img.save(new_path)
        st.success('your saved path is ' + new_path)

img_path = st.file_uploader('Upload your image', ['png','jpg','jpeg'])
new_format = st.selectbox('Select your type to convert', ['png','jpg','jpeg'])

if st.button('Convert'):
    if img_path is not None:
        convert_image(img_path, new_format)
    else:
        st.error('Please upload your image')
