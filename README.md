# Watson Knowledge Catalog (WKC) REST API
Our motivation to create this asset was based on the realization that some tasks in WKC in its current version can only be accomplished through the REST API. With our code we want to demonstrate some key capabilities such as business terms, custom assets and reference data in order to provide a blueprint into other areas. During our implementation we have quickly expanded into other areas such as workflows and jobs to name a few and we have added these into the repository as we went along. The code is not perfect and not everything has been fully coded, but it should get us all started using the API. This asset serves two purposes:
1. It is meant to educate. We would like to demonstrate how the WKC API, can be used.
2. We wanted to create code that would allow us to start quickly in projects where the API is required.

## Goals of this Repository:
- Create clean source code for each of the use cases identified below
- Bring code in shape so it's easily understandable even for beginners
- Code and documentation should act as enabler for teams starting to work with WKC API
- Code and documentation should also act as starting point to solving concrete problems in a project
- It is not overengineered, but useable as QuickStart in projects
- Source code in reusable quality
- Structure code in modules and classes as can be derived from API functions (e.g. module for working with global search, one for terms, one for - reference data, etc.)
- Ensure code is extensible to other API functions not yet covered or implemented
- Notebooks are provided to document general usage for most of the functions available
- Sample json payload structures are provided to document their usage in the context of the functions that are using them

## Prerequisites and Recommended Tools
- Cloud Pak for Data `3.5`
- Github Desktop https://desktop.github.com/
- Git (optional for integration with VSC) https://git-scm.com/downloads
- Python `3.9` https://www.python.org/downloads/
- Visual Studio Code (VSC) https://code.visualstudio.com/
- Python Extension of VSC https://code.visualstudio.com/docs/python/python-tutorial
- Jupyter Extension of VSC https://code.visualstudio.com/docs/python/jupyter-support
- REST Client (optional for curl) https://marketplace.visualstudio.com/items?itemName=humao.rest-client
- JSON Parser (optional or use pprint) http://json.parser.online.fr/

## Installation
1. Make sure the prerequisites are installed.
2. clone this github repository.
3. Install necessary dependencies:
```sh
pip install -r requirements.txt
```
4. Create `.env` file with Secrets:
```sh
cp .envExample .env
```

## Repository Structure
The repository has been structured along the type of content that it holds. Most important is the python code stored in the apis folder. Other folders such as csv, curl, notebooks and payloads are stored in the repository as examples. The htmlReference directory contains an API Reference of the apis.
### apis
This directory contains all the classes wrapping WKC service endpoints. _main.py_ cointains the main class `MainAPI` that creates a default API connection. Other _*.py_ files contain `SubAPI` classes that use the `MainAPI` class in the background and extend its functionality. 
- `MainAPI` in _main.py_
#### endpoints
Each class wraps an specific WKC endpoint and contains a class with functions for that endpoint:
- `AssetsAPI` in _assets.py_
- `CatalogsAPI` in _catalogs.py_
- `CategoriesAPI` in _categories.py_
- `ConnectionsAPI` in _connections.py_
- `DataRequestAPI` in _datarequests.py_
- `TermsAPI` in _glossaryTerms.py_
- `GovArtifactAPI` in _governanceArtifactTypes.py_
- `JobsAPI` in _jobs.py_
- `ProjectsAPI` in _projects.py_
- `RefDataAPI` in _referenceData.py_
- `RulesAPI` in _rules.py_
- `UsersAPI` in _users.py_
- `WorkflowAPI` in _workflows.py_
#### usecases
Contains SubAPI's that combine multiple endpoints to enable more advanced functionalities.
- `AssignTermsAPI` in _assignTerms.py_
- `CategoryTreeAPI` in _categoryTrees.py_
### csv
Folder which can hold permanent or temporary csv files for demos, testing or other purposes
### curl
Folder that holds some (not many) curl scripts
This has only been started and can grow for who prefers curl over python
### htmlReference
Open _htmlReference/apis/index.html_ in a browser to display a API reference.
### notebooks
This folder holds a number of jupyter notebooks that demonstrate how to use the api classes. Please use this as a central starting point exploring the capabilities of this asset.

