================
egggitinfo README
=================

Overview
========
This is a setuptools plugin that plants some git-related information into the .egg-info directory of a python package.  To setuptools this information is refered to as 'metadata'.  It is located in a file called 'git_info.txt', and can be retrieved using the from a Distribution object by calling the `get_metadata(name)` method.  The 'git_info.txt' file stores the following information in JSON format.

git_branch
----------
Stores the name of the active git branch.

git_remotes
-----------
Stores a JSON object of git remotes, where the key is the name of the remote and the value is the url.
