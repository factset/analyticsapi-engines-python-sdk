# Migration Guide: Analytics SDK → Enterprise SDK (Python)

**From**: fds.analyticsapi.engines (Deprecated)  
**To**: fds.sdk.FactSetAnalyticsAPI (Recommended)  
**⚠️ CRITICAL**: All Analytics SDK versions removed from PyPI on Sep 1, 2026

---

## Quick Start

### Step 1: Update Project File

**In your requirements.txt:**

```
# REMOVE
fds-sdk-analyticsapi-engines==6.1.1

# ADD
fds-sdk-factsetanalyticsapi==1.0.0
```

**Or in setup.py:**

```python
# OLD
install_requires=[
    'fds-sdk-analyticsapi-engines==6.1.1',
]

# NEW
install_requires=[
    'fds-sdk-factsetanalyticsapi==1.0.0',
]
```

Or via CLI:

```bash
# Install new
pip install fds-sdk-factsetanalyticsapi==1.0.0

# Remove old
pip uninstall fds-sdk-analyticsapi-engines
```

### Step 2: Update Imports

Find and replace in your code:

```python
# OLD
from fds.analyticsapi.engines.api import PaEngineApi, SparEngineApi, VaultApi
from fds.analyticsapi.engines.model import *

# NEW
from fds.sdk.FactSetAnalyticsAPI.api import PaEngineApi, SparEngineApi, VaultApi
from fds.sdk.FactSetAnalyticsAPI.model import *
```

### Step 3: Update API Calls

Refer to specific API sections below for changes.

---

## Module Mapping

| Analytics SDK | Enterprise SDK |
|---|---|
| `fds.analyticsapi.engines` | `fds.sdk.FactSetAnalyticsAPI` |
| `fds.analyticsapi.engines.api` | `fds.sdk.FactSetAnalyticsAPI.api` |
| `fds.analyticsapi.engines.model` | `fds.sdk.FactSetAnalyticsAPI.model` |
| `fds.analyticsapi.engines.client` | `fds.sdk.FactSetAnalyticsAPI.client` |

---

## API-Specific Migration

### PA Engine API

**Before (Analytics SDK):**
```python
from fds.analyticsapi.engines.api import PaEngineApi
from fds.analyticsapi.engines.model import PACalculationParameters

api_instance = PaEngineApi()
pa_params = PACalculationParameters()
result = api_instance.post_and_calculate(pa_params)
```

**After (Enterprise SDK):**
```python
from fds.sdk.FactSetAnalyticsAPI.api import PaEngineApi
from fds.sdk.FactSetAnalyticsAPI.model import PACalculationParameters

api_instance = PaEngineApi()
pa_params = PACalculationParameters()
result = api_instance.post_and_calculate(pa_params)
```

### SPAR Engine API

**Before (Analytics SDK):**
```python
from fds.analyticsapi.engines.api import SparEngineApi
from fds.analyticsapi.engines.model import SPARCalculationParameters

api_instance = SparEngineApi()
spar_params = SPARCalculationParameters()
result = api_instance.post_and_calculate(spar_params)
```

**After (Enterprise SDK):**
```python
from fds.sdk.FactSetAnalyticsAPI.api import SparEngineApi
from fds.sdk.FactSetAnalyticsAPI.model import SPARCalculationParameters

api_instance = SparEngineApi()
spar_params = SPARCalculationParameters()
result = api_instance.post_and_calculate(spar_params)
```

### Vault API

**Before (Analytics SDK):**
```python
from fds.analyticsapi.engines.api import VaultApi
from fds.analyticsapi.engines.model import VaultCalculationParameters

api_instance = VaultApi()
vault_params = VaultCalculationParameters()
result = api_instance.post_and_calculate(vault_params)
```

**After (Enterprise SDK):**
```python
from fds.sdk.FactSetAnalyticsAPI.api import VaultApi
from fds.sdk.FactSetAnalyticsAPI.model import VaultCalculationParameters

api_instance = VaultApi()
vault_params = VaultCalculationParameters()
result = api_instance.post_and_calculate(vault_params)
```

---

## Configuration Changes

### Authentication

Both SDKs use similar authentication patterns:

```python
# Analytics SDK
from fds.analyticsapi.engines.api_client import ApiClient
from fds.analyticsapi.engines.configuration import Configuration

configuration = Configuration()
configuration.username = 'your-username'
configuration.password = 'your-password'
api_client = ApiClient(configuration)

# Enterprise SDK (same pattern)
from fds.sdk.FactSetAnalyticsAPI.api_client import ApiClient
from fds.sdk.FactSetAnalyticsAPI.configuration import Configuration

configuration = Configuration()
configuration.username = 'your-username'
configuration.password = 'your-password'
api_client = ApiClient(configuration)
```

---

## Installation Methods

### Using pip

```bash
pip install fds-sdk-factsetanalyticsapi==1.0.0
```

### Using requirements.txt

```
fds-sdk-factsetanalyticsapi==1.0.0
```

### Using pipenv

```bash
pipenv install fds-sdk-factsetanalyticsapi==1.0.0
```

### Using poetry

```bash
poetry add fds-sdk-factsetanalyticsapi==1.0.0
```

