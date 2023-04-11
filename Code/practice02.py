# page2
def page2():
    
    import streamlit as st
    import pandas as pd
    
    empty1, con, empty2 = st.columns([1,6,1])
    empty1, con1, con2, empty2 = st.columns([1,3,3,1])
    
    st.sidebar.markdown("# Media elements")
    st.sidebar.markdown("2.media.py")
    
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
            st.audio('./data/MusicSample.mp3')
            
            st.header('3. Video')
            st.video('./data/VideoSample.mp4')
            
        with empty2:
            st.empty()
            
            
    main()
    
page2()