There are special notebooks for each endpoint class in the _endpoints_ directory.

More speciliased notebooks for specific usecases are provided in the _usecases_ directory.
### payloads
Contains _json_ files that can be used to pass into some api functions
The folder structure represents the endpoints and also the api classes for ease of identification
### tests
These are unit tests to validate the core functionality of the api classes of _apis_.

Please make sure all tests pass before creating an update.
### utilities
Holds supporting files such as one for csv file processing

## Developing instructions
Install the dev dependencies with `pip install -r devRequirements.txt`
### Enhancing Code
Code for a specific endpoint should be located in its corresponding class. If class does not yet exist, because a new endpoint is used, then a new class should be created following the same logic as other classes provided.
### Logging
The API is [logging](https://docs.python.org/3/library/logging.html) additional information dependent on the log level that is set. The default log level is `WARN`.
For more detailed information about the HTTP requests that are used the log level can be set to `INFO` or `DEBUG`.

This can be done through setting the log level *at the beginning of a Python script* like this:
```python
import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
```
The logs are then send to `stdout`.
### Unittesting
Execute unittests with `python3 -m pytest`

The pytest log output can be modified in _pytest.ini_. Unittests can also be run from within the VS Code environment.
### Working with files dynamically created for testing and examples
Notbooks (_*.ipynb_), csv's (_*.csv_), curl scripts (_*.http_) and json's (_*.json_) are files of a dynamic type. This repo provides some examples of these. To prevent git from tracking the changes in these files when uploading changes to git it is recommended to set git's [skip-worktree](https://git-scm.com/docs/git-update-index) flag on these files. Recommonded settings are as follows:

#### Linux/Mac
- `find notebooks -name '*.ipynb' | xargs -I % git update-index --skip-worktree %` tells git to avoid tracking the changes in the _notebooks_ directory.
- `git update-index --skip-worktree csv/*` tells git to avoid tracking the changes in the _notebooks_ directory.
- `find curl -name '*.http' | xargs -I % git update-index --skip-worktree %` tells git to avoid tracking the changes of _*.http_ files in the _curl_ directory.
- `find payloads -name '*.json' | xargs -I % git update-index --skip-worktree %` tells git to avoid tracking the changes of _*.json_ files in the _payloads_ directory.

#### Windows Powershell
- `Get-ChildItem -Path notebooks -Filter *.ipynb –Recurse | %{git update-index --skip-worktree $_.FullName}`
- `Get-ChildItem -Path csv -Filter *.csv –Recurse | %{git update-index --skip-worktree $_.FullName}`
- `Get-ChildItem -Path curl -Filter *.http –Recurse | %{git update-index --skip-worktree $_.FullName}`
- `Get-ChildItem -Path payloads -Filter *.json –Recurse | %{git update-index --skip-worktree $_.FullName}`

To verify the state of the configuration use `git ls-files -v` to list all files in the repository. The ones prefixed with an "S" are skipped

To reallow tracking for a certain file `git update-index --no-skip-worktree $FILEPATH` can be executed or you can execute same commands as above but with --no-skip-worktree set.

### Update HTML API Reference
A new HTML API reference can then be created with `pdoc --html apis --force -o htmlReference`

## URLs for our APIs and docs
### Docs
https://cloud.ibm.com/apidocs/watson-data-api-cpd<br/>

### CP4D Version info
https://{hostname}/zen/#/versiondetails<br/>

### Report issues in case docs are not clear
https://github.ibm.com/PrivateCloud-analytics/Zen/issues<br/>

### Swagger UIs and other API docs
https://{hostname}/v3/glossary_terms/api#/<br/>
https://{hostname}/v2/jobs/docs/swagger/#/<br/>
https://{hostname}/v2/cams/explorer/#/<br/>
https://github.ibm.com/PrivateCloud-analytics/zen-core-api/blob/vnext-dev/source/swagger-specs/data_request.yaml<br/>
http://zen-docs1.fyre.ibm.com:3333/docs#operation/postDataRequest<br/>

### Global Search and Metadata Documentation<br/>
https://github.ibm.com/wdp-gov/global-search-service/wiki/THE-API<br/>
https://github.ibm.com/wdp-gov/global-search-service/wiki/Data-Common-To-All-Microservices<br/>
https://github.ibm.com/wdp-gov/global-search-service/wiki/Help-Us-Help-You<br/>
https://github.ibm.com/wdp-gov/global-search-service/wiki/API---Advanced-Search-Cookbook<br/>
https://github.ibm.com/wdp-gov/global-search-service/wiki/Partial-Word-Matches-vs-Multi-Term-or-Phrase-Matches<br/>
https://github.ibm.com/wdp-gov/global-search-service/wiki/10000-Documents-is-all-you-get<br/>
https://github.ibm.com/wdp-gov/wdp-catalog-service/wiki/Processing-duplicate-asset<br/>

### Articles
https://towardsdatascience.com/catalog-external-assets-for-a-360-data-lineage-448c8f6bf2b2<br/>
https://medium.com/ibm-data-ai/tailor-your-data-catalog-with-custom-asset-attributes-a2b468535a48<br/>
https://github.ibm.com/cds-devops/wkc-workflow-service-runbook/blob/master/troubleshooting/CleanUpDraftObjects_WFM10317E.md<br/>

### Additional info
CSVs can be edited with Programs like Excel or with [Pandas](https://pandas.pydata.org/). A nice overview of the functions of Pandas can be seen here at [this cheat sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf?platform=hootsuite).

### Programming resources
Beginners Guide to Python: https://wiki.python.org/moin/BeginnersGuide/NonProgrammers<br/>
Programmers Guide to Python: https://wiki.python.org/moin/BeginnersGuide/Programmers<br/>
Getting Stared with Pandas: https://pandas.pydata.org/docs/getting_started/index.html#<br/>

## Slack channels for Questions
#askanythingwkc<br/>
#global-search<br/>

## Use Cases
With our code we want to demonstrate some key capabilities in order to provide a blueprint into other areas.
During our implementation we have quickly expanded into other areas such as workflows and jobs to name a few and we have added these into the repository as we went along.
Following are the key use cases that we used to develop this asset.
### How do I authenticate?
- Session class
- Hostname, User, Pwd
- Headers, Token
### How do I search?
- Using Global Search to demonstrate how to find artefacts in WKC
- There are many search possibilities, but only some are exploited here.
- In fact we focus on the [lucene search query syntax](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html) and have successfully managed to retrieve all we needed
- So complementary to the other use cases we demonstrate how to search for Terms, Referenzdatasets, Assets
### How do I work with Reference Data?
- We want to demonstrate how to work with reference data in WKC
- We want to be able to find and retireve reference data for the purpose of data validation or loading of DWH dimension data outside WKC
- We also demonstrate how to use CSV function to write extracted reference data values into csv and load a set from csv
### How do I work with Custom Asset Types?
- This use case focusses on exploring how to create your own asset types other than a data asset
- We have tried the book example from the api docs but also created a RestAPI custom asset type
### How do I perfom mass (batch) updates?
- This use case is based on working with terms in the glossary
- The scenario is simple. Since we're currently lacking mass update features in the UI we have to rely on the API to perform such tasks.
- We show how to identify a list of terms through search and write these into a CSV
- Now the CSV can be manipulated by a business user in that for instance tags can be added or a datasteward can be reassigned
- Then the csv can be imported and all terms contained therein updated in the system
- Here we have to observe an optimistc locking mechanism using the revision flag which requires to read each term prior to updating using the revision id read out
