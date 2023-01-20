from xtlsapi import XrayClient, utils, exceptions

xray_client = XrayClient('127.0.0.1', 10085)

user_email = 'uuid@hiddify.com'
inbound_tag = 'vmess-ws'

# Get stats
print(utils.human_readable_bytes(xray_client.get_client_download_traffic(user_email)))
print(utils.human_readable_bytes(xray_client.get_client_upload_traffic(user_email)))
print(utils.human_readable_bytes(xray_client.get_inbound_download_traffic(inbound_tag)))
print(utils.human_readable_bytes(xray_client.get_inbound_upload_traffic(inbound_tag)))

# restart logger
# xray_client.restart_logger()
