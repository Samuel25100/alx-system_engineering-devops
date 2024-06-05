#Fix apache error of php
exec {'echo foo':
command => '/bin/sed -i "s|/class-wp-locale.phpp|/class-wp-locale.php|" /var/www/html/wp-settings.php'
}

service {'apache2':
ensure => 'running',
}
