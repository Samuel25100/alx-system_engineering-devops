# make changes to our configuration file to connect to a server without pwd


file_line { 'ssh_change_private':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'ssh_change_password':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}
