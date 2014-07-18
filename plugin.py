###
# Copyright (c) 2014, Nicholas De Nova
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.ircmsgs as ircmsgs
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Minetest_Rules')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

class Minetest_Rules(callbacks.Plugin):
	"""Add the help for "@plugin help Minetest_Rules" here
	This should describe *how* to use this plugin."""
	pass
	
	def dating(self, irc, msg, args):
		""" takes no arguments
		For Minetest rules output.
		"""
		irc.reply("These servers are NOT a dating service. They are a Minetest gaming system. We are here to play a game and build some cool worlds, not make out. If you want the latter, go search the web for an appropriate resource and confine your dating discussions to those places, or you WILL be removed from here. Period.", prefixNick = False)	
	dating = wrap(dating)
	def skin(self, irc, msg, args):
	    """ takes no arguments
	    Displays how to get a skin on a Minetest server, if the server supports it.
	    """
	    irc.reply("To get a skin, send a link to the skin you want to the server's Owner. Once installed, it will take effect at the next restart (usually around 10:00 AM UTC/5:00 AM EST). Minetest uses the same skin format as Minecraft, just search the web or go to minecraftskins.com or similar. A skin works only on the server it was installed on.", prefixNick = False)
	skin = wrap(skin)
	
	# Alias for "skin"
	def skins(self, irc, msg, args):
		""" takes no arguments
		Displays how to get a skin on a Minetest server, if the server supports it.
		"""
		Minetest_Rules.skin(self, irc, msg, args)
	skins = wrap(skins)
	
	def respect(self, irc, msg, args):
		""" takes no arguments
		Tells a user about respect.
		"""
		irc.reply("We expect users on our servers to treat each other with respect. That means not cussing people out, telling people to shut up , etc. You were not taught by your parents to act any other way, and we expect you to behave appropriately to be here. Treat others as you'd want to be treated. If you can't abide by this simple rule, then leave or you will be removed.", prefixNick = False)
	respect = wrap(respect)
	
	def rules(self, irc, msg, args):
		""" takes no arguments
		Tells people how to find the rules.
		"""
		irc.reply("On every server is a set of rules. In order to build and dig on that server, you must first seek out and read the rules. These are usually found near the spawn building. Then, depending on the server, you may need to present a code to verify that you have read the rules.", prefixNick = False)
	rules = wrap(rules)
	
	def spawn(self, irc, msg, args):
		""" takes no arguments
		Tells people how to use the /spawn command.
		"""
		irc.reply("Most servers have a \"/spawn\" command, that will return you to your starting point. This is especially useful if you need to meet other players, or if you need to get unstuck. To use it, simply type \"/spawn\" into chat.", prefixNick = False)
	rules = wrap(rules)
	
	def  worldcraft(self, irc, msg, args):
		""" takes no arguments
		Tells people about the illegal tablet clients that are frequently used.
		"""
		irc.reply("Worldcraft, Buildcraft, Starve Games and others are unsupported versions of Minetest. You will most likely experience poor performance, low framerate or lag. Either get Minetest for a PC, or, if a tablet is your only option, get it from the Minetest forums (https://forum.minetest.net/viewtopic.php?f=42&t=9389). ", prefixNick = False)
	worldcraft = wrap(worldcraft)
	
	def buildcraft(self, irc, msg, args):
		""" takes no arguments
		Tells people about the illegal tablet clients that are frequently used.
		"""
		Minetest_Rules.worldcraft(self, irc, msg, args)
	buildcraft = wrap(buildcraft)
	
	def lag(self, irc, msg, args):
		""" takes no arguments
		Tells people about the differences between lag and low FPS.
		"""
		irc.reply("Lag is not low FPS. Low FPS makes the game appear slow and glitchy. Lag makes opening chests and doors take a bit of time.", prefixNick = False)
	lag = wrap(lag)
	
	def protect(self, irc, msg, args):
		""" takes no arguments
		Tells people how to properly protect their land.
		"""
		irc.reply("To protect your land, go to one corner of the area, dig into the ground, and type \"/area_pos1\" without quotes. Then, go to the other corner and build into the sky, then type \"/area_pos2\", again, without quotes. After you finish doing that, type \"/protect <your_area_description>\" without quotes (fill in your description instead of <your_area_description>). Your land is now protected! Please note that only protecting rectangles of land are supported.", prefixNick = False)
	protect = wrap(protect)
	
	def asking(self, irc, msg, args):
		""" takes no arguments
		Tells people how to ask a question.
		"""
		irc.reply("Do not just scream \"HELP!\" in chat. If you need something done, say <username>, <your question>. For instance, if you need help with building, say \"sample_dude, I need help building.\".", prefixNick = False)
	asking = wrap(asking)
	
	def language(self, irc, msg, args):
		""" takes no arguments
		Warns users about foul language.
		"""
		irc.reply("This is a family friendly network. This means no foul language in chat. If you do need to curse, please blur it sufficiently (wtf, and s*** are acceptable). If you do swear in chat, you will be asked, then eventually forced to stop. This is considered a major offense and may end in a ban.", prefixNick = False)
	language = wrap(language)
	
Class = Minetest_Rules


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
