from ansible.utils.display import Display
import json

display = Display()

def get_monitors_for_server(server_name):
    return ""

def extract_device_facts(device_facts):

    display.v("Testing writing to the console...")

    rows = []
    ltm_pools = device_facts['ltm_pools']

    virtual_servers = device_facts["virtual_servers"]

    for vs in virtual_servers:
        #json_vs = json.dumps(vs, indent=2)
        #display.v(json_vs)

        row = {}
        try:
            default_pool = vs["default_pool"]
        except:
            default_pool = "undefined"

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
