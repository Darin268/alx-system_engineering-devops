# Puppet manifest to configure SSH client settings
file_line { 'Turn off passwd auth':
path    => '/home/ubuntu.ssh/config',
line    => 'PasswordAuthentication no',
match   => '^PasswordAuthentication.*$',
}


file_line { 'Declare identity file':
path    => '/home/ubuntu/.ssh/config',
line    => 'IdentityFile ~/.ssh/school',
match   => '^IdentityFile.*$',
}
