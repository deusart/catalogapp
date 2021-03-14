# from unittests import modules
# modules.run_test(False)

from tests import catalogapp, cappengine, utils, templates
templates.run_test()
catalogapp.run_test()
cappengine.run_test()
utils.run_test()
print('Test completed!')