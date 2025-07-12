import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Read the cleaned CSV file
df = pd.read_csv('CRM-and-Sales-Pipelines_cleaned.csv')

# Count each value in the Status column
status_counts = df['Status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']

# Sort by count descending for funnel order
status_counts = status_counts.sort_values('Count', ascending=False).reset_index(drop=True)

# Create the funnel chart
fig = go.Figure(go.Funnel(
    y=status_counts['Status'],
    x=status_counts['Count'],
    textinfo="value+percent initial",
    marker={"color": [
        "#FF8C42", "#3A99D8", "#20B2AA", "#444444", "#8BC34A", "#FFC107", "#E91E63", "#9C27B0", "#607D8B"
    ][:len(status_counts)]}
))

fig.update_layout(
    title="Funnel Chart by Status",
    plot_bgcolor='white'
)

# Try to save the image using different methods
try:
    # Method 1: Try with kaleido
    fig.write_image("screenshots/funnel_chart_status.png", width=800, height=600)
    print("Funnel chart saved as 'screenshots/funnel_chart_status.png' using kaleido")
except Exception as e:
    print(f"Kaleido method failed: {e}")
    try:
        # Method 2: Try with orca (if available)
        fig.write_image("screenshots/funnel_chart_status.png", width=800, height=600, engine="orca")
        print("Funnel chart saved as 'screenshots/funnel_chart_status.png' using orca")
    except Exception as e2:
        print(f"Orca method failed: {e2}")
        # Method 3: Save as HTML file
        fig.write_html("screenshots/funnel_chart_status.html")
        print("Funnel chart saved as 'screenshots/funnel_chart_status.html' (HTML format)") 