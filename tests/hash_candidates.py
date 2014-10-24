#!/usr/bin/python
#
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Given a list of candidates on stdin, produce a file of hashes ("map file").
"""

import csv
import sys

import rappor


def main(argv):
  # TODO: need to read params file?
  num_cohorts = 64
  num_hashes = 2
  num_bloombits = 16

  csv_out = csv.writer(sys.stdout)

  for line in sys.stdin:
    word = line.strip()
    row = [word]
    for cohort in xrange(num_cohorts):
      for hash_no in xrange(num_hashes):
        bf_bit = rappor.get_bf_bit(word, cohort, hash_no, num_bloombits) + 1
        row.append(cohort * num_bloombits + bf_bit)
    csv_out.writerow(row)


if __name__ == '__main__':
  try:
    main(sys.argv)
  except RuntimeError, e:
    print >>sys.stderr, e.args[0]
    sys.exit(1)
