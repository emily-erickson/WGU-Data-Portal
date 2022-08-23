import streamlit as st
import pandas as pd
import plotly.express as px


def view_page():
    # Encode dataframe so it can be downloaded as a csv
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    # Import data, put it into dataframes
    attainment_field = pd.DataFrame(pd.read_csv("education/ed_attainment_by_field.csv"))
    occupation_edlevel = pd.DataFrame(pd.read_csv("education/edlevel_by_occupation.csv"))
    occupation_edreqs = pd.DataFrame(pd.read_csv("education/requireded_by_occupation.csv"))

    # Convert column which should be int from string to int
    attainment_field["count"] = attainment_field["count"].str.replace(",","").astype(int)

    st.title("Education Data")

    # Educational attainment section
    st.header("Bachelor's Degree Attainment by Field and Age")

    # Location selectbox
    selected_location = st.selectbox("Region: ", attainment_field["location"].unique().tolist(), key="selected_location")

    # Process data based on selection
    filtered_field = attainment_field[attainment_field["location"] == selected_location]
    filtered_field = filtered_field.pivot(columns="age",index="degree_field", values="count").drop(columns=["All"])

    # Create two columns
    col1a, col1b = st.columns([1,2])

    # For spacing
    col1a.write("")
    col1a.write("")

    # Display filtered data as table
    col1a.table(filtered_field)

    # Download backing data set
    col1a.download_button(
        label="Download Census Degree Attainment Data (S1502)",
        data=convert_df(attainment_field),
        file_name='census_degree_attainment.csv',
        mime='text/csv',
        key='download census_degree_attainment'
    )

    # Wrangle data into form necessary for bar chart
    filtered_field = filtered_field.drop(index=["Total population 25 years and over with a Bachelor's degree or higher"])
    filtered_field["degree_field"] = filtered_field.index.tolist()

    # Create and display bar chart
    fig = px.bar(filtered_field, x="degree_field", y=["25-39", "40-64", "65+"],
                 title=f"Bachelors Degrees By Field and Age in {selected_location}",
                 labels={"variable": "Age Group", "value": "Number of People With Degree",
                         "degree_field": "Field of Degree"}, color_discrete_sequence=px.colors.qualitative.Prism)

    col1b.plotly_chart(fig, use_container_width=True)

    # Second section: Employee educational attainment by occupation
    st.write("***")
    st.header("Employee Educational Attainment By Occupation")

    # Occupation selectbox
    selected_occupation = st.selectbox("Select an occupation", occupation_edlevel["2020 National Employment Matrix title"].unique().tolist())

    # Filter data based on selection
    filtered_edlevel = occupation_edlevel[occupation_edlevel["2020 National Employment Matrix title"] == selected_occupation]

    # Wrangle data into usable form
    filtered_edlevel = filtered_edlevel.drop(columns=["2020 National Employment Matrix title", "2020 National Employment Matrix code"])
    filtered_edlevel = filtered_edlevel.transpose()
    filtered_edlevel = filtered_edlevel.reset_index()
    filtered_edlevel = filtered_edlevel.rename(columns={filtered_edlevel.columns[0]: "edlevel", filtered_edlevel.columns[1]: "percent"})

    # Create two columns
    col1b, col2b = st.columns(2)

    col1b.write("")
    col1b.write("")

    # Display table data and download button in column on left
    col1b.table(filtered_edlevel)
    col1b.download_button(
        label="Download Census Occupational Ed Attainment Data",
        data=convert_df(occupation_edlevel),
        file_name='census_occupation_ed_attainment.csv',
        mime='text/csv',
        key='download census_occupation_ed_attainment'
    )

    # Display pie chart of data in column on the right
    attainment_pie = px.pie(filtered_edlevel, values="percent", names="edlevel", color_discrete_sequence=px.colors.qualitative.Prism, hole=0.4, title="Percent Employed By Ed Level")
    col2b.plotly_chart(attainment_pie, use_contaner_width=True)

    # Third section: education requirements by occupation
    st.write("***")
    st.header("Education Requirements By Occupation")

    # Occupation multiselect
    selected_job = st.multiselect("Select Occupation(s)", occupation_edreqs["2020 National Employment Matrix title"].tolist(), key="selected_job")

    # Prepare data
    filtered_occupation_reqs = occupation_edreqs.drop(columns=["2020 National Employment Matrix code"])
    filtered_occupation_reqs = filtered_occupation_reqs[filtered_occupation_reqs["2020 National Employment Matrix title"].isin(selected_job)]

    # Display filtered data as table
    st.table(filtered_occupation_reqs)

    # Download buttons for generated and backing data csv's, placed side by side
    c1,c2 = st.columns([.2, 1])

    c1.download_button(
        label="Download Generated Table",
        data=convert_df(filtered_occupation_reqs),
        file_name='custom_occupation_requirements.csv',
        mime='text/csv',
        key='download custom_occupation_requirements'
    )

    c2.download_button(
        label="Download Census Occupational Ed Requirements Data",
        data=convert_df(occupation_edreqs),
        file_name='census_occupation_edreqs.csv',
        mime='text/csv',
        key='download census_occupation_edreqs'
    )



