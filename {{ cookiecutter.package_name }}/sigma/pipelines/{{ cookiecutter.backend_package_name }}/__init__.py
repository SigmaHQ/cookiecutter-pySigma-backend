from .{{ cookiecutter.backend_package_name }} import {{ cookiecutter.backend_package_name }}_pipeline
# TODO: add all pipelines that should be exposed to the user of your backend in the import statement above.

pipelines = {
    "{{ cookiecutter.backend_package_name }}_pipeline": {{ cookiecutter.backend_package_name }}_pipeline,   # TODO: adapt identifier to something approproiate
}