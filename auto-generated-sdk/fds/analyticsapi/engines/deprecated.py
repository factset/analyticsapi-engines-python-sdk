"""
This module provides deprecation warnings to SDK consumers
"""

from datetime import datetime


class AnalyticsSdkDeprecationNotice:
    """
    Deprecation notice for the Analytics SDK
    """

    DEPRECATION_DATE = datetime(2026, 8, 31)
    REPLACEMENT_PACKAGE = "fds-sdk-factsetanalyticsapi"
    MIGRATION_GUIDE_URL = "https://github.com/factset/enterprise-sdk"

    DEPRECATION_MESSAGE = (
        "The Analytics SDK is deprecated effective 31-Aug-2026. "
        "Please migrate to the Enterprise SDK (fds-sdk-factsetanalyticsapi). "
        "See https://github.com/factset/enterprise-sdk for details."
    )

    def __init__(self):
        """Private constructor to prevent instantiation"""
        raise RuntimeError("AnalyticsSdkDeprecationNotice is a utility class and should not be instantiated")


__all__ = ["AnalyticsSdkDeprecationNotice"]
