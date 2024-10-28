###############################################################
####                                                       ####
#### Written By: Satyaki De                                ####
#### Written Date:  26-Oct-2024                            ####
#### Modified Date: 27-Oct-2024                            ####
####                                                       ####
#### Objective: This script will read the prompt inputs    ####
#### and then in a series coordinated interactions between ####
#### multiple agents & a follow up response will finally   ####
#### provide the desired solutions, which you can execute  ####
#### it at the end or separately.                          ####
####                                                       ####
###############################################################

import datetime
import logging
import time
import os
import autogen

import clsTemplate as ct
from clsConfigClient import clsConfigClient as cf

# Disabling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

########################################################
################    Global Area   ######################
########################################################

var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print('*' *60)
DInd = cf.conf['DEBUG_IND']

templateVal_1 = ct.templateVal_1
templateVal_2 = ct.templateVal_2
templateVal_3 = ct.templateVal_3
templateVal_4 = ct.templateVal_4
templateVal_5 = ct.templateVal_5

# Set the environment variable to avoid the tokenizers warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Note: You would need to set up these API keys as environment variables
OPENAI_API_KEY = cf.conf["OPEN_AI_KEY"]
MODEL_NAME = cf.conf["MODEL_NAME"]
WORK_DIR = cf.conf["WORK_DIR"]

# Configure the AI models
config_list = [
    {
        'model': MODEL_NAME,
        'api_key': OPENAI_API_KEY
    }
]

# Create the assistant agent
assistant = autogen.AssistantAgent(
    name="AI_Assistant",
    llm_config={
        "config_list": config_list,
    }
)

# Create the user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message=templateVal_1,
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": WORK_DIR,
        "use_docker": False,
    },
)

# Create a math expert agent
engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config={
        "config_list": config_list,
    },
    system_message=templateVal_2,
)

# Create a coding expert agent
game_designer = autogen.AssistantAgent(
    name="GameDesigner",
    llm_config={
        "config_list": config_list,
    },
    system_message=templateVal_3,
)

# Create a coding expert agent
planner = autogen.AssistantAgent(
    name="Planer",
    llm_config={
        "config_list": config_list,
    },
    system_message=templateVal_4,
)

# Create a coding expert agent
critic = autogen.AssistantAgent(
    name="Critic",
    llm_config={
        "config_list": config_list,
    },
    system_message=templateVal_5,
)

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

########################################################
################  End Of Global Area   #################
########################################################

class clsAutoGenAI:
    def __init__(self):
        self.expDesc = str(cf.conf['APP_DESC'])

    def buildAndPlay(self, inputPrompt):
        try:
            user_proxy.initiate_chat(
                assistant,
                message=f"We need to solve the following problem: {inputPrompt}. "
                        "Please coordinate with the admin, engineer, game_designer, planner and critic to provide a comprehensive solution. "
            )

            return 0
        except Exception as e:
            x = str(e)
            print('Error: <<Real-time Translation>>: ', x)

            return 1
