import logging
import mat

logging.basicConfig(filename='main.log',
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s - %(name)s - :%(message)s")

def greetings(): 
    return 'Hello wrold !'

def farewell(): 
    return 'Gooodbye !'

logging.debug(greetings())
logging.debug(farewell())

