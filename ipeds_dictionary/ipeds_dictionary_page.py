import streamlit as st
import pandas as pd


def view_page():
    # Load data
    tables_df = pd.DataFrame(pd.read_csv("ipeds_dictionary/ipeds_tables20.csv"))
    variables_df = pd.DataFrame(pd.read_csv("ipeds_dictionary/ipeds_vartable20.csv"))

    # Prepare data downloads
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    download_tables = convert_df(tables_df)
    download_variables = convert_df(variables_df)

    # Title and header
    st.title("IPEDS Dictionary")
    st.header("Variable Lookup")

    # Subset dataframe to columns we want to show
    variables = variables_df[["varName", "varTitle", "longDescription", "varSource", "TableName", "TableTitle"]]

    # Set up columns--one one right bigger than one on left, small gap between them
    col1a, gap, col1b = st.columns([2,0.1,3])

    with col1a:
        # Radio buttons controlling field to be filtered
        variable_lookup_by = st.radio("Lookup By: ", ["View All", "Variable Name", "Variable Title", "Table Name"], key="variable_lookup_radio")

        # Disable all lookup fields other than the selected one
        if variable_lookup_by == "Variable Name":
            disable_abbr = False
            disable_name = True
            disable_tablename = True
        elif variable_lookup_by == "Variable Title":
            disable_abbr = True
            disable_name = False
            disable_tablename = True
        elif variable_lookup_by == "Table Name":
            disable_abbr = True
            disable_name = True
            disable_tablename = False
        else:
            disable_abbr = False
            disable_name = False
            disable_tablename = False

        # Select boxes with all options for each filter field
        variable_abbr = st.selectbox("Select Variable Name", variables["varName"].tolist(), disabled=disable_abbr)
        variable_name = st.selectbox("Select Variable Title", variables["varTitle"].unique().tolist(), disabled=disable_name)
        table_name = st.selectbox("Select Table Name", variables["TableName"].unique().tolist(), disabled=disable_tablename)

    with col1b:
        # Prepare dataframe based on filter selection
        if variable_lookup_by == "Variable Name":
            variables_filtered = variables[variables["varName"] == variable_abbr]
        elif variable_lookup_by == "Variable Title":
            variables_filtered = variables[variables["varTitle"] == variable_name]
        elif variable_lookup_by == "Table Name":
            variables_filtered = variables[variables["TableName"] == table_name]

        # Button to download all variable data
        st.download_button(
            label="Download Complete IPEDS Variable Documentation",
            data=download_variables,
            file_name='ipeds_variables.csv',
            mime='text/csv',
            key="download tables"
        )

        # Set up placeholder, fill with appropriate information based on filter selection
        placeholder1 = st.empty()
        if variable_lookup_by == "View All":
            placeholder1.empty()
            placeholder1.dataframe(variables)
        elif variable_lookup_by == "Table Name":
            placeholder1.empty()
            placeholder1.dataframe(variables_filtered)
        elif variable_lookup_by == "Variable Title":
            placeholder1.empty()
            placeholder1.table(variables_filtered)
        else:
            placeholder1.empty()
            with placeholder1.container():
                st.markdown(f'#### {variables_filtered["varName"].item()}')
                st.markdown(f'### {variables_filtered["varTitle"].item()}')
                st.markdown(f'**Description:** {variables_filtered["longDescription"].item()}')
                st.markdown(f'**Source:** {variables_filtered["varSource"].item()}')
                st.markdown(f'**Table Name:** {variables_filtered["TableName"].item()}')
                st.markdown(f'**Table Title:** {variables_filtered["TableTitle"].item()}')

    # Divide page, header for tables section
    st.write("***")
    st.header("Table Lookup")

    # Subset dataframe to contain only columns we want to show
    tables = tables_df[["TableName", "TableTitle", "Description", "Release date"]]

    # Configure columns
    col2a, gap2, col2b = st.columns([2,0.1,3])

    with col2a:
        # Radio buttons controlling field to be filtered
        table_lookup_by = st.radio("Lookup by: ", ["View All", "Title", "Name"], key="table_lookup_radio")

        # Disable all lookup fields other than the selected one
        if table_lookup_by == "Title":
            disable_abbr = True
            disable_title = False
        elif table_lookup_by == "Name":
            disable_title = True
            disable_abbr = False
        else:
            disable_title = False
            disable_abbr = False

        # Select boxes with all options for each filter field
        table_name = st.selectbox("Select Table Title", tables["TableTitle"].tolist(), disabled=disable_title)
        table_abbr = st.selectbox("Select Table Name", tables["TableName"].tolist(), disabled=disable_abbr)

    with col2b:
        # Prepare dataframe based on filter selection
        if table_lookup_by == "Title":
            tables_filtered = tables[tables["TableTitle"] == table_name]
        elif table_lookup_by == "Name":
            tables_filtered = tables[tables["TableName"] == table_abbr]

        # Button to download all variable data
        st.download_button(
            label="Download Complete IPEDS Tables Documentation",
            data=download_tables,
            file_name='ipeds_tables.csv',
            mime='text/csv',
            key='download tables'
        )

        # Set up placeholder, fill with appropriate information based on filter selection
        placeholder = st.empty()
        if table_lookup_by == "View All":
            placeholder.empty()
            placeholder.dataframe(tables)
        else:
            placeholder.empty()
            with placeholder.container():
                st.markdown(f'#### {tables_filtered["TableName"].item()}')
                st.markdown(f'### {tables_filtered["TableTitle"].item()}')
                st.markdown(f'**Description:** {tables_filtered["Description"].item()}')
                st.markdown(f'**Release Date:** {tables_filtered["Release date"].item()}')
