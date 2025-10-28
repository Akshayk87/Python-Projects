
from flask import Flask, render_template
import pandas as pd
import regex as re

app = Flask("__name__")

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STAID','STANAME                                 ']]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    print(f"Station: {station}, Date: {date}")
    filename = "data_small\\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Date should be in the format YYYY-MM-DD
    temperature  = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10.0
    print(temperature)
    return { "station": station, "date": date, "temperature": temperature }

@app.route("/api/v1/<station>")
def all_data(station):
    print(f"Station: {station}")
    filename = "data_small\\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["   TG"] = df["   TG"] / 10.0
    data = df[["    DATE", "   TG"]].to_dict(orient="records")
    return { "station": station, "data": data }

@app.route("/api/v1/<station>/<year>")
def yearly_data(station, year):
    print(f"Station: {station}, Year: {year}")
    filename = "data_small\\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    data = df[df["    DATE"].dt.year == int(year)]
    #df["    Date"] = df["    DATE"].astype(str)
    #data = df[df["    DATE"].str.startswith(str(year))]  ")]
    #print(data)
    return { "station": station, "year": year, "data": data.to_dict(orient="records") }




if __name__ == "__main__":
    app.run(debug=True, port = 5001)