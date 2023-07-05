file { '/etc/ssh/sshd_config':
  ensure  => file,
  content => epp('ssh/sshd_config.epp'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => epp('ssh/ssh_config.epp'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

exec { 'reload_sshd_config':
  command     => '/usr/sbin/service sshd reload',
  refreshonly => true,
  subscribe   => File['/etc/ssh/sshd_config'],
}
