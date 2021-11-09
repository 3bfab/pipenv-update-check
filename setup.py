from distutils.core import setup

setup(
  name = 'pipenv_update_check',         # How you named your package folder (MyLib)
  packages = ['pipenv_update_check'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Pip environment update check',   # Give a short description about your library
  author = 'cuneyt',                   # Type in your name
  author_email = 'cuneyt@3bfab.com',      # Type in your E-Mail
  url = 'https://github.com/CuneytTaha/pipenv-update-check',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/CuneytTaha/pipenv-update-check/archive/refs/tags/v_0.1.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'terminaltables',
          'toml',
      ],
  classifiers=[
  ],
)
