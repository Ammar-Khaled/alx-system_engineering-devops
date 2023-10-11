# fix typo in file extension

exec { 'replace':
    provider => shell,
    command  => 'sed -i "s/.phpp/.php" /var/www/html/wp-settings.php'
}
