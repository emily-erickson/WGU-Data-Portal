import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def view_industry_page():
    # Encodes dataframes for download as csv
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    # Create dataframes from csv files
    industry_over_time_df = pd.DataFrame(pd.read_csv("industry/industry_over_time.csv"))
    industry_by_region_df = pd.DataFrame(pd.read_csv("industry/industry_by_region.csv"))

    st.title("Industry Data")
    st.header("Trends in Employees, Hours, and Earnings by Industry")

    # Columns for first section
    col1a, col2a = st.columns([4,1])

    with col2a:
        # For spacing
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        # Select variable of interest and industries to include
        iot_feature = st.selectbox('Select Variable to Trend',('Employees', 'Hours', 'Earnings'))
        iot_industry = st.multiselect('Select Industries', industry_over_time_df["industry"].unique().tolist())

        # Dynamically change graph labels based on selections
        if iot_feature == "Employees":
            y_label = "Thousands of People Employed"
        elif iot_feature == "Hours":
            y_label = "Average Hours Worked Weekly per Worker"
        elif iot_feature == "Earnings":
            y_label = "Average Hourly Earnings (dollars)"

        # For spacing
        st.write("")

        # Download backing data table
        st.download_button(
            label="Download BLS Industry Data (2006-2022)",
            data=convert_df(industry_over_time_df),
            file_name='bls_industries_over_time.csv',
            mime='text/csv',
            key='download bls_industries_over_time'
        )

    with col1a:
        # Build and display line graph based on selected fields
        iot_filtered_data = industry_over_time_df[industry_over_time_df["industry"].isin(iot_industry)]

        fig = px.line(iot_filtered_data, x="date", y=iot_feature.lower(), color="industry",
                      labels={"date": "Date", "employees": "Thousands of People Employed",
                              "hours": "Average Hours Worked Weekly per Worker",
                              "earnings": "Average Hourly Earnings (dollars)"},
                      title=f"{iot_feature.capitalize()} in {', '.join([str(item).capitalize() for item in iot_industry])} Industry Over Time",
                      color_discrete_sequence=px.colors.qualitative.G10)

        fig.update_layout(title={'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
                          xaxis=go.layout.XAxis(tickangle=45),
                          legend=dict(xanchor="center", yanchor="top", x=0, y=-0.17))

        st.plotly_chart(fig, use_container_width=True)

    # Second section
    st.write("***")
    st.header("Industry Prevalence by State")

    col1b, col2b = st.columns([4,1])

    with col2b:
        # Industry multiselect
        industry_choice = st.radio(label="Select an Industry",options=industry_by_region_df["industry"].unique().tolist())

    with col1b:
        # Create and display chloropleth map of percentage of state population working in selected industries
        fig = px.choropleth(industry_by_region_df[industry_by_region_df["industry"] == industry_choice],
                            locations='Code',
                            color='percent_of_state_population',
                            color_continuous_scale='PuBu',
                            hover_name='region',
                            locationmode='USA-states',
                            labels={'percent_of_state_population': '% Employed in Selected Industry'},
                            scope='usa',
                            title=f'Percent of Population Working in {industry_choice}',
                            color_discrete_sequence=px.colors.qualitative.Prism)

        fig.update_layout(legend=dict(xanchor="left", yanchor="middle", x=-2, y=0), width=700, height=700,
                          title={'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'}, dragmode=False)

        st.plotly_chart(fig, use_container_width=True)

    # Third section
    st.write("***")
    st.header("Compare Industry Segments By Region")

    col1c,col2c = st.columns(2)

    with col1c:
        # Create and display pie chart of population percent employed in different industries in selected region
        state_select1 = st.selectbox("Select Region",industry_by_region_df["region"].unique().tolist(), key="state_select1", index=0)

        fig = px.pie(industry_by_region_df[industry_by_region_df["region"] == state_select1], values='employed_count',
                     names='industry', title=f"Percent of {state_select1}'s Population in Different Industries",
                     color_discrete_sequence=px.colors.qualitative.Prism, hole=0.4)

        fig.update_layout(showlegend=True, legend=dict(xanchor="center", yanchor="top", x=0.5, y=-0.1), width=700,
                          height=700, title={'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'})

        st.plotly_chart(fig, use_container_width=True)

    with col2c:
        # Repeat of above code, second column is for comparison
        state_select2 = st.selectbox("Select Region",industry_by_region_df["region"].unique().tolist(),key="state_select2",index=5)

        fig = px.pie(industry_by_region_df[industry_by_region_df["region"] == state_select2], values='employed_count',
                     names='industry', title=f"Percent of {state_select2}'s Population in Different Industries",
                     color_discrete_sequence=px.colors.qualitative.Prism, hole=0.4)

        fig.update_layout(showlegend=True, legend=dict(xanchor="center", yanchor="top", x=0.5, y=-0.1), width=700,
                          height=700, title={'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'})

        st.plotly_chart(fig, use_container_width=True)





