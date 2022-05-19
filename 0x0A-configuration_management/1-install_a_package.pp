# Flask install
package { 'flask':
  provider => 'pip3',
  path => '/usr/bin:/usr/sbin:/bin'
}
