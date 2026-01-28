import pandas as pd
import matplotlib.pyplot as plt

fastFood = pd.read_csv("fast_food_ordering_dataset.csv")

# Remove rows with missing values from both fields and then convert float to str
fastFood = fastFood.dropna(subset=['cuisine_type'])
fastFood['delivery_time_minutes'] = fastFood['delivery_time_minutes'].fillna(0)

### Grouped by cuisine and tried to plot the avg time take for delivery for each cuisine type
avg_delivery_time = fastFood.groupby('cuisine_type')['delivery_time_minutes'].mean()

fig,axes = plt.subplots(1,2,figsize=(12,6))

fastFood['delivery_time_minutes'] = fastFood['delivery_time_minutes'].astype(str)

print(fastFood['delivery_time_minutes'])

# Bar chart: Cuisine vs Delivery Time
axes[0].bar(avg_delivery_time.index, avg_delivery_time.values)
axes[0].set_xlabel('Cuisine Type')
axes[0].set_ylabel('Delivery Time (minutes)')
axes[0].set_title('Delivery Time by Cuisine Type')
axes[0].set_ylim(20, 80)
axes[0].set_xticks(fastFood['cuisine_type'])
axes[0].tick_params(axis='x', rotation=45)


x = fastFood['city']
y = fastFood['order_value']

axes[1].scatter(x,y, color='red')
axes[1].set_xlabel('City')
axes[1].set_ylabel('Order Value')
axes[1].set_title('Order Value by City')

plt.tight_layout()
plt.show()


