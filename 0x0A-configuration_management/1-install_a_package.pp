# Flask install
exec { 'install':
  command  => 'pip3 install flask',
  path     => '/bin:/sbin:/usr/bin:/usr/sbin'
}
