import logging

logging.basicConfig(filename='demo.log',level=logging.DEBUG,filemode='w')

def nameCheck(name):
    if len(name)<2:
        logging.debug('check for name length')
        return 'invalid name'
    elif name.isspace():
         logging.info('check if name is a space')
         return 'invalid name'
    elif name.isalpha():
        logging.warning('check if name is alphabet')
        return 'invalid name'
    elif name.isalpha():
        logging.error('This is a ERROR message')
        return 'invalid name'
    else:
        logging.critical('This is a SUCCESSFULLY ALL CHECKS message')

print(nameCheck('jagadeesh'))