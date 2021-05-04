def get_monitors_for_server(server_name):
    return ""

def extract_device_facts(device_facts):
    rows = []
    #pools = device_facts['ltm_pools']['members']
    #monitors = get_monitors_for_server(server_name)
    ltm_pools = []

    for vs in device_facts['virtual_servers']:
        row = {}
        row["server_name"] = vs['name']
        row["destination_address"] = vs['destination_address']
        row["destination_port"] = vs['destination_port']
        row["description"] = vs['description']
        row["enabled"] = vs['enabled']
        row["availability_status"] = vs['availability_status']
        row["status_reason"] = vs['status_reason']
#        row["monitors"] = vs['monitors']

        rows.append(row)

    return rows



class FilterModule(object):
    filter_map = {
        'get_report_rows': extract_device_facts,
    }

    def filters(self):
        return self.filter_map
