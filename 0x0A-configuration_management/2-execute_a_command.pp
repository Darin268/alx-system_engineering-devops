# Puppet manifest to kill a process named killmenow using pkill

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
