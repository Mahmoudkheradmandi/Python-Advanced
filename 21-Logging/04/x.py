import logging

logging.basicConfig(filename='x.log',
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s - %(name)s - :%(message)s")

# locals() 
# globals()

x = 2 
y = 0

try: 
    print(x/y)
except: 
    logging.exception('Excaption occurred')
    logging.debug(globals())
        
    

