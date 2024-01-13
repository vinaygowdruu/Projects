import re
import pandas as pd

def preprocess(data):
    pattern = '(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s)'

    # Use re.findall to get both messages and dates
    matches = re.findall(pattern, data)

    # Separate messages and dates
    dates = matches[::2]
    messages = re.split(pattern, data)[1::2]

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')

    return df
