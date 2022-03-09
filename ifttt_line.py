import requests

class IFTTTLine:
    
    def __init__(self, event, key):
        self.webhook = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(event, key)
    
    def send_message(self, val1='', val2='', val3=''):
        requests.post(self.webhook, data={'value1': val1, 'value2': val2, 'value3': val3})
        
if __name__ == '__main__':
    IFTTTLine.send_message('test_message')