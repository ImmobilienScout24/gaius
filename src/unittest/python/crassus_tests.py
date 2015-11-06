# -*- coding: utf-8 -*-
from unittest import TestCase
from gaius.crassus import notify_crassus
import boto3
from moto import mock_sns


class CrassusTests(TestCase):

    def setUp(self):
        self.my_mock_sns = mock_sns()
        self.my_mock_sns.start()
        self.sns = boto3.client('sns')
        self.arn = self.sns.create_topic(Name='test_sns')

    def tearDown(self):
        self.my_mock_sns.stop()

    def test_notify_crassus(self):
        response = notify_crassus(
            topic_arn=self.arn['TopicArn'], message='{}')
        self.assertEquals(response['ResponseMetadata']['HTTPStatusCode'], 200)