from flask import render_template
from .decoration import ensure_running

@ensure_running
def page_not_found(error):
    # 因为是从factories.__init__调取的，所以模板也是在factories/templates/里
    return render_template('404.html'), 404