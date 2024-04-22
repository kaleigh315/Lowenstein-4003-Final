# %%
# import dependencies
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# %%
from dash import Dash, html
#import base64
from PIL import Image

# %%
#import data
data= pd.read_csv('UPDATED_data.csv')

# %%
# build a bar chart
fig_new = px.bar(data, 
        x = 'Beverage', 
        y = 'Calories',
        color = 'Beverage')
fig_new.update_layout(
    title_text='Starbucks Drinks',
    xaxis_title="Beverages",
    yaxis_title='Calories',
)

# display the chart
fig_new.show()

# %%
#Image Set Up
image_path = 'image.png'

html.Img(src=image_path)

pil_img = Image.open("image.png")

#def b64_image(image_filename):
    #with open(image_filename, 'rb') as f:
        #image = f.read()
    #return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

# %%
#Dictionary for sizes
all_size_options = {
    'Select a Beverage Type': ['Short', 'Tall', 'Grande', 'Venti'],
    'Brewed Coffee': ['Short', 'Tall', 'Grande', 'Venti'],
    'Caffè Latte': ['Short', 'Tall', 'Grande', 'Venti'],
    'Caffè Mocha': ['Short', 'Tall', 'Grande', 'Venti'],
    'Flavored Latte': ['Short', 'Tall', 'Grande', 'Venti'],
    'Caffè Americano': ['Short', 'Tall', 'Grande', 'Venti'],
    'Cappuccino': ['Short', 'Tall', 'Grande', 'Venti'],
    'Espresso': ['Solo', 'Doppio'],
    'Skinny Latte (Any Flavour)': ['Short', 'Tall', 'Grande', 'Venti'],
    'Caramel Macchiato': ['Short', 'Tall', 'Grande', 'Venti'],
    'White Chocolate Mocha': ['Short', 'Tall', 'Grande', 'Venti'],
    'Hot Chocolate': ['Short', 'Tall', 'Grande', 'Venti'],
    'Caramel Apple Spice': ['Short', 'Tall', 'Grande', 'Venti'],
    'Tazo® Chai Tea Latte': ['Short', 'Tall', 'Grande', 'Venti'],
    'Tazo® Green Tea Latte': ['Short', 'Tall', 'Grande', 'Venti'],
    'Tazo® Full-Leaf Red Tea Latte (Vanilla Rooibos)': ['Short', 'Tall', 'Grande', 'Venti'],
    'Iced Brewed Coffee (With Classic Syrup)': ['Tall', 'Grande', 'Venti'],
    'Shaken Iced Tazo® Tea (With Classic Syrup)': ['Tall'],
    'Banana Chocolate Smoothie': ['Grande'],
    'Orange Mango Banana Smoothie': ['Grande'],
    'Strawberry Banana Smoothie': ['Grande'],
    'Coffee': ['Tall', 'Grande', 'Venti'],
    'Mocha': ['Tall', 'Grande', 'Venti'],
    'Caramel': ['Tall', 'Grande', 'Venti'],
    'Java Chip': ['Tall', 'Grande', 'Venti'],
    'Strawberries & Crème': ['Tall', 'Grande', 'Venti'],
    'Vanilla Bean': ['Tall', 'Grande']
}

# %%
#Dictionary for milk types
all_milk_options = {
    'Short': ['Nonfat', '2%', 'Soymilk','No milk option'],
    'Tall': ['Nonfat', '2%', 'Soymilk','No milk option'],
    'Grande': ['Nonfat', '2%', 'Soymilk','No milk option'],
    'Venti': ['Nonfat', '2%', 'Soymilk','No milk option'],
    'Solo': ['N/A'],
    'Doppio': ['N/A']
}

# %%
#My app

stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=stylesheets)
server = app.server


app.layout = html.Div([
    html.A(html.Button('Click Here for GitHub Repository'), href='https://github.com/LowensteinCa1/Lowenstein-4003-Final.git', target='_blank'),
    html.H1('Starbucks Data', style={'fontFamily': 'Baskerville'}),
    html.Div([
        html.P('Follow the steps below to compare different Starbucks drinks nutritional information!', style={'fontFamily': 'Didot'}),
        html.P('NOTE: for the drinks that do not require milk, you MUST select No Milk Option in order to see the correct graph.', style={'fontFamily': 'Didot'}),
        html.P('1. Choose a beverage from the ''Select a Drink'' dropdown', style={'fontFamily':'Didot'}),
        html.P('2. Choose a size', style={'fontFamily':'Didot'}),
        html.P('3. Choose a type of milk (if the drink you want requires milk).', style={'fontFamily':'Didot'}),
        html.P('Then you will be able to view their nutritional information. Enjoy!!', style={'fontFamily':'Didot'}),
    ]),
    html.Div([
        html.Div([
            html.Img(src=pil_img, className='logo', style={'width': '200px', 'height': '200px'}),
        ], style={'position': 'absolute', 'top': '30px', 'right': '30px', 'zIndex': '2'}),
    ]),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='drinks-dropdown',
                options=[{'label': option, 'value': option} for option in data['Beverage'].unique()],
                value='Select a Beverage Type',
                placeholder="Select a drink"
            ),
            html.Div([
                dcc.RadioItems(id='size-radio', value=None, style={'color': 'green', 'fontFamily': 'Didot'}),
            ], style={'display': 'inline-block'}),
            html.Div([
                dcc.RadioItems(id='milk-radio', value='Nonfat', style={'color': 'green', 'fontFamily': 'Didot'}),
            ], style={'display': 'inline-block'}),
            dcc.Graph(id='fig_new'),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(
                id='drinks-dropdown-2',
                options=[{'label': option, 'value': option} for option in data['Beverage'].unique()],
                value='Select a Beverage Type',
                placeholder="Select a drink"
            ),
            html.Div([
                dcc.RadioItems(id='size-radio-2', value=None, style={'color': 'green', 'fontFamily': 'Didot'}),
            ], style={'display': 'inline-block'}),
            html.Div([
                dcc.RadioItems(id='milk-radio-2', value='Nonfat', style={'color': 'green', 'fontFamily': 'Didot'}),
            ], style={'display': 'inline-block'}),
            dcc.Graph(id='fig_new-2'),
        ], style={'width': '50%', 'display': 'inline-block'}),
    ]),
])

