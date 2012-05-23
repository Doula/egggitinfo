import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='egggitinfo',
      version='0.1',
      description='Plants some git-related data into the .egg-info directory of a python package.',
      long_description=README,
      py_modules = ['egggitinfo'],
      test_suite="egggitinfo",
      entry_points = {
          "egg_info.writers": [
              "git_info.txt = egggitinfo:write_git_info",
          ],
      },
)
