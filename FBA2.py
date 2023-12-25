import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
import os  # for secure password handling
import plotly.graph_objects as go

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', None)

from glob import glob

import plotly.graph_objs as go


monthly_data = pd.read_excel('monthly_data.xlsx')


def main():
    st.set_page_config(layout="wide")
    password = st.text_input("Şifreyi girin", type="password")
    correct_password = os.environ.get('PASSWORD', "1514")  # getting password from environment variable
    if password != correct_password:
        return

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=monthly_data['Ay'],
                             y=monthly_data['Ortalama_Satış_Adedi'],
                             mode='lines+markers',
                             line=dict(color='orangered', width=2),
                             marker=dict(color='orangered', size=8),
                             name='Ortalama_Satış_Adedi'))

    # Grafiği düzenle
    fig.update_layout(title='Aylık Ortalama Satış Adedi',
                      xaxis_title='Tarih',
                      yaxis_title='Oran',
                      template='plotly_dark',
                      height=600,
                      font=dict(size=20, color='black'),
                      legend=dict(x=0.01, y=0.99))

    # Yüzdelik değerleri grafiğe ekleyelim
    for i, row in monthly_data.iterrows():
        fig.add_annotation(
            x=row['Ay'],
            y=row['Ortalama_Satış_Adedi'],
            text=f"{row['Ortalama_Satış_Adedi']:.2}",
            showarrow=True,
            arrowhead=1,
            arrowsize=3,
            arrowwidth=1,
            arrowcolor='red',
            ax=0,
            ay=-20
        )

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
