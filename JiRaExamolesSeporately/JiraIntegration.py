from jira import JIRA


class JiraIntegration:
    def __init__(self, server, username, api_token, project_key):
        self.jira = JIRA(server=server, basic_auth=(username, api_token))
        self.project_key = project_key

    def create_test_case(self, summary, description):
        issue = self.jira.create_issue(project=self.project_key, summary=summary, description=description,
                                       issuetype={'name': 'Test'})
        return issue
