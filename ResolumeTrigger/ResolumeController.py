#! python3


import sys
from pythonosc import osc_message_builder,udp_client,dispatcher,osc_server
import logging
import random
import time
from threading import Thread

logger = logging.getLogger("ResolumeController")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# add ch to logger
logger.addHandler(ch)

def start():

	resolume_controller = ResolumeController( )
	resolume_controller.run()


class ResolumeController(): 

	def __init__(self):
		self.osc_resolume_sender = udp_client.SimpleUDPClient("localhost", 7000)
		self.osc_dispatcher = dispatcher.Dispatcher()

	def run(self):
		
		self.trigger_restart_overlay()

	def create_play_from_begining_message(self):

		return "/layer2/clip1/connect"


	def trigger_restart_overlay(self): 

		message_builder = osc_message_builder.OscMessageBuilder(self.create_play_from_begining_message())
		message_builder.add_arg( 1)
		self.osc_resolume_sender.send(message_builder.build())
  
		logger.info("Restart Show." )


if __name__ == "__main__": 

	start()


