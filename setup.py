from setuptools import setup
from setuptools import setup, find_packages
from pip.req import parse_requirements
import pip

install_reqs = reqs = [str(ir.req) for ir in parse_requirements('requirements.txt',
    session=pip.download.PipSession())]
dev_reqs = [str(ir.req) for ir in parse_requirements('requirements_dev.txt',
    session=pip.download.PipSession())]

setup(
    name='protonamegen',
    version='0.2.0',
    description="Makes silly names for things",
    long_description="""
      I have a few packages that need to not be taken seriously. Thus, they are getting
      silly names. This is how I'm making the names
    """,
    author="Kevin Wierman",
    author_email='kevin.wierman@pnnl.gov',
    url='https://github.com/kwierman/protonamegen',
    packages=find_packages(),
    package_dir={'protonamegen':
                 'protonamegen'},
    entry_points={
        'console_scripts': [
            'gen_proto_name=protonamegen.cli:gen_proto_name',
            'init_proto_name=protonamegen.cli:init_proto_name'
        ]
    },
    include_package_data=True,
    install_requires=reqs,
    license="MIT license",
    zip_safe=False,
    keywords='protonamegen',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=dev_reqs
)
