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

"""Test that each file in fail/ actually fails mypy."""

import os
import unittest

from typing import Iterable

from mypy import api

TEST_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fail')


def get_tests() -> Iterable[str]:
    for dirpath, _, filenames in os.walk(TEST_PATH):
        for filename in filenames:
            yield os.path.join(dirpath, filename)


class TestMypyFails(unittest.TestCase):

    def ensure_mypy_fails(self, filename: str) -> None:
        stdout, stderr, exit_status = api.run([filename])
        self.assertTrue(exit_status, msg=stdout)

    def test_mypy_failures(self) -> None:
        for filename in get_tests():
            with self.subTest(filename=filename):
                self.ensure_mypy_fails(filename)


if __name__ == "__main__":
    unittest.main()
