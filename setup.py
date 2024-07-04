import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='useragents',
    author='Horin',
    author_email='developers@horinsoftwaregroup.com',
    description="By using this service, we can store all the information about users who connect to us on a specific device.",
    keywords='django useragent',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AIMentalTools/useragents.git',
    project_urls={
        'Documentation': 'https://github.com/AIMentalTools/useragents.git',
        'Bug Reports':
            'https://github.com/AIMentalTools/useragents.git/issues',
        'Source Code': 'https://github.com/AIMentalTools/useragents.git',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Framework :: Django :: 4.2',
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Horin License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Django',
    ],
)
