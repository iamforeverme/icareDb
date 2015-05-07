"""
    logging.debug('this is a message')
    logging.info("this is a info")
    logging.disable(30)#logging.WARNING
    logging.warning("this is a warnning")
    logging.critical("this is a critical issue")
    logging.error("this is a error")
    logging.addLevelName(88,"MyCustomError")
    logging.log(88,"this is an my custom error")
    try:
      raise Exception('this is a exception')
    except:
      logging.exception( 'exception')
    """
import logging
def getLogger(name):
	logging.basicConfig(filename = name+".log" , filemode = 'a', level = logging.NOTSET, format = '%(asctime)s - %(levelname)s: %(message)s')
	logger = logging.getLogger(name)
	return logger

# getLogger('abc')