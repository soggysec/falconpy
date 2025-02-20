"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

iocs - CrowdStrike Falcon Indicators of Compromise API interface class

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
# The bulk of the methods within this class have been deprecated. Those
# that are not, have been ported into the new IOC Service Class. Developers
# should move all code over to use this new class (ioc.py) as support for
# this class will eventually be dropped.
# pylint: disable=W0613,R0201   # Allowing unused params and kwargs to prevent breaking change, no self use is ok
from ._util import force_default, handle_single_argument, process_service_request, generate_error_result
from ._service_class import ServiceClass
from ._endpoint._iocs import _iocs_endpoints as Endpoints


class Iocs(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_count(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Number of hosts in your customer account that have observed a given custom IOC.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesCount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DevicesCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ioc(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get an IOC by providing a type and value.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/GetIOC

        # * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
        # This API endpoint is no longer available. Please use the new IOC.indicator_get
        # method defined in the new IOC service class in order to perform this operation.

        return generate_error_result(
            "This method has been deprecated. Please use the new IOC Service Class method "
            "IOC.indicator_get to perform this operation."
            )

    def create_ioc(self: object, body: dict) -> dict:
        """
        Create a new IOC.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/CreateIOC

        # * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
        # This API endpoint is no longer available. Please use the new IOC.indicator_create
        # method defined in the new IOC service class in order to perform this operation.

        return generate_error_result(
            "This method has been deprecated. Please use the new IOC Service Class method "
            "IOC.indicator_create to perform this operation."
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_ioc(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete an IOC by providing a type and value.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DeleteIOC

        # * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
        # This API endpoint is no longer available. Please use the new IOC.indicator_delete
        # method defined in the new IOC service class in order to perform this operation.

        return generate_error_result(
            "This method has been deprecated. Please use the new IOC Service Class method "
            "IOC.indicator_delete to perform this operation."
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_ioc(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Update an IOC by providing a type and value.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/UpdateIOC

        # * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
        # This API endpoint is no longer available. Please use the new IOC.indicator_update
        # method defined in the new IOC service class in order to perform this operation.

        return generate_error_result(
            "This method has been deprecated. Please use the new IOC Service Class method "
            "IOC.indicator_update to perform this operation."
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find hosts that have observed a given custom IOC.
        For details about those hosts, use the hosts API interface.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesRanOn
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DevicesRanOn",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_iocs(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search the custom IOCs in your customer account.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/QueryIOCs

        # * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
        # This API endpoint is no longer available. Please use the new IOC.indicator_search
        # method defined in the new IOC service class in order to perform this operation.

        return generate_error_result(
            "This method has been deprecated. Please use the new IOC Service Class method "
            "IOC.indicator_search to perform this operation."
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def processes_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for processes associated with a custom IOC
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/ProcessesRanOn
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ProcessesRanOn",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_processes(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        For the provided ProcessID retrieve the process details.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/entities.processes
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_processes",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    DevicesCount = devices_count
    GetIOC = get_ioc
    CreateIOC = create_ioc
    DeleteIOC = delete_ioc
    UpdateIOC = update_ioc
    DevicesRanOn = devices_ran_on
    QueryIOCs = query_iocs
    ProcessesRanOn = processes_ran_on
