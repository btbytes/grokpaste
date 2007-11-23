============
Get Grokking 
============

----------------------------------------------
A primer for developing applications with Grok
----------------------------------------------

:Author: Pradeep Kishore Gowda
:Version: 0.1
:Created: 2007.11.20

Copyright (C) 2007 Pradeep Kishore Gowda <pradeep AT btbytes.com>.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2 or
(at your option) any later version published by the Free Software
Foundation.

The source code in this document is subject to the provisions of the
Zope Public License, Version 2.1 (ZPL).

THE SOURCE CODE IN THIS DOCUMENT IS PROVIDED "AS IS" AND ANY AND ALL
EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.

.. raw:: latex

   \newpage


.. contents::
.. .. sectnum::


Getting Started
---------------

Introduction
~~~~~~~~~~~~

Grok is a modern approach to build long lasting, well engineered, modular and extensible applications, including Web applications. The strength of Grok to build such applications stems from Zope3, the technical architecture and code base on which Grok is built. While the design strength of Zope3 makes it an excellent choice to build applications, it also can be daunting for a beginner to get started with Zope3. Grok flattens out the learning curve associated with Zope3 by virtue of treasuring `Convention over Configuration` and `Sensible defaults` over `Explicit and upfront configuration`. 

Thus, grok renders itself available to evolutionary development while still maintaining the advantages such as Zope Component Architecture and making use of large, well tested code-base of Zope3.


Setting up the Python development environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While developing new applications, it is advisable to create a `workspace` which holds the pre-requisite libraries required for development of the current application and actual application itself. Many scripts are available which automate the process of creating new workspace, copying relevant files and eggs(pre-packaged python libraries) to correct location. Eg: ``zopeproject``, ``grokproject``, ``repoze.grok``.

.. note:: 
   Please note that Grok works on Python 2.4.4 and not yet on Python2.5. So, please install python2.4 on your system if you haven't already.

Understanding the Grok System
-----------------------------


Components of Grok
~~~~~~~~~~~~~~~~~~


Installing an existing application
----------------------------------



Kick-starting a new application
-------------------------------
