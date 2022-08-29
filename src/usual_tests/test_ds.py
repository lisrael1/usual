import unittest


class TestDS(unittest.TestCase):
    def test_df_before_import(self):
        with self.assertRaises(NameError):
            pd

    def test_df_after_import(self):
        from usual.ds import pd
        self.assertEqual(pd.options.display.min_rows, 20)


if __name__ == '__main__':
    unittest.main()
