import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import decode

# Load dataframes
static = pd.DataFrame(pd.read_csv("institutions/ipeds_static.csv"))
degrees = pd.DataFrame(pd.read_csv("institutions/degrees_institution.csv"))
dynamic = pd.DataFrame(pd.read_csv("institutions/ipeds_dynamic.csv"))

# Replace numbers in key fields with intelligible strings
stabbr_list = static["STABBR"].tolist()
replace_stabbr = []
for stabbr in stabbr_list:
    replace_stabbr.append(decode.states_reverse.get(stabbr))
static["STABBR"] = replace_stabbr

obereg_list = static["OBEREG"].tolist()
replace_obereg = []
for obereg in obereg_list:
    replace_obereg.append(decode.decode_obereg(obereg))
static["OBEREG"] = replace_obereg

level_list = static["ICLEVEL"].tolist()
replace_level = []
for level in level_list:
    replace_level.append(decode.decode_iclevel(level))
static["ICLEVEL"] = replace_level

control_list = static["CONTROL"].tolist()
replace_control = []
for control in control_list:
    replace_control.append(decode.decode_control(control))
static["CONTROL"] = replace_control
static = static[static["CONTROL"] != "Data Not Available"]

category_list = static["INSTCAT"].tolist()
replace_category = []
for category in category_list:
    replace_category.append(decode.decode_instcat(category))
static["INSTCAT"] = replace_category
static = static[static["INSTCAT"] != "Data not available"]

# Create subset of dynamic data for most recent year
recent_dynamic = dynamic[dynamic["year"] == 2020]


