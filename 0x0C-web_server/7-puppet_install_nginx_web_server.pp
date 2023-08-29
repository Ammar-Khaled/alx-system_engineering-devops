# install and configure nginx

exec { 'install':
  provider => shell,
  command  => 'apt-get -y update ; apt-get -y install nginx ; echo 'Hello World!' | sudo tee /var/www/html/index.nginx-debian.html ; sudo echo 'Ceci n\'est pas une page' | sudo tee /var/www/html/404.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/Ammar-Khaled permanent;\n\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default ; sudo service nginx start '
}
