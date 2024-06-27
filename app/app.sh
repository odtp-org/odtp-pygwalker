#!/bin/bash

############################################################################################
# START OF MANUAL CONFIGURATION. 
# ADAPT THE TEMPLATE HERE.
############################################################################################

#########################################################
# 1. GITHUB CLONING OF REPO
# Clone the repository of your tool and checkout to one specific commit. 
#########################################################

# Not necessary as the tool is in app.py

#########################################################
# 2. CONFIG FILE CONFIGURATION
# Read placeholders and create config file from Environment  
#########################################################

# Not necessary

#########################################################
# 3. INPUT FOLDER MANAGEMENT
#########################################################

# ln -s /odtp/odtp-input/ /odtp/odtp-workdir/input

#########################################################
# 4. TOOL EXECUTION
# While the output is managed by ODTP and placed in /odtp/odtp-output/
#########################################################

streamlit run /odtp/odtp-app/app.py

#########################################################
# 5. OUTPUT FOLDER MANAGEMENT
# The selected output files generated should be placed in the output folder
#########################################################

# Not necessary as there's no output

############################################################################################
# END OF MANUAL USER APP
############################################################################################
