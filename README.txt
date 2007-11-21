=========
GrokPaste
=========

GrokPaste is a pastebin application written using Grok.
GrokPaste is inspired by http://dpaste.com. It is also intended to act as a tutorial application for developers venturing into Zope3 and Grok technologies. 

Installation
------------

If you already have a Zope3 Installation, create a file ``grokpaste.zcml`` with a single line - ``<include package="grokpaste" />`` and put it under ``includes`` directory. 

If you are using ``repoze.grok`` setup, put the same file under ``etc/grok-apps`` directory.

Log on to the server, and you should see a ``Add Application`` portal, where you can give a name to the GrokPaste instance (say, pastebin) and have it installed. 

ChangeLog
---------
 * [r1-5] Initial release

TODO
----

 * Delete pastes after 30 days.
 * Hold pastes if ``Hold`` Option is enabled.
 * ``Copy`` existing paste to a new paste and edit.
 * Shorter URLs, on the lines of reddit (eg: http://app_url/60zd3).
 * Summary report of pastes by language
