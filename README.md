# Python API client for TestIT
Python3 module that implements the API commands of the TestIT test management system
#### testit_api.py v.0.1.0
#### based on swagger description of API methods TestIT v.3.5.1

# Usage
Use to create projects, sections, workitems, autotests, test plans, test runs, etc. in your TestIT system

## Install requires
`requests` lib
```sh
pip install requests
```

## Setting up access
When you create an object of `TestITClient` class, you must pass the `testit_url` and `secretkey` parameters to the class constructor.

`testit_url` - url your TestIT system in format: "https://example.com' (protocol + domain name)

`secretkey` - your "API secret key" from TestIT

```py
client = TestITClient(testit_url='https://my.testit.com',
                      secretkey='MY_TESTIT_API_SECRET_KEY')
```

## Examples

### Create project
For creating project we need method `CreateProject` from `testit_api.py` file. Let's take a look at this method:
```py
    def CreateProject(self, data):
        """
        Create Project

        Use case
        User sets project parameters (listed in request example) and runs method execution
        System creates project
        System returns project model (example listed in response parameters)
        """
        method = "post"
        path = f"/api/v2/projects"
        # data like a ProjectPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)
```
As we can see, the function takes the parameter "data" as input, and this "data"  should be like a `ProjectPostModel`

Okay, look at the `ProjectPostModel` in `testit_models.py` file
```py
ProjectPostModel = {
  "description": "string",
  "name": "string"
}
```
We see that the model has only two fields to fill in, these are "description" and "name", the type of which is "string"

> #### About models
> 
> The `testit_models.py` file contains json-descriptions of TestIT system entity models
> 
> **This file is for reference only**
> 
> These models can be used as `data` in functions, but you should keep in mind that not all model fields are required when you are going to use them
> 
> _Find the required model fields in the swagger documentation for your TestIT system_

Let's use this `ProjectPostModel` and create a project
```py
# import modules
from testit_api import TestITClient
import testit_models

# create TestITClient object
client = TestITClient(testit_url='https://my.testit.com',
                      secretkey='MY_TESTIT_API_SECRET_KEY')
# copy model (using dict.copy() method is mandatory)
project_model = testit_models.ProjectPostModel.copy()
# fill in the model fields
project_model['description'] = 'List of tests for our New Product'
project_model['name'] = 'New Product'
# create project
project = client.CreateProject(project_model)
print(project)
```
Look at the print output
```sh
{
  "attributesScheme": [],
  "testPlansAttributesScheme": null,
  "testCasesCount": 0,
  "sharedStepsCount": 0,
  "checkListsCount": 0,
  "autoTestsCount": 0,
  "isFavorite": true,
  "isDeleted": false,
  "createdDate": "2022-08-25T13:44:47.674Z",
  "modifiedDate": "2022-08-25T13:44:47.674Z",
  "createdById": "985f32b7-e518-46c4-b324-4a6ea89ac032",
  "modifiedById": "985f32b7-e518-46c4-b324-4a6ea89ac032",
  "globalId": 139939,
  "id": "30be9f6e-d059-40ba-8168-ac31e5525b4c",
  "description": "List of tests for our New Product",
  "name": "New Product"
}
```
The project has been created
### Create workitem (test case)
```py
# fill in the model by yourself
testcase_model = {
    "entityTypeName": "TestCases",
    # get projectId from created project 
    "projectId": project["id"],
    # get sectionId using api client function. The main section will be the first in list
    "sectionId": client.GetSectionsByProjectId(project["id"])[0]["id"],
    "name": "Smoke test",
    "state": "NeedsWork",
    "steps": [
        {
            "action": "Turn on the device"
        }
    ],
    "preconditionSteps": [],
    "postconditionSteps": [],
    "tags": [],
    "links": [],
    "attributes": {},
    "duration": 60,
}
testcase = client.CreateWorkItem(testcase_model)
print(testcase)
```
The test case has been created
```sh
{
  "versionId": "173128c8-519b-4fa5-8e3a-c7c14b0aaa4d",
  "medianDuration": 0,
  "isDeleted": false,
  "projectId": "30be9f6e-d059-40ba-8168-ac31e5525b4c",
  "entityTypeName": "TestCases",
  "isAutomated": false,
  "autoTests": [],
  "attachments": [],
  "sectionPreconditionSteps": [],
  "sectionPostconditionSteps": [],
  "versionNumber": 1,
  "iterations": [],
  "createdDate": "2022-08-25T14:54:13.789Z",
  "modifiedDate": "2022-08-25T14:54:13.789Z",
  "createdById": "985f32b7-e518-46c4-b324-4a6ea89ac032",
  "modifiedById": "985f32b7-e518-46c4-b324-4a6ea89ac032",
  "globalId": 139942,
  "id": "173128c8-519b-4fa5-8e3a-c7c14b0aaa4d",
  "sectionId": "f79187fe-d6d9-463c-ae41-8c58b7009129",
  "description": null,
  "state": "NeedsWork",
  "priority": "Lowest",
  "steps": [
    {
      "workItem": null,
      "id": "ebcc11e7-1158-44e6-841b-711f4f5c9cf1",
      "action": "<p>Turn on the device</p>",
      "expected": "",
      "testData": "",
      "comments": "",
      "workItemId": null
    }
  ],
  "preconditionSteps": [],
  "postconditionSteps": [],
  "duration": 300,
  "attributes": {},
  "tags": [],
  "links": [],
  "name": "Smoke test"
}
```
