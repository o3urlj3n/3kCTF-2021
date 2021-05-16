python -m virtualenv ve
. ve/bin/activate
pip install flask
pip install flask_cors
sudo useradd -m app
sudo -u app mkdir ~/test ~/testpy
sudo -u app flask run

rm -r ./ve
