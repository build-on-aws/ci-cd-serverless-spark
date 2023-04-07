import pytest
from pyspark.sql import SparkSession, SQLContext

@pytest.fixture(scope="session")
def mock_views_df():
  spark = (
        SparkSession.builder.master("local[*]")
        .appName("tests")
        .config("spark.ui.enabled", False)
        .getOrCreate()
    )
  return spark.createDataFrame(
    [
      ("72793524234","2023-01-01",47.54554,-122.31475,7.6,"SEATTLE BOEING FIELD, WA US",44.1,24,42.7,24,1017.8,16,017.4,24,8.1,24,1.4,24,6.0,999.9,48.9,"",39.9,"",0.01,"G",999.9,"010000"),
      ("72793524234","2023-01-02",47.54554,-122.31475,7.6,"SEATTLE BOEING FIELD, WA US",37.8,24,34.0,24,1010.1,16,010.2,24,5.2,24,2.5,24,13.0,999.9,50.0,"",30.0,"",0.01,"G",999.9,"100000"),
      ("72793524234","2023-01-03",47.54554,-122.31475,7.6,"SEATTLE BOEING FIELD, WA US",41.0,24,30.5,24,1008.7,22,007.8,24,10.0,24,4.5,24,11.1,999.9,50.0,"",30.0,"",0.00,"G",999.9,"010000"),
      ("72793524234","2023-01-04",47.54554,-122.31475,7.6,"SEATTLE BOEING FIELD, WA US",42.6,24,30.3,24,1010.6,24,009.7,24,10.0,24,2.3,24,14.0, 21.0,51.1,"",35.1,"",0.00,"G",999.9,"000000"),
        ],
    ["STATION","DATE","LATITUDE","LONGITUDE","ELEVATION","NAME","TEMP","TEMP_ATTRIBUTES","DEWP","DEWP_ATTRIBUTES","SLP","SLP_ATTRIBUTES","STP","STP_ATTRIBUTES","VISIB","VISIB_ATTRIBUTES","WDSP","WDSP_ATTRIBUTES","MXSPD","GUST","MAX","MAX_ATTRIBUTES","MIN","MIN_ATTRIBUTES","PRCP","PRCP_ATTRIBUTES","SNDP","FRSHTT"]
  )
