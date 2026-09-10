import streamlit as st

st. title('welcome to streamlit')

#inputs

m1 = st.text_input('Enter Your Input')
st.markdown(m1)

m2 = st.text_area('Enter Your Input')
st.markdown(m2)

st.warning('Please Enter Your Input')

st.success('updated successfully')

m3 = st.selectbox('Please Select' , ['python','java','SQL'])
st.markdown(m3)

st.multiselect ('Please Select' , ['python','java','SQL'])