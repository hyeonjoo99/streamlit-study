# import module
import os
import streamlit as st

# layout settingr
st.set_page_config(layout="wide")

from streamlit_option_menu import option_menu


# main page
def main_page():
    st.markdown("# KT AIVLE SCHOOL DX 3기")
    st.markdown("## streamlit 실습 정리 ")
    st.sidebar.markdown("## 실습 정리")
    st.caption('kt에이블스쿨: https://aivle.kt.co.kr/')
    
    st.markdown("- Text elements \n"
                "- Media elements \n"
                "- Media elements \n"
                "- Input Widgets \n"
                "  - Input Widgets-1 \n"
                "  - Input Widgets-2 \n"
                "- Layouts & Containers \n"
                "  - Layouts & Containers-1")
    st.caption("Layouts & Containers 2,3은 페이지 생성 연습이므로 생략")
    

    
# page1
import Code.practice01 as p1
import Code.practice02 as p2
import Code.practice03 as p3
import Code.practice04_1 as p4_1
import Code.practice04_2 as p4_2
import Code.practice05_1 as p5
    
# side-bar function
page_names_to_funcs = {
    "Main": main_page,
    "1. Text elements": p1.page1,
    "2. Media elements": p2.page2,
    "3. Data display elements": p3.page3,
    "4_1. Input Widgets-1": p4_1.page4_1,
    "4_2. Input Widgets-2": p4_2.page4_2,
    "5. Layouts & Containers": p5.page5,
}


# side-bar selectbox
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()