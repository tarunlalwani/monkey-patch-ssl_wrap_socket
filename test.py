try:
    import requests
    assert requests.__version__ != "2.18.0"
    import requests.packages.urllib3.util.ssl_ as ssl_
    import requests.packages.urllib3.connection as connection
except (ImportError,AssertionError,AttributeError):
    import urllib3.util.ssl_ as ssl_
    import urllib3.connection as connection

import requests
# import urllib3
print("Using " + requests.__version__)
_orig_wrap_socket = ssl_.ssl_wrap_socket

def _ssl_wrap_socket(sock, keyfile=None, certfile=None, cert_reqs=None,
                     ca_certs=None, server_hostname=None,
                     ssl_version=None, ciphers=None, ssl_context=None,
                     ca_cert_dir=None):
    print('SHOULD BE PRINTED')
    return _orig_wrap_socket(sock, keyfile=keyfile, certfile=certfile,
                      cert_reqs=cert_reqs, ca_certs=ca_certs,
                      server_hostname=server_hostname, ssl_version=ssl_version,
                      ciphers=ciphers, ssl_context=ssl_context,
                      ca_cert_dir=ca_cert_dir)

connection.ssl_wrap_socket = _ssl_wrap_socket

res = requests.get("https://www.google.com", verify=True)
