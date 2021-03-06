# This file is part of fedmsg.
# Copyright (C) 2015 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#
""" Tests for anitya messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestNewProject(Base):
    """ These messages are published when a new project is created on
    `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.project.new"
    expected_subti = 'pingou created a new project "foo"'
    expected_link = "https://pagure.io/foo"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo'])
    msg = {
      "i": 1,
      "timestamp": 1427445138,
      "msg_id": "2015-a37b0f13-aead-40eb-ab53-7af8e89e6854",
      "topic": "io.pagure.dev.pagure.project.new",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "agent": "pingou"
      }
    }


class TestNewIssue(Base):
    """ These messages are published when a ticket is opened against a
    project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.new"
    expected_subti = 'pingou opened a new ticket foo#4: "bug"'
    expected_link = "https://pagure.io/foo/issue/4"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 2,
      "timestamp": 1427445817,
      "msg_id": "2015-a9e8a8d6-6197-48b8-9fc9-a03967a9d4bb",
      "topic": "io.pagure.dev.pagure.issue.new",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "issue": {
          "status": "Open",
          "blocks": "",
          "title": "bug",
          "tags": [],
          "comments": [],
          "content": "report",
          "depends": "",
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestNewIssueComment(Base):
    """ These messages are published when a someone comments on a ticket
    opened against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.comment.added"
    expected_subti = 'pingou commented on ticket foo#4: "bug"'
    expected_link = "https://pagure.io/foo/issue/4#comment-380"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 1,
      "timestamp": 1427448698,
      "msg_id": "2015-539fc955-db5a-4bb5-a6a6-4a096a2d795d",
      "topic": "io.pagure.dev.pagure.issue.comment.added",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "issue": {
          "status": "Open",
          "blocks": "",
          "title": "bug",
          "tags": [],
          "comments": [
            {
              "comment": "We should really fix this",
              "date_created": "1427445097",
              "id": 380,
              "parent": None,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              }
            }
          ],
          "content": "report",
          "depends": "",
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestNewIssueTag(Base):
    """ These messages are published when a someone adds a tag on a ticket
    opened against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.tag.added"
    expected_subti = 'pingou tagged ticket foo#4: bug and easyfix'
    expected_link = "https://pagure.io/foo/issue/4"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 4,
      "timestamp": 1427449624,
      "msg_id": "2015-64ac444e-915c-4a6c-820b-59e8daf14584",
      "topic": "io.pagure.dev.pagure.issue.tag.added",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "tags": [
          "easyfix",
          "bug",
        ],
        "issue": {
          "status": "Open",
          "blocks": "",
          "title": "bug",
          "tags": [],
          "comments": [],
          "content": "report",
          "depends": "",
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestRemovedIssueTag(Base):
    """ These messages are published when a someone removes a tag on a
    ticket opened against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.tag.removed"
    expected_subti = 'pingou removed the feature and future tags from '\
        'ticket foo#4'
    expected_link = "https://pagure.io/foo/issue/4"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 4,
      "timestamp": 1427450043,
      "msg_id": "2015-e1921852-c269-4c08-a611-dffe5c39417f",
      "topic": "io.pagure.dev.pagure.issue.tag.removed",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "issue": {
          "status": "Open",
          "blocks": "",
          "title": "bug",
          "tags": "",
          "comments": [],
          "content": "report",
          "depends": "",
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou",
        "tags": [
          "feature",
          "future"
        ]
      }
    }


class TestAssignedIssue(Base):
    """ These messages are published when a someone is assigned to a
    ticket opened against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.assigned.added"
    expected_subti = 'pingou assigned ticket foo#4 to ralph'
    expected_link = "https://pagure.io/foo/issue/4"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 3,
      "timestamp": 1427450780,
      "msg_id": "2015-4ab5479a-1a99-4e26-a52f-e9e1ce423e40",
      "topic": "io.pagure.dev.pagure.issue.assigned.added",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "issue": {
          "status": "Open",
          "blocks": "",
          "title": "bug",
          "tags": [],
          "comments": [],
          "content": "report",
          "assignee": {
            "fullname": "Ralph",
            "emails": [
              "ralph@fedoraproject.org"
            ],
            "name": "ralph"
          },
          "depends": "",
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestResetAssignedIssue(Base):
    """ These messages are published when a someone is reset the assignee
    of a ticket opened against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.assigned.reset"
    expected_subti = 'pingou reset the assignee of ticket foo#4'
    expected_link = "https://pagure.io/foo/issue/4"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 3,
      "timestamp": 1427453148,
      "msg_id": "2015-bc20fa0e-8baa-4b6a-ac44-c30b9e579da3",
      "topic": "io.pagure.dev.pagure.issue.assigned.reset",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "issue": {
          "status": "Open",
          "blocks": "",
          "title": "bug",
          "tags": [],
          "comments": [],
          "content": "report",
          "assignee": None,
          "depends": "",
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestNewIssueDependency(Base):
    """ These messages are published when a someone is reset the assignee
    of a ticket opened against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.dependency.added"
    expected_subti = 'pingou added ticket foo#2 as a dependency of '\
    'ticket foo#4'
    expected_link = "https://pagure.io/foo/issue/2"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/2'])
    msg = {
      "i": 2,
      "timestamp": 1427453868,
      "msg_id": "2015-c8189e0c-ef22-4e72-92cc-9ffa68c35b7b",
      "topic": "io.pagure.dev.pagure.issue.dependency.added",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "issue": {
          "status": "Open",
          "blocks": [4],
          "title": "bug",
          "tags": [],
          "comments": [],
          "content": "report",
          "assignee": None,
          "depends": "",
          "private": False,
          "date_created": "1427442076",
          "id": 2,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "added_dependency": 4,
        "agent": "pingou"
      }
    }


class TestRemovedIssueDependency(Base):
    """ These messages are published when a someone is reset the assignee
    of a ticket opened against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.dependency.removed"
    expected_subti = 'pingou removed ticket foo#4 as a dependency of '\
    'ticket foo#2'
    expected_link = "https://pagure.io/foo/issue/4"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 3,
      "timestamp": 1427454576,
      "msg_id": "2015-cb2e1acd-c6c7-4da4-ba99-c136954bb039",
      "topic": "io.pagure.dev.pagure.issue.dependency.removed",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "removed_dependency": 2,
        "issue": {
          "status": "Open",
          "blocks": [],
          "title": "bug",
          "tags": [
            "0.1"
          ],
          "comments": [],
          "content": "report",
          "assignee": None,
          "depends": [],
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestIssueEdit(Base):
    """ These messages are published when a someone edited a ticket opened
    against a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.edit"
    expected_subti = 'pingou edited the private and status fields of '\
        'ticket foo#4'
    expected_link = "https://pagure.io/foo/issue/4"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo', 'issue/4'])
    msg = {
      "i": 5,
      "timestamp": 1427454847,
      "msg_id": "2015-5755ee3a-43ba-4552-9423-8fe3b0a96662",
      "topic": "io.pagure.dev.pagure.issue.edit",
      "msg": {
        "fields": [
          "status",
          "private"
        ],
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "issue": {
          "status": "Fixed",
          "blocks": [],
          "title": "bug",
          "tags": [
            "0.1"
          ],
          "comments": [],
          "content": "report",
          "assignee": None,
          "depends": [],
          "private": False,
          "date_created": "1427442217",
          "id": 4,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestProjectEdit(Base):
    """ These messages are published when a someone edited a project on
    `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.project.edit"
    expected_subti = 'pingou edited the project_docs fields of '\
        'project foo'
    expected_link = "https://pagure.io/foo"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo'])
    msg = {
      "i": 2,
      "timestamp": 1427455343,
      "msg_id": "2015-3b53c72a-8585-4ddc-ba60-d7e969a0acbb",
      "topic": "io.pagure.dev.pagure.project.edit",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": False,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "fields": [
          "project_docs"
        ],
        "agent": "pingou"
      }
    }


