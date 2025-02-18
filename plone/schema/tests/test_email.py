import unittest


class TestEmail(unittest.TestCase):

    def test_fromUnicode(self):
        from plone.schema.email import Email
        from plone.schema.email import InvalidEmail

        # Value must be string
        self.assertEqual(
            Email().fromUnicode("arthur@example.org"),
            "arthur@example.org",
        )
        with self.assertRaises(InvalidEmail):
            Email().fromUnicode(b"arthur@example.org")

        # We strip spaces.
        self.assertEqual(
            Email().fromUnicode("    arthur@example.org  "),
            "arthur@example.org",
        )

        # We do some validation
        with self.assertRaises(InvalidEmail):
            Email().fromUnicode("arthur")
        with self.assertRaises(InvalidEmail):
            Email().fromUnicode("arthur@")
        with self.assertRaises(InvalidEmail):
            Email().fromUnicode("arthur@one")
        with self.assertRaises(InvalidEmail):
            Email().fromUnicode("@one.two")
