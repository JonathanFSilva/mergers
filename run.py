# -*- coding: utf-8 -*-
# run.py

import os

from app import create_app
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
    """
    descomente a linha abaixo se estiver rodando no c9
    """
    # app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
