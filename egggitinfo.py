import subprocess
import os.path
import re
from pkg_resources import yield_lines

_TEMPLATE = """\
{
    "git_branch" : "%s",
    "git_remotes" : %s
}
"""

def write_git_info(cmd, basename, filename):
    # Check if git is installed
    try:
        output = subprocess.check_output(['which', 'git'])
    except subprocess.CalledProcessError:
        return

    # Check if the current dir is a repo
    if os.path.isdir('.git'):
        # Get branch
        output = subprocess.check_output(['git', 'branch'])
        branches = output.split('\n')
        
        git_branch = None
        for branch in branches:
            if '* ' in branch:
                git_branch = branch.replace('* ', '')
                break

        # Get remotes
        output = subprocess.check_output(['git', 'remote', '-v'])
        remotes = output.split('\n')

        git_remotes = {}
        for remote in remotes:
            remote = remote.replace('\t', ' ')
            remote_info = remote.split(' ') 

            if len(remote_info) == 3:
                name = remote_info[0]
                url = remote_info[1]
                git_remotes[name] = url
            else:
                continue

        import pdb;pdb.set_trace()
        if git_remotes and git_branch:
            cmd.write_or_delete_file("git_info", filename,
                                    _TEMPLATE % (git_branch,
                                                 git_remotes))
        else:
            return