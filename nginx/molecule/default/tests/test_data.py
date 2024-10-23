# test présent par défaut dans le fichier qui vérifie si le fichier /etc/hosts existe dans la cible
def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

# test que nous rajoutons  qui vérifie si le le paquet nginx est bien installé
def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

# test que nous rajoutons  qui vérifie si le le paquet git est est bien installé
def test_git_is_installed(host):
    git = host.package("git")
    assert git.is_installed

# nous rajoutons cette ligne qui fera échouer le test car le fichier datascientest.conf n'existe pas dans le répertoire /etc
def test_hosts_file(host):
    """Validate /etc/datascientest.conf."""
    f = host.file("/etc/datascientest.conf")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
