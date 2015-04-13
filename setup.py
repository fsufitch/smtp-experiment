from setuptools import setup, find_packages

setup(name='xsmtp',
      version='0.1',
      description='SMTP Experiment',
      author='Filip Sufitchi',
      author_email='fsufitchi@gmail.com',
      packages=find_packages('src'),
      package_dir={'':'src'},
      include_package_data=True,
      install_requires=[''],
      entry_points = {'console_scripts': ["xsmtp=xsmtp.server:main",], },
  )
