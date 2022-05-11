# Flask install
exec { 'flask':
  command  => 'pip3 install flask',
  path     => '/usr/bin:/usr/sbin:/bin'
}
