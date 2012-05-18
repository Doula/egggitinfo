from git.exc import InvalidGitRepositoryError
from git import Repo
from pkg_resources import yield_lines

_TEMPLATE = """\
{
    git_branch = "%s",
    git_remotes = ["%s"]
}
"""

def write_git_info(cmd, basename, filename):
    try
        repo = Repo('.')
    except InvalidGitRepositoryError, e:
        return

    # Branch Name
    branch = repo.active_branch
    git_branch = branch.name
    
    # Branch Remotes
    git_remotes_list = [remote.name for remote in repo.remotes]
    git_remotes = '", "'.join(git_remotes_list)

    cmd.write_or_delete_file("git_info", filename,
                         _TEMPLATE % (git_branch,
                                      git_remotes))