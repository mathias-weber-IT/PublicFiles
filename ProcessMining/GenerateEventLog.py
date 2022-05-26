# Databricks notebook source
import random
import time
from datetime import datetime, timedelta
import pandas as pd

event_log = list()

for i in range(20):
    
    event_log.append([i, 'Start Game', 'Player', now.strftime("%H:%M:%S")])
    num1 = random.randint(0, 1)
    num2 = random.randint(0, 1)
    num3 = random.randint(0, 1)
    time1 = now + timedelta(seconds=10)
    time2 = now + timedelta(seconds=20)
    time3 = now + timedelta(seconds=30)
    time4 = now + timedelta(seconds=40)
    if num1 == 1:
        event_log.append([i, 'Reach Level 1', 'Player', time1.strftime("%H:%M:%S")])      
        if num2 == 1:
            event_log.append([i, 'Reach Level 2', 'Player', time2.strftime("%H:%M:%S")])          
            if num3 == 1:
                event_log.append([i, 'Win Game', 'Player', time3.strftime("%H:%M:%S")])
    if num1 == 0 or num2 == 0 or num3 == 0:
        event_log.append([i, 'Lose Game', 'Player', time4.strftime("%H:%M:%S")])
        
df_eventlog  = pd.DataFrame(event_log, columns = ['Case', 'Activity', 'Resource', 'Timestamp'])

# COMMAND ----------

display(df_eventlog)
