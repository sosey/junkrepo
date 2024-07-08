import os

def test_bad_except():
        # When the config file doesn't exist
        cfg_file = os.path.join(os.getcwd(), 'notafile')
        try:
            print("no except clause")
        except:
            pass
