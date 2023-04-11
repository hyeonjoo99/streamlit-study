# import module
import streamlit as st
import pandas as pd

# layout setting
st.set_page_config(layout="wide")
empty1, con, empty2 = st.columns([1,6,1])
empty1, con1, con2, empty2 = st.columns([1,3,3,1])

def main_page():
    st.markdown("# 실습 정리 🎈")
    st.sidebar.markdown("# KT AIVLE SCHOOL DX 3기")
    st.caption('kt에이블스쿨: https://aivle.kt.co.kr/')
    

def page1():
    st.sidebar.markdown("# Text elements 연습문제: 1.text.py")
    
    def main():
        with empty1:
            st.empty()
        with con:
            st.title('Text elements 연습문제: 1.text.py')
            st.caption('🔖 p. 20')
            
        with con1:
            st.title('Code & Latex')
            st.latex('a+ar+ar^2+ar^3')
            
        with con2:
            st.title('write')
            st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
            st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
            st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'], '수준': ['금', '동', '은', '은']}")
            
            df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'], '수준': ['금', '동', '은', '은']})
            st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서 \n', 
                     df, 
                     '\n', 
                     '스트림릿의 write 함수로 표현')
            
        with empty2:
            st.empty()
            
            
    main()

def page2():
    st.sidebar.markdown("Media elements 연습문제: 2.media.py")
    
    def main():
        with empty1:
            st.empty()
            
        with con:    
            st.title('Media elements 연습문제: 2.media.py')
            st.caption('🔖 p. 23')
            
        with con1:
            st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/media')
            
            st.header('1. Image')
            st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80', caption='산에서 본 해돋이')

            
        with con2:
            st.header('2. Audio')
            st.audio('./MusicSample.mp3')
            
            st.header('3. Video')
            st.video('./VideoSample.mp4')
            
        with empty2:
            st.empty()
            
            
    main()

page_names_to_funcs = {
    "Main Page": main_page,
    "01. Text elements": page1,
    "02. Media elements": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()