# Callbacks for the first graph
@app.callback(
    [Output('size-radio', 'options'),
     Output('size-radio', 'value')],
    Input('drinks-dropdown', 'value')
)
def set_size_options_and_value(selected_drink):
    size_options = [{'label': size, 'value': size} for size in all_size_options[selected_drink]]
    return size_options, size_options[0]['value']

@app.callback(
    Output('milk-radio', 'options'),
    Input('size-radio', 'value')
)
def set_milk_options(selected_size):
    milk_options = [{'label': milk, 'value': milk} for milk in all_milk_options[selected_size]]
    return milk_options

@app.callback(
    Output('fig_new', 'figure'),
    [Input('drinks-dropdown', 'value'),
     Input('size-radio', 'value'),
     Input('milk-radio', 'value')] 
)
def update_graph(selected_drink, selected_size, selected_milk):
    filtered_data = data[(data['Beverage'] == selected_drink) & 
                         (data['Size'] == selected_size) & 
                         (data['Milk_type'] == selected_milk)]

    if filtered_data.empty:
        return {'data': [], 'layout': {}}

    columns = filtered_data.columns[3:8]
    values = filtered_data.iloc[0, 3:8].tolist()
    colors = ['#544129', '#7b6853', '#A2907b', '#Bdad9a', '#E8dccd']

    bars = []
    for col, val, color in zip(columns, values, colors):
        bars.append(go.Barpolar(
            r=[val],
            theta=[col],
            name=col,
            marker=dict(color=color),
        ))

    layout = go.Layout(
        title=f'{selected_drink} Drink Nutritional Information',
        polar=dict(
            radialaxis=dict(
                visible=True
            )
        ),
        #edit legend
        legend=dict(x=1.3, y=.9)
    )

    return {'data': bars, 'layout': layout}

#so i can adjust the image position

# Callbacks for the second graph
@app.callback(
    [Output('size-radio-2', 'options'),
     Output('size-radio-2', 'value')],
    Input('drinks-dropdown-2', 'value')
)
def set_size_options_and_value_2(selected_drink):
    size_options = [{'label': size, 'value': size} for size in all_size_options[selected_drink]]
    return size_options, size_options[0]['value']

@app.callback(
    Output('milk-radio-2', 'options'),
    Input('size-radio-2', 'value')
)
def set_milk_options_2(selected_size):
    milk_options = [{'label': milk, 'value': milk} for milk in all_milk_options[selected_size]]
    return milk_options

@app.callback(
    Output('fig_new-2', 'figure'),
    [Input('drinks-dropdown-2', 'value'),
     Input('size-radio-2', 'value'),
     Input('milk-radio-2', 'value')] 
)
def update_graph_2(selected_drink, selected_size, selected_milk):
    filtered_data = data[(data['Beverage'] == selected_drink) & 
                         (data['Size'] == selected_size) & 
                         (data['Milk_type'] == selected_milk)]

    if filtered_data.empty:
        return {'data': [], 'layout': {}}

    columns = filtered_data.columns[3:8]
    values = filtered_data.iloc[0, 3:8].tolist()
    colors = ['#544129', '#7b6853', '#A2907b', '#Bdad9a', '#E8dccd']

    bars = []
    for col, val, color in zip(columns, values, colors):
        bars.append(go.Barpolar(
            r=[val],
            theta=[col],
            name=col,
            marker=dict(color=color),
            showlegend=False
        ))

    layout = go.Layout(
        title=f'{selected_drink} Drink Nutritional Information',
        polar=dict(
            radialaxis=dict(
                visible=True
            )
        ),
        showlegend=False
    )

    return {'data': bars, 'layout': layout}

if __name__ == "__main__":
    app.run_server(jupyter_mode = 'tab', debug=True)




