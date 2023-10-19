# This puppet manifest increases the max open files limit for the 'holberton' user

exec { 'edit':
  provider => shell,
  command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 1024/' /etc/security/limits.conf;
               sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 1024/' /etc/security/limits.conf"
}
