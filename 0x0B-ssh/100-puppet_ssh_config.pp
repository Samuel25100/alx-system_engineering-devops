# make changes to our configuration file to connect to a server without pwd

file {'/etc/ssh/sshd_config':
  ensure  => file,
  content => "\
Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no",
}
