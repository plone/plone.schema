.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

1.2.1 (2020-04-22)
------------------

Bug fixes:


- Minor packaging updates. (#1)
- Fix JSONField with default values saved to `model_source` XML
  [avoinea] (#7)
- Initialize towncrier.
  [gforcada] (#2548)


1.2.0 (2018-06-24)
------------------

New features:

- Improve and complete Plone integration of the JSONField (z3c.form, plone.supermodel, plone.schemaeditor)
  [sneridagh]


1.1.0 (2018-06-23)
------------------

New Features:

- Add new JSONField field and JSONSchema auto validation.
  [sneridagh]


1.0.0 (2016-02-25)
------------------

Fixes:

- Moved translation to plone.app.locales
  [staeff]

- Fixed install_requires to specify correct dependencies.
  [gforcada]


1.0a1 (2014-04-17)
------------------

- Initial release.
  [ianderso,davisagli,frapell]
