# analyticsapi-engines-python-sdk

## Overview
API client library to leverage FactSet's PA Engine, SPAR Engine and Vault API in python.

**`fds.analyticsapi.engines`** - Contains the Python library. It is developed using [open-api-generator](https://github.com/OpenAPITools/openapi-generator).

**`Utilities`** - Contains the EnginesAPI's OpenAPI schema (openapi-schema.json), configuration file (openapi-generator-config.json), OpenAPI's python edited templates and End-to-End tests of library.

#### Supported versions
* Python 3.4+

#### Current versions
* API_VERSION - v2
* PACKAGE_VERSION - 4.0.0

## To install the API client library
* Run the below command.
```
pip install fds.analyticsapi.engines-*.*.*.tar.gz
```

## Generate library
To customize the OpenAPI generator options and generate the library. Please go through [Open API](https://swagger.io/docs/specification/about/) and [open-api-generator](https://github.com/OpenAPITools/openapi-generator) for more details.

### Pre-requisites
* Install [Java SDK8 64 bit version](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).
* Install PyCharm.
* Clone this `analyticsapi-engines-python-sdk` repository.
* Move into the `analyticsapi-engines-python-sdk/Utilities/codegen` folder and run the `download-codegen.bat` file by double clicking it (for downloading the openapi-generator-cli.jar).

### To update and build the library
* Move to the `analyticsapi-engines-python-sdk` location.
* Delete all the contents of `fds.analyticsapi.engines` directory except `.openapi-generator-ignore` script.
* In the `Utilities` folder update the `packageVersion` field to new **PACKAGE_VERSION** in `openapi-generator-config.json` file.
* Run the below command after updating **PACKAGE_VERSION** with correct values.
```
javac -classpath Utilities/codegen/*; Utilities/codegen/CustomPythonClientCodegen.java
java -DapiTests=false -DmodelTests=false -classpath Utilities/codegen/;Utilities/codegen/*; org.openapitools.codegen.OpenAPIGenerator generate --generator-name CustomPythonClientCodegen --input-spec Utilities/codegen/openapi-schema.json --output fds.analyticsapi.engines --config Utilities/codegen/openapi-generator-config.json --http-user-agent engines-api/PACKAGE_VERSION/python --template-dir Utilities/codegen/templates --skip-validate-spec
```
* Run the below command which generates API client library in `dist` directory.
```
python setup.py sdist
```

### Run End-to-End tests

#### Running the Test Cases using PyCharm
* Open the PyCharm.
* Goto `File-> Open`.
* Browse for the `Utilities/test` folder and open it.
* Goto `View-> Tool Windows-> Terminal` and open the terminal.
* In the terminal, move to the location `fds.analyticsapi.engines`.
* Install the library.
```
pip install fds.analyticsapi.engines.*.*.*.tar.gz
```
* Set the below environment variables.
```
ANALYTICS_API_USERNAME_SERIAL = "username-serial" 
ANALYTICS_API_PASSWORD = "apikey" // Generate using developer portal
```
* Open the test folder and the test case you want to run.
* Click on the Run option to run the selected test case.