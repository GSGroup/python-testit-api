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

import json
import os.path
from collections.abc import Mapping, Sequence

import requests


class TestITClient:
    """
    Realize TestIT API as python class
    """
    def __init__(self, testit_url, secretkey):
        """
        :param testit_url: Specify url your TestIT system in format: "https://example.com"
        :param secretkey: Use your "API secret key" from TestIT
        """
        if testit_url.endswith('/'):
            testit_url = testit_url[:-1]
        self.testit_url = testit_url
        self.secretkey = secretkey

    def SendCommand(self, method, path, data=None, request_file=None):
        """
        Send request to TestIT and return response
        """
        # prepare target url
        target_url = self.testit_url + path
        # prepare payload to send
        payload = bytes(json.dumps(data), 'utf-8')
        # prepare headers
        headers = {'Authorization': 'PrivateToken ' + self.secretkey, 'Content-Type': 'application/json'}
        # choose method and send request
        if method == 'post':
            if request_file is None:
                response = requests.post(target_url, headers=headers, data=payload)
            else:
                response = requests.post(target_url, headers=headers, files=request_file)
        elif method == 'put':
            response = requests.put(target_url, headers=headers, data=payload)
        elif method == 'delete':
            response = requests.delete(target_url, headers=headers, data=payload)
        else:
            response = requests.get(target_url, headers=headers)
        # return response
        try:
            return response.json()
        except:
            return response.content

    def AddAttachment(self, file, **parameters):
        """
        Create attachment

        Use case
        User send file
        User runs method execution
        System upload file
        System create attachment
        System return attachment model (listed in response parameters)
        """
        method = "post"
        path = f"/api/v2/attachments"
        request_parameters = list()
        for param in parameters:
            if param == "apiVersion":
                # string
                request_parameters.append(f"apiVersion={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        if isinstance(file, str) and os.path.isfile(file):
            request_file = open(file, mode="rb")
        elif isinstance(file, str) and not os.path.isfile(file):
            raise AssertionError("File object or path to file expected")
        else:
            request_file = file
        return self.SendCommand(method, path, request_file)

    def GetAllAutoTests(self, **parameters):
        """
        Get all AutoTests (if parameters are specified, then it's filtered by them.)

        Use case
        [Optional] User sets search parameters (listed in request parameters) and runs method execution
        System returns all autotests, matching search criteria
        """
        method = "get"
        path = f"/api/v2/autoTests"
        request_parameters = list()
        for param in parameters:
            if param == "projectId":
                # Project internal identifier
                # string (uuid)
                request_parameters.append(f"projectId={parameters[param]}")
            if param == "externalId":
                # Autotest external identifier
                # string
                request_parameters.append(f"externalId={parameters[param]}")
            if param == "globalId":
                # Autotest global identifier
                # integer (int64)
                request_parameters.append(f"globalId={parameters[param]}")
            if param == "Namespace":
                # Name of abstract storage where autotest is located
                # string
                request_parameters.append(f"Namespace={parameters[param]}")
            if param == "isNamespaceNull":
                # Boolean flag which defines if search must include autotests with null value Namespace attribute
                # boolean
                request_parameters.append(f"isNamespaceNull={parameters[param]}")
            if param == "classname":
                # Name of the class where autotest is located
                # string
                request_parameters.append(f"classname={parameters[param]}")
            if param == "isClassnameNull":
                # Boolean flag which defines if search must include autotests with null value Classname attribute
                # boolean
                request_parameters.append(f"isClassnameNull={parameters[param]}")
            if param == "isDeleted":
                # Boolean flag which defines if search must include deleted autotests
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
            if param == "labels":
                # List of autotests labels to filter by
                # array
                request_parameters.append(f"labels={parameters[param]}")
            if param == "stabilityMinimal":
                # Minimal stability value to filter by
                # integer (int32)
                request_parameters.append(f"stabilityMinimal={parameters[param]}")
            if param == "stabilityMaximal":
                # Maximal stability value to filter by
                # integer (int32)
                request_parameters.append(f"stabilityMaximal={parameters[param]}")
            if param == "isFlaky":
                # [Optional] If flaky is set
                # boolean
                request_parameters.append(f"isFlaky={parameters[param]}")
            if param == "includeSteps":
                # Boolean flag which defines if setup, steps and teardown fields must be included
                # boolean
                request_parameters.append(f"includeSteps={parameters[param]}")
            if param == "includeLabels":
                # Boolean flag which defines if labels field must be included
                # boolean
                request_parameters.append(f"includeLabels={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def CreateAutoTest(self, data):
        """
        Create AutoTest

        Use case
        User sets autotest parameters (listed in the example) and runs method execution
        System creates autotest
        [Optional] If steps enumeration is set, system creates step items and relates them to autotest
        [Optional] If setup enumeration is set, system creates setup items and relates them to autotest
        [Optional] If teardown enumeration is set, system creates teardown items and relates them to autotest
        [Optional] If label enumeration is set, system creates labels and relates them to autotest
        [Optional] If link enumeration is set, system creates links and relates them to autotest
        System returns autotest model (example listed in response parameters)
        """
        method = "post"
        path = f"/api/v2/autoTests"
        # data like a AutoTestPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateAutoTest(self, data):
        """
        Update AutoTest

        Use case
        User sets autotest updated parameters values (listed in the example) and runs method execution
        System finds the autotest by the identifier
        System updates autotest parameters
        [Optional] If steps enumeration is set, system creates step items, relates them to autotest
        and deletes relations with current steps( if exist)
        [Optional] If Setup enumeration is set, system creates setup items and relates them to autotest
        and deletes relations with current Setup items (if exist)
        [Optional] If teardown enumeration is set, system creates teardown items and relates them to autotest
        and deletes relations with current teardown items (if exist)
        [Optional] If label enumeration is set, system creates labels and relates them to autotest
        and deletes relations with current Labels (if exist)
        [Optional] If link enumeration is set, system creates links and relates them to autotest
        and deletes relations with current Links (if exist)
        System updates autotest and returns no content response
        """
        method = "put"
        path = f"/api/v2/autoTests"
        # data like a AutoTestPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetAutoTestById(self, autoTestId):
        """
        Get AutoTest by Id or GlobalId

        Use case
        User sets autotest internal or global identifier and runs method execution
        System returns autotest, which internal or global identifier equals the identifier value set in the previous
        action
        """
        method = "get"
        path = f"/api/v2/autoTests/{autoTestId}"
        return self.SendCommand(method, path)

    def DeleteAutoTest(self, autoTestId):
        """
        Delete AutoTest by Id or GlobalId

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier and runs method execution
        System finds the autotest by the identifier
        System deletes autotest and returns no content response
        """
        method = "delete"
        path = f"/api/v2/autoTests/{autoTestId}"
        return self.SendCommand(method, path)

    def CreateMultiple(self, data):
        """
        Create AutoTests multiple

        Use case
        User sets autotest parameters (listed in the example) and runs method execution
        System creates autotest
        [Optional] If steps enumeration is set, system creates step items and relates them to autotest
        [Optional] If setup enumeration is set, system creates setup items and relates them to autotest
        [Optional] If teardown enumeration is set, system creates teardown items and relates them to autotest
        [Optional] If label enumeration is set, system creates labels and relates them to autotest
        [Optional] If link enumeration is set, system creates links and relates them to autotest
        System returns autotest model (example listed in response parameters)
        """
        method = "post"
        path = f"/api/v2/autoTests/bulk"
        # data like a list of AutoTestPostModel
        if isinstance(data, Mapping) and not isinstance(data, Sequence):
            raise AssertionError("requestBody should be a list of dicts")
        return self.SendCommand(method, path, data)

    def UpdateMultiple(self, data):
        """
        Update AutoTests multiple

        Use case
        User sets autotest updated parameters values (listed in the example) and runs method execution
        System finds the autotest by the identifier
        System updates autotest parameters
        [Optional] If steps enumeration is set, system creates step items, relates them to autotest
        and deletes relations with current steps( if exist)
        [Optional] If Setup enumeration is set, system creates setup items and relates them to autotest
        and deletes relations with current Setup items (if exist)
        [Optional] If teardown enumeration is set, system creates teardown items and relates them to autotest
        and deletes relations with current teardown items (if exist)
        [Optional] If label enumeration is set, system creates labels and relates them to autotest
        and deletes relations with current Labels (if exist)
        [Optional] If link enumeration is set, system creates links and relates them to autotest
        and deletes relations with current Links (if exist)
        System updates autotest and returns no content response
        """
        method = "put"
        path = f"/api/v2/autoTests/bulk"
        # data like a list of AutoTestPutModel
        if isinstance(data, Mapping) and not isinstance(data, Sequence):
            raise AssertionError("requestBody should be a list of dicts")
        return self.SendCommand(method, path, data)

    def GetWorkItemsLinkedToAutoTest(self, autoTestId, **parameters):
        """
        Get all WorkItems Ids linked to AutoTest by Id or GlobalId

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier and runs method execution
        System finds the autotest by the identifier
        System finds all actual and not deleted WorkItems related to the found autotest
        System returns the enumeration of WorkItems
        """
        method = "get"
        path = f"/api/v2/autoTests/{autoTestId}/workItems"
        request_parameters = list()
        for param in parameters:
            if param == "isWorkItemDeleted":
                # Boolean flag which defines if search must include deleted worItems
                # boolean
                request_parameters.append(f"isWorkItemDeleted={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def LinkAutoTestToWorkItem(self, data, autoTestId):
        """
        Link AutoTest to WorkItem by Id or GlobalId

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier
        User sets workitem internal (guid format) or global (integer format) identifier
        User runs method execution
        System finds the autotest by the autotest identifier
        System finds the workitem by the workitem identifier
        System relates the workitem with the autotest and returns no content response
        """
        method = "post"
        path = f"/api/v2/autoTests/{autoTestId}/workItems"
        # data like a WorkItemIdModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def DeleteAutoTestLinkFromWorkItem(self, autoTestId, **parameters):
        """
        Delete AutoTest link from WorkItem by Id or GlobalId
        (if workItemId is not specified, then remove all links WorkItems to AutoTest)

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier
        [Optional] User sets workitem internal (guid format) or global (integer format) identifier
        User runs method execution
        System finds the autotest by the autotest identifier
        [Optional] if workitem id is set by User, System finds the workitem by the workitem identifier and unlinks it
        from autotest.
        [Optional] Otherwise, if workitem id is not specified, System unlinks all workitems linked to autotest.
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/autoTests/{autoTestId}/workItems"
        request_parameters = list()
        for param in parameters:
            if param == "workItemId":
                # workItem internal (guid format) or global (integer format) identifier
                # string
                request_parameters.append(f"workItemId={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def GetWorkItemResults(self, autoTestId, **parameters):
        """
        History of TestResults for AutoTest by Id or GlobalId

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier
        User sets getTestResultHistoryReportQuery (listed in the example)
        User runs method execution
        System search for test results using filters set by user in getTestResultHistoryReportQuery and autoTestId
        System returns the enumeration of test results
        """
        method = "get"
        path = f"/api/v2/autoTests/{autoTestId}/testResultHistory"
        request_parameters = list()
        for param in parameters:
            if param == "From":
                # string (date-time)
                request_parameters.append(f"From={parameters[param]}")
            if param == "To":
                # string (date-time)
                request_parameters.append(f"To={parameters[param]}")
            if param == "ConfigurationIds":
                # array
                request_parameters.append(f"ConfigurationIds={parameters[param]}")
            if param == "TestPlanIds":
                # array
                request_parameters.append(f"TestPlanIds={parameters[param]}")
            if param == "UserIds":
                # array
                request_parameters.append(f"UserIds={parameters[param]}")
            if param == "Outcomes":
                # array
                request_parameters.append(f"Outcomes={parameters[param]}")
            if param == "IsAutomated":
                # boolean
                request_parameters.append(f"IsAutomated={parameters[param]}")
            if param == "TestRunIds":
                # array
                request_parameters.append(f"TestRunIds={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def GetTestRuns(self, autoTestId):
        """
        Stopped and completed TestRuns which contain AutoTest by Id or GlobalId

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier
        User runs method execution
        System search for all test runs related to the autotest
        System returns the enumeration of test runs
        """
        method = "get"
        path = f"/api/v2/autoTests/{autoTestId}/testRuns"
        return self.SendCommand(method, path)

    def GetAutoTestAverageDuration(self, autoTestId):
        """
        Get AutoTest average duration by Id or GlobalId

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier
        User runs method execution
        System calculates pass average duration and fail average duration of autotest from all related test results
        System returns pass average duration and fail average duration for autotest
        """
        method = "get"
        path = f"/api/v2/autoTests/{autoTestId}/averageDuration"
        return self.SendCommand(method, path)

    def GetAutoTestChronology(self, autoTestId):
        """
        Get AutoTest chronology by Id or GlobalId

        Use case
        User sets autotest internal (guid format) or global (integer format) identifier
        User runs method execution
        System search all test results related to autotest (with default limit equal 100)
        System orders the test results by CompletedOn property descending and then orders by CreatedDate property
        descending
        System returns test result chronology for autotest
        """
        method = "get"
        path = f"/api/v2/autoTests/{autoTestId}/chronology"
        return self.SendCommand(method, path)

    def GetConfigurationById(self, configurationId):
        """
        Get Configuration by Id or GlobalId

        Use case
        User sets configuration internal (guid format) or global (integer format) identifier
        User runs method execution
        System search configuration using the identifier
        System returns configuration
        """
        method = "get"
        path = f"/api/v2/configurations/{configurationId}"
        return self.SendCommand(method, path)

    def CreateConfiguration(self, data):
        """
        Create Configuration

        Use case
        User sets configuration model (listed in the request example)
        User runs method execution
        System creates configuration
        System returns created configuration (listed in the response example)
        """
        method = "post"
        path = f"/api/v2/configurations"
        # data like a ConfigurationPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateConfiguration(self, data):
        """
        Update Configuration

        Use case
        User sets configuration updated properties(listed in the request example)
        User runs method execution
        System updated configuration using updated properties
        System returns no content response
        """
        method = "put"
        path = f"/api/v2/configurations"
        # data like a ConfigurationPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetAllParameters(self, **parameters):
        """
        Get all parameters (if isDeleted is true, return deleted parameters)

        Use case
        [Optional] User sets isDeleted field value
        [Optional] If User sets isDeleted field value as true, System search all deleted parameters
        [Optional] If User sets isDeleted field value as false, System search all parameters which are not deleted
        If User did not set isDeleted field value, System search all parameters
        System returns array of all found parameters(listed in response model)
        """
        method = "get"
        path = f"/api/v2/parameters"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Boolean flag which defines if search must include deleted parameters
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def CreateParameter(self, data):
        """
        Create parameter

        Use case
        User sets parameter model (listed in the request example)
        User runs method execution
        System creates parameter
        System returns parameter model
        """
        method = "post"
        path = f"/api/v2/parameters"
        # data like a ParameterPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateParameter(self, data):
        """
        Update parameter

        Use case
        User sets parameter updated properties(listed in the request example)
        User runs method execution
        System updated parameter using updated properties
        System returns no content response
        """
        method = "put"
        path = f"/api/v2/parameters"
        # data like a ParameterPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetParameterById(self, parameterId):
        """
        Get parameter by id

        Use case
        User sets parameter internal (guid format) identifier
        User runs method execution
        System search parameter using the identifier
        System returns parameter
        """
        method = "get"
        path = f"/api/v2/parameters/{parameterId}"
        return self.SendCommand(method, path)

    def DeleteParameter(self, parameterId):
        """
        Delete parameter by id

        Use case
        User sets parameter internal (guid format) identifier
        System search and delete parameter
        System returns deleted parameter
        """
        method = "delete"
        path = f"/api/v2/parameters/{parameterId}"
        return self.SendCommand(method, path)

    def DeleteByName(self, name):
        """
        Delete parameter by name

        Deletes parameter and all it's values
        """
        method = "delete"
        path = f"/api/v2/parameters/name/{name}"
        return self.SendCommand(method, path)

    def GetAllProjects(self, **parameters):
        """
        Get all Projects (if isDeleted is true, return deleted Projects)

        Use case
        [Optional] User sets isDeleted field value
        [Optional] If User sets isDeleted field value as true, System search all deleted projects
        [Optional] If User sets isDeleted field value as false, System search all projects which are not deleted
        If User did not set isDeleted field value, System search all projects
        System returns array of all found projects(listed in response model)
        """
        method = "get"
        path = f"/api/v2/projects"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Boolean flag which defines if search must include deleted projects
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
            if param == "projectName":
                # string
                request_parameters.append(f"projectName={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

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

    def UpdateProject(self, data):
        """
        Update Project

        Use case
        User sets project parameters (listed in request example) and runs method execution
        System updates project
        System returns updated project model (example listed in response parameters)
        """
        method = "put"
        path = f"/api/v2/projects"
        # data like a ProjectPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetProjectById(self, projectId):
        """
        Get Project by Id or GlobalId

        Use case
        User sets project internal or global identifier and runs method execution
        System search project
        System returns project (example listed in response parameters)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}"
        return self.SendCommand(method, path)

    def DeleteProject(self, projectId):
        """
        Delete Project by Id or GlobalId

        Use case
        User sets project internal or global identifier and runs method execution
        System search and delete project
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/projects/{projectId}"
        return self.SendCommand(method, path)

    def RestoreProject(self, projectId):
        """
        Restore Project by Id or GlobalId

        Use case
        User sets project internal or global identifier and runs method execution
        System search and restores deleted project
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/projects/{projectId}/restore"
        return self.SendCommand(method, path)

    def GetSectionsByProjectId(self, projectId, **parameters):
        """
        Get Sections for Project by Id or GlobalId

        Use case
        User sets project internal or global identifier and runs method execution
        System search project
        System search all sections related to the project
        System returns array of sections (listed in response)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/sections"
        request_parameters = list()
        for param in parameters:
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def GetAutoTestsNamespaces(self, projectId):
        """
        Get AutoTests Namespaces for Project by Id or GlobalId

        Use case
        User sets project internal or global identifier and runs method execution
        System search project
        System search all autotest related to the project
        System returns array of autotest with namespaces and classnames (listed in response)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/autoTestsNamespaces"
        return self.SendCommand(method, path)

    def GetWorkItemsByProjectId(self, projectId, **parameters):
        """
        Get WorkItems for Project by Id or GlobalId (if isDeleted is true, return deleted WorkItems)

        Use case
        User sets project internal or global identifier
        [Optional] User sets isDeleted field value
        User runs method execution
        System search project
        [Optional] If User sets isDeleted field value as true, System search all deleted workitems related to project
        [Optional] If User sets isDeleted field value as false, System search all workitems related to project which
        are not deleted
        If User did not set isDeleted field value, System search all  workitems related to project
        System returns array of found workitems (listed in response model)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/workItems"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Boolean flag which defines if search must include deleted workitems
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
            if param == "tagNames":
                # Array of workitem tag names
                # array
                request_parameters.append(f"tagNames={parameters[param]}")
            if param == "includeIterations":
                # boolean
                request_parameters.append(f"includeIterations={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def GetConfigurationsByProjectId(self, projectId):
        """
        Get Configurations for Project by Id or GlobalId

        Use case
        User sets project internal or global identifier
        User runs method execution
        System search project
        System search all configurations related to project
        System returns array of found configurations (listed in response model)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/configurations"
        return self.SendCommand(method, path)

    def GetAttributesByProjectId(self, projectId, **parameters):
        """
        Get Projects Attributes by Id or GlobalId

        Use case
        User sets project internal or global identifier
        [Optional] User sets isDeleted field value
        User runs method execution
        System search project
        [Optional] If User sets isDeleted field value as true, System search all deleted attributes related to
        project
        [Optional] If User sets isDeleted field value as false, System search all attributes related to project which
        are not deleted
        [Optional] If User did not set isDeleted field value, System search all attributes related to project
        System returns array of found attributes (listed in response model)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/attributes"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Boolean flag which defines if search must include deleted attributes
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def CreateProjectsAttribute(self, data, projectId):
        """
        Create Projects Attribute

        Use case
        User sets attribute parameters (listed in request example) and runs method execution
        System search project
        System creates attribute and relates it to the project
        System returns project attribute properties (example listed in response parameters)
        """
        method = "post"
        path = f"/api/v2/projects/{projectId}/attributes"
        # data like a CustomAttributePostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateProjectsAttribute(self, data, projectId):
        """
        Update Projects Attribute

        Use case
        User sets project parameters (listed in request example) and runs method execution
        System updates project
        System updates attribute related to the project
        System returns no content response
        """
        method = "put"
        path = f"/api/v2/projects/{projectId}/attributes"
        # data like a CustomAttributeModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetAttributeByProjectId(self, projectId, attributeId):
        """
        Get Projects Attribute by Id

        Use case
        User sets project internal or global identifier
        User sets project attribute identifier
        User runs method execution
        System search project
        System search project attribute
        System returns project attribute (listed in response model)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/attributes/{attributeId}"
        return self.SendCommand(method, path)

    def DeleteProjectsAttribute(self, projectId, attributeId):
        """
        Delete Projects Attribute by Id

        Use case
        User sets project identifier and runs method execution
        User sets attribute identifier
        User runs method execution
        System search project
        System search and delete attribute
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/projects/{projectId}/attributes/{attributeId}"
        return self.SendCommand(method, path)

    def GetTestPlansByProjectId(self, projectId, **parameters):
        """
        Get TestPlans for Project by Id or GlobalId (if isDeleted is true, return deleted TestPlans)

        Use case
        User sets project internal or global identifier
        [Optional] User sets isDeleted field value
        User runs method execution
        System search project
        [Optional] If User sets isDeleted field value as true, System search all deleted test plans related to
        project
        [Optional] If User sets isDeleted field value as false, System search all test plans related to project which
        are not deleted
        [Optional] If User did not set isDeleted field value, System search all v related to project
        System returns array of found test plans (listed in response model)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/testPlans"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Boolean flag which defines if search must include deleted test plans
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def GetTestRunsByProjectId(self, projectId, **parameters):
        """
        Get TestRuns for Project by Id or GlobalId

        Use case
        User sets project internal or global identifier
        User runs method execution
        System search project
        System search all test runs related to project
        System returns array of found test runs (listed in response model)
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/testRuns"
        request_parameters = list()
        for param in parameters:
            if param == "NotStarted":
                # boolean
                request_parameters.append(f"NotStarted={parameters[param]}")
            if param == "InProgress":
                # boolean
                request_parameters.append(f"InProgress={parameters[param]}")
            if param == "Stopped":
                # boolean
                request_parameters.append(f"Stopped={parameters[param]}")
            if param == "Completed":
                # boolean
                request_parameters.append(f"Completed={parameters[param]}")
            if param == "CreatedDateFrom":
                # string (date-time)
                request_parameters.append(f"CreatedDateFrom={parameters[param]}")
            if param == "CreatedDateTo":
                # string (date-time)
                request_parameters.append(f"CreatedDateTo={parameters[param]}")
            if param == "TestPlanId":
                # string (uuid)
                request_parameters.append(f"TestPlanId={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def Export(self, data, projectId, **parameters):
        """
        Export Project with tests, sections and configurations in json file

        Use case
        User sets project internal or global identifier
        User runs method execution
        System search project
        System returns project data as json file, containing project data, related attributes, sections and
        workitems
        """
        method = "post"
        path = f"/api/v2/projects/{projectId}/export"
        request_parameters = list()
        for param in parameters:
            if param == "includeAttachments":
                # boolean
                request_parameters.append(f"includeAttachments={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        # data like a ProjectExportQueryModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def ExportWithTestPlansAndConfigurations(self, data, projectId, **parameters):
        """
        Export Project with tests, sections, configurations, testPlans, testSuites and testPoints as json file

        Use case
        User sets project internal or global identifier
        User runs method execution
        System search project
        System returns project data as json file, containing project data, related attributes, sections, workitems,
        test plans, test suites, test points and configurations
        """
        method = "post"
        path = f"/api/v2/projects/{projectId}/export-by-testPlans"
        request_parameters = list()
        for param in parameters:
            if param == "includeAttachments":
                # boolean
                request_parameters.append(f"includeAttachments={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        # data like a ProjectExportWithTestPlansPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def Import(self, file, **parameters):
        """
        Import Project from json file
        Project can be imported only once (this method or ImportToExistingProject)
        Next import will sync content in previously imported project.

        Use case
        User attaches project as json file taken from export or export-by-testPlans method
        User runs method execution
        System creates project
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/projects/import"
        request_parameters = list()
        for param in parameters:
            if param == "apiVersion":
                # string
                request_parameters.append(f"apiVersion={parameters[param]}")
            if param == "includeAttachments":
                # boolean
                request_parameters.append(f"includeAttachments={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        if isinstance(file, str) and os.path.isfile(file):
            request_file = open(file, mode="rb")
        elif isinstance(file, str) and not os.path.isfile(file):
            raise AssertionError("File object or path to file expected")
        else:
            request_file = file

        return self.SendCommand(method, path, request_file)

    def ImportToExistingProject(self, file, projectId, **parameters):
        """
        Import to existing Project from json file.
        Sections can be imported in only one target project!

        Use case
        User attaches project as json file taken from export or export-by-testPlans method
        User runs method execution
        System updates project
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/projects/{projectId}/import"
        request_parameters = list()
        for param in parameters:
            if param == "apiVersion":
                # string
                request_parameters.append(f"apiVersion={parameters[param]}")
            if param == "includeAttachments":
                # boolean
                request_parameters.append(f"includeAttachments={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        if isinstance(file, str) and os.path.isfile(file):
            request_file = open(file, mode="rb")
        elif isinstance(file, str) and not os.path.isfile(file):
            raise AssertionError("File object or path to file expected")
        else:
            request_file = file

        return self.SendCommand(method, path, request_file)

    def GetCustomAttributeTestPlanProjectRelations(self, projectId):
        """
        Get project for test plans attributes

        Use case
        User runs method execution
        System returns project for test plans attributes by project identifier
        """
        method = "get"
        path = f"/api/v2/projects/{projectId}/testPlans/attributes"
        return self.SendCommand(method, path)

    def CreateCustomAttributeTestPlanProjectRelations(self, data, projectId):
        """
        Add attributes to project for test plans

        Use case
        User sets project internal or global identifier and attributes identifiers
        User runs method execution
        System updates project and add attributes to project for test plans
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/projects/{projectId}/testPlans/attributes"
        # data should be a list of uuid string
        if isinstance(data, Mapping) and not isinstance(data, Sequence):
            raise AssertionError("requestBody should be a list of items")
        return self.SendCommand(method, path, data)

    def DeleteCustomAttributeTestPlanProjectRelations(self, projectId, attributeId):
        """
        Delete attribute from project for test plans

        Use case
        User sets project internal or global identifier and attribute identifier
        User runs method execution
        System updates project and delete attribute from project for test plans
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/projects/{projectId}/testPlans/attribute/{attributeId}"
        return self.SendCommand(method, path)

    def UpdateCustomAttributeTestPlanProjectRelations(self, data, projectId):
        """
        Update project attribute for test plan

        Use case
        User sets project internal or global identifier and attribute model
        User runs method execution
        System updates project and project attribute for test plan
        System returns no content response
        """
        method = "put"
        path = f"/api/v2/projects/{projectId}/testPlans/attribute"
        # data like a CustomAttributeTestPlanProjectRelationPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def DeleteProjectAutoTests(self, projectId):
        """
        Delete all AutoTests from Project

        Use case
        User sets project internal or global identifier
        User runs method execution
        System delete all autotests from project
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/projects/{projectId}/autoTests"
        return self.SendCommand(method, path)

    def GetSectionById(self, sectionId, **parameters):
        """
        Get Section by id

        Use case
        User sets section internal (guid format) identifier
        User runs method execution
        System search section by the section identifier
        [Optional] If isDeleted flag equals false, deleted workitems are not being searched.
        If true, deleted workitems are also being searched, null for all workitems.
        System returns section
        """
        method = "get"
        path = f"/api/v2/sections/{sectionId}"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Flag that defines if deleted section must be include in the response
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def DeleteSection(self, sectionId):
        """
        Delete Section by id

        Use case
        User sets section identifier
        User runs method execution
        System search section by the identifier
        System search and delete nested sections of the found section
        System search and delete workitems related to the found nested sections
        System deletes initial section and related workitem
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/sections/{sectionId}"
        return self.SendCommand(method, path)

    def CreateSection(self, data):
        """
        Create Section

        Use case
        User sets section properties (listed in request example)
        User runs method execution
        System creates section property values
        System returns section (listed in response example)
        """
        method = "post"
        path = f"/api/v2/sections"
        # data like a SectionPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateSection(self, data):
        """
        Update Section

        Use case
        User sets section properties (listed in request example)
        User runs method execution
        System search section by the identifier
        System updates section using the property values
        System returns no content response
        """
        method = "put"
        path = f"/api/v2/sections"
        # data like a SectionPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def Rename(self, data):
        """
        Rename Section

        Use case
        User sets section identifier and new name (listed in request example)
        User runs method execution
        System search section by the identifier
        System updates section name using the new name
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/sections/rename"
        # data like a SectionRenameModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def Move(self, data):
        """
        Move Section. Can be moved inside another section. It is possible to indicate a project

        Use case
        User sets section identifier, old parent identifier, parent identifier and  next section identifier (listed
        in request example)
        User runs method execution
        System search section by the identifier
        System unlink section from the old parent and links to the new one
        System updates section rank using the next section identifier
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/sections/move"
        # data like a SectionMoveModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetWorkItemsBySectionId(self, sectionId, **parameters):
        """
        Get WorkItems for Section (if isDeleted is true, return deleted WorkItems)

        Use case
        User sets section identifier
        User runs method execution
        System search section by the identifier
        System search workitems related to the section
        [Optional] If isDeleted flag equals false, deleted workitems are not being searched.
        If true, deleted workitems are also being searched, null for all workitems.
        System returns workitem collection
        """
        method = "get"
        path = f"/api/v2/sections/{sectionId}/workItems"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Flag that defines if deleted workitems must be include in the response
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
            if param == "tagNames":
                # Array of workitem tag names
                # array
                request_parameters.append(f"tagNames={parameters[param]}")
            if param == "includeIterations":
                # boolean
                request_parameters.append(f"includeIterations={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def GetTestPlanById(self, testPlanId):
        """
        Get TestPlan by Id

        Use case
        User sets test plan identifier
        User runs method execution
        System search  test plan by the identifier
        System returns test plan
        """
        method = "get"
        path = f"/api/v2/testPlans/{testPlanId}"
        return self.SendCommand(method, path)

    def DeleteTestPlan(self, testPlanId):
        """
        Delete TestPlan

        Use case
        User sets test plan identifier
        User runs method execution
        System delete test plan
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/testPlans/{testPlanId}"
        return self.SendCommand(method, path)

    def CreateTestPlan(self, data):
        """
        Create TestPlan

        Use case
        User sets test plan properties (listed in request example)
        User runs method execution
        System creates test plan
        System returns test plan (listed in response example)
        """
        method = "post"
        path = f"/api/v2/testPlans"
        # data like a TestPlanPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateTestPlan(self, data):
        """
        Update TestPlan

        Use case
        User sets test plan properties(listed in request example)
        User runs method execution
        System updates test plan
        System returns no content response
        """
        method = "put"
        path = f"/api/v2/testPlans"
        # data like a TestPlanPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def RestoreTestPlan(self, testPlanId):
        """
        Restore TestPlan

        Use case
        User sets test plan identifier
        User runs method execution
        System restores test plan
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testPlans/{testPlanId}/restore"
        return self.SendCommand(method, path)

    def Clone(self, testPlanId):
        """
        Clone TestPlan

        Use case
        User sets test plan identifier
        User runs method execution
        System clones test plan
        System returns test plan (listed in response example)
        """
        method = "post"
        path = f"/api/v2/testPlans/{testPlanId}/clone"
        return self.SendCommand(method, path)

    def Start(self, testPlanId):
        """
        Start TestPlan

        Use case
        User sets test plan identifier
        User runs method execution
        System starts the test plan and updates test plan status
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testPlans/{testPlanId}/start"
        return self.SendCommand(method, path)

    def Pause(self, testPlanId):
        """
        Pause TestPlan

        Use case
        User sets test plan identifier
        User runs method execution
        System pauses the test plan and updates test plan status
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testPlans/{testPlanId}/pause"
        return self.SendCommand(method, path)

    def Complete(self, testPlanId):
        """
        Complete TestPlan

        Use case
        User sets test plan identifier
        User runs method execution
        System completes the test plan and updates test plan status
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testPlans/{testPlanId}/complete"
        return self.SendCommand(method, path)

    def GetTestSuitesById(self, testPlanId):
        """
        Get TestSuites Tree By Id

        Use case
        User sets test plan identifier
        User runs method execution
        System finds test suites related to the test plan
        System returns test suites as a tree model (listed in response example)
        """
        method = "get"
        path = f"/api/v2/testPlans/{testPlanId}/testSuites"
        return self.SendCommand(method, path)

    def AddWorkItemsWithSections(self, data, testPlanId):
        """
        Add WorkItems to TestPlan with Sections as TestSuites

        Use case
        User sets TestPlan identifier
        User sets WorkItem identifiers (listed in request example)
        User runs method execution
        System added WorkItems and Sections to TestPlan
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testPlans/{testPlanId}/workItems/withSections"
        # data should be a list of uuid string
        if isinstance(data, Mapping) and not isinstance(data, Sequence):
            raise AssertionError("requestBody should be a list of items")
        return self.SendCommand(method, path, data)

    def AddTestPointsWithSections(self, data, testPlanId):
        """
        Add test-points to test suite with sections
        """
        method = "post"
        path = f"/api/v2/testPlans/{testPlanId}/test-points/withSections"
        # data like a WorkItemSelectModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetAttachments(self, testResultId):
        """
        Get all attachments of TestResult

        Use case
        User sets testResultId
        User runs method execution
        System search all attachments of the test result
        System returns attachments enumeration
        """
        method = "get"
        path = f"/api/v2/testResults/{testResultId}/attachments"
        return self.SendCommand(method, path)

    def CreateAttachment(self, file, testResultId):
        """
        Upload and link attachment to TestResult

        Use case
        User sets testResultId
        User attaches a file
        System creates attachment and links it to the test result
        System returns attachment identifier
        """
        method = "post"
        path = f"/api/v2/testResults/{testResultId}/attachments"
        if isinstance(file, str) and os.path.isfile(file):
            request_file = open(file, mode="rb")
        elif isinstance(file, str) and not os.path.isfile(file):
            raise AssertionError("File object or path to file expected")
        else:
            request_file = file

        return self.SendCommand(method, path, request_file)

    def DownloadAttachment(self, attachmentId, testResultId, **parameters):
        """
        Get attachment of TestResult

        Use case
        User sets attachmentId and testResultId
        [Optional] User sets resize configuration
        User runs method execution
        System search attachments by the attachmentId and the testResultId
        [Optional] If resize configuration is set, System resizes the attachment according to the resize
        configuration
        [Optional] Otherwise, System does not resize the attachment
        System returns attachment as a file
        """
        method = "get"
        path = f"/api/v2/testResults/{testResultId}/attachments/{attachmentId}"
        request_parameters = list()
        for param in parameters:
            if param == "Width":
                # integer (int32)
                request_parameters.append(f"Width={parameters[param]}")
            if param == "Height":
                # integer (int32)
                request_parameters.append(f"Height={parameters[param]}")
            if param == "ResizeOption":
                if parameters[param] not in ['Crop', 'AddBackgroundStripes']:
                    raise AssertionError("Unsupported value")
                request_parameters.append(f"ResizeOption={parameters[param]}")
            if param == "BackgroundColor":
                # string
                request_parameters.append(f"BackgroundColor={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def DeleteAttachment(self, testResultId, attachmentId):
        """
        Remove attachment and unlink from TestResult

        Use case
        User sets testResultId and attachmentId
        User attaches a file
        User runs method execution
        System deletes attachment and unlinks it from the test result
        System returns attachment identifier
        """
        method = "delete"
        path = f"/api/v2/testResults/{testResultId}/attachments/{attachmentId}"
        return self.SendCommand(method, path)

    def GetAttachment(self, attachmentId, testResultId):
        """
        Get Metadata of TestResult's attachment

        Use case
        User sets attachmentId and testResultId
        User runs method execution
        System search attachment by the attachmentId and the testResultId
        System returns attachment data
        """
        method = "get"
        path = f"/api/v2/testResults/{testResultId}/attachments/{attachmentId}/info"
        return self.SendCommand(method, path)

    def CreateEmpty(self, data):
        """
        Create empty TestRun

        Use case
        User sets test run model (listed in the request example)
        User runs method execution
        System creates test run
        System returns test run model
        """
        method = "post"
        path = f"/api/v2/testRuns"
        # data like a TestRunV2PostShortModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateEmpty(self, data):
        """
        Update empty TestRun

        Use case
        User sets test run properties (listed in the request example)
        User runs method execution
        System updates test run
        System returns returns no content response
        """
        method = "put"
        path = f"/api/v2/testRuns"
        # data like a TestRunV2PutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def CreateAndFillByWorkItems(self, data):
        """
        Create TestRun with TestPoints selected using ConfigurationIds and WorkItem Ids

        Use case
        User sets test run properties (listed in the request example)
        User sets relative configuration and workitem ids
        User runs method execution
        System creates test run
        System finds workitems and configurations using ids listed by user
        System creates test result by test points which use workitems and configurations
        System returns test run model
        """
        method = "post"
        path = f"/api/v2/testRuns/byWorkItems"
        # data like a TestRunFillByWorkItemsPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def CreateAndFillByConfigurations(self, data):
        """
        Create TestRun with TestPointSelectors based on ConfigurationId and WorkItem Ids

        Use case
        User sets test run properties (listed in the request example)
        User sets relative configuration and workitem ids
        User runs method execution
        System creates test run
        System finds workitems and configurations using ids listed by user
        System creates test result by test points which use workitems and configurations
        System returns test run model
        """
        method = "post"
        path = f"/api/v2/testRuns/byConfigurations"
        # data like a TestRunFillByConfigurationsPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def CreateAndFillByAutoTests(self, data):
        """
        Create TestRun without TestPoints using ConfigurationIds and AutoTestIds

        Use case
        User sets test run properties (listed in the request example)
        User sets relative configuration and workitem ids
        User runs method execution
        System creates test run
        System finds autotests and configurations using ids listed by user
        System creates test result by test points which use autotests and configurations
        System returns test run model
        """
        method = "post"
        path = f"/api/v2/testRuns/byAutoTests"
        # data like a TestRunFillByAutoTestsPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetTestRunById(self, testRunId):
        """
        Get TestRun by Id

        Use case
        User sets test run identifier
        User runs method execution
        System finds test run
        System returns test run
        """
        method = "get"
        path = f"/api/v2/testRuns/{testRunId}"
        return self.SendCommand(method, path)

    def StartTestRun(self, testRunId):
        """
        Start TestRun

        Use case
        User sets test run identifier
        User runs method execution
        System starts test run
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testRuns/{testRunId}/start"
        return self.SendCommand(method, path)

    def StopTestRun(self, testRunId):
        """
        Stop TestRun

        Use case
        User sets test run identifier
        User runs method execution
        System stops test run
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testRuns/{testRunId}/stop"
        return self.SendCommand(method, path)

    def CompleteTestRun(self, testRunId):
        """
        Complete TestRun

        Use case
        User sets test run identifier
        User runs method execution
        System completes test run
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testRuns/{testRunId}/complete"
        return self.SendCommand(method, path)

    def SetAutoTestResultsForTestRun(self, data, testRunId):
        """
        Set AutoTest Results For TestRun

        Use case
        User sets test run identifier
        User sets test result model (listed in request parameters)
        User runs method execution
        System sets test results of autotest listed in request in test run
        System returns array of test results identifiers
        """
        method = "post"
        path = f"/api/v2/testRuns/{testRunId}/testResults"
        # data like a list of AutoTestResultsForTestRunModel
        if isinstance(data, Mapping) and not isinstance(data, Sequence):
            raise AssertionError("requestBody should be a list of dicts")
        return self.SendCommand(method, path, data)

    def GetTestSuiteById(self, testSuiteId):
        """
        Get TestSuite by Id

        Use case
        User sets test suite identifier
        User runs method execution
        System search test suite by identifier
        System returns test suite
        """
        method = "get"
        path = f"/api/v2/testSuites/{testSuiteId}"
        return self.SendCommand(method, path)

    def DeleteTestSuite(self, testSuiteId):
        """
        Delete TestSuite

        Use case
        User sets test suite identifier
        User runs method execution
        System search test suite by identifier
        System deletes test suite
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/testSuites/{testSuiteId}"
        return self.SendCommand(method, path)

    def CreateTestSuite(self, data):
        """
        Create TestSuite

        Use case
        User sets test suite model (listed in request parameters)
        User runs method execution
        System creates test suite
        System returns test suite
        """
        method = "post"
        path = f"/api/v2/testSuites"
        # data like a TestSuiteV2PostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateTestSuite(self, data):
        """
        Update TestSuite

        Use case
        User sets test suite model (listed in request parameters)
        User runs method execution
        System updates test suite
        System returns test suite
        """
        method = "put"
        path = f"/api/v2/testSuites"
        # data like a TestSuiteV2PutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetTestPointsById(self, testSuiteId):
        """
        Get TestPoints By Id

        Use case
        User sets test suite identifier
        User runs method execution
        System search test suite by identifier
        System search test points related to the test suite
        System returns test points array
        """
        method = "get"
        path = f"/api/v2/testSuites/{testSuiteId}/testPoints"
        return self.SendCommand(method, path)

    def GetTestResultsById(self, testSuiteId):
        """
        Get TestResults By Id

        Use case
        User sets test suite identifier
        User runs method execution
        System search test suite by identifier
        System search test points related to the test suite
        System search test results related to the test points
        System returns test results array
        """
        method = "get"
        path = f"/api/v2/testSuites/{testSuiteId}/testResults"
        return self.SendCommand(method, path)

    def GetWorkItemsById(self, testSuiteId, **parameters):
        """
        Get WorkItems By Id

        Use case
        User sets test suite identifier
        [Optional] User sets isDeleted property as true
        User runs method execution
        System search test suite by identifier
        System search test points related to the test suite
        System search workitems related to the test points
        [Optional] User sets isDeleted property is set as true, System includes deleted workitems
        Otherwise, system applies filter which excludes deleted workitems from all found workitems
        System returns workitems array
        """
        method = "get"
        path = f"/api/v2/testSuites/{testSuiteId}/workItems"
        request_parameters = list()
        for param in parameters:
            if param == "isDeleted":
                # Flag that defines if deleted workitems must be include in the response
                # boolean
                request_parameters.append(f"isDeleted={parameters[param]}")
            if param == "tagNames":
                # Array of workitem tag names
                # array
                request_parameters.append(f"tagNames={parameters[param]}")
            if param == "Skip":
                # Amount of items to be skipped (offset)
                request_parameters.append(f"Skip={parameters[param]}")
            if param == "Take":
                # Amount of items to be taken (limit)
                request_parameters.append(f"Take={parameters[param]}")
            if param == "OrderBy":
                # SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC)
                request_parameters.append(f"OrderBy={parameters[param]}")
            if param == "SearchField":
                # Property name for searching
                request_parameters.append(f"SearchField={parameters[param]}")
            if param == "SearchValue":
                # Value for searching
                request_parameters.append(f"SearchValue={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def SetWorkItemsByTestSuiteId(self, data, testSuiteId):
        """
        Set WorkItems By TestSuite Id

        Use case
        User sets test suite identifier
        User sets collection of workitems identifiers
        User runs method execution
        System search test suite by identifier
        System search test points related to the test suite
        System search workitems
        System restores(if exist) or creates test points with listed workitems
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testSuites/{testSuiteId}/workItems"
        # data should be a list of uuid string
        if isinstance(data, Mapping) and not isinstance(data, Sequence):
            raise AssertionError("requestBody should be a list of items")
        return self.SendCommand(method, path, data)

    def AddTestPointsToTestSuite(self, data, testSuiteId):
        """
        Add test-points to test suite
        """
        method = "post"
        path = f"/api/v2/testSuites/{testSuiteId}/test-points"
        # data like a WorkItemSelectModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetConfigurationsByTestSuiteId(self, testSuiteId):
        """
        Get Configurations By Id

        Use case
        User sets test suite identifier
        User runs method execution
        System search test suite by identifier
        System search test points related to the test suite
        System search configurations related to the test points
        System returns configurations array
        """
        method = "get"
        path = f"/api/v2/testSuites/{testSuiteId}/configurations"
        return self.SendCommand(method, path)

    def SetConfigurationsByTestSuiteId(self, data, testSuiteId):
        """
        Set Configurations By TestSuite Id

        Use case
        User sets test suite identifier
        User sets collection of configuration identifiers
        User runs method execution
        System search test suite by identifier
        System search test points related to the test suite
        System search configuration
        System restores(if exist) or creates test points with listed configuration
        System returns no content response
        """
        method = "post"
        path = f"/api/v2/testSuites/{testSuiteId}/configurations"
        # data should be a list of uuid string
        if isinstance(data, Mapping) and not isinstance(data, Sequence):
            raise AssertionError("requestBody should be a list of items")
        return self.SendCommand(method, path, data)

    def GetWorkItemById(self, workItemId, **parameters):
        """
        Get Test Case, Checklist or Shared Step by Id or GlobalId

        Use case
        User sets workitem identifier
        [Optional] User sets workitem version identifier
        [Optional] User sets workitem version number
        User runs method execution
        System search workitem by identifier
        [Optional] if User sets workitem version identifier, system search workitem version by identifier.
        [Optional] if user sets workitem version number, system search workitem version by number
        Otherwise, system search last workitem version
        System returns workitem
        """
        method = "get"
        path = f"/api/v2/workItems/{workItemId}"
        request_parameters = list()
        for param in parameters:
            if param == "versionId":
                # WorkItem version (guid format) identifier"
                # string (uuid)
                request_parameters.append(f"versionId={parameters[param]}")
            if param == "versionNumber":
                # WorkItem version number (0 is the last version)"
                # integer (int32)
                request_parameters.append(f"versionNumber={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def DeleteWorkItem(self, workItemId):
        """
        Delete Test Case, Checklist or Shared Step by Id or GlobalId

        Use case
        User sets workitem identifier
        User runs method execution
        System deletes workitem
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/workItems/{workItemId}"
        return self.SendCommand(method, path)

    def GetIterations(self, workItemId, **parameters):
        """
        Get iterations by workitem Id or GlobalId
        """
        method = "get"
        path = f"/api/v2/workItems/{workItemId}/iterations"
        request_parameters = list()
        for param in parameters:
            if param == "versionId":
                # WorkItem version (guid format) identifier
                # string (uuid)
                request_parameters.append(f"versionId={parameters[param]}")
            if param == "versionNumber":
                # WorkItem version number (0 is the last version)"
                # integer (int32)
                request_parameters.append(f"versionNumber={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)

    def CreateWorkItem(self, data):
        """
        Create Test Case, Checklist or Shared Step

        Use case
        User sets workitem properties (listed in request parameters)
        User runs method execution
        System creates workitem by identifier
        System returns workitem model (listed in response parameters)
        """
        method = "post"
        path = f"/api/v2/workItems"
        # data like a WorkItemPostModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def UpdateWorkItem(self, data):
        """
        Update Test Case, Checklist or Shared Step

        Use case
        User sets workitem properties (listed in request parameters)
        User runs method execution
        System updates workitem by identifier
        System returns updated workitem model (listed in response parameters)
        """
        method = "put"
        path = f"/api/v2/workItems"
        # data like a WorkItemPutModel
        if not isinstance(data, Mapping) and isinstance(data, Sequence):
            raise AssertionError("requestBody should be a dict")
        return self.SendCommand(method, path, data)

    def GetAutoTestsForWorkItem(self, workItemId):
        """
        Get all AutoTests linked to WorkItem by Id or GlobalId

        Use case
        User sets workitem identifier
        User runs method execution
        System search workitem by identifier
        System search all autotests, related to found workitem
        System returns list of found autotests
        """
        method = "get"
        path = f"/api/v2/workItems/{workItemId}/autoTests"
        return self.SendCommand(method, path)

    def DeleteAllWorkItemsFromAutoTest(self, workItemId):
        """
        Delete all links AutoTests from WorkItem by Id or GlobalId

        Use case
        User sets workitem identifier
        User runs method execution
        System search workitem by identifier
        System search and delete all autotests, related to found workitem
        System returns no content response
        """
        method = "delete"
        path = f"/api/v2/workItems/{workItemId}/autoTests"
        return self.SendCommand(method, path)

    def GetWorkItemChronology(self, workItemId):
        """
        Get WorkItem chronology by Id or GlobalId

        Use case
        User sets workitem identifier
        User runs method execution
        System search workitem by identifier
        System search test results of all autotests, related to found workitem
        System sort results by CompletedOn ascending, then by CreatedDate ascending
        System returns sorted collection of test results
        """
        method = "get"
        path = f"/api/v2/workItems/{workItemId}/chronology"
        return self.SendCommand(method, path)

    def GetWorkItemVersions(self, workItemId, **parameters):
        """
        Get WorkItem versions

        Use case
        User sets workitem identifier
        [Optional] User sets workitem version identifier
        User runs method execution
        System search workitem by identifier
        [Optional] If User set workitem version identifier, System search workitem version by version identifier
        Otherwise, system search all version of workitem
        System returns array of workitem version models (listed in response example)
        """
        method = "get"
        path = f"/api/v2/workItems/{workItemId}/versions"
        request_parameters = list()
        for param in parameters:
            if param == "workItemVersionId":
                # WorkItem version (guid format) identifier"
                # string (uuid)
                request_parameters.append(f"workItemVersionId={parameters[param]}")
            if param == "versionNumber":
                # WorkItem version (integer format) number"
                # integer (int32)
                request_parameters.append(f"versionNumber={parameters[param]}")
        if request_parameters:
            path += "?" + "&".join(request_parameters)
        return self.SendCommand(method, path)
