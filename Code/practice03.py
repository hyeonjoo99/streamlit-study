# page3
def page3():
    
    import streamlit as st
    import pandas as pd
    
    empty1, con, empty2 = st.columns([1,6,1])
    empty1, con1, con2, empty2 = st.columns([1,3,3,1])
    empty3, con0, empty4 = st.columns([1,6,1])
    empty3, con3, con4, empty4 = st.columns([1,3,3,1])
    
    st.sidebar.markdown("# Data display elements")
    st.sidebar.markdown("3.data.py")
    
    def main1():
        with empty1:
            st.empty()
            
        with con:
            st.title('Data display elements 연습문제: 3.data.py')
            st.caption('🔖 p. 26')
            
        with con1: 
            st.header('1. Metric')
        
            st.metric(label="Temperature", value='30.5℃', delta='2.5℃')
            st.metric(label="Temperature", value='28℃', delta='-2.5℃')
        
            st.header('2. columns')
            col1, col2, col3 = st.columns(3) 
            col1.metric("기온", "30.5 °C", "2.5 °C")
            col2.metric("풍속", "9 mph", "-8%")
            col3.metric("습도", "86%", "4%")

        with con2:
            file_path = 'https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv'
            st.header('3. Dataframe 조회하기')
            titanic = pd.read_csv(file_path)
            st.markdown('- st.table(상위 15행)')
            st.caption('table- 형태 고정')
            st.table(titanic.head(15))
            
        with empty2:
            st.empty()
    
    main1()  
    
    
    def main2():
        with empty3:
            st.empty()
            
        with con0: 
            st.divider()
            st.caption('🔖 p. 27')
            
        with con3:
            st.markdown('- st.dataframe(상위 15행)')
            st.caption('dataframe, write- 10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블 확대')
            file_path = 'https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv'
            titanic = pd.read_csv(file_path)
            st.dataframe(titanic.head(15))
            st.markdown('- st.write(상위 15행)')
            st.write(titanic.head(15))

        with con4:
            st.header('4. Dataframe 수정하기')
            edited_titanic = st.experimental_data_editor(titanic)
                
            if st.button('Press button to Save titanic_st.csv'):
                edited_titanic.to_csv('titanic_st.csv')
                st.write('💾 Saved')
            
        with empty4:
            st.empty()

    main2()
    
page3()

