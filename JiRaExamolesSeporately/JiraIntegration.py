from jira import JIRA
from jira.exceptions import JIRAError


class JiraIntegration:
    def __init__(self, server, username, api_token, project_key):
        self.server = server
        self.username = username
        self.api_token = api_token
        self.project_key = project_key

        try:
            self.jira = JIRA(server=server, basic_auth=(username, api_token))
        except JIRAError as e:
            raise ValueError(f"Error connecting to Jira: {e}")

    def create_test_case(self, summary, description):
        try:
            issue = self.jira.create_issue(project=self.project_key, summary=summary, description=description,
                                           issuetype={'name': 'Test'})
            return issue
        except JIRAError as e:
            raise ValueError(f"Error creating test case: {e}")


# from jira import JIRA
#
#
# class JiraIntegration:
#     def __init__(self, server, username, api_token, project_key):
#         self.jira = JIRA(server=server, basic_auth=(username, api_token))
#         self.project_key = project_key
#
#     def create_test_case(self, summary, description):
#         issue = self.jira.create_issue(project=self.project_key, summary=summary, description=description,
#                                        issuetype={'name': 'Test'})
#         return issue

