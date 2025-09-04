import logging
#Logging is an essential practice for tracking events that occur during the execution of a program. It helps developers understand the flow of their code, debug errors, and analyze performance
logger=logging.getLogger(__name__)
logger.propagate= False
logger.info("hello from the helper")
#create handler
stream_h=logging.StreamHandler()
file_h=logging.FileHandler("file.log")

#level and the format'
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("this is a error")