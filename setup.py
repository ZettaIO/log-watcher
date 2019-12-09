from setuptools import setup, find_packages


setup(
    name='log_watcher',
    version='1.0.0',
    description="A small tool use to watch for rare events in log files sending an alert immediately.",
    packages=find_packages(),
    install_requires=[
        'requests_oauthlib==1.0.0',
        'inotify==0.2.10',
    ],
    entry_points={'console_scripts': [
        'log-watcher = log_watcher.cli:main',
    ]},
    python_requires='>=2.7, <3',
)
