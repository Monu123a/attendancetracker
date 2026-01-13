import time

def get_timestamp():
    return  int(time.time())

def format_date(dt):
    return  dt.strftime('%Y-%m-%d')

def parse_date(date_str):
    from datetime import datetime
    return  datetime.strptime(date_str, '%Y-%m-%d')

def sanitize_string(s):
    return  s.strip().lower()

def build_response(data):
    return  {'payload': data}