class TestProjectUserAdded(Base):
    """ These messages are published when a someone gave admins rights on a
    project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.project.user.added"
    expected_subti = 'pingou added "ralph" to project foo'
    expected_link = "https://pagure.io/foo"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo'])
    msg = {
      "i": 4,
      "timestamp": 1427455518,
      "msg_id": "2015-b3c2e568-259a-4b1f-9ecc-79493b89687a",
      "topic": "io.pagure.dev.pagure.project.user.added",
      "msg": {
        "new_user": "ralph",
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": False,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "agent": "pingou"
      }
    }


class TestProjectTagRemoved(Base):
    """ These messages are published when a someone removed a tag of a
    project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.project.tag.removed"
    expected_subti = 'pingou removed tags "easyfix1" from project foo'
    expected_link = "https://pagure.io/foo"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo'])
    msg = {
      "i": 5,
      "timestamp": 1427455744,
      "msg_id": "2015-c6db4dd3-0a87-4eee-aab7-7758f566f36e",
      "topic": "io.pagure.dev.pagure.project.tag.removed",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": False,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "agent": "pingou",
        "tags": [
          "easyfix1"
        ]
      }
    }


class TestProjectTagEdited(Base):
    """ These messages are published when a someone edited a tag of a
    project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.project.tag.edited"
    expected_subti = 'pingou altered tags on project foo from ' + \
        '"easyfix1" to "easyfix"'
    expected_link = "https://pagure.io/foo"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/foo'])
    msg = {
      "i": 2,
      "timestamp": 1427456487,
      "msg_id": "2015-79d76ac7-5c66-460d-8a39-17849e462a85",
      "topic": "io.pagure.dev.pagure.project.tag.edited",
      "msg": {
        "project": {
          "description": "bar",
          "parent": None,
          "project_docs": False,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427441537",
          "id": 7,
          "name": "foo"
        },
        "new_tag": "easyfix",
        "old_tag": "easyfix1",
        "agent": "pingou"
      }
    }


class TestProjectForked(Base):
    """ These messages are published when a someone edited a tag of a
    project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.project.forked"
    expected_subti = 'pingou forked project "fedmsg" to "pingou/fedmsg"'
    expected_link = "https://pagure.io/fork/pingou/fedmsg"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/pingou/fedmsg'])
    msg = {
      "i": 3,
      "timestamp": 1427456769,
      "msg_id": "2015-7ec8cd76-8ed7-4360-ac32-2e881273a7c2",
      "topic": "io.pagure.dev.pagure.project.forked",
      "msg": {
        "project": {
          "description": "",
          "parent": {
            "description": "",
            "parent": None,
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "ralph",
              "emails": [
                "ralph@fedoraproject.org"
              ],
              "name": "ralph"
            },
            "date_created": "1426595173",
            "id": 5,
            "name": "fedmsg"
          },
          "project_docs": True,
          "issue_tracker": True,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          },
          "date_created": "1427453169",
          "id": 8,
          "name": "fedmsg"
        },
        "agent": "pingou"
      }
    }


