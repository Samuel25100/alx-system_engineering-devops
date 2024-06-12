#Configure nginx to accept more user 10000
file_line { 'increase_worker_connections':
  path  => '/etc/nginx/nginx.conf',
  line  => 'worker_connections 10000;',
  match => '^worker_connections\s+\d+;$',
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}
