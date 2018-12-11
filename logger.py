import logging


# Logging level Debug > Info > Warning > Error > Critical
if __name__ == '__main__':
    print('hi')
    logging.basicConfig(filename='./test.log', level=logging.INFO)
    logging.debug('Loggin Debug Test')
    logging.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Logging File Output Test@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    logging.info('Log Info Test')
    logging.warning('Logging Warning Test')
    logging.error('Logging Error Test')
    logging.critical('Logging Critical Test')
    logging.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Logging File Output Test@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
