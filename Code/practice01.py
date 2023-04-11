# page1
def page1():
    
    import streamlit as st
    import pandas as pd
    
    empty1, con, empty2 = st.columns([1,6,1])
    empty1, con1, con2, empty2 = st.columns([1,3,3,1])

    st.sidebar.markdown("# Text elements")
    st.sidebar.markdown("1.text.py")
    
    def main():
        with empty1:
            st.empty()
            
        with con:
            st.title('Text elements 연습문제: 1.text.py')
            st.caption('🔖 p. 20')
            
        with con1:
            st.header('Code & Latex')
            st.latex('a+ar+ar^2+ar^3')
            
        with con2:
            st.header('write')
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
    
page1()