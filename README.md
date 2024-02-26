# uk_project
A Simple ETL project using Biomedical Data, SQLite and Python
Data Source - https://archive.ics.uci.edu/dataset/45/heart+disease

Database used - SQLite
Language - Python

Files:

load_data_into_database.py -

There are four data files in DAT format collected from different locations which are Cleveland, Switzerlands, Hungary, and Long Beach - VA.

A database and a table based on the dataset columns are created and all the rows from each data file are appened to the table.

bins_and_plots.py -

The data from the table is then converted into dataframe using pandas and bin counts as well as bar plots for each continuous variable are created.

test.py and import_test.py -

Used for testing purposes.
