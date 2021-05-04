def get_monitors_for_server(server_name):
    return ""

def extract_device_facts(device_facts):
    row = {}
    rows = []
    pools = device_facts['ltm_pools']['members']
    server_name = ""
    destination_address = ""
    destination_port = ""
    description = ""
    enabled = ""
    availability_status = ""
    status_reason = ""
    monitors = get_monitors_for_server(server_name)
    ltm_pools = []

    for vs in device_facts['virtual_servers']:
        row["server_name"] = vs['name']
        row["destination_address"] = vs['destination_address']
        row["destination_port"] = vs['destination_port']
        row["description"] = vs['description']
        row["enabled"] = vs['enabled']
        row["availability_status"] = vs['availability_status']
        row["status_reason"] = vs['status_reason']
        row["monitors"] = vs['monitors']
        rows.append(row)
        
    return device_facts.keys()



class FilterModule(object):
    filter_map = {
        'get_report_rows': extract_device_facts,
    }

    def filters(self):
        return self.filter_map
