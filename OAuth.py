from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

github_blueprint =  make_github_blueprint(client_id=' ', client_secret=' ')
app.register_blueprint(github_blueprint, url_prefix='/github_login')

@app.route('/github')
def github_login():
	return redirect(url_for('github.login'))
