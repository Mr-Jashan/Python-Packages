from distutils.core import setup
setup(
  name = 'Topsis-Jashan',         # How you named your package folder (MyLib)
  packages = ['Topsis-Jashan'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python package to find TOPSIS for multi-criteria decision analysis method',   # Give a short description about your library
  author = 'Jashan Walia',                   # Type in your name
  author_email = 'walia.jashan3@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Mr-Jashan/Python-Packages/tree/main/Topsis-Jashan',   # Provide either the link to your github or to your website
  keywords = ['Easy to Use', 'Fascinating concept', 'Topsis', 'TIET'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'math',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
