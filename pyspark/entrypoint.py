import sys
from datetime import date

from jobs.extreme_weather import ExtremeWeather

from pyspark.sql import SparkSession

if __name__ == "__main__":
    """
    Usage: extreme-weather [year]
    Displays extreme weather stats (highest temperature, wind, precipitation) for the given, or latest, year.
    """
    spark = SparkSession.builder.appName("ExtremeWeather").getOrCreate()

    if len(sys.argv) > 1 and sys.argv[1].isnumeric():
        year = sys.argv[1]
    else:
        year = date.today().year

    df = spark.read.csv(f"s3://noaa-gsod-pds/{year}/", header=True, inferSchema=True)
    print(f"The amount of weather readings in {year} is: {df.count()}\n")

    print(f"Here are some extreme weather stats for {year}:")
    stats_to_gather = [
        {"description": "Highest temperature", "column_name": "MAX", "units": "°F"},
        {"description": "Highest all-day average temperature", "column_name": "TEMP", "units": "°F"},
        {"description": "Highest wind gust", "column_name": "GUST", "units": "mph"},
        {"description": "Highest average wind speed", "column_name": "WDSP", "units": "mph"},
        {"description": "Highest precipitation", "column_name": "PRCP", "units": "inches"},
    ]

    ew = ExtremeWeather()
    for stat in stats_to_gather:
        max_row = ew.findLargest(df, stat["column_name"])
        print(
            f"  {stat['description']}: {max_row[stat['column_name']]}{stat['units']} on {max_row.DATE} at {max_row.NAME} ({max_row.LATITUDE}, {max_row.LONGITUDE})"
        )
