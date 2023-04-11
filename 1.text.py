# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

st.title('Unit 1. Text elements')

# p. 14
st.caption('🔖 p. 14')

# title, header, subheader, text, cation
st.title('This is the title')
st.header('This is the header')
st.subheader('This is the subheader')
st.text('This is the text')
st.caption('Caption in small font')

st.divider() # st.markdown("""---""")

# p. 15
st.caption('🔖 p. 15')

# Markdown
st.markdown("#This is a Markdown title")
st.markdown("##This is a Markdown header")
st.markdown("###This is a Markdown subheader")
st.markdown('this is the markdown')
st.markdown('this is **the markdown 진하게**')
st.markdown('this is _the markdown 기울임_')
st.markdown('this is *the markdown 기울임*')
st.markdown('this is **_the markdown 진하고 기울임_**')

st.divider()

# p. 16
st.caption('🔖 p. 16')
st.markdown('- item\n'
            '  - item\n' # 2칸
            '  - item\n' # 2칸
            '    - item\n' # 4칸
            '- item')

st.markdown("1. item 1\n"
            "   1. item 1.1\n" # 3칸
            "   2. item 1.2\n" # 3칸
            "      1. item 1.2.1\n" # 6칸
            "2. item 2")

st.divider()

# p. 17 Text elements 연습문제: 1.text.py
st.caption('🔖 p. 17')

con1, con2 = st.columns(2)
def main():
    with con1:
        # title, header, subheader, text, caption 연습하기
        st.title('Text elements')
        st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')
        st.header('Header: 데이터 분석 표현')
        st.subheader('subheader: 스트림릿')
        st.text('Text: this is the Streamlit')
        st.caption('Caption: Streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹어플리케이션 툴이다')
        
    with con2:
        # markdown 연습하기
        st.markdown('# Markdown')
        st.markdown('## Markdown')
        st.markdown('### Markdown')
        st.markdown('_Markdown_')
        st.markdown('- _Markdown_')
        
main() 

st.divider()

# p. 18
st.caption('🔖 p. 18')

# code, LaTeX-수학식 표현
st.code('x=1234')
st.latex(r'''a+ar+ar^2+ar^3+\cdots+ar^{n-1}=\sum_{k=0}^{n-1}ar^k=a\left(\frac{1-r^{n}}{1-r}\right)''')

st.divider()


# p. 19
st.caption('🔖 p. 19')

# st.write
# String, data_frame, chart, graph, LaTex 등의 objects를 App에 출력할 수 있다.
st.write('this is a string write')
st.write('Hello, *World!* 😄')

df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.divider()

# p. 20 Text elements 연습문제: 1.text.py
st.caption('🔖 p. 20')

con1, con2 = st.columns(2)
def main():
    with con1:
        # Code & Latex
        st.title('Code & Latex')
        st.latex('a+ar+ar^2+ar^3')
        
    with con2:
        # markdown 연습하기
        st.title('write')
        st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
        st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
        st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'], '수준': ['금', '동', '은', '은']}")
        
        df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'], '수준': ['금', '동', '은', '은']})
        st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서 \n', 
         df, 
         '\n', 
         '스트림릿의 write 함수로 표현')
        
main() 

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run 1.text.py
