# Create file school in /tmp with permission, owner, and content of I love puppet
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
}
