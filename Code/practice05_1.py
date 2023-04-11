# page5
def page5():
    
    import streamlit as st
    import pandas as pd
    
    empty1, con, empty2 = st.columns([1,6,1])

    st.sidebar.markdown("# Layouts & Containers")
    st.sidebar.markdown("5-1.layouts.py")
    
    def main():
        with empty1:
            st.empty()
            
        with con:
            st.title('Unit 5. Layouts & Containers')
            st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/layout')
            
            # sidebar- with 사용하기 📧  📱  ☎︎
            with st.sidebar:
                st.divider() 
                
                st.header('1. Sidebar')
                
                add_selectbox = st.sidebar.selectbox('어떻게 연락 드릴까요?',
                                                     ('Email', 'Mobile phone', 'Office phone'))
                
                if add_selectbox == 'Email':
                    st.sidebar.title('📧')
                elif add_selectbox == 'Mobile phone':
                    st.sidebar.title('📱')
                else:
                    st.sidebar.title('☎︎')
                    
            # columns  
            st.header('2. Columns')
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.text('A cat')
                st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb')
                
            with col2:
                st.text('A dog')
                st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb')
                
            with col3:
                st.text('An owl')
                st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb')

                
            # tabs  
            st.header('3. Tabs')
            tab1, tab2, tab3 = st.tabs(['고양이', '개', '부엉이'])           
            with tab1:
                st.caption('Cat')
                st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb', width=200)
            with tab2:
                st.caption('Dog')
                st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb', width=200)
            with tab3:
                st.caption('Owl')
                st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb', width=200)

        with empty2:
            st.empty()
                 
    main()
    
page5()