class TestNewPullRequestComment(Base):
    """ These messages are published when a someone commented on a
    pull-request of a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.pull-request.comment.added"
    expected_subti = 'pingou commented on pull-request#6 of '\
        'project "test"'
    expected_link = "https://pagure.io/test/pull-request/6#comment-16"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/test', 'pull-request/6'])
    msg = {
      "i": 2,
      "timestamp": 1427457362,
      "msg_id": "2015-cbf24329-b51c-4160-983c-ffa45ef63863",
      "topic": "io.pagure.dev.pagure.pull-request.comment.added",
      "msg": {
        "pullrequest": {
          "status": True,
          "branch_from": "master",
          "uid": "0a7d6b626b934511b6355dd48926916a",
          "title": "test request",
          "commit_start": "788efeaaf86bde8618f594a8181abb402e1dd904",
          "project": {
            "description": "test project",
            "parent": None,
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426500194",
            "id": 1,
            "name": "test"
          },
          "commit_stop": "5ca3e1c7ccff3327ebeb2f07eaa9bf3820d3f5c8",
          "repo_from": {
            "description": "test project",
            "parent": {
              "description": "test project",
              "parent": None,
              "project_docs": True,
              "issue_tracker": True,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              },
              "date_created": "1426500194",
              "id": 1,
              "name": "test"
            },
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426843440",
            "id": 6,
            "name": "test"
          },
          "comments": [
            {
              "comment": "This is looking good!",
              "parent": None,
              "filename": None,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              },
              "commit": None,
              "date_created": "1427453701",
              "line": None,
              "id": 16
            }
          ],
          "branch": "master",
          "date_created": "1426843718",
          "id": 6,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestNewPullRequestclosed(Base):
    """ These messages are published when a someone closed a pull-request
    of a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.pull-request.closed"
    expected_subti = 'pingou closed (without merging) pull-request#6 '\
        'of project "test"'
    expected_link = "https://pagure.io/test/pull-request/6"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/test', 'pull-request/6'])
    msg = {
      "i": 2,
      "timestamp": 1427458544,
      "msg_id": "2015-c9636fda-3a4c-452b-85ee-870e29f63a03",
      "topic": "io.pagure.dev.pagure.pull-request.closed",
      "msg": {
        "pullrequest": {
          "status": False,
          "branch_from": "master",
          "uid": "0a7d6b626b934511b6355dd48926916a",
          "title": "test request",
          "commit_start": "788efeaaf86bde8618f594a8181abb402e1dd904",
          "project": {
            "description": "test project",
            "parent": None,
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426500194",
            "id": 1,
            "name": "test"
          },
          "commit_stop": "5ca3e1c7ccff3327ebeb2f07eaa9bf3820d3f5c8",
          "repo_from": {
            "description": "test project",
            "parent": {
              "description": "test project",
              "parent": None,
              "project_docs": True,
              "issue_tracker": True,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              },
              "date_created": "1426500194",
              "id": 1,
              "name": "test"
            },
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426843440",
            "id": 6,
            "name": "test"
          },
          "comments": [
            {
              "comment": "Sorry but this won't do",
              "parent": None,
              "filename": None,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              },
              "commit": None,
              "date_created": "1427453701",
              "line": None,
              "id": 16
            },
          ],
          "branch": "master",
          "date_created": "1426843718",
          "id": 6,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou",
        "merged": False
      }
    }


