# -*- coding: utf-8 -*-

RESOURCE_MAPPING = {
    'me': {
        'resource': 'me',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/users.md'
    },
    'me_with_related_data': {
        'resource': 'me?with_related_data=true',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/users.md'
    },
    'projects': {
        'resource': 'projects',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/projects.md'
    },
    'project': {
        'resource': 'projects/{project_id}',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/projects.md'
    },
    'project_users': {
        'resource': 'projects/{project_id}/project_users',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/projects.md'
    },
    'project_tasks': {
        'resource': 'projects/{project_id}/tasks',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/projects.md'
    },
    'tags': {
        'resource': 'tags',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/tags.md'
    },
    'tag': {
        'resource': 'tags/{tag_id}',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/tags.md'
    },
    'time_entries': {
        'resource': 'time_entries',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/time_entries.md'
    },
    'start_time_entry': {
        'resource': 'time_entries/start',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/time_entries.md'
    },
    'stop_time_entry': {
        'resource': 'time_entries/{time_entry_id}/stop',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/time_entries.md'
    },
    'time_entry': {
        'resource': 'time_entries/{time_entry_id}',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/time_entries.md'
    },
    'current_time_entry': {
        'resource': 'time_entries/current',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/time_entries.md'
    },
    'current_time_entry': {
        'resource': 'time_entries/current',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/time_entries.md'
    },
    'workspaces': {
        'resource': 'workspaces',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md'
    },
    'workspace': {
        'resource': 'workspaces/{workspace_id}',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md'
    },
    'workspace_users': {
        'resource': 'workspaces/{workspace_id}/users',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md'
    },
    'workspace_clients': {
        'resource': 'workspaces/{workspace_id}/clients',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md'
    },
    'workspace_clients': {
        'resource': 'workspaces/{workspace_id}/clients',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md'
    },
    'workspace_tasks': {
        'resource': 'workspaces/{workspace_id}/tasks',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md'
    },
    'workspace_tags': {
        'resource': 'workspaces/{workspace_id}/tags',
        'docs': 'https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md'
    },
}
