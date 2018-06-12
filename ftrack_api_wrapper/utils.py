# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
# Import local modules
from ftrack_api_wrapper.core import Session

SESSION = None


def get_instance_session():
    global SESSION
    if not SESSION:
        SESSION = Session()
    return SESSION


def create_thumbnail(project_name, parent_name, task_name, image_path):
    session = get_instance_session()
    task = session.get_task_by_name(project_name, parent_name, task_name)
    if task:
        session.upload_thumbnail_by_task_id(task['id'], image_path)
    else:
        print "not find task in ftrack."
