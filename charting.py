import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

import numpy as np
import pandas as pd

from typing import Union
from typing import Optional
from PIL import Image

#---
# chart config
#---
class ColorDiscrete:
  tableau = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC']
  colorbrewer = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33', '#A65628', '#F781BF', '#999999']
  google = ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800', '#FF5722'] 
  d3 = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF']
  ilo = ['#0094D2', '#E6007E', '#F47D30', '#212121', '#F0F0F0'] 
  okabe_ito = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000', '#F0E442', '#D55E00']
  economist = ['#E3120B', '#4C4C4C', '#6D6E71', '#8E8D8F', '#AAAAB2', '#B6B4B5', '#C1BDBA', '#C9C5B6', '#D2CDC2', '#D9D5CD']
  mckinsey = ['#4A90E2', '#F5A623', '#7ED321', '#D0021B', '#417505', '#BD10E0', '#50E3C2', '#F8E71C', '#F78B00', '#000000']
  deloitte = ['#00A5DC', '#49276D', '#8A0000', '#007681', '#9A7227', '#84BE41', '#7C7474', '#D12F2F', '#F8931D', '#000000']
  nhk_jp = ['#E60012', '#579D1C', '#4B1E66', '#1B255E', '#1E4896', '#00A0E9', '#009944', '#6CBB5A', '#D1C000', '#E39800']
  abc_aus = ['#E14100', '#008C45', '#00AEEF', '#7600A1', '#80C342', '#005BB5', '#93C6E0', '#F15A29', '#DF7C00', '#00B5E2']

  gecko7 = ['#004457', '#567583', '#9baab1', '#e2e2e2', '#b8e8e3', '#83ede3', '#05f1e3']
  gecko5 = ['#004457', '#798f9a', '#e2e2e2', '#a0ebe3', '#05f1e3']
  gecko3 = ['#004457', '#798f9a', '#05f1e3']

  gecko_v1 = ['#00989d', '#2438a3', '#004457', '#567583', '#ffa500', '#664200', '#757bd8e']
    
GECKO_LOGO = Image.open("./resources/BlackShortText_Logo_Horizontal-long.png")

def watermark_settings():
    return [dict(
        source= GECKO_LOGO,
        xref="paper", yref="paper",
        x=0.98, y=0.02,
        sizex=0.20, sizey=0.20, opacity= 0.25,
        xanchor="right", yanchor="bottom"
    )]

def legend_settings_dark(orientation='v', max_per_row=7):
    settings = dict(
        x=0,
        y=1,
        title_text='',
        font=dict(
            family="Times New Roman",
            size=12,
            color="white"
        ),
        bgcolor='rgba(0,75,154,0.3)',
        bordercolor="ivory",
        borderwidth=1,
        orientation=orientation,
    )
    # if orientation == 'h':
    #     settings['traceorder'] = 'grouped'
    #     settings['tracegroupgap'] = max_per_row
    return settings


#---
# Theme config
#---
def initialize_plotly_themes():
    pio.templates["gecko_v1"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.gecko_v1,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )

    pio.templates["gecko7"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.gecko7,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )

    pio.templates["gecko5"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.gecko5,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )
    pio.templates["gecko3"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.gecko3,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )
    pio.templates["tableau"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.tableau,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )
    pio.templates["ilo"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.ilo,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )
    pio.templates["d3"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.d3,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )
    pio.templates["google"] = go.layout.Template(
        layout={
            'colorway': ColorDiscrete.google,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {'gridcolor': 'grey'},
            'yaxis': {'gridcolor': 'grey'},
        }
    )

