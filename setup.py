from setuptools import setup, find_packages

version = '1.3.1.dev0'

setup(name='plone.schema',
      version=version,
      description="",
      long_description=open("README.md").read(),
      classifiers=[
        "Framework :: Zope2",
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        ],
      keywords='plone schema ttw',
      author='David Glick',
      author_email='dglick@gmail.com',
      url='http://svn.plone.org/svn/plone/plone.schemaeditor',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
