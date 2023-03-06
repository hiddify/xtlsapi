from xtlsapi import XrayClient, utils, exceptions

xray_client = XrayClient('127.0.0.1', 10085)

uuid='9623a083-b4bf-4dac-83c2-02ba9b948714'
user_email = f'{uuid}@hiddify.com'
protocol='vmess'# vless,trojan,vmess,shadowsocks
inbound_tag = 'vmess-ws'

# Get stats
print(utils.human_readable_bytes(xray_client.get_client_download_traffic(user_email)))
print(utils.human_readable_bytes(xray_client.get_client_upload_traffic(user_email)))
print(utils.human_readable_bytes(xray_client.get_inbound_download_traffic(inbound_tag)))
print(utils.human_readable_bytes(xray_client.get_inbound_upload_traffic(inbound_tag)))


user=None
# Add & Remove client
if protocol=='vmess':
    #vmess
    user = xray_client.add_client(inbound_tag, uuid, user_email,'vmess',alter_id=0)
elif protocol=='vless':
    #vless
    user = xray_client.add_client(inbound_tag, uuid, user_email,'vless',flow="xtls-rprx-vision")
elif protocol=='trojan':
    #trojan
    user = xray_client.add_client(inbound_tag, uuid, user_email,'trojan')
elif protocol=='shadowsocks':
    #shadowsocks
    user = xray_client.add_client(inbound_tag, uuid, user_email,'shadowsocks',cipher='chacha20_poly1305')

if user:
    print(user)
    xray_client.remove_client(inbound_tag, user_email)

# restart logger
# xray_client.restart_logger()