#---
# Charting
#---
def make_bar_chart(
    df: pd.DataFrame, 
    scope_col: Optional[str] = 'scope', 
    year_col: Optional[str] = 'date', 
    category_col: Optional[str] = 'category', 
    value_col: str = 'financed_emissions', 
    aggregation: str = 'sum', 
    percent: bool = False, 
    theme: Optional[str] = None, 
    title: Optional[str] = 'Bar plot', 
    height: Optional[int] = None, 
    width: Optional[int] = None, 
    watermark=True,
    legend: bool = True,
    legend_dark: bool= False
):
    # Initialize figure
    fig = go.Figure()
    
    # Group and aggregate data
    group_cols = []
    if year_col:
        group_cols.append(year_col)
    if category_col:
        group_cols.append(category_col)
        
    if group_cols:
        grouped_df = df.groupby(group_cols).agg({value_col: aggregation}).reset_index()
    else:
        grouped_df = df.copy()
    
    # Handle datetime and convert to year if needed
    if year_col and pd.api.types.is_datetime64_any_dtype(df[year_col]):
        grouped_df[year_col] = grouped_df[year_col].dt.year
    
    # Handle percentage calculations
    if percent:
        total_value = grouped_df[value_col].sum()
        grouped_df[value_col] = 100 * grouped_df[value_col] / total_value
    
    # Create the plot
    for cat in grouped_df[category_col].unique() if category_col else [None]:
        cat_data = grouped_df[grouped_df[category_col] == cat] if category_col else grouped_df
        
        fig.add_trace(go.Bar(
            y=cat_data[year_col] if year_col else [cat],
            x=cat_data[value_col],
            name=str(cat) if cat else 'Total',
            text=cat_data[value_col].apply(lambda x: f"<b>{cat if cat else 'Total'}</b><br><b>{x:.2f}</b>"),
            textposition='inside',
            orientation='h',
        ))
    
    fig.update_layout(
        title=title,
        title_x = 0.5,
        barmode='stack',
        height=height,
        width=width,
        showlegend=legend,
    )

    # Update datetime axis format
    unique_dates = grouped_df[year_col].nunique() if year_col else 0
    if unique_dates == 1:
        fig.update_yaxes(tickvals=[grouped_df[year_col].iloc[0]], ticktext=['Total'])
    elif unique_dates > 1:
        fig.update_yaxes(tickformat="%d-%m-%Y")

    if watermark:
        fig.update_layout(images= watermark_settings())
    
    if theme:
        fig.update_layout(template=theme)

    if legend_dark:
        fig.update_layout(legend = legend_settings_dark())
    
    return fig


def make_donut_chart(
    df, 
    group_col='category', 
    value_col='financed_emissions',
    hole=0.3, 
    percent=False, 
    title='', 
    center_text=None, 
    height=None, 
    width=None, 
    theme=None, 
    watermark=True,
    legend=True,
    legend_dark=False
):
    # Group the data
    grouped_data = df.groupby(group_col).agg({value_col: 'sum'}).reset_index()
    sorted_labels = df[group_col].unique()
    grouped_data.set_index(group_col, inplace=True)
    grouped_data = grouped_data.loc[sorted_labels].reset_index()
    
    total_emissions = grouped_data[value_col].sum()
    grouped_data['percent'] = (grouped_data[value_col] / total_emissions) * 100

    if percent:
        grouped_data.loc[:, value_col] = 100 * grouped_data[value_col] / total_emissions
    
    # Create the figure
    fig = go.Figure(data=[go.Pie(
        labels=grouped_data[group_col],
        values=grouped_data[value_col],
        hole=hole,
        customdata=grouped_data['percent'],
        textinfo='label+percent',
        insidetextorientation='horizontal',
        texttemplate="<b>%{label}</b>:<br>%{value:.2f}<br>%{customdata:.2f}%",
        sort=False,
    )])
    
    # Update layout
    fig.update_layout(
        title=title,
        title_x=0.5,
        height=height,
        width=width,
        annotations=[dict(text=center_text, x=0.5, y=0.5, font_size=14, showarrow=False)], 
    )
    if theme:
        fig.update_layout(template=theme)
    if watermark:
        fig.update_layout(images=watermark_settings())
    if not legend:
        fig.update_layout(showlegend=False)
    if legend_dark:
        fig.update_layout(legend = legend_settings_dark())

    return fig


