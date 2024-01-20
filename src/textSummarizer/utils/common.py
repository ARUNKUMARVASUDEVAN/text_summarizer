import os #portable way of using operating system
from box.exceptions import BoxValueError  #is used handle the exception happen when we use box API
import yaml # to read and write yaml file
from textSummarizer.logging import logger #used for logging all the details 
from ensure import ensure_annotations  #validate conditions
from box import ConfigBox 
from pathlib import Path
from typing import Any

