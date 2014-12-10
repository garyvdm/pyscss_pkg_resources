pyscss_pkg_resources
====================

pyScss extension to allow for loading of import for pkg_resource.


Use example
-----------

Put `substyle.scss` in `mypkg/style`.

    extension = pyscss_pkg_resources.PkgResourcesExtension('mypkg', 'style')
    compiler = scss.compiler.Compiler(extensions=(extension, ))
    out = compiler.compile_string('@import "substyle.scss";')
