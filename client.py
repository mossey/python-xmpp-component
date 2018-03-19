import json
import logging
import xml.etree.ElementTree as ET
from sleekxmpp import ClientXMPP


def message(msg):
    msg.reply("payload not provided \n").send()
    return


class EchoBot(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", message)

        # If you wanted more functionality, here's how to register plugins:
        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0199')  # XMPP Ping

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

        # If you are working with an OpenFire server, you will
        # need to use a different SSL version:
        # import ssl
        # self.ssl_version = ssl.PROTOCOL_SSLv3

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

        # queue_.queue_p2p_request(
        # payload="Kd4tQTgA1so9oNOytI5r49JF5S/ucwojvXsBK/81xEjYJpM9pO5m/smaStYCNPgCBZeigYMORHV2YSr7eh5yqKukPeLz9c2qNR4Rol75Hi8AIqhs07i9+JKaN226/8nrjOltX07TWD039iE+y/Jx0quEnZs+5s2QWllELrNURdFO47G3Prp18NOE40SqvuW88dJ7DqefBmzAKid8eAQiLoiZ56UUYcFZ1splXxOAuIS3x51ZqlfLsAybMzpR5ZvDE6Cd29EsVGSLhr9fiNs4ZJ4qiEVgx0RJitypf5gf1+upINyL3jjkS582b1Ep2U83O0020U2Kb1gMQxmRqZJO+A==")



        # xmpp.disconnect(wait=True)

        # schedule=scheduler.Scheduler task=schedule.add( self, name="Tuma", seconds=1, callback= self.send_message(
        # mto='user4@52.174.184.45', mbody='This is a message',mtype="chat"), args=None, kwargs=None, repeat=False)
        # task.run()


        # s=sched.scheduler(time.time, time.sleep)
        # s.enter( delay=1, priority=1, action=self.tuma_message, argument=(self,))
        # s.run()
        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # can generate IqError and IqTimeout exceptions
        #
        # try:
        #     self.get_rqueue.py:7oster()
        # except IqError as err:
        #     logging.error('There was an error getting the roster')
        #     logging.error(err.iq['error']['condition'])
        #     self.disconnect()
        # except IqTimeout:
        #     logging.error('Server is taking too long to respond')
        #     self.disconnect()

    def tuma_message(self, event, to, message):
        self.send_message(mto=to, mbody=message, mtype="chat")


if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    xmpp_username = "mosess@localhost"
    xmpp_password = "passwor"

    xmpp = EchoBot(xmpp_username, xmpp_password)
    xmpp.connect()

    xmpp.process(block=True)