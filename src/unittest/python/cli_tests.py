#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest2 import TestCase
from mock import patch
from gaius import cli
from gaius.service import DeploymentErrorException


class CliTests(TestCase):

    @patch('gaius.service.receive')
    @patch('gaius.service.notify')
    @patch('gaius.service.cleanup')
    @patch('gaius.cli.docopt')
    def test_should_communicate(self, mock_docopt, mock_cleanup, mock_notify, mock_receive):
        parameters = {
            '--stack': 'mystack',
            '--parameters': 'parameter1=value1,parameter2=value2',
            '--trigger-channel': 'my::topic::arn',
            '--region': 'eu-west-1',
            '--back-channel': 'crassus-output',
            '--timeout': '600'
        }
        mock_docopt.return_value = parameters
        cli.communicate()
        mock_cleanup.assert_called_once_with(
            'crassus-output', 30, 'mystack', 'eu-west-1')
        mock_notify.assert_called_once_with(
            'mystack',
            'parameter1=value1,parameter2=value2',
            'my::topic::arn', 'eu-west-1')
        mock_receive.assert_called_once_with(
            'crassus-output', 600, 'mystack', 'eu-west-1')

    @patch('gaius.service.receive')
    @patch('gaius.service.notify')
    @patch('gaius.service.cleanup')
    @patch('gaius.cli.docopt')
    def test_should_fail_with_error(self, mock_docopt, mock_cleanup, mock_notify,
                                    mock_receive):
        """
        sys.exit in cli throws SystemExit. We catched that.
        """
        mock_receive.side_effect = DeploymentErrorException("failed")
        with self.assertRaises(SystemExit):
            cli.communicate()