class TestNewPullRequestMerged(Base):
    """ These messages are published when a someone merged a pull-request
    of a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.pull-request.closed"
    expected_subti = 'pingou merged pull-request#7 of project "test"'
    expected_link = "https://pagure.io/test/pull-request/7"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/test', 'pull-request/7'])
    msg = {
      "i": 3,
      "timestamp": 1427458778,
      "msg_id": "2015-22ec6669-91fe-4c32-b324-db80fba696dd",
      "topic": "io.pagure.dev.pagure.pull-request.closed",
      "msg": {
        "pullrequest": {
          "status": False,
          "branch_from": "master",
          "uid": "d4182a2ac2d541d884742d3037c26e56",
          "title": "test request",
          "commit_start": "788efeaaf86bde8618f594a8181abb402e1dd904",
          "project": {
            "description": "test project",
            "parent": None,
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426500194",
            "id": 1,
            "name": "test"
          },
          "commit_stop": "5ca3e1c7ccff3327ebeb2f07eaa9bf3820d3f5c8",
          "repo_from": {
            "description": "test project",
            "parent": {
              "description": "test project",
              "parent": None,
              "project_docs": True,
              "issue_tracker": True,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              },
              "date_created": "1426500194",
              "id": 1,
              "name": "test"
            },
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426843440",
            "id": 6,
            "name": "test"
          },
          "comments": [
            {
              "comment": "awesome!",
              "parent": None,
              "filename": "test",
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              },
              "commit": "fa72f315373ec5f98f2b08c8ffae3645c97aaad2",
              "date_created": "1426843778",
              "line": 5,
              "id": 1
            }
          ],
          "branch": "master",
          "date_created": "1426843732",
          "id": 7,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou",
        "merged": True
      }
    }


class TestNewPullRequestNew(Base):
    """ These messages are published when a someone opens a new pull-request
    on a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.pull-request.new"
    expected_subti = 'pingou opened pull-request#21: "Improve loading '\
        'speed" on project "test"'
    expected_link = "https://pagure.io/test/pull-request/21"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/test', 'pull-request/21'])
    msg = {
      "i": 4,
      "timestamp": 1427459070,
      "msg_id": "2015-1f03dc6a-3a0b-4b09-a06d-e4ca7d374729",
      "topic": "io.pagure.dev.pagure.pull-request.new",
      "msg": {
        "pullrequest": {
          "status": True,
          "branch_from": "test",
          "uid": "2bf721f0fbd34977aab78b5e1959e504",
          "title": "Improve loading speed",
          "commit_start": None,
          "project": {
            "description": "test project",
            "parent": None,
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426500194",
            "id": 1,
            "name": "test"
          },
          "commit_stop": None,
          "repo_from": {
            "description": "test project",
            "parent": {
              "description": "test project",
              "parent": None,
              "project_docs": True,
              "issue_tracker": True,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "emails": [
                  "pingou@fedoraproject.org"
                ],
                "name": "pingou"
              },
              "date_created": "1426500194",
              "id": 1,
              "name": "test"
            },
            "project_docs": True,
            "issue_tracker": True,
            "user": {
              "fullname": "Pierre-YvesChibon",
              "emails": [
                "pingou@fedoraproject.org"
              ],
              "name": "pingou"
            },
            "date_created": "1426843440",
            "id": 6,
            "name": "test"
          },
          "comments": [],
          "branch": "master",
          "date_created": "1427455470",
          "id": 21,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "emails": [
              "pingou@fedoraproject.org"
            ],
            "name": "pingou"
          }
        },
        "agent": "pingou"
      }
    }


