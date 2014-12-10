import unittest

import scss.compiler

import pyscss_pkg_resources

class TestExtension(unittest.TestCase):

    def test_1(self):

        extension = pyscss_pkg_resources.PkgResourcesExtension('pyscss_pkg_resources', '')
        compiler = scss.compiler.Compiler(extensions=(extension, ))
        out = compiler.compile_string('@import "test.scss";')
        self.assertEqual(
            'a {\n'
            '  color: red; }\n',
            out)
