"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_endpoint._user_management - Internal API endpoint constant library

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

_user_management_endpoints = [
  [
    "GetRoles",
    "GET",
    "/user-roles/entities/user-roles/v1?ids={}",
    "Get info about a role",
    "user_management",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "ID of a role. Find a role ID from `/customer/queries/roles/v1` or `/users/queries/roles/v1`.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GrantUserRoleIds",
    "POST",
    "/user-roles/entities/user-roles/v1",
    "Assign one or more roles to a user",
    "user_management",
    [
      {
        "type": "string",
        "description": "ID of a user. Find a user's ID from `/users/entities/user/v1`.",
        "name": "user_uuid",
        "in": "query",
        "required": True
      },
      {
        "description": "Role ID(s) of the role you want to assign",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "RevokeUserRoleIds",
    "DELETE",
    "/user-roles/entities/user-roles/v1?ids={}",
    "Revoke one or more roles from a user",
    "user_management",
    [
      {
        "type": "string",
        "description": "ID of a user. Find a user's ID from `/users/entities/user/v1`.",
        "name": "user_uuid",
        "in": "query",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more role IDs to revoke. Find a role's ID from `/users/queries/roles/v1`.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetAvailableRoleIds",
    "GET",
    "/user-roles/queries/user-role-ids-by-cid/v1",
    "Show role IDs for all roles available in your customer account. For more information on each role, "
    "provide the role ID to `/customer/entities/roles/v1`.",
    "user_management",
    []
  ],
  [
    "GetUserRoleIds",
    "GET",
    "/user-roles/queries/user-role-ids-by-user-uuid/v1",
    "Show role IDs of roles assigned to a user. For more information on each role, provide the role ID to "
    "`/customer/entities/roles/v1`.",
    "user_management",
    [
      {
        "type": "string",
        "description": "ID of a user. Find a user's ID from `/users/entities/user/v1`.",
        "name": "user_uuid",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "RetrieveUser",
    "GET",
    "/users/entities/users/v1?ids={}",
    "Get info about a user",
    "user_management",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "ID of a user. Find a user's ID from `/users/entities/user/v1`.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "CreateUser",
    "POST",
    "/users/entities/users/v1",
    "Create a new user. After creating a user, assign one or more roles with POST /user-roles/entities/user-roles/v1",
    "user_management",
    [
      {
        "description": "Attributes for this user. `uid` (required) is the user's email address, which is their username "
        "in Falcon.\n\nOptional attributes:\n\n<ul><li>`firstName`</li><li>`lastName`</li><li>`password`</li></ul>\n\n"
        "As a best practice, we recommend omitting `password`. If single sign-on is enabled for your customer account, "
        "the `password` attribute is ignored. If single sign-on is not enabled, we send a user activation request to their "
        "email address when you create the user with no `password`. The user should use the activation email to set their "
        "own password.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateUser",
    "PATCH",
    "/users/entities/users/v1",
    "Modify an existing user's first or last name",
    "user_management",
    [
      {
        "type": "string",
        "description": "ID of a user. Find a user's ID from `/users/entities/user/v1`.",
        "name": "user_uuid",
        "in": "query",
        "required": True
      },
      {
        "description": "Attributes for this user. All attributes (shown below) are optional.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteUser",
    "DELETE",
    "/users/entities/users/v1",
    "Delete a user permanently",
    "user_management",
    [
      {
        "type": "string",
        "description": "ID of a user. Find a user's ID from `/users/entities/user/v1`.",
        "name": "user_uuid",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "RetrieveEmailsByCID",
    "GET",
    "/users/queries/emails-by-cid/v1",
    "List the usernames (usually an email address) for all users in your customer account",
    "user_management",
    []
  ],
  [
    "RetrieveUserUUIDsByCID",
    "GET",
    "/users/queries/user-uuids-by-cid/v1",
    "List user IDs for all users in your customer account. For more information on each user, "
    "provide the user ID to `/users/entities/user/v1`.",
    "user_management",
    []
  ],
  [
    "RetrieveUserUUID",
    "GET",
    "/users/queries/user-uuids-by-email/v1",
    "Get a user's ID by providing a username (usually an email address)",
    "user_management",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "A username. This is usually the user's email address, but may vary based on your configuration.",
        "name": "uid",
        "in": "query",
        "required": True
      }
    ]
  ]
]
