# Install flask from pip3 with version 2.1.0
package {'flask':
  ensure => 'Flask 2.1.0',
  source => 'pip3'
}
