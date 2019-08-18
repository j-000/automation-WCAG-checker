import re
import requests
from custommodels import Checkpoint

class Scanner:

    def __init__(self):
        self._checkpoints = Checkpoint.get_all()
        self._rules = {
            '1': self._should_contain,
            '2': self._should_contain,
            '3': self._should_contain,
            '4': self._should_not_contain,
        }
    
    def _get_html(self, url):
        req = requests.get(url)
        return req.text if req.status_code > 199 and req.status_code < 400 else req.status_code

    def _transform(self, s):
        return re.compile(s)
    
    def _should_contain(self, html_text, checkpoint):
        regex = self._transform(checkpoint['regex'])

        match_array = re.findall(regex, html_text)
        if len(match_array) > 0:
            return True
        return False

    def _should_not_contain(self, html_text, checkpoint):
        regex = self._transform(checkpoint['regex'])

        match_array = re.findall(regex, html_text)
        if len(match_array) > 0:
            return False
        return True

    def _count_instances(self, html_text, checkpoint):
        regex = self._transform(checkpoint['regex'])
        return False


    def scan(self, url):
        scan_report = {}

        html_text = self._get_html(url)
        if type(html_text) is int:
            return {'error': 'Request failed.'}
        for checkpoint in self._checkpoints:
            id = str(checkpoint['id'])

            func = self._rules[id]
            checkpoint_test_response = func(html_text, checkpoint)
            scan_report.update({id: { 'name': checkpoint['name'], 'result': 'passed' if checkpoint_test_response else 'failed' } })
        return scan_report
            
