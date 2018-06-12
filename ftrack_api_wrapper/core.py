# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
# Import third-party modules
import ftrack_api


class Session(ftrack_api.Session):
    """Wrapper ftrack session"""
    def __init__(self,
                 server_url=None,
                 api_key=None,
                 api_user=None,
                 auto_populate=True,
                 plugin_paths=None,
                 cache=None,
                 cache_key_maker=None,
                 auto_connect_event_hub=True,
                 schema_cache_path=None,
                 plugin_arguments=None):
        super(Session, self).__init__(
            server_url, api_key, api_user, auto_populate, plugin_paths, cache,
            cache_key_maker, auto_connect_event_hub, schema_cache_path,
            plugin_arguments)

    def query(self, expression, page_size=500):
        return super(Session, self).query(expression, page_size)

    def get_status(self, name):
        str_ = 'Status where name is "{}"'
        return self.query(str_.format(name)).first()

    def get_project_by_id(self, project_id):
        str_ = 'Project where id is "{}"'
        return self.query(str_.format(project_id)).first()

    def get_task_by_id(self, task_id):
        str_ = 'Task where id is "{}"'
        return self.query(str_.format(task_id)).first()

    def get_task_by_name(self, project_name, parent_name, task_name):
        str_ = 'Task where name is "{}" and' \
               ' project.name is "{}" and ' \
               'parent.name is "{}"'
        return self.query(str_.format(task_name, project_name,
                                      parent_name)).first()

    def get_project_by_name(self, project_name):
        str_ = 'Project where name is "{}"'
        return self.query(str_.format(project_name)).first()

    def get_project_schema_by_name(self, schema_name):
        str_ = 'ProjectSchema where name is "{}"'
        return self.query(str_.format(schema_name)).first()

    def get_project_schema_by_id(self, project_name):
        str_ = 'ProjectSchema where id is "{}"'
        return self.query(str_.format(project_name)).first()

    def get_seq_by_name(self, project_name, seq_name):
        str_ = 'Sequence where parent.name is "{}" and name is "{}"'
        return self.query(str_.format(project_name, seq_name)).first()

    def get_user_by_name(self, user_name=None):
        str_ = 'User where username is "{}"'
        return self.query(str_.format(user_name)).first()

    def get_user_by_id(self, id_):
        str_ = 'User where id is "{}"'
        return self.query(str_.format(id_)).first()

    def change_status(self, task_, status_name):
        status = self.get_status(status_name)
        task_['status_id'] = status['id']
        self.commit()

    def get_assets_version_by_id(self, version_id):
        return self.query('AssetVersion', version_id).first()

    def get_in_progress_tasks(self, project_name, user_name):
        info = self.query('Task where project.name = "{}" and '
                          'status.name is "In Progress" and '
                          'assignments.resource.username = "{}"'.format(project_name,
                                                                        user_name)).all()
        return info

    def get_asset_by_task_name(self, id_):
        str_ = 'Asset where context_id is {}'
        return self.query(str_.format(id_)).first()

    def get_server_location(self):
        return self.query('Location where name is "ftrack.server"').one()

    def upload_thumbnail_by_task_id(self, my_task_id, image_path):
        task = self.get('Task', my_task_id)

        thumbnail_component = self.create_component(
            image_path,
            dict(name='thumbnail'),
            location=self.get_server_location())
        task['thumbnail'] = thumbnail_component
        self.commit()

    def get_note_by_id(self, note_id):
        str_ = 'Note Where parent.id is {}'
        return self.query(str_.format(note_id)).first()
