import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer = lambda x:
                         dumps(x).encode('utf-8'))

producer.send('user_Topic', value="{'hello':'charuka'}")

# bootstrap_servers = '127.0.0.1:9092'

# producer = KafkaProducer(bootstrap_servers= bootstrap_servers)

# topic = 'user_Topic'

# message  = b'hello, tawanda'

# producer.send(topic,message)

producer.flush()

producer.close()