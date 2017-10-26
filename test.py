try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

import requests
_orig_wrap_socket = requests.packages.urllib3.util.ssl_.ssl_wrap_socket

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

requests.packages.urllib3.util.ssl_.ssl_wrap_socket = _ssl_wrap_socket
reload(requests.packages.urllib3.connection)
res = requests.get("https://www.google.com", verify=True)
