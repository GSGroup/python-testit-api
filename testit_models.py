# Copyright (c) "Сifra" LLC, 2022, https://github.com/GSGroup
# Permission to use, copy, modify, and/or distribute this software
# for any purpose with or without fee is hereby granted,
# provided that the above copyright notice and this permission notice appear in all copies.
# THE SOFTWARE IS PROVIDED "AS IS" AND GS GROUP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
# IN NO EVENT SHALL GS GROUP BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES
# OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
# ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

AutoTestPostModel = {
  "workItemIdsForLinkWithAutoTest": [
    "uuid"
  ],
  "shouldCreateWorkItem": "boolean",
  "externalId": "string",
  "links": [
    {
      "title": "string",
      "url": "string",
      "description": "string",
      "type": "choose one from: Related | BlockedBy | Defect | Issue | Requirement | Repository",
      "hasInfo": "boolean"
    }
  ],
  "projectId": "string",
  "name": "string",
  "namespace": "string",
  "classname": "string",
  "steps": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "setup": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "teardown": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "title": "string",
  "description": "string",
  "labels": [
    {
      "name": "string"
    }
  ],
  "isFlaky": "boolean"
}
AutoTestPutModel = {
  "id": "string",
  "workItemIdsForLinkWithAutoTest": [
    "uuid"
  ],
  "externalId": "string",
  "links": [
    {
      "id": "string",
      "title": "string",
      "url": "string",
      "description": "string",
      "type": "choose one from: Related | BlockedBy | Defect | Issue | Requirement | Repository",
      "hasInfo": "boolean"
    }
  ],
  "projectId": "string",
  "name": "string",
  "namespace": "string",
  "classname": "string",
  "steps": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "setup": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "teardown": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "title": "string",
  "description": "string",
  "labels": [
    {
      "name": "string"
    }
  ],
  "isFlaky": "boolean"
}
AutoTestResultsForTestRunModel = {
  "configurationId": "string",
  "links": [
    {
      "title": "string",
      "url": "string",
      "description": "string",
      "type": "choose one from: Related | BlockedBy | Defect | Issue | Requirement | Repository",
      "hasInfo": "boolean"
    }
  ],
  "failureReasonNames": [
    "string"
  ],
  "autoTestExternalId": "string",
  "outcome": "string",
  "message": "string",
  "traces": "string",
  "startedOn": "string",
  "completedOn": "string",
  "duration": "integer",
  "attachments": [
    {
      "id": "string"
    }
  ],
  "parameters": {
    "additionalProp": "string"
  },
  "properties": {
    "additionalProp": "string"
  },
  "stepResults": [
    {
      "title": "string",
      "description": "string",
      "startedOn": "string",
      "completedOn": "string",
      "duration": "integer",
      "outcome": "string",
      "attachments": {
        "id": "string"
      },
      "parameters": {
        "additionalProp": "string"
      }
    }
  ],
  "setupResults": [
    {
      "title": "string",
      "description": "string",
      "startedOn": "string",
      "completedOn": "string",
      "duration": "integer",
      "outcome": "string",
      "attachments": {
        "id": "string"
      },
      "parameters": {
        "additionalProp": "string"
      }
    }
  ],
  "teardownResults": [
    {
      "title": "string",
      "description": "string",
      "startedOn": "string",
      "completedOn": "string",
      "duration": "integer",
      "outcome": "string",
      "attachments": {
        "id": "string"
      },
      "parameters": {
        "additionalProp": "string"
      }
    }
  ]
}
ConfigurationPostModel = {
  "description": "string",
  "isActive": "boolean",
  "capabilities": {
    "additionalProp": "string"
  },
  "projectId": "string",
  "isDefault": "boolean",
  "name": "string"
}
ConfigurationPutModel = {
  "id": "string",
  "description": "string",
  "isActive": "boolean",
  "capabilities": {
    "additionalProp": "string"
  },
  "projectId": "string",
  "isDefault": "boolean",
  "name": "string"
}
CustomAttributeModel = {
  "id": "string",
  "options": [
    {
      "id": "string",
      "isDeleted": "boolean",
      "value": "string",
      "isDefault": "boolean"
    }
  ],
  "type": "choose one from: string | datetime | options | user | multipleOptions",
  "isDeleted": "boolean",
  "name": "string",
  "enabled": "boolean",
  "required": "boolean",
  "isGlobal": "boolean"
}
CustomAttributePostModel = {
  "options": [
    {
      "value": "string",
      "isDefault": "boolean"
    }
  ],
  "type": "choose one from: string | datetime | options | user | multipleOptions",
  "name": "string",
  "enabled": "boolean",
  "required": "boolean",
  "isGlobal": "boolean"
}
CustomAttributeTestPlanProjectRelationPutModel = {
  "id": "string",
  "enabled": "boolean",
  "required": "boolean"
}
ParameterPostModel = {
  "value": "string",
  "name": "string"
}
ParameterPutModel = {
  "id": "string",
  "value": "string",
  "name": "string"
}
ProjectExportQueryModel = {
  "sectionIds": [
    "uuid"
  ],
  "workItemIds": [
    "uuid"
  ]
}
ProjectExportWithTestPlansPostModel = {
  "testPlansIds": [
    "uuid"
  ]
}
ProjectPostModel = {
  "description": "string",
  "name": "string"
}
ProjectPutModel = {
  "id": "string",
  "description": "string",
  "name": "string"
}
SectionMoveModel = {
  "id": "string",
  "oldParentId": "string",
  "parentId": "string",
  "nextSectionId": "string"
}
SectionPostModel = {
  "name": "string",
  "projectId": "string",
  "parentId": "string",
  "preconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "postconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ]
}
SectionPutModel = {
  "id": "string",
  "name": "string",
  "projectId": "string",
  "parentId": "string",
  "preconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "postconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ]
}
SectionRenameModel = {
  "id": "string",
  "name": "string"
}
TestPlanPostModel = {
  "tags": [
    {
      "name": "string"
    }
  ],
  "name": "string",
  "startDate": "string",
  "endDate": "string",
  "description": "string",
  "build": "string",
  "projectId": "string",
  "productName": "string",
  "hasAutomaticDurationTimer": "boolean",
  "attributes": {
    "additionalProp": "string"
  }
}
TestPlanPutModel = {
  "id": "string",
  "lockedById": "string",
  "tags": [
    {
      "name": "string"
    }
  ],
  "name": "string",
  "startDate": "string",
  "endDate": "string",
  "description": "string",
  "build": "string",
  "projectId": "string",
  "productName": "string",
  "hasAutomaticDurationTimer": "boolean",
  "attributes": {
    "additionalProp": "string"
  }
}
TestRunFillByAutoTestsPostModel = {
  "projectId": "string",
  "name": "string",
  "configurationIds": [
    "uuid"
  ],
  "autoTestExternalIds": [
    "string"
  ],
  "description": "string",
  "launchSource": "string"
}
TestRunFillByConfigurationsPostModel = {
  "testPointSelectors": [
    {
      "configurationId": "string",
      "workitemIds": [
        "uuid"
      ]
    }
  ],
  "projectId": "string",
  "testPlanId": "string",
  "name": "string",
  "description": "string",
  "launchSource": "string"
}
TestRunFillByWorkItemsPostModel = {
  "configurationIds": [
    "uuid"
  ],
  "workitemIds": [
    "uuid"
  ],
  "projectId": "string",
  "testPlanId": "string",
  "name": "string",
  "description": "string",
  "launchSource": "string"
}
TestRunV2PostShortModel = {
  "projectId": "string",
  "name": "string",
  "description": "string",
  "launchSource": "string"
}
TestRunV2PutModel = {
  "id": "string",
  "name": "string",
  "description": "string",
  "launchSource": "string"
}
TestSuiteV2PostModel = {
  "parentId": "string",
  "testPlanId": "string",
  "name": "string"
}
TestSuiteV2PutModel = {
  "id": "string",
  "parentId": "string",
  "name": "string"
}
WorkItemIdModel = {
  "id": "string"
}
WorkItemPostModel = {
  "entityTypeName": "choose one from: TestCases | CheckLists | SharedSteps",
  "description": "string",
  "state": "choose one from: NeedsWork | NotReady | Ready",
  "priority": "choose one from: Lowest | Low | Medium | High | Highest",
  "steps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "preconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "postconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "duration": "integer",
  "attributes": {
    "additionalProp": "string"
  },
  "tags": [
    {
      "name": "string"
    }
  ],
  "attachments": [
    {
      "id": "string"
    }
  ],
  "iterations": [
    {
      "parameters": {
        "id": "string"
      },
      "id": "string"
    }
  ],
  "links": [
    {
      "title": "string",
      "url": "string",
      "description": "string",
      "type": "choose one from: Related | BlockedBy | Defect | Issue | Requirement | Repository",
      "hasInfo": "boolean"
    }
  ],
  "name": "string",
  "projectId": "string",
  "sectionId": "string",
  "autoTests": [
    {
      "id": "string"
    }
  ]
}
WorkItemPutModel = {
  "attachments": [
    {
      "id": "string"
    }
  ],
  "iterations": [
    {
      "parameters": {
        "id": "string"
      },
      "id": "string"
    }
  ],
  "autoTests": [
    {
      "id": "string"
    }
  ],
  "id": "string",
  "sectionId": "string",
  "description": "string",
  "state": "choose one from: NeedsWork | NotReady | Ready",
  "priority": "choose one from: Lowest | Low | Medium | High | Highest",
  "steps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "preconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "postconditionSteps": [
    {
      "id": "string",
      "action": "string",
      "expected": "string",
      "testData": "string",
      "comments": "string",
      "workItemId": "string"
    }
  ],
  "duration": "integer",
  "attributes": {
    "additionalProp": "string"
  },
  "tags": [
    {
      "name": "string"
    }
  ],
  "links": [
    {
      "id": "string",
      "title": "string",
      "url": "string",
      "description": "string",
      "type": "choose one from: Related | BlockedBy | Defect | Issue | Requirement | Repository",
      "hasInfo": "boolean"
    }
  ],
  "name": "string"
}
WorkItemSelectModel = {
  "filter": {
    "nameOrId": "string",
    "includeIds": [
      "string"
    ],
    "excludeIds": [
      "string"
    ],
    "name": "string",
    "globalIds": [
      "integer"
    ],
    "attributes": {
      "additionalProp": [
        "string"
      ]
    },
    "isDeleted": "boolean",
    "projectIds": [
      "string"
    ],
    "sectionIds": [
      "string"
    ],
    "createdByIds": [
      "string"
    ],
    "modifiedByIds": [
      "string"
    ],
    "states": "choose one from: NeedsWork | NotReady | Ready",
    "priorities": "choose one from: Lowest | Low | Medium | High | Highest",
    "entityTypes": [
      "string"
    ],
    "createdDateMinimal": "string",
    "createdDateMaximal": "string",
    "modifiedDateMinimal": "string",
    "modifiedDateMaximal": "string",
    "durationMinimal": "integer",
    "durationMaximal": "integer",
    "isAutomated": "boolean",
    "tagNames": [
      "string"
    ],
    "autoTestIds": [
      "string"
    ],
    "exceptWorkItemIds": [
      "string"
    ]
  },
  "extractionModel": {
    "includeWorkItems": [
      "string"
    ],
    "includeSections": [
      "string"
    ],
    "includeProjects": [
      "string"
    ],
    "excludeWorkItems": [
      "string"
    ],
    "excludeSections": [
      "string"
    ],
    "excludeProjects": [
      "string"
    ]
  }
}
