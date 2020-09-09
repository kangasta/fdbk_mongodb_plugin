import os
from unittest import TestCase
import warnings

from unittest.mock import Mock, patch

from fdbk.utils import CommonTest

from pymongo import MongoClient
from fdbk_mongodb_plugin import ConnectionClass


MONGO_URL = 'mongodb://localhost:27017'
MONGO_ARGS = (MONGO_URL,)


class DynamoDbConnectionCommonTest(CommonTest, TestCase):
    def setUp(self):
        self.C = ConnectionClass(*MONGO_ARGS)

    def tearDown(self):
        self.C._db.drop_collection("topics")
        self.C._db.drop_collection("data")
