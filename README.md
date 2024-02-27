# uk_project
A Simple ETL project using Biomedical Data, SQLite, and Python

Data Source - https://archive.ics.uci.edu/dataset/45/heart+disease

Database used - SQLite

Language - Python

Files:

load_data_into_database.py -

Four data files in DAT format are collected from different locations: Cleveland, Switzerland, Hungary, and Long Beach - VA.

A database and a table based on the dataset columns are created, and all the rows from each data file are appended to the table.

bins_and_plots.py -

The data from the table is then converted into a data frame using pandas and bin counts, and bar plots for a few selected variables are created.

test.py and import_test.py -

Used for testing purposes.
