from setuptools import setup

setup(
    name='ipatool',
    version='0.1.0',
    description='A tool for interacting with the Apple App Store',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NyaMisty/ipatool-py',
    py_modules=['main'],
    packages=['reqs', 'reqs/schemas'],
    install_requires=[
        'rich>=10.2.2',
        'requests>=2.25.0'
    ],
    entry_points={
        'console_scripts': [
            'ipatoolpy = main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)