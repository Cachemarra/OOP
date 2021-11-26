#%% Configuration of the logging
import logging as log


log.basicConfig(level=log.INFO, # Level of prints (DEBUG, INFO, WARNING, ERROR, CRITICAL.)
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p'
                )

#%% Test
if __name__ == '__main__':

    log.debug('Debug Message')
    log.info('Info Message')
    log.warning('Warning Message')
    log.error('Error Message')
    log.critical('Critical Error Message')
