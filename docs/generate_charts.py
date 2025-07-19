import matplotlib.pyplot as plt
import numpy as np
import os

charts_dir = "charts"
os.makedirs(charts_dir, exist_ok=True)

# Slide 2: Horizontal Bar Chart
countries = ['Italy', 'Germany', 'France']
opportunities = [173, 124, 123]
percentages = [27.9, 29.5, 29.1]
colors = ['#ef5350', '#4caf50', '#2196f3']

plt.figure(figsize=(8, 3))
bars = plt.barh(countries, opportunities, color=colors)
for i, (bar, pct) in enumerate(zip(bars, percentages)):
    plt.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f"{opportunities[i]} ({pct}%)", va='center')
plt.title("Top 3 Countries by Pipeline Opportunities")
plt.xlabel("Opportunities")
plt.tight_layout()
plt.savefig(f"{charts_dir}/slide2.png")
plt.close()

# Slide 3: Line Chart
quarters = ['2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1', '2025 Q2']
values = [0.35, 1.72, 2.12, 2.33, 1.51, 0.25]

plt.figure(figsize=(8, 4))
plt.plot(quarters, values, marker='o', color='#3498db', linewidth=3)
for i, v in enumerate(values):
    plt.text(i, v + 0.1, f"${v}M", ha='center', va='bottom')
plt.title("Sales Forecast Based on Expected Close Date")
plt.ylabel("Sales ($M)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(f"{charts_dir}/slide3.png")
plt.close()

# Slide 4: Circular Chart (Donut)
labels = ['Italy', 'Germany', 'France', 'Overall']
sizes = [10.4, 10.5, 9.8, 9.6]
colors = ['#FF6384', '#4BC0C0', '#FFCD56', '#2c3e50']

plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Win Rate by Country vs. Overall Benchmark")
plt.tight_layout()
plt.savefig(f"{charts_dir}/slide4.png")
plt.close()

# Slide 5: Vertical Bar Chart
products = ['SAAS', 'Services', 'Custom Solution']
values = [961, 847, 488]
colors = ['#4CAF50', '#FFC107', '#2196F3']

plt.figure(figsize=(7, 4))
bars = plt.bar(products, values, color=colors)
for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, f"${values[i]}K", ha='center')
plt.title("Total Opportunity Value by Product")
plt.ylabel("Value ($K)")
plt.tight_layout()
plt.savefig(f"{charts_dir}/slide5.png")
plt.close()

# Slide 6: Funnel Chart (Stacked Bar as Approximation)
statuses = ['Opportunity', 'Qualified', 'Sales Accepted', 'New', 'Churned Customer', 'Disqualified', 'Customer']
percentages = [28.9, 18.9, 17.6, 17.1, 5.9, 5.9, 5.7]
colors = ['#66BB6A', '#FFD54F', '#D84315', '#673AB7', '#4DD0E1', '#8D6E63', '#42A5F5']

plt.figure(figsize=(6, 6))
bottom = 0
for i in range(len(statuses)):
    plt.bar('Pipeline', percentages[i], bottom=bottom, color=colors[i], label=f"{statuses[i]} ({percentages[i]}%)")
    bottom += percentages[i]
plt.title("Pipeline Distribution by Status")
plt.ylabel("Percentage (%)")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig(f"{charts_dir}/slide6.png")
plt.close() 