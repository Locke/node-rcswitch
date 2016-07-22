{
  'targets': [
    {
      'target_name': 'rcswitch',
      'sources': [
        'src/rcswitch.cpp',
        'src/RCSwitchNode.cpp',
        'externals/rcswitch-pi/RCSwitch.cpp',
        'externals/rcswitch-pi/RFSniffer.cpp'
      ],
      'include_dirs': [
        '/usr/local/include',
        "<!(node -e \"require('nan')\")"
      ],
      'ldflags': [
        '-lwiringPi'
      ]
    }
  ]
}
