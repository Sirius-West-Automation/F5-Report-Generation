def get_monitors_for_server(server_name):
    return ""

def extract_device_facts(device_facts):
    rows = []
    ltm_pools = device_facts['ltm_pools']


    for vs in device_facts['virtual_servers']:
        row = {}
        default_pool = vs['default_pool']

        row["server_name"] = vs['name']
        row["destination_address"] = vs['destination_address']
        row["destination_port"] = vs['destination_port']
        row["description"] = vs['description']
        row["enabled"] = vs['enabled']
        row["availability_status"] = vs['availability_status']
        row["status_reason"] = vs['status_reason']

        for pool in ltm_pools:
            if pool['full_path'] == default_pool:
                for monitor in pool['monitors']:
                    row["monitor"] = monitor
                    row["pool_name"] = pool['name']
                    rows.append(row)

    return rows



class FilterModule(object):
    filter_map = {
        'get_report_rows': extract_device_facts,
    }

    def filters(self):
        return self.filter_map
