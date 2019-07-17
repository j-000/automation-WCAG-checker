import re
import requests

class Scanner:

    def __init__(self, checkpoints):
        self.checkpoints = checkpoints
        self.rules = {
            '1': self.should_contain,
            '2': self.should_contain,
            '3': self.should_contain,
            '4': self.should_not_contain,
        }
    
    def get_html(self, url):
        req = requests.get(url)
        return req.text if req.status_code > 199 and req.status_code < 400 else req.status_code

    def transform(self, s):
        return re.compile(s)
    
    def should_contain(self, html_text, checkpoint):
        regex = self.transform(checkpoint['regex'])

        match_array = re.findall(regex, html_text)
        if len(match_array) > 0:
            return True
        return False

    def should_not_contain(self, html_text, checkpoint):
        regex = self.transform(checkpoint['regex'])

        match_array = re.findall(regex, html_text)
        if len(match_array) > 0:
            return False
        return True

    def count_instances(self, html_text, checkpoint):
        regex = self.transform(checkpoint['regex'])
        return False


    def scan(self, url):
        scan_report = {}

        html_text = self.get_html(url)
        if type(html_text) is int:
            return {'error': 'Request failed.'}
        for checkpoint in self.checkpoints:
            id = str(checkpoint['id'])

            func = self.rules[id]
            checkpoint_test_response = func(html_text, checkpoint)
            scan_report.update({id: { 'name': checkpoint['name'], 'result': 'passed' if checkpoint_test_response else 'failed' } })
        return scan_report
            
