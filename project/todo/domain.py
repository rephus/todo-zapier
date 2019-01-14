import requests
import logging
from todo import settings 

logger = logging.getLogger(__name__)

def notify(message): 
    response = requests.post(settings.ZAPPIER_URL, data={'text': message})
    logger.info("Response from Zapier: {}".format(response.content))
