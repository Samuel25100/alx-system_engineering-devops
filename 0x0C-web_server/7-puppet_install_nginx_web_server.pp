# configuring your server with Puppet to install nginx and other change

package { 'nginx':
  ensure => installed
}

file {'/var/www/html/index.nginx-debian.html':
  content => 'Hello World!'
}

file_line {'modify':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4;',
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
