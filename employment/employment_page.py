import streamlit as st
import pandas as pd
import plotly.express as px


def view_employment_page():
    # Encode dataframes to prepare them for download as csv
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    # Create dataframes from csvs
    predictions = pd.DataFrame(pd.read_csv("employment/employment_projections_by_occupation.csv"))
    national_employment = pd.DataFrame(pd.read_csv("employment/oesm_nat.csv"))

    st.title("Employment Data")

    ## Job projections section
    st.header("Employment Projections, 2020-2030")

    # Most growth, most decline -- by both number and percent of field
    # Prepare dataframes to generate tables
    predictions_li = predictions[predictions["Occupation type"] == "Line item"]
    most_growth_count = predictions_li[["title", "Employment, 2020", "Employment, 2030", "Employment change, 2020-30"]]
    most_growth_count["Employment change, 2020-30"] = most_growth_count["Employment change, 2020-30"].str.replace(",","").astype(float)
    most_growth_percent = predictions_li[["title", "Percent employment change, 2020-30"]]
    most_growth_percent["Percent employment change, 2020-30"] = most_growth_percent["Percent employment change, 2020-30"]

    # Create and display the datatables in columns
    left, gap, right = st.columns([2, 0.1, 2])

    left.markdown("### Most Projected Growth")
    left.write("Most Growth By Count (in Thousands)")
    left.table(most_growth_count.sort_values(by='Employment change, 2020-30', ascending=False)[:10])
    left.write("Most Growth By Percent")
    left.table(most_growth_percent.sort_values(by="Percent employment change, 2020-30", ascending=False)[:10])

    right.markdown("### Most Projected Decline")
    right.write("Most Decline By Count (in Thousands)")
    right.table(most_growth_count.sort_values(by='Employment change, 2020-30', ascending=True)[:10])
    right.write("")
    right.write("")
    right.write("")
    right.write("Most Decline By Percent")
    right.table(most_growth_percent.sort_values(by="Percent employment change, 2020-30", ascending=True)[:10])

    # Second section, build table of data for selected occupations
    st.write("***")
    st.header("Projections By Field and Occupation")

    # Subset data based on whether occupation is category name or specific instance
    specific_occupations = predictions[predictions["Occupation type"] == "Line item"]
    specific_fields = predictions[predictions["Occupation type"] == "Summary"]

    # User selects level to filter by ...
    filter_by = st.radio("View Projections By: ", ["Field", "Specific Occupation"], horizontal=True, key="filter_by")

    # ...flags disable field that isn't selected
    if filter_by == "Field":
        disable_field = False
        disable_category = True
    elif filter_by == "Specific Occupation":
        disable_field = True
        disable_category = False

    # Field multiselect
    selected_field = st.multiselect(
        "Select Field(s)",
        specific_fields["title"].tolist(),
        key="fields_select",
        disabled=disable_field
    )

    # Occupation multiselect
    selected_occupation = st.multiselect(
        "Select Occupation(s)",
        specific_occupations["title"].tolist(),
        key="occupation_select",
        disabled=disable_category
    )

    # Filter and process dataframe
    field = predictions[predictions["Occupation type"] == "Summary"]
    occupation = predictions[predictions["Occupation type"] == "Line item"]

    field = field[["title","Employment, 2020","Employment, 2030","Employment distribution, percent, 2020","Employment distribution, percent, 2030","Employment change, 2020-30","Percent employment change, 2020-30","Occupational openings, 2020-30 annual average"]]
    occupation = occupation[["title","Employment, 2020","Employment, 2030","Employment distribution, percent, 2020","Employment distribution, percent, 2030","Employment change, 2020-30","Percent employment change, 2020-30","Occupational openings, 2020-30 annual average"]]

    if filter_by == "Field":
        filtered_data = field[field["title"].isin(selected_field)]
    else:
        filtered_data = occupation[occupation["title"].isin(selected_occupation)]

    # Dsiplay table of filtered data
    st.table(filtered_data)

    # Download buttons for both generated and backing data, formatted side by side
    st.write("")
    c1,c2 = st.columns([.2, 1])

    c1.download_button(
        label="Download Generated Table",
        data=convert_df(filtered_data),
        file_name='custom_occupation_projections.csv',
        mime='text/csv',
        key='download tables'
    )
    c2.download_button(
        label="Download All OESM Employment Projections",
        data=convert_df(predictions),
        file_name='oesm_employment_projections_by_occupation.csv',
        mime='text/csv',
        key='download tables'
    )

    ## Third section: historical employment number, w/ filter by state optional
    st.write("***")
    st.header("Historical Employment and Wages")

    # Prepare datasets
    employment_specific_occupations = national_employment[national_employment["OCC_GROUP"] == "detailed"]
    employment_specific_fields = national_employment[national_employment["OCC_GROUP"] == "major"]

    # Select filter level
    employment_filter_by = st.radio("Filter by:", ["Field", "Specific Occupation"], horizontal=True, key="employment_filter_by")

    # Toggle flag which disables input widget that isn't selected
    if employment_filter_by == "Field":
        employment_disable_category = True
        employment_disable_field = False
    else:
        employment_disable_field = True
        employment_disable_category = False

    # Field multisselect
    employment_selected_field = st.multiselect(
        "Select field(s)",
        employment_specific_fields["OCC_TITLE"].unique().tolist(),
        key="employment_fields_select",
        disabled=employment_disable_field
    )

    # Occupation multiselect
    employment_selected_occupation = st.multiselect(
        "Select occupation(s)",
        employment_specific_occupations["OCC_TITLE"].unique().tolist(),
        key="employment_occupation_select",
        disabled=employment_disable_category
    )

    # Filter data based on selections
    if employment_filter_by == "Field":
        employment_filtered_data = employment_specific_fields[employment_specific_fields["OCC_TITLE"].isin(employment_selected_field)]
    else:
        employment_filtered_data = employment_specific_occupations[employment_specific_occupations["OCC_TITLE"].isin(employment_selected_occupation)]

    # Display visualizations in two columns
    col1, col2 = st.columns(2)

    # Line graph of number of employees
    with col1:
        # TOT_EMP was string, needed to be converted to int
        employment_filtered_data["TOT_EMP"] = employment_filtered_data["TOT_EMP"].str.replace(",", "").astype(int)

        employment_line = px.line(employment_filtered_data, x="year", y="TOT_EMP", color="OCC_TITLE", labels={"year":"Year", "TOT_EMP":"Total Employment"}, title = "Total Employment By Occupation Over Time", color_discrete_sequence=px.colors.qualitative.G10)
        employment_line.update_layout(legend=dict(xanchor="center", yanchor="top", x=0.5, y=-0.2))

        st.plotly_chart(employment_line, use_container_width=True)

    ## Line graph of median wage
    with col2:
        # A_MEDIAN was string, needed to be converted to int
        employment_filtered_data["A_MEDIAN"] = employment_filtered_data["A_MEDIAN"].str.replace(",","").astype(int)

        fig = px.line(employment_filtered_data, x="year", y="A_MEDIAN", color="OCC_TITLE", labels={"year":"Year", "A_MEDIAN":"Median Annual Earnings (in dollars)"}, title = "Median Annual Earnings By Occupation Over Time", color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_layout(legend=dict(xanchor="center", yanchor="top", x=0.5, y=-0.2))

        st.plotly_chart(fig, use_container_width=True)

    # Display buttons to download generated and backing tables side by side
    st.write("")
    s1,s2 = st.columns([.25, 1])

    s1.download_button(
        label="Download Displayed Data as CSV",
        data=convert_df(employment_filtered_data),
        file_name='displayed_employment_and_wage_data.csv',
        mime='text/csv',
        key='download tables'
    )

    s2.download_button(
        label="Download Raw BLS Employment and Wage Data",
        data=convert_df(national_employment),
        file_name='bls_employment_and_wage_data.csv',
        mime='text/csv',
        key='download tables'
    )

