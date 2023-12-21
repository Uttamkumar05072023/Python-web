import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Hello coder",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

left_column,right_column=st.columns((2.5,1.5))
with left_column:
    st.title("Hello coder program in all popular languages 😀")
with right_column:
    st_lottie(lottie_coding,height=150,key="coding")

st.write("---")
st.write("##")


st.subheader("In C Programming language")
st.code(
    """
    #include<stdio.h>
    #include<conio.h>
    void main()
    {
        printf("Hello coder");
        getch();    
    }""")
st.write("##")


st.subheader("In C++ Programming language")
st.markdown("In C++ Programming we have to ways to write Hello coder program")
left_column,right_column=st.columns(2)
with left_column:
    st.markdown("- 1st way")
    st.code("""
            #include<iostream>
            int main()
            {
                std::cout<<"Hello coder";
                return 0;
            }
            """)
with right_column:
    st.markdown("- 2nd way")
    st.code("""
            #include<iostream>
            using namespace std;
            int main()
            {
                cout<<"Hello coder";
                return 0;
            }
            """)
st.write("##")
    

st.subheader("In Java Programming language")
st.code("""
        class HelloCoder{
            public static void main(String[] args){
                System.out.println("Hello coder");
            }
        }""")
st.write("##")


st.subheader("In Python Programming language")
st.code("""
        print("Hello coder")
        """)
st.write("---")

st.header("Feedback form")
feedback=st.text_area("Share your experience")
button=st.button("Submit")