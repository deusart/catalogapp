# test modules import

from config import settings
from core import outputs
settings.OUTPUT = outputs.trace_none

def run_test(all_results = True):
    
    if all_results == True:
        def test_passed(module):
            print(f"[Passed] Module '{module}' import passed.")
    else:
        def test_passed(module):
            pass

    def test_failed(module, exeption):
        message = str(exeption).replace("'","")
        print(f"[Failed] Module '{module}' import failed.")
        print(f"[Failed] {message}.")

    # core
    try:
        import core
    except Exception as exeption:
        test_failed('core', exeption)
    else:
        test_passed('core')

    try:
        from core import debug
    except Exception as error:
       test_failed('core.debug', exeption)
    else:
        test_passed('core.debug')

    try:
        from core import files
    except Exception as error:
       test_failed('core.files', exeption)
    else:
        test_passed('core.files')

    try:
        from core import http
    except Exception as error:
       test_failed('core.http', exeption)
    else:
        test_passed('core.http')

    # config
    try:
        import config
    except Exception as exeption:
        test_failed('config', exeption)
    else:
        test_passed('config')

    try:
        from config import settings
    except Exception as exeption:
        test_failed('config.settings', exeption)
    else:
        test_passed('config.settings')

    # catalogapp
    try:
        import catalogapp
    except Exception as exeption:
        test_failed('catalogapp', exeption)
    else:
        test_passed('catalogapp')

    try:
        from catalogapp import base
    except Exception as error:
       test_failed('catalogapp.base', exeption)
    else:
        test_passed('catalogapp.base')

    try:
        from catalogapp import catalogs
    except Exception as error:
       test_failed('catalogapp.catalogs', exeption)
    else:
        test_passed('catalogapp.catalogs')

    # catalogapp.engine
    try:
        import catalogapp.engine
    except Exception as exeption:
        test_failed('catalogapp.engine', exeption)
    else:
        test_passed('catalogapp.engine')

    try:
        from catalogapp.engine import calculations
    except Exception as error:
       test_failed('catalogapp.engine.calculations', exeption)
    else:
        test_passed('catalogapp.engine.calculations')

    try:
        from catalogapp.engine import engine
    except Exception as error:
       test_failed('catalogapp.engine.engine', exeption)
    else:
        test_passed('catalogapp.engine.engine')

    try:
        from catalogapp.engine import entities
    except Exception as error:
       test_failed('catalogapp.engine.entities', exeption)
    else:
        test_passed('catalogapp.engine.entities')

    try:
        from catalogapp.engine import templates
    except Exception as error:
       test_failed('catalogapp.engine.templates', exeption)
    else:
        test_passed('catalogapp.engine.templates')


