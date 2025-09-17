<img alt="FactSet" src="https://www.factset.com/hubfs/Assets/images/factset-logo.svg" height="56" width="290">

# Analytics API Engines Python SDK

[![build](https://img.shields.io/github/workflow/status/factset/analyticsapi-engines-python-sdk/CI)](https://github.com/factset/analyticsapi-engines-python-sdk/actions?query=workflow%3ACI)
[![PyPi](https://img.shields.io/pypi/v/fds.analyticsapi.engines)](https://pypi.org/project/fds.analyticsapi.engines/)
![API version](https://img.shields.io/badge/API-v2-blue)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)
![Deprecated](https://img.shields.io/badge/status-deprecated-red)

*```**Note: This library is no longer maintained and is deprecated. Please use``` [enterprise-sdk](https://github.factset.com/FactSet/enterprise-sdk) ```instead.```*

Use this library to integrate with FactSet's Analytics APIs. Below APIs are supported by this SDK.

* [PA Engine API](https://developer.factset.com/api-catalog/pa-engine-api)
* [SPAR Engine API](https://developer.factset.com/api-catalog/spar-engine-api)
* [Vault API](https://developer.factset.com/api-catalog/vault-api)

## Contents

* [auto-generated-sdk](auto-generated-sdk) - Auto-generated code using [Analytics API Engines SDK Generator](https://github.com/factset/analyticsapi-engines-sdk-generator)
* [examples](examples) - Sample project containing code snippets to quickly get started with the SDK  
* [tests](tests) - Integration tests

## Requirements

* Python 3.4 or higher

## Installation

* Install the latest SDK using pip:

  ```sh
  pip install fds.analyticsapi.engines
  ```

* Alternatively, download or clone this repository and install the SDK by  running Setuptools in the SDK installation directory:

  ```sh
  git clone https://github.com/factset/analyticsapi-engines-python-sdk.git
  cd auto-generated-sdk
  python setup.py install --user
  ```

## Usage

Refer [examples](examples) project for sample code snippets to quickly get started with the SDK

## Tests

First, clone the repo locally and `cd` into the directory.

```sh
git clone https://github.com/factset/analyticsapi-engines-python-sdk.git
```

Then, to make local package in `auto-generated-sdk` accessible to the tests, you have to build and register them in pip

```sh
cd auto-generated-sdk/
python setup.py sdist
pip install .
```

Next, install dependencies that the tests directory needs.

```sh
cd tests/
pip install -r requirements.txt
```

Before running the tests, set the below environment variables. Use the [Developer Portal Manage API Keys page](https://developer.factset.com/manage-api-keys) to get these values.

```sh
export ANALYTICS_API_USERNAME_SERIAL = "username-serial"
export ANALYTICS_API_PASSWORD = "apikey"
```

Run the tests with below command.

```sh
python -m test
```

**note when checking out different branches, you will have to re-install the auto-generated-sdk directory before running tests again
```sh
cd auto-generated-sdk/
pip list # to view what version of fds.analyticsapi.engines is installed
pip uninstall fds.analyticsapi.engines <version>
python setup.py sdist
pip install .
```

## Contributing

* Files in [auto-generated-sdk](auto-generated-sdk) directory are auto-generated and should not be manually edited here. Refer [Analytics API Engines SDK Generator](https://github.com/factset/analyticsapi-engines-sdk-generator) for instructions on how to modify these files.
* Projects [examples](examples) and [tests](tests) are open to enhancements and bug fixes. Please create a pull requests with the proposed changes.
