from config import settings, outputs
settings.OUTPUT = outputs.trace_none
from catalogapp.cappengine import templates

def run_test(all_results=False):

    if all_results == True:
        def test_passed(test):
            print(f"[Passed] Test '{test}' is passed.")
    else:
        def test_passed(test):
            pass

    def test_failed(test, exeption):
        message = str(exeption).replace("'","")
        print(f"[Failed] Test '{test}' is failed.")
        print(f"[Failed] {message}.")

    try:
        from catalogapp.cappengine import templates
    except Exception as exeption:
        test_failed('import templates', exeption)
    else:
        test_passed('import templates')
    
    try:
        assert templates.filters.empty == ''
    except Exception as exeption:
        test_failed('filters content', exeption)
    else:
        test_passed('filters content')

    try:
        assert templates.urls.authorization == 'https://catalog.app/api/authorization'
    except Exception as exeption:
        test_failed('urls content', exeption)
    else:
        test_passed('urls content')

    try:
        assert templates.paths.catalogs == ''
    except Exception as exeption:
        test_failed('paths content', exeption)
    else:
        test_passed('paths content')