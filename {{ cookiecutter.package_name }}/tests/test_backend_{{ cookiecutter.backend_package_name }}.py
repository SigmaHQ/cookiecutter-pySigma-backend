import pytest
from sigma.backends.{{ cookiecutter.backend_package_name }} import {{ cookiecutter.backend_class_name }}

@pytest.fixture
def {{ cookiecutter.backend_package_name }}_backend():
    return {{ cookiecutter.backend_class_name }}()

# TODO: implement tests for all backend features that don't belong to the base class defaults, e.g. features that were
# implemented with custom code, deferred expressions etc.

{% if cookiecutter.additional_output_formats %}
{% for format in cookiecutter.output_formats.split(",") %}
def test_{{ cookiecutter.backend_package_name }}_{{ format }}_output({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    """Test for output format {{ format }}."""
    # TODO: implement a test for the output format
{% endfor %}
{% endif %}