class TestPullRequestFlagAdded(Base):
    """ These messages are published when a someone flags a pull-request
    on a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.pull-request.flag.added"
    expected_subti = 'Jenkins flagged test#1 with "Tests failed"'
    expected_link = "https://pagure.io/test/pull-request/1"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/test', 'pull-request/1'])
    msg = {
          "username": "pingou",
          "i": 3,
          "timestamp": 1433167960,
          "msg_id": "2015-e7094e2a-1259-49da-91f5-635e81011ffa",
          "topic": "io.pagure.dev.pagure.pull-request.flag.added",
          "msg": {
            "flag": {
              "comment": "Tests failed",
              "username": "Jenkins",
              "uid": "jenkins_build_pagure_100+seed",
              "url": "http://jenkins.cloud.fedoraproject.org/",
              "percent": "0",
              "pull_request_uid": "cb0cc178203046fe86f675779b31b913",
              "user": {
                "fullname": "PY C",
                "default_email": "bar@pingou.com",
                "emails": [
                  "bar@pingou.com",
                  "foo@pingou.com"
                ],
                "name": "pingou"
              },
              "date_created": "1433160759"
            },
            "pullrequest": {
              "status": True,
              "branch_from": "master",
              "uid": "cb0cc178203046fe86f675779b31b913",
              "title": "test pull-request",
              "commit_start": None,
              "project": {
                "description": "test project #1",
                "parent": None,
                "settings": {
                  "Minimum_score_to_merge_pull-request": -1,
                  "Web-hooks": None,
                  "project_documentation": True,
                  "pull_requests": True,
                  "Only_assignee_can_merge_pull-request": False,
                  "issue_tracker": True
                },
                "user": {
                  "fullname": "PY C",
                  "default_email": "bar@pingou.com",
                  "emails": [
                    "bar@pingou.com",
                    "foo@pingou.com"
                  ],
                  "name": "pingou"
                },
                "date_created": "1433160759",
                "id": 1,
                "name": "test"
              },
              "commit_stop": None,
              "repo_from": {
                "description": "test project #1",
                "parent": None,
                "settings": {
                  "Minimum_score_to_merge_pull-request": -1,
                  "Web-hooks": None,
                  "project_documentation": True,
                  "pull_requests": True,
                  "Only_assignee_can_merge_pull-request": False,
                  "issue_tracker": True
                },
                "user": {
                  "fullname": "PY C",
                  "default_email": "bar@pingou.com",
                  "emails": [
                    "bar@pingou.com",
                    "foo@pingou.com"
                  ],
                  "name": "pingou"
                },
                "date_created": "1433160759",
                "id": 1,
                "name": "test"
              },
              "assignee": None,
              "comments": [],
              "branch": "master",
              "date_created": "1433160759",
              "id": 1,
              "user": {
                "fullname": "PY C",
                "default_email": "bar@pingou.com",
                "emails": [
                  "bar@pingou.com",
                  "foo@pingou.com"
                ],
                "name": "pingou"
              }
            },
            "agent": "pingou"
          }
        }


class TestPullRequestFlagUpdated(Base):
    """ These messages are published when a someone updates a flag on a
    pull-request on a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.pull-request.flag.updated"
    expected_subti = 'Jenkins updated the flags on test#1 with: '\
        '"Tests passed"'
    expected_link = "https://pagure.io/test/pull-request/1"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/test', 'pull-request/1'])
    msg = {
          "username": "pingou",
          "i": 4,
          "timestamp": 1433167960,
          "msg_id": "2015-e7094e2a-1259-49da-91f5-635e81011ffa",
          "topic": "io.pagure.dev.pagure.pull-request.flag.updated",
          "msg": {
            "flag": {
              "comment": "Tests passed",
              "username": "Jenkins",
              "uid": "jenkins_build_pagure_101+seed",
              "url": "http://jenkins.cloud.fedoraproject.org/",
              "percent": "100",
              "pull_request_uid": "cb0cc178203046fe86f675779b31b913",
              "user": {
                "fullname": "PY C",
                "default_email": "bar@pingou.com",
                "emails": [
                  "bar@pingou.com",
                  "foo@pingou.com"
                ],
                "name": "pingou"
              },
              "date_created": "1433160759"
            },
            "pullrequest": {
              "status": True,
              "branch_from": "master",
              "uid": "cb0cc178203046fe86f675779b31b913",
              "title": "test pull-request",
              "commit_start": None,
              "project": {
                "description": "test project #1",
                "parent": None,
                "settings": {
                  "Minimum_score_to_merge_pull-request": -1,
                  "Web-hooks": None,
                  "project_documentation": True,
                  "pull_requests": True,
                  "Only_assignee_can_merge_pull-request": False,
                  "issue_tracker": True
                },
                "user": {
                  "fullname": "PY C",
                  "default_email": "bar@pingou.com",
                  "emails": [
                    "bar@pingou.com",
                    "foo@pingou.com"
                  ],
                  "name": "pingou"
                },
                "date_created": "1433160759",
                "id": 1,
                "name": "test"
              },
              "commit_stop": None,
              "repo_from": {
                "description": "test project #1",
                "parent": None,
                "settings": {
                  "Minimum_score_to_merge_pull-request": -1,
                  "Web-hooks": None,
                  "project_documentation": True,
                  "pull_requests": True,
                  "Only_assignee_can_merge_pull-request": False,
                  "issue_tracker": True
                },
                "user": {
                  "fullname": "PY C",
                  "default_email": "bar@pingou.com",
                  "emails": [
                    "bar@pingou.com",
                    "foo@pingou.com"
                  ],
                  "name": "pingou"
                },
                "date_created": "1433160759",
                "id": 1,
                "name": "test"
              },
              "assignee": None,
              "comments": [],
              "branch": "master",
              "date_created": "1433160759",
              "id": 1,
              "user": {
                "fullname": "PY C",
                "default_email": "bar@pingou.com",
                "emails": [
                  "bar@pingou.com",
                  "foo@pingou.com"
                ],
                "name": "pingou"
              }
            },
            "agent": "pingou"
          }
        }


