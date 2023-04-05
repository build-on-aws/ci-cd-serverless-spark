from pyspark.sql import DataFrame, Row
from pyspark.sql import functions as F

class ExtremeWeather:
  def findLargest(self, df: DataFrame, col_name: str) -> Row:
      """
      Find the largest value in `col_name` column.
      Values of 99.99, 999.9 and 9999.9 are excluded because they indicate "no reading" for that attribute.
      While 99.99 _could_ be a valid value for temperature, for example, we know there are higher readings.
      """
      return (
          df.select(
              "STATION", "DATE", "LATITUDE", "LONGITUDE", "ELEVATION", "NAME", col_name
          )
          .filter(~F.col(col_name).isin([99.99, 999.9, 9999.9]))
          .orderBy(F.desc(col_name))
          .limit(1)
          .first()
      )
