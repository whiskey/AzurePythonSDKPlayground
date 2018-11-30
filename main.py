from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient

client = get_client_from_cli_profile(ResourceManagementClient)
rgs = client.resource_groups.list()
for rg in rgs:
    data = {'name': rg.name, 'location': rg.location}
    print('Resource Group: {name} @ {location}'.format(**data))

# raw JSON instead? try this!
# for rg in client.resource_groups.list(raw=True):
#     print(rg)
