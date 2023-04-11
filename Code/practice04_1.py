# page4-1
def page4_1():
    
    import streamlit as st
    import pandas as pd
    
    empty1, con, empty2 = st.columns([1,6,1])
    empty1, con1, con2, empty2 = st.columns([1,3,3,1])
    empty3, con_1, empty4 = st.columns([1,6,1])
    empty3, con3, con4, empty4 = st.columns([1,3,3,1])
    empty5, con_2, empty6 = st.columns([1,6,1])
    empty5, con5, con6, empty6 = st.columns([1,3,3,1])
    
    st.sidebar.markdown("# Input Widgets-1")
    st.sidebar.markdown("4-1.input.py")
    
    def main1():
        with empty1:
            st.empty()
            
        with con:    
            st.title('Input Widgets 연습문제: 4-1.input.py')
            st.caption('🔖 p. 32')
            
        with con1:
            st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')
            st.header('1. Button')
            
            # button
            if st.button('Say hello'):
                st.write('Hello')
            else:
                st.write('Goodbye')
            
            # radio button
            st.header('2. Radio button')
            genre = st.radio('좋아하는 영화 장르를 선택하세요', 
                             ('코미디', 'SF', '액션'))
            
            if genre ==  '코미디':
                st.write('코미디 유쾌하신 분이시군요')
            elif genre == 'SF':
                st.write('저도 SF 좋아합니다')
            else:
                st.write('멋지십니다.')
                
            # checkbox
            st.header('3. Checkbox')
            agree = st.checkbox('I agree')
            
            if agree:
                st.write('😄'*10)

            
        with con2:
            
            # select box
            st.header('4. Select box')
            option = st.selectbox('어떻게 연락 드릴까요?',
                                  ('Email', 'Mobile phone', 'Office phone'))
            st.write('네', option, '잘 알겠습니다')
            
            # Multi select
            st.header('5. Multi select')
            options = st.multiselect('좋아하는 색을 모두 선택하세요', 
                                     ['Green', 'Yellow', 'Red', 'Blue'], 
                                     ['Yellow', 'Red'])
            st.write('선호 색상: ')
            for i in options:
                st.write(i)
            
        with empty2:
            st.empty()
            
            
    main1()
    
    def main2():
        from datetime import datetime 
        with empty3:
            st.empty()
            
        with con_1: 
            st.divider()
            st.caption('🔖 p. 34')
            
        with con3:
            st.header('6. Input: Text/Number')
            
            # text_input
            st.subheader('**_text_input_**')
            title = st.text_input('최애 영화를 입력하세요 ', 
                                  'Sound of Music') # 최초 입력 값
            st.write('당신이 가장 좋아하는 영화는 : ', title)

            # number_input
            st.subheader('**_number_input_**')
            number = st.number_input('Insert a number(1-10)', 
                                     min_value=1, max_value=10, value=5, step=1) # min~max value:입력 허용구간, value:최초 입력 값, step:증분 값
            st.write('The current number is ', number)

        with con4:
            st.header('7. Date input')
            ymd = st.date_input('When is your birthday',
                                datetime(2000, 9, 6)) # 최초 입력 값
            st.write('Your birthday is:', ymd)
            
        with empty4:
            st.empty()

    main2()
    
    def main3():
        from datetime import datetime 
        with empty5:
            st.empty()
            
        with con_2: 
            st.divider()
            st.caption('🔖 p. 36')
            
        with con5:
            st.header('8. Slider')
            
            # slider
            st.subheader('**_Slider- 이전 구간_**')
            age = st.slider('나이가 어떻게 되세요 ? ', 
                            0, 130, 25)
            st.write('I am', age, 'years old')

            st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
            values = st.slider('값 구간을 선택하세요',
                               0.0, 100.0, (25.0, 75.0))
            st.write('Values: ', values)

        with con6:
            st.subheader('**_년 월 일 사이 구간_**')
            slider_date = st.slider('날짜 구간을 선택하세요',
                                    min_value=datetime(2022, 1, 1),
                                    max_value=datetime(2022, 12, 31),
                                    value=(datetime(2022, 6, 1), datetime(2022, 7, 31)),
                                    format='YY/MM/DD')
            st.write('slider date: ', slider_date)
            st.write('slider_date[0]: ', slider_date[0], 'slider_date[1]: ', slider_date[1] )
            
        with empty6:
            st.empty()

    main3()
    
page4_1()