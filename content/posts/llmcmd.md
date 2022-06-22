+++
title = "Natural language interfaces for the command line and privacy"
date = "2022-06-22T06:15:54+01:00"
author = "ssamot"
tags = ["Artificial intelligence", "privacy" ]
description = "Natural language interfaces"
+++

Microsoft released a natural language interface for the command line (https://github.com/microsoft/Codex-CLI), while a past effort can been seen here: https://github.com/tom-doerr/zsh_codex.  What I find worrying is that there is currently no way of using a local model --- these services do remote calls. Which means that you are bound to call OpenAI's APIs, which pretty much guarantees loss of privacy. It looks like alternatives are doing much on the privacy front -- see here:  https://www.tabnine.com/. 

We urgently need to create sensible open source alternatives for NL2Whatever platforms, both at a hardware and at a software level -- we are currently seeing a revolution in software development that will trickle down to all kinds of computer user interactions, and we risk being locked in data-hungry monopolies.
