"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

custom_ioa - Falcon Custom Indicators of Attack API Interface Class

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
from ._util import parse_id_list, force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._custom_ioa import _custom_ioa_endpoints as Endpoints


class CustomIOA(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_patterns(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get pattern severities by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-patterns
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_patterns",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_platforms(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get platforms by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-platformsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_platformsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rule groups by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-groupsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rule_groupsMixin0",
            keywords=kwargs,
            params=parameters
            )

    def create_rule_group(self: object,
                          body: dict,
                          cs_username: str = None  # pylint: disable=W0613  # cs_username is deprecated
                          ) -> dict:
        """
        Create a rule group for a platform with a name and an optional description. Returns the rule group.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule-groupMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_rule_groupMixin0",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groups(self: object,
                           cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                           parameters: dict = None,
                           **kwargs) -> dict:
        """
        Delete rule groups by ID.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rule-groupsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_rule_groupsMixin0",
            keywords=kwargs,
            params=parameters
            )

    def update_rule_group(self: object,
                          body: dict,
                          cs_username: str = None  # pylint: disable=W0613  # cs_username is deprecated
                          ) -> dict:
        """
        Update a rule group. The following properties can be modified: name, description, enabled.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rule-groupMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rule_groupMixin0",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_types(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rule types by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-types
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rule_types",
            keywords=kwargs,
            params=parameters
            )

    def get_rules_get(self: object, ids) -> dict:
        """
        Get rules by ID and optionally version in the following format: ID[:version]
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rules-get
        body_payload = {}
        body_payload["ids"] = parse_id_list(ids).split(",")
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rules_get",
            body=body_payload
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rules by ID and optionally version in the following format: ID[:version].
        The max number of IDs is constrained by URL size.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rulesMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rulesMixin0",
            keywords=kwargs,
            params=parameters
            )

    def create_rule(self: object,
                    body: dict,
                    cs_username: str = None  # pylint: disable=W0613  # cs_username is deprecated
                    ) -> dict:
        """
        Create a rule within a rule group. Returns the rule.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_rule",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rules(self: object,
                     cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                     parameters: dict = None,
                     **kwargs
                     ) -> dict:
        """
        Delete rules from a rule group by ID.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rules
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_rules",
            keywords=kwargs,
            params=parameters
            )

    def update_rules(self: object,
                     body: dict,
                     cs_username: str = None  # pylint: disable=W0613  # cs_username is deprecated
                     ) -> dict:
        """
        Update rules within a rule group. Return the updated rules.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rules
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rules",
            body=body
            )

    def validate(self: object, body: dict) -> dict:
        """
        Validates field values and checks for matches if a test string is provided.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/validate
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="validate",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_patterns(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get all pattern severity IDs
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-patterns
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_patterns",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_platforms(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get all platform IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-platformsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_platformsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups_full(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find all rule groups matching the query with optional filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groups-full
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_groups_full",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Finds all rule group IDs matching the query with optional filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groupsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_groupsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_types(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get all rule type IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-types
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_types",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Finds all rule IDs matching the query with optional filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rulesMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rulesMixin0",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    get_platformsMixin0 = get_platforms
    get_rule_groupsMixin0 = get_rule_groups
    create_rule_groupMixin0 = create_rule_group
    delete_rule_groupMixin0 = delete_rule_groups  # Typo fix
    delete_rule_groupsMixin0 = delete_rule_groups
    update_rule_groupMixin0 = update_rule_group
    get_rulesMixin0 = get_rules
    query_platformsMixin0 = query_platforms
    query_rule_groupsMixin0 = query_rule_groups
    query_rulesMixin0 = query_rules


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Custom_IOA = CustomIOA  # pylint: disable=C0103
