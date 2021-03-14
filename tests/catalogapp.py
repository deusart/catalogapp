from config import settings, outputs
settings.OUTPUT = outputs.trace_none

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
        import catalogapp
    except Exception as exeption:
        test_failed('import catalogapp', exeption)
    else:
        test_passed('import catalogapp')

    