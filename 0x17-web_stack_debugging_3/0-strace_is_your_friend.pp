# Puppet manifest to fix Apache 500 error
exec { 'fix_apache_error':
  command     => '/bin/sed -i "s/old_value/new_value/g" /path/to/config_file',
  refreshonly => true,
  subscribe   => File['/path/to/config_file'],
}

file { '/path/to/config_file':
  ensure  => present,
  content => template('path/to/template.erb'),
}
