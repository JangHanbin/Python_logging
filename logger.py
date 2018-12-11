import logging


# Logging level Debug > Info > Warning > Error > Critical
if __name__ == '__main__':
    logger = logging.getLogger('LogTester')
    logger.setLevel(logging.INFO)
    fomatter = logging.Formatter('[ % (levelname)s | % (filename)s: % (lineno)s] % (asctime)s > % (message)s')
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add File handler & Stream Handler for print to file & console output
    fh = logging.FileHandler('./test_logger.log')
    sh = logging.StreamHandler()

    # add File Handler & Stream Handler to logging instance
    logger.addHandler(fh)
    logger.addHandler(sh)

    logger.debug('Logger Debug Test')
    logger.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Logging File Output Test@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    logger.info('Logger Info Test')
    logger.warning('Logger Warning Test')
    logger.error('Logger Error Test')
    logger.critical('Logger Critical Test')
    logger.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Logging File Output Test@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    ### Single output Example ###
    # logging.basicConfig(filename='./test.log', level=logging.INFO)
    # logging.debug('Loggin Debug Test')
    # logging.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Logging File Output Test@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # logging.info('Log Info Test')
    # logging.warning('Logging Warning Test')
    # logging.error('Logging Error Test')
    # logging.critical('Logging Critical Test')
    # logging.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Logging File Output Test@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    ### Single output Example ###