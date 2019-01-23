from setuptools import setup

setup(
    name='lektor-extra-config',
    version='0.1',
    author=u'Paul McLanahan',
    author_email='paul@mclanahan.net',
    license='MIT',
    py_modules=['lektor_extra_config'],
    install_requires=['everett==0.9'],
    entry_points={
        'lektor.plugins': [
            'extra-config = lektor_extra_config:ExtraConfigPlugin',
        ]
    }
)
