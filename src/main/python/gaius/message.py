# -*- coding: utf-8 -*-


class DeploymentResponse(dict):

    """
    A message that crassus returns for events such as fail or success
    events for stack deployments/updates. These messages will be
    transmitted as JSON encoded strings, used by Gaius.

    It is initialized with the following parameters:
    - status: STATUS_FAILURE or STATUS_SUCCESS
    - stack_name: the stack name the notification message stands for
    - version: a version identifier for the message. Defaults as '1.0'
    - message: the textual message for the notification.
    """

    STATUS_SUCCESS = 'success'
    STATUS_FAILURE = 'failure'

    def __init__(self, status, timestamp, stackName, version, message, emitter):
        self['status'] = status
        self['timestamp'] = timestamp
        self['stackName'] = stackName
        self['version'] = version
        self['message'] = message
        self['emitter'] = emitter
