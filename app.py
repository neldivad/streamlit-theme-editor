import colorsys

import streamlit as st

import fragments
import util
from util import ThemeColor
from charting import *

st.set_page_config(
  layout="wide",
  initial_sidebar_state="expanded",
)
    
preset_colors: list[tuple[str, ThemeColor]] = [
    ("Default light", ThemeColor(
            primaryColor="#ff4b4b",
            backgroundColor="#ffffff",
            secondaryBackgroundColor="#f0f2f6",
            textColor="#31333F",
        )),
    ("Default dark", ThemeColor(
            primaryColor="#ff4b4b",
            backgroundColor="#0e1117",
            secondaryBackgroundColor="#262730",
            textColor="#fafafa",
    ))
]

theme_from_initial_config = util.get_config_theme_color()
if theme_from_initial_config:
    preset_colors.append(("From the config", theme_from_initial_config))

default_color = preset_colors[0][1]


def sync_rgb_to_hls(key: str):
    # HLS states are necessary for the HLS sliders.
    rgb = util.parse_hex(st.session_state[key])
    hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
    st.session_state[f"{key}H"] = round(hls[0] * 360)
    st.session_state[f"{key}L"] = round(hls[1] * 100)
    st.session_state[f"{key}S"] = round(hls[2] * 100)


def sync_hls_to_rgb(key: str):
    h = st.session_state[f"{key}H"]
    l = st.session_state[f"{key}L"]
    s = st.session_state[f"{key}S"]
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    st.session_state[key] = f"#{round(r * 255):02x}{round(g * 255):02x}{round(b * 255):02x}"


def set_color(key: str, color: str):
    st.session_state[key] = color
    sync_rgb_to_hls(key)


if 'preset_color' not in st.session_state or 'backgroundColor' not in st.session_state or 'secondaryBackgroundColor' not in st.session_state or 'textColor' not in st.session_state:
    set_color('primaryColor', default_color.primaryColor)
    set_color('backgroundColor', default_color.backgroundColor)
    set_color('secondaryBackgroundColor', default_color.secondaryBackgroundColor)
    set_color('textColor', default_color.textColor)


st.title("Streamlit color theme editor")


def on_preset_color_selected():
    _, color = preset_colors[st.session_state.preset_color]
    set_color('primaryColor', color.primaryColor)
    set_color('backgroundColor', color.backgroundColor)
    set_color('secondaryBackgroundColor', color.secondaryBackgroundColor)
    set_color('textColor', color.textColor)


st.selectbox("Preset colors", key="preset_color", options=range(len(preset_colors)), format_func=lambda idx: preset_colors[idx][0], on_change=on_preset_color_selected)

if st.button("🎨 Generate a random color scheme 🎲"):
    primary_color, text_color, basic_background, secondary_background = util.generate_color_scheme()
    set_color('primaryColor', primary_color)
    set_color('backgroundColor', basic_background)
    set_color('secondaryBackgroundColor', secondary_background)
    set_color('textColor', text_color)


def color_picker(label: str, key: str, default_color: str, l_only: bool) -> None:
    col1, col2 = st.columns([1, 3])
    with col1:
        color = st.color_picker(label, key=key, on_change=sync_rgb_to_hls, kwargs={"key": key})
    with col2:
        r,g,b = util.parse_hex(default_color)
        h,l,s = colorsys.rgb_to_hls(r,g,b)
        if l_only:
            if f"{key}H" not in st.session_state:
                st.session_state[f"{key}H"] = round(h * 360)
        else:
            st.slider(f"H for {label}", key=f"{key}H", min_value=0, max_value=360, value=round(h * 360), format="%d°", label_visibility="collapsed", on_change=sync_hls_to_rgb, kwargs={"key": key})

        st.slider(f"L for {label}", key=f"{key}L", min_value=0, max_value=100, value=round(l * 100), format="%d%%", label_visibility="collapsed", on_change=sync_hls_to_rgb, kwargs={"key": key})

        if l_only:
            if f"{key}S" not in st.session_state:
                st.session_state[f"{key}S"] = round(s * 100)
        else:
            st.slider(f"S for {label}", key=f"{key}S", min_value=0, max_value=100, value=round(s * 100), format="%d%%", label_visibility="collapsed", on_change=sync_hls_to_rgb, kwargs={"key": key})

    return color


primary_color = color_picker('Primary color', key="primaryColor", default_color=default_color.primaryColor, l_only=True)
text_color = color_picker('Text color', key="textColor", default_color=default_color.textColor, l_only=True)
background_color = color_picker('Background color', key="backgroundColor", default_color=default_color.backgroundColor, l_only=True)
secondary_background_color = color_picker('Secondary background color', key="secondaryBackgroundColor", default_color=default_color.secondaryBackgroundColor, l_only=True)


st.header("WCAG contrast ratio")
st.markdown("""
Check if the color contrasts of the selected colors are enough to the WCAG guidelines recommendation.
For the details about it, see some resources such as the [WCAG document](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) or the [MDN page](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast).""")

def synced_color_picker(label: str, value: str, key: str):
    def on_change():
        st.session_state[key] = st.session_state[key + "2"]
        sync_rgb_to_hls(key)
    st.color_picker(label, value=value, key=key + "2", on_change=on_change)

