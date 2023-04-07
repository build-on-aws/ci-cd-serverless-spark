from jobs.extreme_weather import ExtremeWeather

from pyspark.sql import SparkSession

if __name__ == "__main__":
    """
    Usage: integration_test
    Validation job to ensure everything is working well
    """
    spark = (
        SparkSession.builder.appName("integration-ExtremeWeather")
        .getOrCreate()
    )
    df = spark.read.csv("s3://noaa-gsod-pds/2022/72793524234.csv", header=True, inferSchema=True)
    assert df.count()==365, f"expected 365 records, got: {count}. failing job."

    ew = ExtremeWeather()
    max_temp = ew.findLargest(df, 'TEMP').TEMP
    max_wind_speed = ew.findLargest(df, 'MXSPD').MXSPD
    max_wind_gust = ew.findLargest(df, 'GUST').GUST
    max_precip = ew.findLargest(df, 'PRCP').PRCP
    assert max_temp == 78.7, f"expected max temp of 78.7, got: {max_temp}. failing job."
    assert max_wind_speed == 19.0, f"expected max wind speed of 19.0, got: {max_wind_speed}. failing job."
    assert max_wind_gust == 36.9, f"expected max wind gust of 36.9, got: {max_wind_gust}. failing job."
    assert max_precip == 1.55, f"expected max precip of 1.55, got: {max_precip}. failing job."
