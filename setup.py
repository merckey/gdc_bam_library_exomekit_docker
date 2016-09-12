#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = 'gdc_bam_library_exomekit_docker',
      author = 'Jeremiah H. Savage',
      author_email = 'jeremiahsavage@gmail.com',
      version = 0.1,
      description = 'relate a BAM library/readgroup to an exome kit',
      url = 'https://github.com/jeremiahsavage/gdc_bam_library_exomekit_docker/',
      license = 'Apache 2.0',
      packages = find_packages(),
      install_requires = [
      ],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      entry_points={
          'console_scripts': ['gdc_bam_library_exomekit_docker=gdc_bam_library_exomekit_docker.__main__:main']
      }
)
