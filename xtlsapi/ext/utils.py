import uuid
import math
import socket
import secrets

from xtlsapi.xray_api.common.serial import typed_message_pb2


def to_typed_message(message):
    return typed_message_pb2.TypedMessage(
        type=message.DESCRIPTOR.full_name, value=message.SerializeToString()
    )


def ip2bytes(ip: str):
    return bytes([int(i) for i in ip.split('.')])


def generate_random_tag():
    return secrets.token_urlsafe()


def generate_random_name(hex_count=8):
    return f"{secrets.token_hex(hex_count)}"


def generate_random_user_id():
    return uuid.uuid4().hex


def generate_random_email(tld='vump.com', hex_count=8):
    return f"{generate_random_name(hex_count)}@{tld}"


def generate_random_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


def human_readable_bytes(size_bytes):
    if not size_bytes:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"