---

## Building and Testing

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
pip install fds-sdk-factsetanalyticsapi==1.0.0
```

### Run Tests

```bash
pytest tests/
```

Verify all tests pass with the new SDK.

### Address Deprecation Warnings

If you see warnings like:
```
DeprecationWarning: fds.analyticsapi.engines is deprecated
```

Make sure you've:
1. Removed all old package references
2. Updated all import statements
3. No old SDK code remains

---

## Troubleshooting

### Problem: "No module named 'fds.sdk.FactSetAnalyticsAPI'"

**Solution**: Verify package is installed:
```bash
pip list | grep fds-sdk-factsetanalyticsapi
```

Should show the new package installed.

If not installed:
```bash
pip install fds-sdk-factsetanalyticsapi==1.0.0
```

### Problem: "ModuleNotFoundError: No module named 'fds.analyticsapi.engines'"

**Solution**: Update import statements:
```python
# Change from:
from fds.analyticsapi.engines.api import PaEngineApi

# To:
from fds.sdk.FactSetAnalyticsAPI.api import PaEngineApi
```

### Problem: "ImportError: cannot import name 'PACalculationParameters'"

**Solution**: Clear cache and reinstall:
```bash
pip cache purge
pip install --force-reinstall fds-sdk-factsetanalyticsapi==1.0.0
```

### Problem: "AttributeError: module has no attribute 'post_and_calculate'"

**Solution**: Verify API class names in new SDK:
```bash
pip show fds-sdk-factsetanalyticsapi
```

Check the API documentation for the correct method names.

---

## Migration Checklist

- [ ] Backup current project
- [ ] Create new virtual environment
- [ ] Update requirements.txt: Remove old package
- [ ] Update requirements.txt: Add new package
- [ ] Run `pip install -r requirements.txt`
- [ ] Update all import statements
- [ ] Update API calls to use new modules
- [ ] Check Python compatibility (Python 3.6+)
- [ ] Fix any import errors
- [ ] Run tests (`pytest tests/`)
- [ ] Test application functionality
- [ ] Verify authentication works
- [ ] Check error handling
- [ ] Performance test (optional)
- [ ] Document changes (optional)
- [ ] Deploy to staging environment
- [ ] Verify in staging
- [ ] Deploy to production

---

## Critical Timeline - NO GRACE PERIOD

| Date | Action | Impact |
|------|--------|--------|
| **Aug 31, 2026** | ⏰ FINAL DAY | Last day to use Analytics SDK |
| **Sep 1, 2026** | 🚫 COMPLETE REMOVAL | ALL versions deleted from PyPI |
| **Sep 1+** | 📌 ENTERPRISE SDK ONLY | Only option for new installations |

**IMPORTANT**: There is NO grace period. Migration MUST be complete by Aug 31, 2026.

From Sep 1, 2026:
- ❌ Cannot download Analytics SDK
- ❌ Cannot restore package  
- ❌ Cannot add to new projects
- ✅ Enterprise SDK is the ONLY option

---

## ⚠️ MANDATORY REQUIREMENT

**Migration MUST be completed by August 31, 2026**

After Aug 31:
- ❌ Analytics SDK becomes completely unavailable
- ❌ No new installations possible
- ❌ No support or patches
- ✅ Enterprise SDK is the ONLY available option

---

## Getting Help - URGENT MIGRATION SUPPORT

### Critical Support
- **Email**: analytics.api.support@factset.com (Priority: MIGRATION)
- **Subject**: [URGENT] Analytics SDK Migration Required by Aug 31, 2026

### Documentation
- [Enterprise SDK GitHub](https://github.com/factset/enterprise-sdk/tree/main/code/python)
- [FactSet Developer Portal](https://developer.factset.com)
- [API Reference](https://developer.factset.com/api-catalog)

### Support
- **GitHub Issues**: https://github.com/factset/enterprise-sdk/issues

### Examples
- [Enterprise SDK Examples](https://github.com/factset/enterprise-sdk/tree/main/code/python/examples)
- [API Documentation](https://developer.factset.com)

### ⚠️ ACTION REQUIRED
**Do NOT wait** - Start migration immediately. Analytics SDK will be completely removed from PyPI on Sep 1, 2026.

---

## What's Different?

### Improvements in Enterprise SDK
✅ Better performance  
✅ Smaller package size  
✅ More frequent updates  
✅ Better error messages  
✅ Modern Python support (3.6+)  
✅ Comprehensive examples  
✅ Active support team  

### Key Changes
- Package name changed from `fds-sdk-analyticsapi-engines` to `fds-sdk-factsetanalyticsapi`
- Module path changed from `fds.analyticsapi.engines` to `fds.sdk.FactSetAnalyticsAPI`
- Same API classes and methods (backward compatible in functionality)
- Better error handling and validation

---

## Success Criteria

After migration, you should be able to:
✓ Install package without errors  
✓ Import all modules successfully  
✓ All tests pass  
✓ Application runs without errors  
✓ API calls return expected results  
✓ Error handling works correctly  
✓ Performance is equal or better  

---

**Migration Guide Version**: 1.0  
**Last Updated**: August 7, 2026  
**Status**: Ready for Use
