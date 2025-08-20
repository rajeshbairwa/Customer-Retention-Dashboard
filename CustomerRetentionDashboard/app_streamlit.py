import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Customer Retention Dashboard', layout='wide')

@st.cache_data
def load_data():
    df = pd.read_csv('data/synthetic_transactions.csv', parse_dates=['order_date'])
    df['year_month'] = df['order_date'].dt.to_period('M').astype(str)
    return df

df = load_data()

st.title('Customer Retention Dashboard (Synthetic)')

# KPIs
total_customers = df['customer_id'].nunique()
total_orders = len(df)
total_revenue = df['amount'].sum()

c1, c2, c3 = st.columns(3)
c1.metric('Active Customers', f'{total_customers:,}')
c2.metric('Total Orders', f'{total_orders:,}')
c3.metric('Total Revenue (₹)', f'{total_revenue:,.0f}')

# Monthly revenue
monthly_rev = df.groupby('year_month')['amount'].sum().reset_index()

fig1 = plt.figure()
plt.plot(monthly_rev['year_month'], monthly_rev['amount'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
st.pyplot(fig1)

# Repeat purchase rate
df_sorted = df.sort_values(['customer_id', 'order_date'])
df_sorted['is_repeat'] = df_sorted.groupby('customer_id').cumcount() > 0
repeat_rate = df_sorted.groupby('year_month')['is_repeat'].mean().reset_index()
repeat_rate['is_repeat'] = (repeat_rate['is_repeat'] * 100).round(2)

fig2 = plt.figure()
plt.plot(repeat_rate['year_month'], repeat_rate['is_repeat'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title('Repeat Purchase Rate (%)')
plt.xlabel('Month')
plt.ylabel('% Customers who are repeat')
plt.tight_layout()
st.pyplot(fig2)

st.sidebar.header('Filters')
state_filter = st.sidebar.multiselect('State', sorted(df['state'].unique()))
category_filter = st.sidebar.multiselect('Category', sorted(df['category'].unique()))

mask = pd.Series(True, index=df.index)
if state_filter:
    mask &= df['state'].isin(state_filter)
if category_filter:
    mask &= df['category'].isin(category_filter)

df_f = df[mask]
st.subheader('Filtered Summary (last 12 months)')
st.write(df_f.groupby('year_month')['amount'].sum().reset_index().tail(12))

st.caption('Synthetic dataset generated for portfolio use. Not real customer data.')
