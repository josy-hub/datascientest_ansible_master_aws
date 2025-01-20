"""Role testing files using testinfra."""

import requests

def test_services_running(host):
    nginx = host.service("nginx")
    mysql = host.service("mysql")

    assert nginx.is_running
    assert mysql.is_running

def test_magento_homepage(host):
    response = requests.get("http://ec2-13-38-35-28.eu-west-3.compute.amazonaws.com")
    assert response.status_code == 200, "La page d'accueil Magento ne répond pas correctement"


def test_magento_db_connection(host):
    command = host.run("mysql -u magento_user -ppassword -e 'SHOW DATABASES;'")
    assert "magento_db" in command.stdout, "Magento n'a pas accès à la base de données"
