"""
# This module authuenticates the watson langugae service and define functions for:
# a) English to French b) French to English
"""
import os

#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

# Fetching the service credentials
apikey = os.environ['apikey']
url = os.environ['url']

#Autheticating the service 
authenticator = IAMAuthenticator(apikey)

# Creating the translation object
wlt = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

wlt.set_service_url(url)

# function for E2F
def english_to_french(english_text):
    """
    Function for  English to French Translation
    """
    french_text = wlt.translate(text=english_text,source='en',target='fr').get_result()
    return french_text

# Function for F2E
def french_to_english(french_text):
    """
    Function for  French to English Translation
    """
    wlt.set_service_url(url)
    english_text = wlt.translate(text=french_text,source='fr',target='en').get_result()
    return english_text