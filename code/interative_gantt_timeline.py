# This is a snippet. To use this on your site, include the libraries
#    (streamlit, plotly.express, etc)

########## Timeline Plot
st.header("Programs and Orgs Timeline Plot")
orgs_data = pd.read_csv(
    "data/Orgs_Progs.csv"
)
orgs_data = orgs_data.sort_values("Name")
orgs_data.drop("Supports_ET_Trinary",axis=1,inplace=True)
orgs_data.drop("Alt_Name",axis=1,inplace=True)

timeline = px.timeline(
	orgs_data, 
	x_start = "Start_Year_Min", 
	x_end = "End_Year_Max",
	y = "Name",
	color = 'Governmental',
	hover_data = ['Name','Country', 'Governmental'],
	category_orders = {'Name': orgs_data['Name']},
	labels = {'Name':""},
) 

orgs_data['delta'] = orgs_data['End_Year_Max'] - orgs_data['Start_Year_Min']
orgs_data=orgs_data.fillna("")
timeline.layout.xaxis.type="linear"
timeline.data[0].x = orgs_data['delta'].tolist()

st.plotly_chart(timeline, use_container_width=True)
st.write("Hint: If you're on a mobile device, try holding it 'sideways' to maximize width.")
st.write("")


