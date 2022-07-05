import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
import chart_studio.plotly as py

#plotting as a figure, one series shown
# fig1 = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1]))
# fig.update_layout(title_text='hello world')


# plotting as a plot with data, multiple series, can do multiple plots w col#s
fig3 = make_subplots(rows=1, cols=2, specs=[[{"type": "scatter"},
                                            {"type": "scatter"}]])
# Add bar traces to subplot (1, 1)
fig3.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17]), row=1, col=1)
fig3.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[16, 5, 11, 9]), row=1, col=1)
fig3.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1]), row=1, col=1)

# Add surface trace to subplot (1, 2)
# Read data from a csv
#z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")
#fig.add_surface(z=z_data)

# Hide legend
fig3.update_layout(showlegend=False, title_text="multi series test",height=500,width=800,)

pio.write_html(fig3, file='hello_world.html', auto_open=True)
