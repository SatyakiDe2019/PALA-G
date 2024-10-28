#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 27-Oct-2024                     ####
#### Modified On 27-Oct-2024                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### clsAutoGenAI class to initiate the          ####
#### AutoGen agents to perform certain tasks in  ####
#### real-time.                                  ####
####                                             ####
#####################################################

# We keep the setup code in a different class as shown below.
import clsAutoGenAI as agi
from clsConfigClient import clsConfigClient as cf

import datetime
import logging

def main():
    try:
        # Other useful variables
        debugInd = 'Y'

        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('Start Time: ', str(var))

        # Initiating Log Class
        general_log_path = str(cf.conf['LOG_PATH'])

        # Enabling Logging Info
        logging.basicConfig(filename=general_log_path + 'genAutoGenLog.log', level=logging.INFO)

        print('Build your own application!')

        # Passing source data csv file
        x1 = agi.clsAutoGenAI()

        problemStatement = input('Provide your input goals to create solution:')

        r1 = x1.buildAndPlay(problemStatement)

        if (r1 == 0):
            print('Successfully Build the Application with Demo!')
        else:
            print('Failed to build or run the demo!')

        var2 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        print('End Time: ', str(var2))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
