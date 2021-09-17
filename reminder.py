import os
from twilio.rest import Client
import pandas as pd
import numpy as np
import datetime as dt
from functools import reduce

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

today=dt.datetime.today()
tdm=today.strftime("%d")+'-'+today.strftime("%m")
tomorrow=today +dt.timedelta(days=1)
tmdm=tomorrow.strftime("%d")+'-'+tomorrow.strftime("%m")

age_df = pd.read_csv("age.csv")

today_b_matched=age_df[age_df['DOB'].str.contains(tdm, na=False)]
tomorrow_b_matched=age_df[age_df['DOB'].str.contains(tmdm, na=False)]

today_a_matched=age_df[age_df['Marriage'].str.contains(tdm, na=False)]
tomorrow_a_matched=age_df[age_df['Marriage'].str.contains(tmdm, na=False)]

today_b_name = reduce(lambda n1, n2: n1+' '+n2, today_b_matched['Name'], '').strip().replace(" ", ", ")
tomorrow_b_name = reduce(lambda n1, n2: n1+' '+n2, tomorrow_b_matched['Name'], '').strip().replace(" ", ", ")

today_a_name = reduce(lambda n1, n2: n1+' '+n2, today_a_matched['Name'], '').strip().replace(" ", ", ")
tomorrow_a_name = reduce(lambda n1, n2: n1+' '+n2, tomorrow_a_matched['Name'], '').strip().replace(" ", ", ")


if not(tomorrow_b_name==''):
    message = client.messages \
                .create(
                     body='Tomorrow is '+ tomorrow_b_name+' birthday',
                     from_='+14784491207',
                     to='+919960713863'
                 )
    
if not(today_b_name==''):
    message = client.messages \
                .create(
                     body='Today is '+ today_b_name +' birthday',
                     from_='+14784491207',
                     to='+919960713863'
                 )

                 if not(tomorrow_a_name==''):
        message = client.messages \
                .create(
                     body='Tomorrow is '+ tomorrow_a_name+' Wedding Anniversary',
                     from_='+14784491207',
                     to='+919960713863'
                 )
        
if not(today_a_name==''):
        message = client.messages \
                .create(
                     body='Today is '+ today_a_name+' Wedding Anniversary',
                     from_='+14784491207',
                     to='+919960713863'
                 )

