#Configure nginx to accept more user 10000
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
}