def view_page():
    # Encode dataframes as csv so they can be downloaded
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    # Page title and column configuration
    st.title("Specific Institutions Data")
    col0a, col0b = st.columns([2, 3])

    with col0a:
        with st.form("school_search"):
            # Form which allows users to select how they want to filter the data
            st.markdown("**Filter Schools**")
            state_select = st.multiselect("State", static["STABBR"].sort_values().unique().tolist(), default=[])
            region_select = st.multiselect("Region", static["OBEREG"].unique().tolist())
            level_select = st.multiselect("Level", static["ICLEVEL"].unique().tolist())
            control_select = st.multiselect("Control", static["CONTROL"].unique().tolist())
            category_select = st.multiselect("Category", static['INSTCAT'].unique().tolist())
            enrtot_range = st.slider("Total Enrollment", recent_dynamic["ENRTOT"].min().astype(int), recent_dynamic["ENRTOT"].max().astype(int),
                                     (recent_dynamic["ENRTOT"].min().astype(int), recent_dynamic["ENRTOT"].max().astype(int)))
            submitted = st.form_submit_button("Submit")

    with col0b:
        # Take form imput and filter data accordingly
        filtered_schools = static

        if bool(state_select):
            filtered_schools = filtered_schools[filtered_schools["STABBR"].isin(state_select)]
        if bool(region_select):
            filtered_schools = filtered_schools[filtered_schools["OBEREG"].isin(region_select)]
        if bool(level_select):
            filtered_schools = filtered_schools[filtered_schools["ICLEVEL"].isin(level_select)]
        if bool(control_select):
            filtered_schools = filtered_schools[filtered_schools["CONTROL"].isin(control_select)]
        if bool(category_select):
            filtered_schools = filtered_schools[filtered_schools["INSTCAT"].isin(category_select)]
        if bool(enrtot_range):
            enr_min = enrtot_range[0]
            enr_max = enrtot_range[1]
            cross_table = recent_dynamic[recent_dynamic["ENRTOT"] >= enr_min]
            cross_table = cross_table[recent_dynamic["ENRTOT"] <= enr_max]
            cross_table = cross_table["UNITID"].tolist()
            filtered_schools = filtered_schools[filtered_schools["UNITID"].isin(cross_table)]

        # Create and display map of schools in filtered dataset
        fig = go.Figure(data=go.Scattergeo(
            lon=filtered_schools['longitude'],
            lat=filtered_schools['latitude'],
            text=filtered_schools['INSTNM'],
            mode='markers'
        ))

        fig.update_layout(
            geo_scope='usa', height=600, margin={"r": 0, "t": 0, "l": 0, "b": 0}
        )
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(filtered_schools)

    # Button to download list of filtered schools
    csv = convert_df(filtered_schools)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='school_list.csv',
        mime='text/csv',
    )

    # School specific data section
    st.write("***")
    st.header("School-Specific Data")

    # Select a school, filter data accordingly
    selected_school = st.selectbox("Select a School: ", static["INSTNM"].unique().tolist())
    static_row = static[static["INSTNM"] == selected_school]
    unitid = static_row["UNITID"].item()

    # Display information about school from static table
    st.write("")
    st.markdown(f"# {static_row['INSTNM'].item()}")

    st.markdown("### Basic Info")
    gleft, col1, gap, col2, gright = st.columns([.1, 2, .1, 4, 4])

    col1.markdown(
        f"**Address**  \n{static_row['ADDR'].item()}  \n{static_row['CITY'].item()}, {static_row['STABBR'].item()} {static_row['ZIP'].item()}  \n{static_row['WEBADDR'].item()}  \n")
    col1.markdown(f"**Region:** {decode.decode_obereg(static_row['OBEREG'].item())}  \n")
    col2.markdown(
        f"**Control:** {decode.decode_control(static_row['CONTROL'].item())}  \n**ICLEVEL:** {decode.decode_iclevel(static_row['ICLEVEL'].item())}  \n")
    col2.markdown(
        f"**Offers Undergraduate Programs? :**  {decode.decode_binary(static_row['UGOFFER'].item())}  \n**Offers Graduate Programs? :**  {decode.decode_binary(static_row['GROFFER'].item())}  \n**Category:** {decode.decode_instcat(static_row['INSTCAT'].item())}  \n")
    gright.markdown(
        f"**HBCU? :**  {decode.decode_binary(static_row['HBCU'].item())}  \n**Landgrant Institution? :**  {decode.decode_binary(static_row['LANDGRNT'].item())}  \n**Tribal School? :**  {decode.decode_binary(static_row['TRIBAL'].item())}  \n**Has Medical Program? :**  {decode.decode_binary(static_row['MEDICAL'].item())}")

    st.write("")
    st.write("")

    leftgap, content = st.columns([.01, 10.1])
    content.markdown(f"**Enrollment Profile:**  \n{decode.decode_c18enprf(static_row['C18ENPRF'].item())}  \n")
    content.markdown(
        f"**Undergraduate Enrollment Profile:**  \n{decode.decode_c18ugprf(static_row['C18UGPRF'].item())}  \n")
    content.markdown(
        f"**Undergraduate Instructional Program:**  \n{decode.decode_c18ipug(static_row['C18IPUG'].item())}  \n")
    content.markdown(
        f"**Graduate Instructional Program:**  \n{decode.decode_c18ipgrd(static_row['C18IPGRD'].item())}  \n")

    st.markdown("\n")

    # Historical data section, prepare dynamic dataset
    st.markdown("### Historical Data")
    school_dynamic = dynamic[dynamic["UNITID"] == unitid]

    # Enrollment over time line graph
    st.markdown("#### Enrollment Over Time")
    enrollment_over_time = school_dynamic[["ENRTOT", "EFUG", "EFGRAD", "year"]].melt(id_vars=["year"],
                                                                                     value_vars=["ENRTOT", "EFUG",
                                                                                                 "EFGRAD"]).drop_duplicates()
    enrollment_over_time["variable"] = enrollment_over_time["variable"].replace(
        {"ENRTOT": "Total Enrollment", "EFUG": "Full Time Undergraduate Enrollment",
         "EFGRAD": "Full Time Graduate Enrollment"})
    enr_over_time_line = px.line(enrollment_over_time, x="year", y="value", color="variable",
                                 labels={"variable": "", "year": "Year", "value": "Number of Students"},
                                 title="Enrollment Over Time By Student Level")
    st.plotly_chart(enr_over_time_line, use_container_width=True)

    # Student demographics over time section
    st.markdown("#### Student Demographics Over Time")

    # Select year slider, filter data appropriately
    chosen_year = st.slider("Slide to change year", min_value=2012, max_value=2020, key='dynamic', value=2020)
    dynamic_year = school_dynamic[school_dynamic['year'] == chosen_year]

    # Prepare race data
    demographics = dynamic_year[
        ["ENRTOT", "PCTENRWH", "PCTENRBK", "PCTENRHS", "PCTENRAP", "PCTENRAS", "PCTENRNH", "PCTENRAN", "PCTENR2M",
         "PCTENRUN", "PCTENRNR", "PCTENRW"]]
    demographics["ENRWH"] = demographics["ENRTOT"] * (demographics["PCTENRWH"] / 100)
    demographics["ENRBK"] = demographics["ENRTOT"] * (demographics["PCTENRBK"] / 100)
    demographics["ENRHS"] = demographics["ENRTOT"] * (demographics["PCTENRHS"] / 100)
    demographics["ENRAP"] = demographics["ENRTOT"] * (demographics["PCTENRAP"] / 100)
    demographics["ENRAS"] = demographics["ENRTOT"] * (demographics["PCTENRAS"] / 100)
    demographics["ENRAN"] = demographics["ENRTOT"] * (demographics["PCTENRAN"] / 100)
    demographics["ENR2M"] = demographics["ENRTOT"] * (demographics["PCTENR2M"] / 100)
    demographics["ENRUN"] = demographics["ENRTOT"] * (demographics["PCTENRUN"] / 100)
    demographics["ENRNR"] = demographics["ENRTOT"] * (demographics["PCTENRNR"] / 100)
    demographics["ENRW"] = demographics["ENRTOT"] * (demographics["PCTENRW"] / 100)
    demographics["ENRM"] = demographics["ENRTOT"] * (1 - (demographics["PCTENRW"] / 100))

    # Prepare data for race pie chart
    race = demographics[["ENRWH", "ENRBK", "ENRHS", "ENRAP", "ENRAS", "ENRAN", "ENR2M", "ENRUN", "ENRNR"]][
           :1].transpose()
    race = race.rename(
        index={"ENRWH": "White", "ENRBK": "Black", "ENRHS": "Hispanic", "ENRAP": "Asian/P. Islander", "ENRAS": "Asian",
               "ENRAN": "Indian/Native", "ENR2M": "2 or More", "ENRUN": "Unknown", "ENRNR": "Not Reported"})
    race["race"] = list(race.index.values)
    race = race.rename(columns={race.columns[0]: "count"})

    # Prepare data for pie chart
    gender = demographics[["ENRW", "ENRM"]][:1].transpose()
    gender = gender.rename(index={"ENRM": "Male", "ENRW": "Female"})
    gender["gender"] = list(gender.index.values)
    gender = gender.rename(columns={gender.columns[0]: "count"})

    # Prepare data for level pie chart
    level = dynamic_year[["EFUG", "EFGRAD"]][:1].transpose()
    level = level.rename(index={"EFUG": "Undergraduate", "EFGRAD": "Graduate"})
    level["level"] = list(level.index.values)
    level = level.rename(columns={level.columns[0]: "count"})

    # Create and display demographic pie charts
    race_pie = px.pie(race, values="count", names="race", color_discrete_sequence=px.colors.qualitative.Prism,
                      title="Enrollment By Race", hole=0.4)
    gender_pie = px.pie(gender, values="count", names="gender", color_discrete_sequence=px.colors.qualitative.Prism,
                        title="Enrollment By Gender", hole=0.4)
    level_pie = px.pie(level, values="count", names="level", color_discrete_sequence=px.colors.qualitative.Prism,
                       title="Enrollment By Level", hole=0.4)

    a1, a2, a3 = st.columns(3)

    a1.plotly_chart(race_pie, use_container_width=True)
    a2.plotly_chart(gender_pie, use_container_width=True)
    a3.plotly_chart(level_pie, use_container_width=True)

    # Create and display cost of attendance line graph
    cost = school_dynamic[
        ["TUFEYR3", "CINSON", "COTSON", "CINSOFF", "COTSOFF", "CINSFAM", "COTSFAM", "year"]].drop_duplicates(
        "year").melt(id_vars=['year'],
                     value_vars=["TUFEYR3", "CINSON", "COTSON", "CINSOFF", "COTSOFF", "CINSFAM", "COTSFAM"])
    cost["variable"] = cost["variable"].replace(
        {"TUFEYR3": "Tuition + Fees Only", "CINSON": "In State, On Campus COA", "COTSON": "Out of State, On Campus COA",
         "CINSOFF": "In State, Off Campus COA", "COTSOFF": "Out of State, Off Campus COA",
         "CINSFAM": "In State, With Family COA", "COTSFAM": "Out of State, With Family"})

    st.markdown("#### Cost of Attendance Over Time")

    cost_line = px.line(cost, x="year", y="value", color="variable",
                        color_discrete_sequence=px.colors.qualitative.Prism,
                        labels={"year": "Year", "value": "Average Cost (in dollars)", "variable": ""},
                        title="Tuition + Fees and Cost of Attendance for Different Student Groups")
    st.plotly_chart(cost_line, use_container_width=True)

    # Create and display online course enrollment line graph
    online = school_dynamic[
        ["PCTDEEXC", "PCTDESOM", "PCUDEEXC", "PCUDESOM", "PCGDEEXC", "PCGDESOM", "year"]].drop_duplicates("year").melt(
        id_vars=['year'], value_vars=["PCTDEEXC", "PCTDESOM", "PCUDEEXC", "PCUDESOM", "PCGDEEXC", "PCGDESOM"])
    online["variable"] = online["variable"].replace(
        {"PCTDEEXC": "All Students, Fully Online", "PCTDESOM": "All Students, Some Online",
         "PCUDEEXC": "Undergraduate, Fully Online", "PCUDESOM": "Undergraduate, Some Online",
         "PCGDEEXC": "Graduate, Fully Online", "PCGDESOM": "Graduate, Some Online"})

    st.markdown("#### Online Enrollment Over Time")

    online_line = px.line(online, x="year", y="value", color="variable",
                          color_discrete_sequence=px.colors.qualitative.Prism,
                          labels={"year": "Year", "value": "Average Cost (in dollars)", "variable": ""},
                          title="Percent Enrolled In Online Courses By Student Level")
    st.plotly_chart(online_line, use_container_width=True)

    # Majors section
    st.markdown("### Majors")

    # Decode cipcodes
    school_majors = degrees[degrees["UNITID"] == unitid]
    cipcodes_pre = school_majors["CIPCODE"].tolist()
    cipcodes_post = []
    for cipcode in cipcodes_pre:
        temp = decode.truncate(cipcode, 2)
        temp = decode.all_cipcodes.get(temp)
        cipcodes_post.append(temp)
    school_majors["major_name"] = cipcodes_post

    # Separate data into specific majors and categories so completions counts aren't double counted
    school_majors_categories = school_majors.query("CIPCODE == degree_category")
    school_majors_specific = school_majors.query("CIPCODE != degree_category")

    # Year selection slider
    year = st.slider("Slide to change year", min_value=2011, max_value=2020, value=2020, key='majors')

    # Create dataframe of top undergraduate majors
    ug_majors_specific = school_majors_specific[school_majors_specific["AWLEVEL"] <= 5]
    ug_majors_specific = ug_majors_specific[ug_majors_specific["year"] == year]
    ug_majors_specific = ug_majors_specific.groupby(["major_name"])["CTOTALT"].sum().reset_index()

    number_degrees_awarded = ug_majors_specific["CTOTALT"].sum()
    ug_majors_specific["pct_all_majors_awarded"] = ug_majors_specific["CTOTALT"] / number_degrees_awarded
    top_ug_majors_specific = ug_majors_specific.sort_values(by="CTOTALT", ascending=False)
    top_ug_majors_specific.index = np.arange(1, len(top_ug_majors_specific) + 1)

    # Create dataframe of top undergraduate major categories
    ug_majors_categories = school_majors_categories[school_majors_categories["AWLEVEL"] <= 5]
    ug_majors_categories = ug_majors_categories[ug_majors_categories["year"] == year]
    top_ug_categories = ug_majors_categories.groupby('major_name')["CTOTALT"].sum().reset_index().sort_values(
        by="CTOTALT", ascending=False)
    top_ug_categories.index = np.arange(1, len(top_ug_categories) + 1)

    # Display table and pie chart of top undergraduate categories
    st.markdown(f"#### Undergraduate Degrees Awarded in {year} By Category")
    d1, d2 = st.columns([1, 2])

    top_ug_categories = top_ug_categories.rename(columns={"major_name": "Category Name", "CTOTALT": "Number Earned"})
    d1.table(top_ug_categories)

    fig2 = px.pie(top_ug_categories, values="Number Earned", names="Category Name",
                  color_discrete_sequence=px.colors.qualitative.Prism)
    fig2.update_layout(legend=dict(xanchor="center", yanchor="top", x=0.6, y=-0.1), width=900, height=900)
    d2.plotly_chart(fig2, use_container_width=True)

    # Create and display bar graph of all undergraduate majors
    st.markdown(f"#### Complete {year} Undergraduate Major Breakdown")
    reversed_ug_majors_specific = top_ug_majors_specific.sort_values(by="CTOTALT", ascending=True)

    fig1 = px.bar(reversed_ug_majors_specific, y="major_name", x='CTOTALT',
                  color_discrete_sequence=px.colors.qualitative.Prism,
                  labels={"major_name": "Major", "CTOTALT": "Number Earned"})
    fig1.update_layout(height=800)
    st.plotly_chart(fig1, use_container_width=True)

    # Create dataframe for top specific graduate majors
    grad_majors_specific = school_majors_specific[school_majors_specific["AWLEVEL"] > 5]
    grad_majors_specific = grad_majors_specific[grad_majors_specific["year"] == year]
    grad_majors_specific = grad_majors_specific.groupby(["major_name"])["CTOTALT"].sum().reset_index()
    top_grad_majors_specific = grad_majors_specific.sort_values(by="CTOTALT", ascending=False)
    top_grad_majors_specific.index = np.arange(1, len(top_grad_majors_specific) + 1)

    # Create dataframe for top graduate major categories
    grad_majors_categories = school_majors_categories[school_majors_categories["AWLEVEL"] > 7]
    top_grad_majors_categories = grad_majors_categories[grad_majors_categories["year"] == year].sort_values(
        by="CTOTALT", ascending=False)
    top_grad_categories = top_grad_majors_categories.groupby('major_name')["CTOTALT"].sum().reset_index().sort_values(
        by="CTOTALT", ascending=False)
    top_grad_categories.index = np.arange(1, len(top_grad_categories) + 1)

    # Display top graduate major categories table and pie chart
    st.markdown(f"#### Graduate Degrees Awarded in {year} By Category")
    e1, e2 = st.columns([1, 2])

    top_grad_categories = top_grad_categories.rename(
        columns={"major_name": "Category Name", "CTOTALT": "Number Earned"})
    e1.table(top_grad_categories)

    fig3 = px.pie(top_grad_categories, values="Number Earned", names="Category Name",
                  color_discrete_sequence=px.colors.qualitative.Prism)
    fig3.update_layout(legend=dict(xanchor="center", yanchor="top", x=0.54, y=-0.1), width=1000, height=1000)
    fig3.update_traces(textposition='inside')
    fig3.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    e2.plotly_chart(fig3, use_container_width=True)

    # Display top specific graduate major bar chart
    st.markdown(f"### Complete {year} Graduate Major Breakdown")
    reversed_grad_majors_specific = top_grad_majors_specific.sort_values(by="CTOTALT", ascending=True)

    fig4 = px.bar(reversed_grad_majors_specific, y="major_name", x='CTOTALT',
                  color_discrete_sequence=px.colors.qualitative.Prism,
                  labels={"major_name": "Major", "CTOTALT": "Number Earned"})
    fig4.update_layout(height=800)
    st.plotly_chart(fig4, use_container_width=True)

    # Select major, see its popularity over time
    st.markdown(f"#### Major Popularity Over Time")

    # Filters
    level = st.radio("Student Level", ["All", "Undergraduate", "Graduate"], horizontal=True)
    type = st.radio("Aggregate By", ["Majors", "Categories"], horizontal=True)

    # Create dataframe based on filters so following filters will only include values in data
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

    # Convert major_name column from unspecified object to string
    df["major_name"] = df["major_name"].str.title()

    # Select majors
    selected_majors = st.multiselect(
        f'Select {type}:',
        df["major_name"].unique().tolist(),
    )

    # Prepare data based on selections
    df = df.groupby(["major_name", "year"])["CTOTALT"].sum().reset_index()
    df = df[df["major_name"].isin(selected_majors)]

    # Dynamically assign graph labels based on selections
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

    # Display graph of major completions count over time
    fig = px.line(df, x='year', y='CTOTALT', color='major_name',
                  labels={"year": "Year", "major_name": key_label, "CTOTALT": "Number of Degrees Completed"},
                  title=f"{title_level} Completions By Major Over Time")
    st.plotly_chart(fig, use_container_width=True)
