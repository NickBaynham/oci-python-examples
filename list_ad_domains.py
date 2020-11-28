import oci
config = oci.config.from_file("../config", "DEFAULT")
identity = oci.identity.IdentityClient(config)
ads_list = identity.list_availability_domains(config['tenancy']).data
for ad in ads_list:
  print(ad.name)

