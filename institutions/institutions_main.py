import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import decode


def display_institutions_page():
    # Encode dataframe so it can be downloaded as a csv
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    # Load data into dataframes
    static = pd.DataFrame(pd.read_csv("institutions/ipeds_static.csv"))
    degrees = pd.DataFrame(pd.read_csv("institutions/degrees_main.csv"))
    dynamic = pd.DataFrame(pd.read_csv("institutions/ipeds_dynamic.csv"))

    # Decoding numeric inputs into intelligible strings
    static_mapped = static
    obereg_list = static_mapped["OBEREG"].tolist()
    mapped_obereg = []
    for obereg in obereg_list:
        mapped_obereg.append(decode.decode_obereg(obereg))
    static_mapped["OBEREG"] = mapped_obereg

    control_list = static_mapped["CONTROL"].tolist()
    mapped_control = []
    for control in control_list:
        mapped_control.append(decode.decode_control(control))
    static_mapped["CONTROL"] = mapped_control

    level_list = static_mapped["ICLEVEL"].tolist()
    mapped_level = []
    for level in level_list:
        mapped_level.append(decode.decode_iclevel(level))
    static_mapped["ICLEVEL"] = mapped_level

    # Title and first section header
    st.title("Institutions")
    st.header("Schools")

    # Select location
    geo_filter = st.radio("Filter By: ", ["Show All", "Region(s)", "State(s)"], horizontal=True)

    # Flag to enable only selected filter
    if geo_filter == "Region(s)":
        disable_regions = False
        disable_states = True
    elif geo_filter == "State(s)":
        disable_states = False
        disable_regions = True
    elif geo_filter == "Show All":
        disable_regions = True
        disable_states = True

    # Select locations for chosen filter
    select_regions = st.multiselect("Select Region(s)", static_mapped["OBEREG"].unique().tolist(),
                                    disabled=disable_regions)
    select_states = st.multiselect("Select State(s)", static_mapped["STABBR"].unique().tolist(),
                                   disabled=disable_states)

    # Create filtered dataframe
    if geo_filter == "Region(s)":
        filtered_static = static_mapped[static_mapped["OBEREG"].isin(select_regions)]
    elif geo_filter == "State(s)":
        filtered_static = static_mapped[static_mapped["STABBR"].isin(select_states)]
    elif geo_filter == "Show All":
        filtered_static = static_mapped

    # School level and control pie charts
    st.write("")
    st.write("")
    st.markdown("#### School Level and Control In Selected Area(s)")

    # Display number of schools in filtered dataframe
    st.metric(label="Number of Schools in Selection", value=filtered_static['UNITID'].count())

    # Configure columns
    col1a, col1b = st.columns(2)

    # Use static_filtered UNITID's to filter dynamic datasets
    dynamic_filtered = dynamic[dynamic["UNITID"].isin(filtered_static["UNITID"].tolist())]

    # Slice of filtered dynamic data with most current year
    dynamic_current = dynamic_filtered[dynamic_filtered["year"] == 2020]

    # Get enrollment numbers by school control for pie chart
    static_public = filtered_static[filtered_static["CONTROL"] == "Public"]
    enr_public = dynamic_current[dynamic_current["UNITID"].isin(static_public["UNITID"])]["ENRTOT"].sum()

    static_private_nonprofit = filtered_static[filtered_static["CONTROL"] == "Private Not For-Profit"]
    enr_private_nonprofit = dynamic_current[dynamic_current["UNITID"].isin(static_private_nonprofit["UNITID"])][
        "ENRTOT"].sum()

    static_private_profit = filtered_static[filtered_static["CONTROL"] == "Private For-Profit"]
    enr_private_profit = dynamic_current[dynamic_current["UNITID"].isin(static_private_profit["UNITID"])][
        "ENRTOT"].sum()

    # Create and display control pie chart
    control_pie = px.pie(values=[enr_public, enr_private_nonprofit, enr_private_profit],
                         names=["Public", "Private Nonprofit", "Private For-Profit"],
                         color_discrete_sequence=px.colors.qualitative.Prism, hole=0.4, title="School Control")
    col1a.plotly_chart(control_pie, use_container_width=True)

    # Get enrollment numbers by school level for pie chart
    static_4plus = filtered_static[filtered_static["ICLEVEL"] == "4-year (or higher)"]
    count_4plus = dynamic_current[dynamic_current["UNITID"].isin(static_4plus["UNITID"])]["ENRTOT"].sum()

    static_2to4 = filtered_static[filtered_static["ICLEVEL"] == "2-year (less than 4 year)"]
    count_2to4 = dynamic_current[dynamic_current["UNITID"].isin(static_2to4["UNITID"])]["ENRTOT"].sum()

    static_2less = filtered_static[filtered_static["ICLEVEL"] == "less than 2-year"]
    count_2less = dynamic_current[dynamic_current["UNITID"].isin(static_2less["UNITID"])]["ENRTOT"].sum()

    # Create and display level pie chart
    level_pie = px.pie(values=[count_4plus, count_2to4, count_2less],
                       names=["4-year (or higher)", "2-year (less than 4 year)", "less than 2-year"],
                       color_discrete_sequence=px.colors.qualitative.Prism, hole=0.4, title="School Levels")
    col1b.plotly_chart(level_pie, use_container_width=True)

    # Create table of 7 schools with biggest enrollment in selected area
    biggest_enr = dynamic_current[["UNITID", "ENRTOT", "EFUG", "EFGRAD"]]
    biggest_enr = biggest_enr.drop_duplicates(subset="UNITID").sort_values(by="ENRTOT", ascending=False)[:7]

    # Replace UNITIDs with school names
    biggest_enr_list = biggest_enr["UNITID"].tolist()
    replacement_names = []
    for unitid in biggest_enr_list:
        replacement_names.append(filtered_static[filtered_static["UNITID"] == unitid]["INSTNM"].item())
    biggest_enr["UNITID"] = replacement_names

    # Rename columns so table names are intelligible
    biggest_enr = biggest_enr.rename(
        columns={"UNITID": "Name", "ENRTOT": "Total Enrollment", "EFUG": "Full Time Undergraduate Enrollment",
                 "EFGRAD": "Full Time Graduate Enrollment"})

    # Descriptive header and table
    st.markdown("#### 7 Largest Schools In Selected Area(s)")
    st.table(biggest_enr)

    # Enrollment over time line graph
    st.markdown("#### Student Enrollment Over Time In Selected Area(s)")

    # Prepate enrollment data
    enr_over_time = dynamic_filtered[["UNITID", "ENRTOT", "EFUG", "EFGRAD", "year"]].drop_duplicates(
        subset=["UNITID", "year"])
    enr_over_time = enr_over_time.groupby("year")["ENRTOT", "EFUG", "EFGRAD"].sum().reset_index()

    # Create and display line plot of total enrollment over time
    enrtot_line = px.line(enr_over_time, x="year", y="ENRTOT",
                          labels={"year": "Year", "ENRTOT": "Number of Students Enrolled"},
                          title="Total Enrollment Over Time", color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(enrtot_line, use_container_width=True)

    # Create columns
    col2a, col2b = st.columns(2)

    # Smaller graphs of full time undergrad and grad enrollment over time
    efug_line = px.line(enr_over_time, x="year", y="EFUG",
                        labels={"year": "Year", "EFUG": "Number of Full Time Undergraduate Students Enrolled"},
                        title="Full Time Undergraduate Enrollment Over Time",
                        color_discrete_sequence=px.colors.qualitative.Prism)
    col2b.plotly_chart(efug_line, use_container_width=True)

    efgrad_line = px.line(enr_over_time, x="year", y="EFGRAD",
                          labels={"year": "Year", "EFGRAD": "Number of Full Time Graduate Students Enrolled"},
                          title="Full Time Graduate Enrollment Over Time",
                          color_discrete_sequence=px.colors.qualitative.Prism)
    col2a.plotly_chart(efgrad_line, use_container_width=True)

    # Section to show cost of attendance over time
    # Prepare data
    dynamic_unagg = dynamic_filtered.drop_duplicates(subset=["UNITID", "year"])

    cost = dynamic_unagg[["TUFEYR3", "CINSON", "COTSON", "CINSOFF", "COTSOFF", "CINSFAM", "COTSFAM", "year"]]
    cost = cost.groupby("year")[
        "TUFEYR3", "CINSON", "COTSON", "CINSOFF", "COTSOFF", "CINSFAM", "COTSFAM"].mean().reset_index()
    cost = cost.melt(id_vars=['year'],
                     value_vars=["TUFEYR3", "CINSON", "COTSON", "CINSOFF", "COTSOFF", "CINSFAM", "COTSFAM"])
    cost["variable"] = cost["variable"].replace(
        {"TUFEYR3": "Tuition + Fees Only", "CINSON": "In State, On Campus COA", "COTSON": "Out of State, On Campus COA",
         "CINSOFF": "In State, Off Campus COA", "COTSOFF": "Out of State, Off Campus COA",
         "CINSFAM": "In State, With Family COA", "COTSFAM": "Out of State, With Family"})

    # Header, create and display line graph of cost of attendance over time
    st.markdown("#### Cost of Attendance Over Time")
    cost_line = px.line(cost, x="year", y="value", color="variable",
                        color_discrete_sequence=px.colors.qualitative.Prism,
                        labels={"year": "Year", "value": "Average Cost (in dollars)", "variable": ""})
    st.plotly_chart(cost_line, use_container_width=True)

    # Prepare data for showing enrollment in online courses over time
    online = dynamic_unagg[["ENRTOT", "PCTDEEXC", "PCTDESOM", "year"]]

    online["Some Online Classes"] = (online["ENRTOT"] * (online["PCTDESOM"] / 100)).astype(int)
    online["Fully Online Classes"] = (online["ENRTOT"] * (online["PCTDEEXC"] / 100)).astype(int)
    online = online.groupby("year")["ENRTOT", "Some Online Classes", "Fully Online Classes"].sum().reset_index()
    online["Percent Enrolled in Some Online Courses"] = online["Some Online Classes"] / online["ENRTOT"]
    online["Percent Enrolled in Fully Online Courses"] = online["Fully Online Classes"] / online["ENRTOT"]

    # Dataframe for online enrollment counts
    online_count = online[["year", "Some Online Classes", "Fully Online Classes"]]
    online_count = online_count.melt(id_vars=['year'], value_vars=["Some Online Classes", "Fully Online Classes"])

    # Dataframe for online enrollment as a percentage of total enrollment
    online_percent = online[
        ["year", "Percent Enrolled in Some Online Courses", "Percent Enrolled in Fully Online Courses"]]
    online_percent = online_percent.melt(id_vars=['year'], value_vars=["Percent Enrolled in Some Online Courses",
                                                                       "Percent Enrolled in Fully Online Courses"])

    # Display header, configure columns
    st.markdown("#### Online Course Enrollment Over Time")
    col3a, col3b = st.columns(2)

    # Create and display count and percentage graphs
    online_count_line = px.line(online_count, x="year", y="value", color="variable",
                                title="Students in Online Courses (As Count)",
                                labels={"year": "Year", "variable": "", "value": "Number of Students"},
                                color_discrete_sequence=px.colors.qualitative.Prism)
    col3a.plotly_chart(online_count_line, use_container_width=True)

    online_percent_line = px.line(online_percent, x="year", y="value", color="variable",
                                  title="Students in Online Courses (As Persentage of Total Enrollment)",
                                  labels={"year": "Year", "variable": "",
                                          "value": "Percent of Total Students Enrolled"},
                                  color_discrete_sequence=px.colors.qualitative.Prism)
    col3b.plotly_chart(online_percent_line, use_container_width=True)

    # Majors section
    st.write("***")
    st.markdown("### Majors")

    # Map cipcode numbers to intelligible category and degree names
    majors_aggregate = degrees
    cipcodes_pre = majors_aggregate["CIPCODE"].tolist()
    cipcodes_post = []
    for cipcode in cipcodes_pre:
        temp = decode.truncate(cipcode, 2)
        temp = decode.all_cipcodes.get(temp)
        cipcodes_post.append(temp)

    majors_aggregate["major_name"] = cipcodes_post

    # Separate categories from specific degrees so aggregations aren't double counting
    school_majors_categories = majors_aggregate.query("CIPCODE == degree_category")
    school_majors_specific = majors_aggregate.query("CIPCODE != degree_category")

    # Year selection slider
    year = st.slider("Slide to change year", min_value=2011, max_value=2020, value=2020, key='majors')

    # Get dataset with top undergraduate majors
    ug_majors_specific = school_majors_specific[school_majors_specific["AWLEVEL"] <= 5]
    ug_majors_specific = ug_majors_specific[ug_majors_specific["year"] == year]
    ug_majors_specific = ug_majors_specific.groupby(["major_name"])["CTOTALT"].sum().reset_index()

    number_degrees_awarded = ug_majors_specific["CTOTALT"].sum()
    ug_majors_specific["pct_all_majors_awarded"] = ug_majors_specific["CTOTALT"] / number_degrees_awarded
    top_ug_majors_specific = ug_majors_specific.sort_values(by="CTOTALT", ascending=False)
    top_ug_majors_specific.index = np.arange(1, len(top_ug_majors_specific) + 1)

    # Get dataset with top undergraduate categories
    ug_majors_categories = school_majors_categories[school_majors_categories["AWLEVEL"] <= 5]
    ug_majors_categories = ug_majors_categories[ug_majors_categories["year"] == year]
    top_ug_categories = ug_majors_categories.groupby('major_name')["CTOTALT"].sum().reset_index().sort_values(
        by="CTOTALT", ascending=False)
    top_ug_categories.index = np.arange(1, len(top_ug_categories) + 1)

    # Display top undergraduate categories table and pie chart
    st.markdown(f"#### Top 25 Undergraduate Majors in {year} By Category")
    d1, d2 = st.columns([1, 2])

    top_ug_categories = top_ug_categories.rename(columns={"major_name": "Category Name", "CTOTALT": "Number Earned"})
    d1.table(top_ug_categories[:25])

    fig2 = px.pie(top_ug_categories[:25], values="Number Earned", names="Category Name",
                  color_discrete_sequence=px.colors.qualitative.Prism)
    fig2.update_layout(legend=dict(xanchor="center", yanchor="top", x=0.6, y=-0.1), width=900, height=900)
    d2.plotly_chart(fig2, use_container_width=True)

    # Display top 50 undergraduate majors
    st.markdown(f"#### {year} Top 50 Undergraduate Majors")
    reversed_ug_majors_specific = top_ug_majors_specific[:50].sort_values(by="CTOTALT", ascending=True)

    fig1 = px.bar(reversed_ug_majors_specific, y="major_name", x='CTOTALT',
                  color_discrete_sequence=px.colors.qualitative.Prism,
                  labels={"major_name": "Major", "CTOTALT": "Number Earned"})
    fig1.update_layout(height=900)
    st.plotly_chart(fig1, use_container_width=True)

    # Get dataset with top specific graduate majors
    grad_majors_specific = school_majors_specific[school_majors_specific["AWLEVEL"] > 5]
    grad_majors_specific = grad_majors_specific[grad_majors_specific["year"] == year]
    grad_majors_specific = grad_majors_specific.groupby(["major_name"])["CTOTALT"].sum().reset_index()
    top_grad_majors_specific = grad_majors_specific.sort_values(by="CTOTALT", ascending=False)
    top_grad_majors_specific.index = np.arange(1, len(top_grad_majors_specific) + 1)

    # Get dataset with top graduate major cateogries
    grad_majors_categories = school_majors_categories[school_majors_categories["AWLEVEL"] > 7]
    top_grad_majors_categories = grad_majors_categories[grad_majors_categories["year"] == year].sort_values(
        by="CTOTALT", ascending=False)
    top_grad_categories = top_grad_majors_categories.groupby('major_name')["CTOTALT"].sum().reset_index().sort_values(
        by="CTOTALT", ascending=False)
    top_grad_categories.index = np.arange(1, len(top_grad_categories) + 1)

    # Display top 25 graduate major categories table and pie chart
    st.markdown(f"#### Top 25 Graduate Majors in {year} By Category")
    e1, e2 = st.columns([1, 2])

    top_grad_categories = top_grad_categories.rename(
        columns={"major_name": "Category Name", "CTOTALT": "Number Earned"})
    e1.table(top_grad_categories[:25])

    fig3 = px.pie(top_grad_categories[:25], values="Number Earned", names="Category Name",
                  color_discrete_sequence=px.colors.qualitative.Prism)
    fig3.update_layout(legend=dict(xanchor="center", yanchor="top", x=0.54, y=-0.1), width=1000, height=1000)
    fig3.update_traces(textposition='inside')
    fig3.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    e2.plotly_chart(fig3, use_container_width=True)

    # Display top 50 graduate majors as bar chart
    st.markdown(f"### {year} Top 50 Graduate Majors")
    reversed_grad_majors_specific = top_grad_majors_specific[:50].sort_values(by="CTOTALT", ascending=True)

    fig4 = px.bar(reversed_grad_majors_specific, y="major_name", x='CTOTALT',
                  color_discrete_sequence=px.colors.qualitative.Prism,
                  labels={"major_name": "Major", "CTOTALT": "Number Earned"})
    fig4.update_layout(height=900)
    st.plotly_chart(fig4, use_container_width=True)

    # Select major, see its popularity over time
    st.markdown(f"#### Major Popularity Over Time")

    # Filters
    level = st.radio("Student Level", ["All", "Undergraduate", "Graduate"], horizontal=True)
    type = st.radio("Aggregate By", ["Majors", "Categories"], horizontal=True)

    # Prepare dataframe with options for multiself which follows based on above filter selctions
    if level == "All" and type == "Categories":
        df = school_majors_categories
    elif level == "Undergraduate" and type == "Categories":
        df = school_majors_categories[school_majors_categories["AWLEVEL"] <= 5]
    elif level == "Graduate" and type == "Categories":
        df = school_majors_categories[school_majors_categories["AWLEVEL"] > 5]
    elif level == "All" and type == "Majors":
        df = school_majors_specific
    elif level == "Undergraduate" and type == "Majors":
        df = school_majors_specific[school_majors_specific["AWLEVEL"] <= 5]
    elif level == "Graduate" and type == "Majors":
        df = school_majors_specific[school_majors_specific["AWLEVEL"] > 5]

    # Format major_name columns as string
    df["major_name"] = df["major_name"].str.title()

    # Select majors
    selected_majors = st.multiselect(
        f'Select {type}:',
        df["major_name"].unique().tolist(),
        default=[]
    )

    # Prepare dataframe based on selections
    df = df.groupby(["major_name", "year"])["CTOTALT"].sum().reset_index()
    df = df[df["major_name"].isin(selected_majors)]

    # Dynamically change labels on the graph based on selections
    if type == "Majors":
        key_label = "Major"
    elif type == "Categories":
        key_label = "Category"

    if level == "Undergraduate":
        title_level = "Undergraduate"
    elif level == "Graduate":
        title_level = "Graduate"
    else:
        title_level = ""

    # Create and display line graph of major/category completions over time
    fig = px.line(df, x='year', y='CTOTALT', color='major_name',
                  labels={"year": "Year", "major_name": key_label, "CTOTALT": "Number of Degrees Completed"},
                  title=f"{title_level} Completions By Major Over Time")
    st.plotly_chart(fig, use_container_width=True)
