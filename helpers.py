from datetime import datetime as dt

#--------------Define some helper functions for next code block--------------
def clear_time(date_: dt) -> dt:
  return date_.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

# NOTE: datetime.datetime.fromisoformat or datetime.date.fromisoformat is better
def to_time(date_string: str) -> dt:
  '''Turns a str in desired format to datetime.datetime'''
  return clear_time(dt.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z"))