class TestGitCommit(Base):
    """ These messages are published when a someone updates a flag on a
    pull-request on a project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.git.receive"
    expected_subti = 'pingou pushed to pagure (bleach). '\
        '"Use the default attributes for bleach and then add our own"'
    expected_link = "https://pagure.io/pagure/131e07ed2538839d509880a011cd7d55c0967171"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['project/pagure'])
    msg = {
        'i': 1,
        'msg': {
            'commit': {
                'agent': 'git',
                'branch': 'refs/heads/bleach',
                'email': 'pingou@fedoraproject.org',
                'message': 'Use the default attributes for bleach and then add our own',
                'name': 'Pierre-Yves Chibon',
                'path': '/srv/git/repositories/pagure.git',
                'repo': {
                    'date_created': '1431549490',
                    'description': 'A git centered forge',
                    'id': 10,
                    'name': 'pagure',
                    'parent': None,
                    'settings': {
                        'Minimum_score_to_merge_pull-request': -1,
                        'Only_assignee_can_merge_pull-request': False,
                        'Web-hooks': None,
                        'issue_tracker': True,
                        'project_documentation': True,
                        'pull_requests': True},
                        'user': {
                            'fullname': 'Pierre-YvesChibon',
                            'name': 'pingou'
                        }
                },
                'rev': '131e07ed2538839d509880a011cd7d55c0967171',
                'seen': False,
                'stats': {
                    'files': {
                        'pagure/ui/filters.py': {
                            'additions': 4,
                            'deletions': 4,
                            'lines': 8
                        }
                    },
                    'total': {
                        'additions': 4,
                        'deletions': 4,
                        'files': 1,
                        'lines': 8
                    }
                },
                'summary': 'Use the default attributes for bleach and then add our own',
                'username': None}},
         'msg_id': '2015-c6561fe2-3815-469c-a288-8f36cf8fdda3',
         'source_name': 'datanommer',
         'source_version': '0.6.5',
         'timestamp': 1434213042.0,
         'topic': 'io.pagure.prod.pagure.git.receive'
    }

class TestIssueDrop(Base):
    """ These messages are published when a ticket is deleted against a
    project on `pagure <https://pagure.io>`_.
    """
    expected_title = "pagure.issue.drop"
    expected_subti = 'yangl1996 deleted ticket docs-test#42: "foobar"'
    expected_link = "https://pagure.io/docs-test/issue/42"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "4535d62cac804e6e0cb25386c9a7701e680deb176efa79829d076fc63c2b96e7" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['yangl1996'])
    expected_objects = set(['project/docs-test', 'issue/42'])
    msg = {
        'source_name': 'datanommer',
        'i': 1,
        'timestamp': 1434790435.0,
        'msg_id': '2015-9ab3ba70-02aa-4034-a532-8791696165fd',
        'topic': 'io.pagure.prod.pagure.issue.drop',
        'source_version': '0.6.5',
        'msg': {
            'project': {
                'description': '',
                'parent': None,
                'settings': {
                    'Minimum_score_to_merge_pull-request': '-1',
                    'Web-hooks': 'http://128.199.82.190:7655',
                    'project_documentation': 'y',
                    'pull_requests': 'y',
                    'Enforce_signed-off_commits_in_pull-request': False,
                    'Only_assignee_can_merge_pull-request': False,
                    'issue_tracker': 'y'
                },
                'user': {
                    'fullname': 'Lei Yang',
                    'name': 'yangl1996'
                },
                'date_created': '1434262409',
                'id': 78,
                'name': 'docs-test'
            },
            'issue': {
                'status': 'Open',
                'blocks': [],
                'tags': [],
                'title': 'foobar',
                'comments': [],
                'content': 'report',
                'assignee': None,
                'depends': [],
                'private': False,
                'date_created': '1434789890',
                'id': 42,
                'user': {
                    'fullname': 'Lei Yang',
                    'name': 'yangl1996'
                }
            },
            'agent': 'yangl1996'
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
