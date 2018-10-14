from setuptools import setup

setup(
    name='starlette-boilerplate',
    version='2018.1.0',

    description='Boilerplate for Starlette server',

    # Keywords
    keywords=['Amatobahn', 'Starlette', 'boilerplate'],

    # The project's main homepage.
    url='https://www.IamGregAmato.com',

    # Author details.
    author='Greg Amato',
    author_email='amatobahn@gmail.com',

    # License
    license='MIT License',

    # Classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],

    # Packages
    packages=['starlette-boilerplate'],

    # Required dependencies. Will be installed by pip
    # when the project is installed.
    install_requires=['requests', 'starlette', 'uvicorn', 'python-multipart', 'ujson'],
)