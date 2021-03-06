from setuptools import setup, find_packages

setup(
    name='smartmin',
    version=__import__('smartmin').__version__,
    license="BSD",

    install_requires = [
        "django>=1.7",
        "django-guardian>=1.2.0",
        "django_compressor",
        "pytz",
        "xlutils",
    ],

    description="Scaffolding system for Django object management.",
    long_description=open('README.rst').read(),

    author='Nyaruka Ltd',
    author_email='code@nyaruka.com',

    url='http://github.com/nyaruka/smartmin',
    download_url='http://github.com/nyaruka/smartmin/downloads',

    include_package_data=True,

    packages=find_packages(),

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
