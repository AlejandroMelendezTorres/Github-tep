import pandas as pd 
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters
import plotly.express as px

# Force layout to fill the entire width of your screen
st.set_page_config(layout="wide")

# load data from Data/sellers.xlsx
df = pd.read_excel('Data/sellers.xlsx')

# --- DATA PROCESSING ---
df['FULL_NAME'] = df['NAME'] + " " + df['LASTNAME']

# --- LAYOUT STRUCTURE (Two Columns) ---
left_col, right_col = st.columns([1, 1.5])

# --- LEFT COLUMN: Filters, Dropdowns, and Cards ---
with left_col:
    st.markdown("### Controls & Vendor Profile")
    
    # Apply Dynamic Filters (Region)
    dynamic_filters = DynamicFilters(df, filters=['REGION'])
    dynamic_filters.display_filters() 
    filtered_df = dynamic_filters.filter_df()
    
    st.markdown("---")
    
    # Vendor dropdown selector
    selected_vendor = st.selectbox(
        "Select a Vendor:", 
        options=filtered_df['FULL_NAME'].unique()
    )
    
    if selected_vendor and not filtered_df.empty:
        vendor_rows = filtered_df[filtered_df['FULL_NAME'] == selected_vendor]
        
        if not vendor_rows.empty:
            total_income = vendor_rows['INCOME'].sum()
            total_units = vendor_rows['SOLD UNITS'].sum()
            total_sales = vendor_rows['TOTAL SALES'].sum()
            avg_sales = vendor_rows['SALES AVERAGE'].mean() 
            
            card_col1, card_col2 = st.columns(2)
            with card_col1:
                st.metric(label="Total Income", value=f"${total_income:,.2f}")
                st.metric(label="Total Sales", value=f"${total_sales:,.2f}")
            with card_col2:
                st.metric(label="Total Sold Units", value=f"{total_units:,}")
                st.metric(label="Sales Average (Mean)", value=f"${avg_sales:,.2f}")

# --- RIGHT COLUMN: Charts and Raw Data ---
with right_col:
    st.markdown("### Performance Analytics")
    
    # FIX: Group data by REGION first to handle math math rules correctly
    df_regional = filtered_df.groupby('REGION').agg({
        'SOLD UNITS': 'sum',
        'TOTAL SALES': 'sum',
        'SALES AVERAGE': 'mean' # Ensures this column uses average, not sum
    }).reset_index()
    
    # Reshape the safely aggregated regional dataframe
    df_long = pd.melt(
        df_regional, 
        id_vars=['REGION'], 
        value_vars=['SOLD UNITS', 'TOTAL SALES', 'SALES AVERAGE'],
        var_name='Metric', 
        value_name='Value'
    )
    
    # Create the horizontal grouped bar chart
    fig = px.bar(
        df_long,
        x='Value',
        y='REGION',
        color='Metric', 
        barmode='group',
        orientation='h', 
        title='Sales Performance by Region (Properly Aggregated)'
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=300)
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("#### Vendor Data Registry")
    st.dataframe(
        filtered_df.drop(columns=['FULL_NAME']), 
        use_container_width=True,
        height=250 
    )
