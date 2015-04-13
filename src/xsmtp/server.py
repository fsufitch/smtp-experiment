import asyncore
from smtpd import SMTPServer

class XSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print("Peer", peer)
        print("Mailfrom", mailfrom)
        print("Rcpttos", rcpttos)
        print("Data", data)
        print("=================")
        with open('/tmp/xsmtp.txt', 'w') as f:
            print("Peer", peer, file=f)
            print("Mailfrom", mailfrom, file=f)
            print("Rcpttos", rcpttos, file=f)
            print("Data", data, file=f)
            

def main():
    print("hi")
    server = XSMTPServer(('127.0.0.1', 25), None)
    
    asyncore.loop()
