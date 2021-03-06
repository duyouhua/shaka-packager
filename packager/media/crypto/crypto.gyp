# Copyright 2017 Google Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

{
  'variables': {
    'shaka_code': 1,
  },
  'targets': [
    {
      'target_name': 'crypto',
      'type': '<(component)',
      'sources': [
        'encryption_handler.cc',
        'encryption_handler.h',
      ],
      'dependencies': [
        '../base/media_base.gyp:media_base',
        '../codecs/codecs.gyp:codecs',
      ],
    },
    {
      'target_name': 'crypto_unittest',
      'type': '<(gtest_target_type)',
      'sources': [
        'encryption_handler_unittest.cc',
      ],
      'dependencies': [
        '../../testing/gtest.gyp:gtest',
        '../../testing/gmock.gyp:gmock',
        '../base/media_base.gyp:media_handler_test_base',
        '../test/media_test.gyp:media_test_support',
        'crypto',
      ]
    },
  ],
}

