def extract_device_facts(device_facts):
    row = {}
    rows = []
    return device_facts.keys



class FilterModule(object):
    filter_mnap = {
        'get_report_rows': extract_device_facts,
    }
    
    data = extract_device_facts

    def filters(self):
        return data