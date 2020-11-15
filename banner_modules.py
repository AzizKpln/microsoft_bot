#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
import undetected_chromedriver as uc
import time
import random
from clint.textui import colored
import os
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import speech_recognition as sr
from winreg import *
import requests
import json
import string
import logging
print(colored.blue("""
  __  __ _                           __ _   ____        _   
 |  \/  (_)                         / _| | |  _ \      | |  
 | \  / |_  ___ _ __ ___  ___  ___ | |_| |_| |_) | ___ | |_ 
 | |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|  _ < / _ \| __|
 | |  | | | (__| | | (_) \__ \ (_) | | | |_| |_) | (_) | |_ 
 |_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|____/ \___/ \__|

                    by:Aziz Kaplan
                    version:1.0
                    Lisence:LGPL-3.0 License
                                                            
        """))