import os

def test_bad_except():
        # When the config file doesn't exist
        cfg_file = os.path.join(os.getcwd(), 'notafile')
        try:
            print("failure test in non-bandit config repo")
        except:
            pass