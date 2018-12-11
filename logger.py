import logging


if __name__ == '__main__':
    print('hi')
    logging.basicConfig(level=logging.INFO)
    logging.info('Logging Info Test.')
    logging.warning('Logging Warning Test')