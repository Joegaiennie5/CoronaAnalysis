# CoronaAnalysis
2020 US Corona Data Pipeline

The goal of this project was to create a Data Pipeline using the John Hopkins COVID data found on github : https://github.com/CSSEGISandData/COVID-19.
This project currently consist of a Python script which pulls data from this github repository (https://github.com/CSSEGISandData/COVID-19), 
cleanses & graphs the data, and then inserts the data into a SQL Server database hosted on AWS RDS. I have scheduled the script to run daily using a windows batch file, 
so I no longer need to run the script manually.

Next steps for this project will include predictive analytics and using PowerBI to create interactive visualizations of the data.
