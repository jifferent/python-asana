# This file is automatically generated by generate.py using api.json

class _Projects:
    def __init__(self, client=None):
        self.client = client

    def create(self, params={}, **options):
        """Dispatches a POST request to /projects of the API to create a new project."""
        return self.client.post('/projects', params, **options)

    def update(self, project_id, params={}, **options):
        """Dispatches a PUT request to /projects/:projectId to update the project."""
        path = '/projects/%s' % (project_id)
        return self.client.put(path, params, **options)

    def find_by_id(self, project_id, params={}, **options):
        """Dispatches a GET request to /projects/:projectId of the API to get information about the project."""
        path = '/projects/%s' % (project_id)
        return self.client.get(path, params, **options)

    def find_by_workspace(self, workspace_id, params={}, **options):
        """Dispatches a GET request to /workspaces/:workspaceId/projects to get all the projects associated with the workspace."""
        path = '/workspaces/%s/projects' % (workspace_id)
        return self.client.get_collection(path, params, **options)

    def find_all(self, params={}, **options):
        """Dispatches a GET request to /projects of the API to get information about all projects that the dispatcher as access to."""
        return self.client.get_collection('/projects', params, **options)

    def create_in_workspace(self, workspace_id, params={}, **options):
        """Dispatches a POST request to /workspaces/:workspaceId/projects of the API to create a new project within the workspace."""
        path = '/workspaces/%s/projects' % (workspace_id)
        return self.client.post(path, params, **options)

    def delete(self, project_id, params={}, **options):
        """Dispatches a DELETE requte to /projects/:projectId to delete the project."""
        path = '/projects/%s' % (project_id)
        return self.client.delete(path, params, **options)
