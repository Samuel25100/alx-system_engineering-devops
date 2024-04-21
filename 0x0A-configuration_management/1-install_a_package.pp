# install flask from pip3 with version 2.1.0

package { 'flask':
  ensure  => installed,
  require => Exec['install_flask']
}

exec { 'install_flask':
  command => '/usr/bin/pip install flask=2.0.1',
}
