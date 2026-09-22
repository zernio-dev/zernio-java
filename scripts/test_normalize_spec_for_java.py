import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    'normalize', Path(__file__).with_name('normalize-spec-for-java.py')
)
normalize = importlib.util.module_from_spec(spec)
spec.loader.exec_module(normalize)


class EnumArrayTest(unittest.TestCase):
    def test_enum_arrays_use_lists_without_losing_enum_values(self):
        schema = {'type': 'array', 'uniqueItems': True,
                  'items': {'type': 'string', 'enum': ['whatsapp', 'messenger']}}
        normalize.collapse_unexpressible_unions(schema, '$', [])
        self.assertNotIn('uniqueItems', schema)
        self.assertEqual(schema['items']['enum'], ['whatsapp', 'messenger'])

    def test_non_enum_arrays_keep_set_semantics(self):
        schema = {'type': 'array', 'uniqueItems': True, 'items': {'type': 'string'}}
        normalize.collapse_unexpressible_unions(schema, '$', [])
        self.assertTrue(schema['uniqueItems'])


if __name__ == '__main__':
    unittest.main()
