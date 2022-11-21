import dash
from dash import dcc,html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
app = dash.Dash(__name__)


df_linked_club=pd.read_csv('Linked_club_int.csv')
df_CEvent_freq = df_linked_club['Event'].value_counts()

fig1 = px.bar(df_CEvent_freq)

df_Club_freq = df_linked_club['Club_Name'].value_counts()

fig6 = px.bar(df_Club_freq)



df_fest_linked=pd.read_csv('F_fest_linked.csv')
df_fEvent_freq = df_fest_linked['Event'].value_counts()

fig2=px.bar(df_fEvent_freq)

df_fest_freq = df_fest_linked['Fest_Name'].value_counts()
df_fest_freq

fig3 = px.bar(df_fest_freq)

df_st_freq = df_fest_linked['Name'].value_counts()
df_st_freq = df_st_freq[:20]

fig4 = px.bar(df_st_freq)

df_C_St_freq = df_linked_club['Name'].value_counts()
df_C_St_freq = df_C_St_freq[:20]

fig5=px.bar(df_C_St_freq)









app.layout = html.Div(children=[
   # elements from the top of the page
   html.Div([
      html.H1(children='Fest Participation'),
      html.Div(children='''
      Fest 2 had a significant increase in partcipation preceeding fest 1. We can conclude from this that Fest 1 was a success and should proceed with the same strategy. '''),

      dcc.Graph(
         id='graph3',
         figure=fig3
      ),
   ]),
   html.Div([
      html.H1(children='Fest Event Participation'),
      html.Div(children='''
      We can notice the the first 5 events in each of the fest have the highest amount of participation. Rest of the events in each fest see a 30% decline.'''),

      dcc.Graph(
         id='graph2',
         figure=fig2
      ),
   ]),
   html.Div([
      html.H1(children='Most Active participants in fests'),
      html.Div(children='''
      20 most active participants in fests'''),

      dcc.Graph(
         id='graph4',
         figure=fig4
      ),
   ]),
   html.Div([
      html.H1(children='Clubs Participation'),
      html.Div(children='''
      . '''),

      dcc.Graph(
         id='graph6',
         figure=fig6
      ),
   ]),
   html.Div([
      html.H1(children='Club Event Participation'),
      html.Div(children='''
      We can notice a steep decline in the number of participants by the third event.Close to a 50% decline.'''),

      dcc.Graph(
         id='graph1',
         figure=fig1
      ),
   ]),
   # New Div for all elements in the new 'row' of the page
   
   
   
   html.Div([
      html.H1(children='Most Active participants in Clubs'),
      html.Div(children='''
       20 most active participants in clubs'''),

      dcc.Graph(
         id='graph5',
         figure=fig5
      ),
   ]),
])

if __name__ == '__main__':
   app.run_server(debug=True)