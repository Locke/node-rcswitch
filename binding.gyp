{
  'targets': [
    {
      'target_name': 'rcswitch',
      'defines': [ 'RPI' ],
      'sources': [ 'src/rcswitch.cpp', 'src/RCSwitchNode.cpp', 'externals/rc-switch/RCSwitch.cpp' ],
      'include_dirs': [ '/usr/local/include', "<!(node -e \"require('nan')\")" ],
      'ldflags': [ '-lwiringPi' ]
    }
  ]
}
