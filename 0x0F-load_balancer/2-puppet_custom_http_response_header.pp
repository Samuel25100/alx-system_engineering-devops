# task #0, we’d like you to automate the task of creating a
# custom HTTP header response

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file {'/etc/nginx/sites-available/default':
  ensure => 'file'
}

file_line{'X-Served-By':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  line    => '    server_name _;\n            add_header X-Served-By $hostname;',
  match   => 'server_name _;',
  require => Exec['sudo service nginx']
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
