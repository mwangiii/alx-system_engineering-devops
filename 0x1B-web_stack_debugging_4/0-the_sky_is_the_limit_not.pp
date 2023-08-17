# script to fix ulimit in nginx
# set limit to above 2000

exec {'replace' :
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
  onlyif   => "grep -qE '^ULIMIT=\"-n .*\"$' /etc/default/nginx",
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}