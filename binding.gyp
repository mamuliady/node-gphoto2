{
  'targets': [
    {
      'target_name': 'gphoto2',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'sources': [
        'src/autodetect.cc',
        'src/binding.cc',
        'src/camera.cc',
        'src/camera_helpers.cc',
        'src/gphoto.cc'
      ],
      'cflags': [
        '--std=c++14'
      ],
      'cflags!': [
        '-fno-exceptions'
      ],
      'target_arch': 'arm',
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CPLUSPLUSFLAGS' : [
              '-std=c++14',
              '-stdlib=libc++',
              '<!(/opt/homebrew/bin/pkg-config --cflags libgphoto2)',
            ]
          },
          'link_settings': {
            'libraries': [
              '<!(/opt/homebrew/bin/pkg-config --libs libgphoto2)',
              '<!(/opt/homebrew/bin/pkg-config --libs libgphoto2_port)'
            ]
          },
        }],
        ["OS=='linux'", {
            'link_settings': {
              'libraries': [
                '-lgphoto2',
                '-lgphoto2_port'
              ]
            },

        }],

      ]
    }
  ]
}