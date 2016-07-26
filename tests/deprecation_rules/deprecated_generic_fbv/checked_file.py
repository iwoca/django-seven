# Old generic fbv calls
url_patterns = [
    url(r'^direct_url$'. direct_to_template('direct_template.html')),
    url(r'^redirect_url$'. redirect_to('redirect_template.html')),
]
