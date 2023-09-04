# Configure Nginx so that its HTTP response contains a custom header

exec { 'install_and_conf_nginx':
  provider => shell
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo echo "Holberton School" > /var/www/html/index.nginx-debian.html ; sudo echo "Ceci n\'est pas une page" > /usr/share/nginx/html/custom_404.html ; sudo sed -i "s/server_name _;/server_name _;\n\n\trewrite ^\/redirect_me https:\/\/github.com\/Ammar-Khaled permanent;\n\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default ; sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/sites-available/default ; sudo service nginx start'
}
