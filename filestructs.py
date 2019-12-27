#! /usr/bin/env python3
from pyspark.sql.types import *

class FileStructs(object):
    DATA_STOCK = StructType([
          StructField('date', TimestampType(), False)
        , StructField('open_price', DecimalType(10,0), False)
        , StructField('high_price', DecimalType(10,0), False)
        , StructField('low_price', DecimalType(10,0), False)
        , StructField('close_price', DecimalType(10,0), False)
    ])
  