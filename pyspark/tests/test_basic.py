def test_is_this_on():
    assert 1 == 1

from jobs.extreme_weather import ExtremeWeather
def test_extract_latest_daily_value(mock_views_df):
    ew = ExtremeWeather()
    assert ew.findLargest(mock_views_df, "TEMP").TEMP == 44.1
