# Copyright 2020-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test type checking of pymongo."""

import unittest

from typing import Iterable, List, Dict, Any

from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ServerSelectionTimeoutError


class TestPymongo(unittest.TestCase):
    client: MongoClient
    coll: Collection

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = MongoClient(
            serverSelectionTimeoutMS=250, directConnection=False)
        cls.coll = cls.client.test.test
        try:
            cls.client.admin.command('ping')
        except ServerSelectionTimeoutError as exc:
            raise unittest.SkipTest(f'Could not connect to MongoDB: {exc}')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.close()

    def test_insert_find(self) -> None:
        doc = {'my': 'doc'}
        coll2 = self.client.test.test2
        result = self.coll.insert_one(doc)
        self.assertEqual(result.inserted_id, doc['_id'])
        retreived = self.coll.find_one({'_id': doc['_id']})
        if retreived:
            # Documents returned from find are mutable.
            retreived['new_field'] = 1
            result2 = coll2.insert_one(retreived)
            self.assertEqual(result2.inserted_id, result.inserted_id)

    def test_cursor_iterable(self) -> None:
        def to_list(iterable: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
            return list(iterable)
        self.coll.insert_one({})
        cursor = self.coll.find()
        docs = to_list(cursor)
        self.assertTrue(docs)


if __name__ == "__main__":
    unittest.main()
