import base64
import hashlib
import hmac
import time
import urllib.parse

from decouple import config

from .utils import query_external_service_sync


class Kraken(object):
    @staticmethod
    def __get_kraken_signature(urlpath: str, data: dict, secret: str) -> str:
        postdata: dict = urllib.parse.urlencode(data)
        encoded: str = (str(data["nonce"]) + postdata).encode()
        message: str = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac: str = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
        sigdigest: str = base64.b64encode(mac.digest())
        return sigdigest.decode()

    @classmethod
    def get_kraken_user_balance(cls, api_key: str, private_key: str):
        api_url: str = config("KRAKEN_URL")
        uri_path: str = "/0/private/Balance"
        url: str = api_url + uri_path

        data: str = {"nonce": str(int(1000 * time.time()))}
        headers: dict = {}
        headers["API-Key"] = api_key
        # get_kraken_signature() as defined in the 'Authentication' section
        headers["API-Sign"] = cls.__get_kraken_signature(uri_path, data, private_key)

        response: dict = query_external_service_sync(
            url, http_method="post", headers=headers, body=data
        )
        if "result" in response:
            print(f"\nKraken Balances: {response['result']}\n")
        else: 
            print(f"\nKraken Error: {response['error']}\n")
