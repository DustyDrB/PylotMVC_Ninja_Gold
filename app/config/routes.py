"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['POST']['/process_money'] = 'Welcome#process_money'
