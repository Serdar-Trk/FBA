import pandas as pd
import plotly.express as px
import streamlit as st
import os  # for secure password handling

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', None)
sales_by_date2022 = pd.read_excel('sales_by_date2022.xlsx')
sales_by_date2023 = pd.read_excel('sales_by_date2023.xlsx')

def main():
    st.set_page_config(layout="wide")



    fig = px.bar(sales_by_date2022, x='Fatura_Tarihi', y='Counts', color='Satış_Adedi',
                 labels={'Fatura_Tarihi': 'Tarih', 'Counts': 'Sayı'},
                 title='Tarihe Göre Benzersiz Satış Adedi Dağılımı(2022)')

    # Grafiği gösterin
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(sales_by_date2023, x='Fatura_Tarihi', y='Counts', color='Satış_Adedi',
                 labels={'Fatura_Tarihi': 'Tarih', 'Counts': 'Sayı'},
                 title='Tarihe Göre Benzersiz Satış Adedi Dağılımı(2023)')

    # Grafiği gösterin
    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
