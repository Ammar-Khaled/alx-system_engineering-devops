# This puppet manifest increases the nginx max open files limit to fix problem of high amount of requests

exec { 'edit':
  provider => shell,
  command  => "sudo sed -i 's/15/4096/' /etc/default/nginx; sudo service nginx restart"
}
