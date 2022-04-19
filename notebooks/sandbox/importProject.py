#!/usr/bin/env python
# coding: utf-8

# # Train, promote and deploy Boston house prices prediction model

# This notebook contains steps and code to demonstrate support of AI Lifecycle features in Cloud Pak for Data. 
# It contains steps and code to work with [`cpdctl`](https://github.com/IBM/cpdctl) CLI tool available in IBM github repository. 
# It also introduces commands for getting model and training data, persisting model, deploying model
# and promoting it between deployment spaces.
# 
# Some familiarity with Python is helpful. This notebook uses Python 3.7.
# 

# In[1]:


import base64
import json
import os
import platform
import requests
import tarfile
import zipfile
from IPython.core.display import display, HTML


# ## CPD Credentials

# In[2]:


CPD_USER_NAME = 'admin'
CPD_USER_PASSWORD = 'CP4DDataFabric'
CPD_URL = 'https://datafabric.ibmcloudpack.com:12864'

 
version_r = get_ipython().getoutput('cpdctl version')
CPDCTL_VERSION = version_r.s

print("cpdctl version: {}".format(CPDCTL_VERSION))


# ### Add CPD profile and context configuration

# Add "cpd_user" user to the `cpdctl` configuration

# In[6]:


get_ipython().system(' cpdctl config user set cpd_user --username {CPD_USER_NAME} --password {CPD_USER_PASSWORD}')


# Add "cpd" profile to the `cpdctl` configuration

# In[7]:


get_ipython().system(' cpdctl config profile set cpd --url {CPD_URL} --user cpd_user')


# Add "cpd" context to the `cpdctl` configuration

# In[8]:


get_ipython().system(' cpdctl config context set cpd --profile cpd --user cpd_user')


# List available contexts

# In[9]:


get_ipython().system(' cpdctl config context list')


# In[10]:


get_ipython().system(' cpdctl config context use cpd')



RESTORED_PROJECT_NAME = 'cpdctl-demo-restored-project'
JMES_QUERY = "resources[?entity.name == '{}'].metadata.guid".format(RESTORED_PROJECT_NAME)
result = get_ipython().getoutput('cpdctl project list --output json --jmes-query "{JMES_QUERY}"')
PROJECT_IDS = json.loads(result.s)
if PROJECT_IDS:
    for project_id in PROJECT_IDS:
        print('Deleting project with ID: {}'.format(project_id))
        get_ipython().system('cpdctl project delete --project-id {project_id}')


get_ipython().system('cpdctl project list --output json')

import uuid
STORAGE = {"type": "assetfiles", "guid": str(uuid.uuid4())}
STORAGE_JSON = json.dumps(STORAGE)
result = get_ipython().getoutput('cpdctl project create --name {RESTORED_PROJECT_NAME} --output json --raw-output --storage \'{STORAGE_JSON}\' --jmes-query \'location\'')
RESTORED_PROJECT_ID = result.s.split('/')[-1]
print("The new '{}' project ID is: {}".format(RESTORED_PROJECT_NAME, RESTORED_PROJECT_ID))


result = get_ipython().getoutput('cpdctl asset import start --project-id {RESTORED_PROJECT_ID} --import-file project-assets.zip --output json --jmes-query "metadata.id" --raw-output')
IMPORT_ID = result.s
print("The new import ID is: {}".format(IMPORT_ID))

get_ipython().system('cpdctl asset import get --project-id {RESTORED_PROJECT_ID} --import-id {IMPORT_ID}')


get_ipython().system('cpdctl asset search --query \'*:*\' --type-name asset --project-id {RESTORED_PROJECT_ID}')

