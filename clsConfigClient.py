################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 28-Oct-2024               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal Sarvam AI's LLM evaluation    ####
#### solution to fetch the KPIs to tune it. ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'DATA_PATH': Curr_Path + sep + 'data' + sep,
        'OUTPUT_PATH': Curr_Path + sep + 'output' + sep,
        'TEMP_PATH': Curr_Path + sep + 'temp' + sep,
        'IMAGE_PATH': Curr_Path + sep + 'Image' + sep,
        'AUDIO_PATH': Curr_Path + sep + 'audio' + sep,
        'SESSION_PATH': Curr_Path + sep + 'my-app' + sep + 'src' + sep + 'session' + sep,
        'WORK_DIR': 'coding',
        'APP_DESC': 'AutoGen Demo!',
        'DEBUG_IND': 'Y',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'input.json',
        'MODEL_NAME': 'gpt-4',
        'CHANNEL_NAME': 'sd_channel',
        'OPEN_AI_KEY': "sk-fz&8dhVXG7zksdjdidj93838JJDFhXPnN3Y9Pt2889KMeKe",
        "DB_PATH": Curr_Path + sep + 'data' + sep
    }
