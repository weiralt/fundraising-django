from payment.MPG import *
from datetime import datetime
from base64 import b64encode
from Crypto.Cipher import AES
import hashlib

class NewWebPayment:
    def __init__(self, merchant_order_no, amt, item_descr):
        self.merchant_order_no = merchant_order_no
        self.amt = amt
        self.item_descr = item_descr

    def get_trade_info(self):
        data = (
            f"MerchantID={MERCHANT_ID}&"
            f"RespondType={RESPONDTYPE}&"
            f"TimeStamp={datetime.now().strftime('%s')}&"
            f"Version={VERSION}&"
            f"MerchantOrderNo={self.merchant_order_no}&"
            f"Amt={self.amt}&"
            f"ItemDesc={self.item_descr}&"
            f"CREDIT=1&"
            f"VACC=1&"
            f"ReturnURL={RETURN_URL}&"
            f"NotifyURL={NOTIFY_URL}&"
            f"ClientBackURL={CLIENTBACK_URL}&"
            f"CustomerURL={CUSTOMER_URL}"
            )

        return data

    @staticmethod
    def get_trade_sha(key, iv, encrypt_trade_info):
        raw_trade_sha =(
            f"HashKey={key}&"
            f"{encrypt_trade_info}&"
            f"HashIV={iv}"
            )
        return raw_trade_sha

    @staticmethod
    def addpadding(raw_trade_info, blocksize=32):
        length = len(raw_trade_info.encode('utf8'))
        padding = blocksize - (length % blocksize)
        raw_trade_info += chr(padding) * padding
        return raw_trade_info

    @staticmethod
    def unpadding(trade_info_pad, blocksize=32):
        for i in range(0, len(trade_info_pad)-1):
            if trade_info_pad[i] < blocksize:
                trade_info = trade_info_pad[0: i]
                break
        return trade_info

    # key and iv must be bytes type, remember to covert before
    @staticmethod
    def encrypt(raw_trade_info_pad, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        ct_bytes = cipher.encrypt(raw_trade_info_pad)
        encrypt_trade_info = ct_bytes.hex()
        return encrypt_trade_info

    @staticmethod
    def sha256hex(raw_trade_sha):
        bin_trade_sha = raw_trade_sha.encode('ascii')
        trade_sha = hashlib.sha256(bin_trade_sha).hexdigest()
        return trade_sha.upper()

    @staticmethod
    def decrypt(encrypt_trade_info, key, iv):
        trade_info_to_bin = bytes.fromhex(encrypt_trade_info)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        trade_info_pad = cipher.decrypt(trade_info_to_bin)
        return trade_info_pad