def make_grouped_line_chart(
    df, 
    group_col,
    value_col,
    date_col=None,
    percent=False, 
    resample_freq=None,
    stacked=True,
    show_delta=True,
    title='',
    theme=None, 
    watermark=True, 
    legend=True, 
    legend_dark=False, 
    height=None, 
    width=None
):
    # Filter and aggregate data
    temp = df.copy()
    
    # Resampling
    if resample_freq and pd.api.types.is_datetime64_any_dtype(temp[date_col]):
        temp.set_index(date_col, inplace=True)
        temp = temp.groupby([group_col, pd.Grouper(freq=resample_freq)]).sum().reset_index()

    total_emissions_by_time = temp.groupby(date_col)[ value_col ].transform('sum')
    if percent:
        temp.loc[:, value_col] = 100 * temp[value_col] / total_emissions_by_time
    temp = temp.groupby([date_col, group_col]).agg({value_col: 'sum'}).reset_index()

    try:
        temp['category_n'] = temp[group_col].str.extract('(\d+)').astype(int)
        temp = temp.sort_values(['category_n', date_col], ascending=[True, True])
    except Exception as e:
        print(e)

    # Initialize color map
    unique_categories = temp[group_col].unique()
    if theme and theme in pio.templates:
        colors = pio.templates[theme].layout.colorway  # Retrieve color sequence from theme
    else:
        colors = pio.templates['streamlit'].layout.colorway  # Fallback to default colors
    color_map = {cat: colors[i % len(colors)] for i, cat in enumerate(unique_categories)}

    unique_dates = temp[date_col].nunique() if date_col else 0
    if unique_dates < 2:
        fig = go.Figure()
        for cat in unique_categories:
            cat_data = temp[temp[group_col] == cat]
            fig.add_trace(go.Bar(
                x=[cat],
                y=cat_data[value_col],
                name=cat,
                marker=dict(color=color_map[cat])
            ))
            fig.update_layout(barmode='group')
    else:
      if show_delta:
          fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.01, row_heights=[0.7, 0.3])
      else:
          fig = make_subplots(rows=1, cols=1)

      # Line chart
      for cat in unique_categories:
          cat_data = temp[temp[group_col] == cat].sort_values(date_col)
          fig.add_trace(go.Scatter(
              x=cat_data[date_col],
              y=cat_data[value_col],
              mode='lines',
              stackgroup='one' if stacked else None,
              name=cat,
              opacity=0.2 if stacked else None,
              legendgroup=cat,
              line=dict(
                  color=color_map[cat], 
                  width=4 if not stacked else None
              )
          ), row=1, col=1)
      
      if show_delta:
          # Bar chart for YoY / MoM / QoQ change
          temp['interval_change'] = temp.groupby(group_col)[value_col].pct_change() * 100  # Calculate resampled interval change
          for cat in unique_categories:
              cat_data = temp[temp[group_col] == cat].sort_values(date_col)
              fig.add_trace(go.Bar(
                  x=cat_data[date_col],
                  y=cat_data['interval_change'],
                  name=cat,
                  legendgroup=cat,
                  showlegend=False,
                  marker=dict(color=color_map[cat])
              ), row=2, col=1)
        
    # Update layout
    fig.update_layout(
        title=title,
        hovermode="x",
        height=height,
        width=width,
        xaxis_title='',
        yaxis_title='Emissions (%)' if percent else 'Emissions'
    )
    
    if theme:
        fig.update_layout(template=theme)
    if watermark:
        fig.update_layout(images=watermark_settings())
    if not legend:
        fig.update_layout(showlegend=False)
    if legend_dark:
        orientation = 'h'  # or 'v' for vertical
        max_per_row = 7
        fig.update_layout(legend=legend_settings_dark(orientation, max_per_row))

    return fig
