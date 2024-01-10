from wasteDetection.logger import logging
# logging.info("Welcome to my custom log 2")
from wasteDetection.exception import AppException
import sys



try:
    b= 3/"5"
except Exception as e:
    raise AppException(e, sys)
