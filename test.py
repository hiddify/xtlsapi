from xtlsapi import XrayClient, utils, exceptions

xray_client = XrayClient('1.2.3.4', 1234)
user_id = utils.generate_random_user_id()
user_email = utils.generate_random_email()
inbound_tag = 'inbound-tag'

# Get stats
print(utils.human_readable_bytes(xray_client.get_client_download_traffic('user-email@mail.com')))
print(utils.human_readable_bytes(xray_client.get_client_upload_traffic('user-email@mail.com')))
print(utils.human_readable_bytes(xray_client.get_inbound_download_traffic(inbound_tag)))
print(utils.human_readable_bytes(xray_client.get_inbound_upload_traffic(inbound_tag)))
print(utils.human_readable_bytes(xray_client.get_total_download_traffic()))
print(utils.human_readable_bytes(xray_client.get_total_upload_traffic()))

# Add & Remove client
user = xray_client.add_client(inbound_tag, user_id, user_email)
if user:
    print(user)
    xray_client.remove_client(inbound_tag, user_email)

# restart logger
xray_client.restart_logger()