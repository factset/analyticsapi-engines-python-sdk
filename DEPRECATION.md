# Analytics SDK Python - Deprecation Notice

**Status**: ⚠️ **DEPRECATED** - Effective August 31, 2026

---

## Important Notice

The **FactSet Analytics SDK for Python** (`fds.analyticsapi.engines`) is **officially deprecated** as of **August 31, 2026**.

### Timeline

| Date | Status | Action |
|------|--------|--------|
| **Until Aug 31, 2026** | Active | Limited security fixes only |
| **Aug 31, 2026** | Final Release | Last day of support - FINAL DATE |
| **Sep 1, 2026+** | Removed | ALL versions removed from PyPI - Enterprise SDK REQUIRED |

### What This Means

✅ **Existing Projects**: Continue to work (installed before Sep 1)  
❌ **New Projects**: Cannot install Analytics SDK from Sep 1, 2026 onwards  
❌ **New Installs**: IMPOSSIBLE after Aug 31, 2026 - Enterprise SDK ONLY  
⚠️ **Security Issues**: NO patches after Aug 31, 2026  
🔄 **Migration REQUIRED**: Must complete migration by Aug 31, 2026

---

## Migration Required

### Why Migrate?

- **Long-term Support**: Enterprise SDK is the actively maintained solution
- **New Features**: Enterprise SDK receives regular updates and features
- **Security**: Security patches provided for years to come
- **Support**: Dedicated support team for enterprise deployments

### How to Migrate

#### Step 1: Review Current Usage

```python
# Identify all code using the Analytics SDK
from fds.analyticsapi.engines.api import PaEngineApi, SparEngineApi, VaultApi
from fds.analyticsapi.engines.model import *
```

#### Step 2: Update Requirements File

```ini
# OLD: Analytics SDK (Deprecated)
fds-sdk-analyticsapi-engines==6.1.1

# NEW: Enterprise SDK
fds-sdk-factsetanalyticsapi==1.0.0
```

#### Step 3: Update Imports

```python
# OLD: Analytics SDK
from fds.analyticsapi.engines.api import PaEngineApi, SparEngineApi, VaultApi
from fds.analyticsapi.engines.model import *

# NEW: Enterprise SDK
from fds.sdk.FactSetAnalyticsAPI.api import PaEngineApi, SparEngineApi, VaultApi
from fds.sdk.FactSetAnalyticsAPI.model import *
```

#### Step 4: Update API Calls

Refer to the [Migration Guide](./MIGRATION.md) for specific API changes.

### Installation Methods

**pip:**
```bash
pip install fds-sdk-factsetanalyticsapi==1.0.0
```

**requirements.txt:**
```
fds-sdk-factsetanalyticsapi==1.0.0
```

**pipenv:**
```bash
pipenv install fds-sdk-factsetanalyticsapi==1.0.0
```

---

## Key Dates

### FINAL DATE: August 31, 2026
**LAST DAY** for Analytics SDK support and availability

### From September 1, 2026
- ✂️ **ALL versions REMOVED from PyPI**
- 🚫 **NO new installations possible**
- 🚫 **NO package discovery on PyPI**
- ⚠️ **Only Enterprise SDK available**
- 📦 **Existing installations continue to work (cached versions)**

### Migration Window
- **Start**: Now
- **Deadline**: August 31, 2026
- **After Deadline**: Enterprise SDK REQUIRED for any new projects or installations

---

## FAQ

### Q: Will my existing project break after Aug 31?
**A**: No, existing installations will continue to work. However, you won't be able to install new versions or restore on new machines without having cached versions.

### Q: What if I don't migrate by Aug 31?
**A**: CRITICAL - After Aug 31, you CANNOT:
- ❌ Install Analytics SDK from PyPI (removed)
- ❌ Add package to new projects
- ❌ Restore on new virtual environments without cached version
- ❌ Get any security patches or support

**Only Option**: Migrate to Enterprise SDK immediately after Aug 31

### Q: Is the Enterprise SDK a replacement?
**A**: Yes, the Enterprise SDK is the recommended replacement. It provides:
- Same functionality
- Better performance
- Active maintenance
- Long-term support

### Q: How long do I have to migrate?
**A**: You have until **August 31, 2026** ONLY:
- ✅ Until Aug 31: Analytics SDK available from PyPI
- ❌ From Sep 1: ALL versions REMOVED from PyPI
- ⚠️ No grace period - complete removal on Sep 1

### Q: Do I need to change my code?
**A**: Minor changes may be required. See [Migration Guide](./MIGRATION.md).

### Q: Can I still use my cached version?
**A**: Yes, if you have it installed or cached locally. After unlisting, you cannot download it from PyPI unless you explicitly specify the version from cache.

### Q: What about support?
**A**: Limited support available until Aug 31, 2026. After that date, support team will focus on Enterprise SDK.

---

## Support & Resources

### Migration Assistance
- **Enterprise SDK GitHub**: https://github.com/factset/enterprise-sdk/tree/main/code/python
- **Migration Guide**: https://developer.factset.com
- **Email Support**: analytics.api.support@factset.com

### Repositories
- **Analytics SDK (This Repo)**: https://github.com/factset/analyticsapi-engines-python-sdk
- **Enterprise SDK**: https://github.com/factset/enterprise-sdk
- **API Documentation**: https://developer.factset.com/api-catalog

---

## Affected APIs

This deprecation affects the following FactSet Analytics APIs:

- **PA Engine API** - Portfolio Analysis
- **SPAR Engine API** - Style Performance Attribution
- **Vault API** - Portfolio Management

All functionality is available in the Enterprise SDK with improved performance and support.

---

## Questions?

If you have questions about the deprecation or migration:

1. Check the [Migration Guide](./MIGRATION.md)
2. Review [Deprecation Documentation](./DEPRECATION.md)
3. Contact: **analytics.api.support@factset.com**

---

**Last Updated**: August 7, 2026  
**Deprecation Effective Date**: August 31, 2026  
**Status**: In Effect
