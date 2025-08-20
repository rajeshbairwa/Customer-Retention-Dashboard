import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/synthetic_transactions.csv', parse_dates=['order_date'])
df['year_month'] = df['order_date'].dt.to_period('M').astype(str)

# Monthly revenue
monthly_rev = df.groupby('year_month')['amount'].sum().reset_index()

plt.figure()
plt.plot(monthly_rev['year_month'], monthly_rev['amount'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('images/monthly_revenue.png')

# Repeat purchase rate
df_sorted = df.sort_values(['customer_id', 'order_date'])
df_sorted['is_repeat'] = df_sorted.groupby('customer_id').cumcount() > 0
repeat_rate = df_sorted.groupby('year_month')['is_repeat'].mean().reset_index()
repeat_rate['is_repeat'] = (repeat_rate['is_repeat'] * 100).round(2)

plt.figure()
plt.plot(repeat_rate['year_month'], repeat_rate['is_repeat'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title('Repeat Purchase Rate (%)')
plt.xlabel('Month')
plt.ylabel('% Customers who are repeat')
plt.tight_layout()
plt.savefig('images/repeat_purchase_rate.png')
