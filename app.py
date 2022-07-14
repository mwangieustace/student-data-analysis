import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sn
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide')
from PIL import Image
import statsmodels.api as sm



def main():
    st.title("Factors affecting student performance in school")
    @st.cache
    def data_reader():
        df = pd.read_csv('student_data.csv')
        return df
    df = data_reader()

    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Data', 'EDA'], 
            icons=['house', 'file-spreadsheet', 'bar-chart-line'], menu_icon="cast", default_index=0)
    
    
    if selected == 'Home':
        st.subheader("There are a number of factors affecting stuent performance in school")
        st.write("Students' academic performance is affected by several factors which include students' learning skills, parental background, peer influence, teachers' quality, learning infrastructure among others.Below is a research, analysis and report of the findings")
        ## importing image
        student_img = Image.open("students.jpg")
        st.image(student_img, caption='students in Makori school studying')
    
    elif selected == 'Data':
        st.subheader('student Dataset for the research')
        st.write(df)

    elif selected == 'EDA':
        st.subheader('Research visualizations for insight generation')
        ## create a select box
        school_list = ["ALL", "MS","GP"]
        school_selector = st.selectbox('Select school', school_list)
        gender_col, address_col, inter_col, rom_col = st.columns(4)
        if school_selector == 'All':
            df1 = df
        elif school_selector == 'GP':
            df1 = df[df['school']=='GP']
        else:
             df1 = df[df['school']=='MS']
        with gender_col:
            def gender_donut():
                df2 = df1.groupby(['Gender'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='Gender', names=df2.index, title='Number of students', hole=0.5, template='ggplot2')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "Total Sales by Region", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            gender_donut()
        with address_col:
            def address_donut():
                df2 = df1.groupby(['address'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='address', names=df2.index, title='Number of students', hole=0.5, template='seaborn')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "addrees", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            address_donut()
        with inter_col:
            def inter_donut():
                df2 = df1.groupby(['internet'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='internet', names=df2.index, title='Number of students', hole=0.5, template='plotly')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "Intenet access", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            inter_donut()
        with rom_col:
            def rom_donut():
                df2 = df1.groupby(['romantic'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='romantic', names=df2.index, title='Number of students', hole=0.5, template='ggplot2')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "In romantic relationship", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            rom_donut()
        st.markdown("<h3 style='text-align: center;  margin: 3px'>Performance in Exam 1 and Examp 2</h1>", unsafe_allow_html=True)
        school_list_1 = ['All','GP', "MS"]
        school_selector_1 = st.selectbox('Select School', school_list_1, key='dist')
        if school_selector_1 == 'All':
            df3 = df
        elif school_selector_1 == 'GP':
            df3 = df[df['school']=='GP']
        else:
             df3 = df[df['school']=='MS']
        exam1_col, exam2_col = st.columns(2)
        with exam1_col:
            def exam1_box():
                fig = px.box(df3, x='Gender', y='Exam1_score', color='internet', template='ggplot2')
                fig.update_layout(title_text = "Exam 1 Performance", title_x = 0.5)
                
                st.plotly_chart(fig, use_container_width=True)
            exam1_box()
        with exam2_col:
            def exam2_box():
                fig = px.box(df3, x='Gender', y='Exam2_score', color='internet', template='ggplot2')
                fig.update_layout(title_text = "Exam 2 Performance", title_x = 0.5)
                st.plotly_chart(fig, use_container_width=True)
            exam2_box()


        st.markdown("<h3 style='text-align: center;  margin: 3px'>histogram on exam1 and exam2</h1>", unsafe_allow_html=True)
        school_list_3 = ['All','GP', "MS"]
        school_selector_3 = st.selectbox('Select School', school_list_3, key='hist')
        if school_selector_3 == 'All':
            df4 = df
        elif school_selector_3 == 'GP':
            df4 = df[df['school']=='GP']
        else:
            df4 = df[df['school']=='MS']
        exam1_col, exam2_col = st.columns(2)
        with exam1_col:
            def exam1_hist():
                fig= px.scatter(df4, x='Exam1_score', y='Exam2_score', color='internet', title='Scatterplot of exam1 and exam2')
                fig.update_layout(title_text = "Exam1 and Exam2 Performance", title_x = 0.5)
                st.plotly_chart(fig, use_container_width=True)
            exam1_hist()

        
        st.markdown("<h3 style='text-align: center;  margin: 3px'>regression plot on exam1 and exam2</h1>", unsafe_allow_html=True)
        school_list_4 = ['All','GP', "MS"]
        school_selector_4 = st.selectbox('Select School', school_list_4, key='reg')
        if school_selector_4 == 'All':
            df5 = df
        elif school_selector_4 == 'GP':
            df5 = df[df['school']=='GP']
        else:
            df5 = df[df['school']=='MS']
        exam1_col, exam2_col = st.columns(2)
        with exam1_col:
            def exam1_box():
             fig = px.scatter(df5, x='Exam1_score', y='Exam2_score', color='internet', title='Regession plot of G1 and G2',
              trendline='ols')
             fig.update_layout(title_text = "regression plot for exam1 and exam2 ", title_x = 0.5)
             st.plotly_chart(fig, use_container_width=True)
            exam1_box()

        st.markdown("<h3 style='text-align: center;  margin: 3px'>a scatter plot matrix on the data</h1>", unsafe_allow_html=True)
        school_list_5 = ['All','GP', "MS"]
        school_selector_5 = st.selectbox('Select School', school_list_5, key='sctmat')
        if school_selector_5 == 'All':
            df5 = df
        elif school_selector_5 == 'GP':
            df5 = df[df['school']=='GP']
        else:
            df5 = df[df['school']=='MS']
        exam1_col, exam2_col = st.columns(2)
        with exam1_col:
             fig = px.scatter_matrix(df5,
                dimensions=["age", "studytime", "absences", "Exam1_score", "Exam2_score"], color="Gender")
        st.plotly_chart(fig, use_container_width=True)

        
        st.markdown("<h3 style='text-align: center;  margin: 3px'>a heatmap on the data</h1>", unsafe_allow_html=True)
        school_list_6 = ['All','GP', "MS"]
        school_selector_6 = st.selectbox('Select School', school_list_6, key='htmap')
        if school_selector_6 == 'All':
            df6 = df
        elif school_selector_6 == 'GP':
            df6 = df[df['school']=='GP']
        else:
            df6 = df[df['school']=='MS']
        exam1_col, exam2_col = st.columns(2)
        with exam1_col:
            matrix = df6.corr()
            fig = fig = px.imshow(matrix)
        st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()