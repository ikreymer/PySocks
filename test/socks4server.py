from twisted.internet import reactor
from twisted.protocols.socks import SOCKSv4Factory

def run_proxy():
    reactor.listenTCP(1080, SOCKSv4Factory("/dev/null"))
    try:
        reactor.run()
    except (KeyboardInterrupt, SystemExit):
        reactor.stop()

if __name__ == "__main__":
    print "Running SOCKS4 proxy server"
    run_proxy()
