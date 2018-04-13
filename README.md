# Barista
IOT Alexa-Coffee Pot Integration App.

The objective of Barista is its smart home appliance ability to integrate the coffee making process with Amazon Spot and a Raspberry Pi GPIO. Barista is a skill product developed on Amazon Web Services that is integrated with Raspberry Pi GPIO capabilities by using the GPIO API and connections to turn on/off a coffee pot via server access. The user interacts with Barista primarily through Amazon Spot’s Alexa speech recognition. The Barista skilled is automatically updated from Amazon Web Services to the integrated Amazon Spot. Once updated, the Spot will access the skill that will access the Raspberry Pi’s server through a series of voice commands. The server access will run a Python program that utilizes the GPIO api to turn on/off the one button coffee pot.

Once integrated in concert, users may enable the coffee making processes through voice commands such as:

“Barista Brew Coffee” - will initiate coffee making processes
“Barista Stop” - will kill coffee making processes

It is expected that the reader is familiar with Amazon Web Services, Amazon Alexa, and server access such as ssh.
