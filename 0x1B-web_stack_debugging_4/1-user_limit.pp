# Change the number of user limit for holberton
exec {'change_limit':
  command => '/bin/sed -i "s|nofile [0-9]| nofile 500|g" /etc/security/limits.conf'
}
