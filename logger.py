import logging


# Logging level Debug > Info > Warning > Error > Critical
if __name__ == '__main__':
    print('hi')
    logging.basicConfig(level=logging.INFO)
    logging.debug('Loggin Debug Test')
    logging.info('Logging Info Test.')
    logging.warning('Logging Warning Test')
    logging.error('Logging Error Test')
    logging.critical('Logging Critical Test')
    