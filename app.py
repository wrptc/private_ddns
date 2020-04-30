import os
import json
from flask import request, Flask

config = json.load(open('config.json'))
PASSWD = config['sudo_passwd']
HOSTS = config['hosts']

def sh(command):
    os.system(f'echo {PASSWD} | sudo -S {command}')

def update_hosts(host, dest):
    sh(f'sed -i \'/{host}/d\' {HOSTS}')
    sh(f'sed -i \'$a\\{dest}  {host}\' {HOSTS}')
    
app = Flask(__name__)
@app.route('/hosts', methods=['POST'])
def hosts():
    host = request.form.get('host')
    dest = request.form.get('dest')
    update_hosts(host, dest)
    return 'OK'

if __name__ == '__main__':
    app.run('0.0.0.0')
