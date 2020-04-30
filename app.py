import os
import json
from flask import request, Flask

config = json.load(open('config.json'))
PASSWD = config['sudo_passwd']
HOSTS = config['hosts']
app = Flask(__name__)


def sh(command):
    os.system('echo {} | sudo -S {}'.format(PASSWD, command))


def update_hosts(host, dest):
    sh('sed -i \'/{}/d\' {}'.format(host, HOSTS))
    sh('sed -i \'$a\\{}  {}\' {}'.format(dest, host, HOSTS))


@app.route('/hosts', methods=['POST'])
def hosts():
    host = request.form.get('host')
    dest = request.form.get('dest')
    update_hosts(host, dest)
    return 'OK'


if __name__ == '__main__':
    app.run('0.0.0.0')
