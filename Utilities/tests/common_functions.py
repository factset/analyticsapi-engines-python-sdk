from fds.analyticsapi.engines.configuration import Configuration
from fds.analyticsapi.engines.api_client import ApiClient

import common_parameters

class CommonFunctions:

    @staticmethod
    def build_api_client():
        if (common_parameters.user_name and common_parameters.password):
            config = Configuration()
            config.host = common_parameters.base_url
            config.username = common_parameters.user_name
            config.password = common_parameters.password
            config.verify_ssl = False

            return ApiClient(config)

        raise ValueError("Please set ANALYTICS_API_USERNAME_SERIAL and ANALYTICS_API_PASSWORD environment variables.")
