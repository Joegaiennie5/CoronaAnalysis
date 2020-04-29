{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import all libraries\n",
    "import pandas as pd\n",
    "from datetime import datetime,timedelta,date\n",
    "import time\n",
    "import urllib\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pyodbc \n",
    "from decimal import Decimal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use read_CSV() to extract data from John Hopkins GITHUB\n",
    "today = date.today()\n",
    "yesterday = today - timedelta(days=1)\n",
    "date_Converted = yesterday.strftime(\"%m-%d-%Y\")\n",
    "try:\n",
    "    url = \"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/\" + date_Converted + \".csv\"\n",
    "    df = pd.read_csv(url)\n",
    "except urllib.error.HTTPError:\n",
    "    f = open(\"C:\\\\Users\\\\JosephGaiennie\\\\Desktop\\\\Python\\\\Corona_Logs.txt\", \"a\")\n",
    "    f.write(str(time.time()) +  \" \" + \"HTTPError\")\n",
    "    f.close()\n",
    "df = df.fillna(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Graph confirmed cases against each State and Save the immage\n",
    "df.plot(kind='bar',x='Province_State',y='Confirmed')\n",
    "fig = plt.gcf()\n",
    "fig.set_size_inches(20, 10.5)\n",
    "plt.xticks(fontsize=14)\n",
    "y = [min(df[\"Confirmed\"]),max(df[\"Confirmed\"])]\n",
    "plt.yticks(np.arange(y[0], y[1], 10000))\n",
    "plt.savefig(\"C:\\\\Users\\\\JosephGaiennie\\\\Desktop\\\\Python\\\\CoronaVirusPics\\\\USCoronaVirus\" + date_Converted + \".png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use pyodbc library to make a connection to sql server database hosted on AWS using RDS\n",
    "server = 'practicedatabase.c8pv3jjiflii.us-east-2.rds.amazonaws.com' \n",
    "database = 'CoronaDB' \n",
    "#username = '' Hidden\n",
    "#password = '' Hidden\n",
    "conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)\n",
    "cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'\n",
    "#                      'Server=LAPTOP-D3KCPF8R;'\n",
    "#                      'Database=Practice_DB;'\n",
    "#                      'Trusted_Connection=yes;')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for index, row in df.iterrows():\n",
    "    cursor.execute(\n",
    "        \"\"\"INSERT INTO [dbo].[COVID19_Analysis] ([State]\n",
    "           ,[Date]\n",
    "           ,[Deaths]\n",
    "           ,[Recovered]\n",
    "           ,[Incident_Rate]\n",
    "           ,[People_Tested]\n",
    "           ,[People_Hospitilized]\n",
    "           ,[Moralitiy_Rate]\n",
    "           ,[Confirmed]) VALUES(?,?,?,?,?,?,?,?,?)\n",
    "           \"\"\",\n",
    "                   (row['Province_State'],date_Converted,row['Deaths'],row['Recovered'],(row['Incident_Rate']),row['People_Tested'],int(row['People_Hospitalized']),row['Mortality_Rate'],row['Confirmed']))\n",
    "    conn.commit()\n",
    "conn.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
