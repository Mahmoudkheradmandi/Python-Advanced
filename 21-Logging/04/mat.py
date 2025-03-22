import logging

logger = logging.getLogger(__name__) # my logging name is file name 
logger.setLevel(logging.ERROR)
formater = logging.Formatter("%(asctime)s:%(levelname)s - %(name)s -:%(message)s")

# file handler : 
file_handler = logging.FileHandler('mat.log')
file_handler.setFormatter(formater)
logger.addHandler(file_handler)


# logging.basicConfig(filename='mat.log',
#                     level=logging.ERROR,
#                     format="%(asctime)s:%(levelname)s:%(message)s")

def greetings(): 
    return 'Hello wrold !'

def farewell(): 
    return 'Gooodbye !'

# logging.error(greetings())
# logging.error(farewell())


logger.error(greetings())
logger.error(farewell())