col1, col2, col3 = st.columns(3)
with col2:
    synced_color_picker("Background color", value=background_color, key="backgroundColor")
with col3:
    synced_color_picker("Secondary background color", value=secondary_background_color, key="secondaryBackgroundColor")

col1, col2, col3 = st.columns(3)
with col1:
    synced_color_picker("Primary color", value=primary_color, key="primaryColor")
with col2:
    fragments.contrast_summary("Primary/Background", primary_color, background_color)
with col3:
    fragments.contrast_summary("Primary/Secondary background", primary_color, secondary_background_color)

col1, col2, col3 = st.columns(3)
with col1:
    synced_color_picker("Text color", value=text_color, key="textColor")
with col2:
    fragments.contrast_summary("Text/Background", text_color, background_color)
with col3:
    fragments.contrast_summary("Text/Secondary background", text_color, secondary_background_color)


st.header("Config")

st.subheader("Config file (`.streamlit/config.toml`)")
st.code(f"""
[theme]
primaryColor="{primary_color}"
backgroundColor="{background_color}"
secondaryBackgroundColor="{secondary_background_color}"
textColor="{text_color}"
""", language="toml")

st.subheader("Command line argument")
st.code(f"""
streamlit run app.py \\
    --theme.primaryColor="{primary_color}" \\
    --theme.backgroundColor="{background_color}" \\
    --theme.secondaryBackgroundColor="{secondary_background_color}" \\
    --theme.textColor="{text_color}"
""")


if st.checkbox("Apply theme to this page"):
    st.info("Select 'Custom Theme' in the settings dialog to see the effect")

    def reconcile_theme_config():
        keys = ['primaryColor', 'backgroundColor', 'secondaryBackgroundColor', 'textColor']
        has_changed = False
        for key in keys:
            if st._config.get_option(f'theme.{key}') != st.session_state[key]:
                st._config.set_option(f'theme.{key}', st.session_state[key])
                has_changed = True
        if has_changed:
            st.experimental_rerun()

    reconcile_theme_config()

    fragments.sample_components("body")
    with st.sidebar:
        fragments.sample_components("sidebar")


#--------
# Custom
#----------
import pandas as pd
import numpy as np
import random

def generate_toy_df():
    def generate_data(n, scope, start_year, end_year, category=None, emissions=1):
        years = np.linspace(start_year, end_year, n, endpoint=False).astype(int)
        data = []

        for i, year in enumerate(years):
            reduction_factor = 0.995 ** i
            current_emissions = emissions * np.random.power(0.8) * reduction_factor
            data.append([year, f'Scope {scope}', category, current_emissions])

        return pd.DataFrame(data, columns=['year', 'scope', 'category', 'emissions'])

    s1mc = generate_data(n=random.randint(30, 50), scope=1, start_year=2015, end_year=2026, category='Mobile Combustion', emissions=3)
    s1fe = generate_data(n=random.randint(5, 25), scope=1, start_year=2015, end_year=2026, category='Fugitive Emissions', emissions=7)
    s1sc = generate_data(n=random.randint(30, 50), scope=1, start_year=2015, end_year=2026, category='Stationary Combustion', emissions=3)
    s2ie = generate_data(n=random.randint(30, 45), scope=2, start_year=2015, end_year=2026, category='Indirect Emissions', emissions=5)
    s3c = [generate_data(n=random.randint(50, 100), scope=3, start_year=2015, end_year=2026, category=f'Category {i+1}') for i in range(15)]

    # Combine all data into one DataFrame
    df = pd.concat([s1mc, s1fe, s1sc, s2ie] + s3c, ignore_index=True)
    df['emissions'] = df['emissions'] * random.randint(1000, 50000)
    return df

def create_line_simulation():
    def random_timeseries(initial_value: float, volatility: float, count: int, trend: float = 0.0) -> list:
        time_series = [initial_value]
        for _ in range(count - 1):
            next_value = time_series[-1] + initial_value * random.gauss(0.2, 0.4) * volatility + trend
            time_series.append(next_value)
        return time_series

    
    months = pd.date_range(start='2019-01-01', end='2021-12-01', freq='MS')
    categories = [f'Category_{i+1}' for i in range(12)]
    
    values = []
    for _ in categories:
        cat_values = random_timeseries(initial_value=random.uniform(100,100), volatility=0.2, count=len(months), trend=2)
        values.extend(cat_values)

    data = {
        'date': np.tile(months, len(categories)),
        'category': np.repeat(categories, len(months)),
        'value': values
    }
    df = pd.DataFrame(data)
    return df

with st.sidebar:
    st.subheader('Select chart theme')
    chart_options = ['gecko3', 'gecko5', 'gecko7', 'gecko_v1', 'ilo', 'tableau', 'google']
    
    chart_theme = st.selectbox('Select theme', options=chart_options)

initialize_plotly_themes()
ts= create_line_simulation()
df = create_toy_df()

st.write(ts)

fig1 = make_grouped_line_chart(
    ts, 
    group_col='category', 
    value_col='value', 
    date_col='date', 
    resample_freq='Q', 
    stacked=False,
    theme=chart_theme
)
st.plotly_chart(fig1, use_container_width=True)


st.write(df)
fig2 = make_donut_chart(
    df, group_col='category', value_col='financed_emissions', center_text='Pie chart',
)
