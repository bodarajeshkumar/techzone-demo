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


# List available projects in current context

# In[11]:


get_ipython().system(' cpdctl project list')


# ### Access the selected project assets

# Get cpdctl-demo project ID and show details

# In[12]:


result = get_ipython().getoutput("cpdctl project list --output json --raw-output --jmes-query 'resources[0].metadata.guid'")
PROJECT_ID = result.s


# In[13]:


get_ipython().system(' cpdctl project get --project-id {PROJECT_ID}')


# Get project details in JSON format and extract it's name

# In[14]:


get_ipython().system(' cpdctl project get --project-id {PROJECT_ID} --output json')


# In[15]:


result = get_ipython().getoutput('cpdctl project get --project-id {PROJECT_ID} --output json --jmes-query "entity.name" --raw-output')
PROJECT_NAME = result.s
print("'{}' project ID is: {}".format(PROJECT_NAME, PROJECT_ID))

EXPORT = {
    "all_assets": True
}
EXPORT_JSON = json.dumps(EXPORT)
print(EXPORT_JSON)
result = get_ipython().getoutput('cpdctl asset export start --project-id {PROJECT_ID} --assets \'{EXPORT_JSON}\' --name demo-project-assets --output json --jmes-query "metadata.id" --raw-output')
EXPORT_ID = result.s
print('Export ID: {}'.format(EXPORT_ID))

get_ipython().system('cpdctl asset export download --project-id {PROJECT_ID} --export-id {EXPORT_ID} --output-file project-assets.zip --progress')



