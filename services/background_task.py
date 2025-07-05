from asyncio import sleep
from datetime import datetime
from logging import Logger

from constants.settings import END_TIME, START_TIME, SLEEP_INTERVAL
from utils.logger import get_logger

logger: Logger = get_logger(__name__)


async def background_task():
    """
        all the tasks mentioned here will be running in the background
    """
    global logger

    logger.info("BACKGROUND TASK STARTED")

    # this part will loop till the trading times end
    current_time = datetime.now()

    while current_time < END_TIME:
        current_time = datetime.now()

        # if the trading has not started then iterate every 1 sec else iterate every 30 sec
        if START_TIME < current_time:
            await sleep(SLEEP_INTERVAL)
        else:
            await sleep(1)

    logger.info("TASK ENDED")
