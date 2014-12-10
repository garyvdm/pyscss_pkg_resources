import os.path
import pkg_resources

import scss.extension
import scss.source

class PkgResourcesExtension(scss.extension.Extension):

    def __init__(self, package_or_requirement, base_dir):
        self.package_or_requirement = package_or_requirement
        self.base_dir = base_dir


    def handle_import(self, name, compilation, rule):
        full_name = os.path.join(self.base_dir, name)
        stream = pkg_resources.resource_stream(self.package_or_requirement, full_name)
        return  scss.source.SourceFile.from_file(stream)




