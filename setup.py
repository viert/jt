from setuptools import setup, find_packages

setup(
    name = "jt",
    version = "0.1-1",
    packages = find_packages(),

    scripts = ['jt'],
    install_requires = [ 'jinja2' ],

    author = "Pavel Vorobyov",
    author_email = "aquavitale@yandex.ru",
    description = "Pluggable jinja2 cli",
    license = "MIT",
    keywords = "jinja2 cli",
    url = "https://github.com/viert/jt"
)

