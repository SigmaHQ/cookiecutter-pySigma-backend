import pytest
from sigma.collection import SigmaCollection
from sigma.backends.{{ cookiecutter.backend_package_name }} import {{ cookiecutter.backend_class_name }}

@pytest.fixture
def {{ cookiecutter.backend_package_name }}_backend():
    return {{ cookiecutter.backend_class_name }}()

# TODO: implement tests for some basic queries and their expected results.
def test_{{ cookiecutter.backend_package_name }}_and_expression({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel:
                    fieldA: valueA
                    fieldB: valueB
                condition: sel
        """)
    ) == ['<insert expected result here>']

def test_{{ cookiecutter.backend_package_name }}_or_expression({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel1:
                    fieldA: valueA
                sel2:
                    fieldB: valueB
                condition: 1 of sel*
        """)
    ) == ['<insert expected result here>']

def test_{{ cookiecutter.backend_package_name }}_and_or_expression({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel:
                    fieldA:
                        - valueA1
                        - valueA2
                    fieldB:
                        - valueB1
                        - valueB2
                condition: sel
        """)
    ) == ['<insert expected result here>']

def test_{{ cookiecutter.backend_package_name }}_or_and_expression({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel1:
                    fieldA: valueA1
                    fieldB: valueB1
                sel2:
                    fieldA: valueA2
                    fieldB: valueB2
                condition: 1 of sel*
        """)
    ) == ['<insert expected result here>']

def test_{{ cookiecutter.backend_package_name }}_in_expression({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel:
                    fieldA:
                        - valueA
                        - valueB
                        - valueC*
                condition: sel
        """)
    ) == ['<insert expected result here>']

def test_{{ cookiecutter.backend_package_name }}_regex_query({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel:
                    fieldA|re: foo.*bar
                    fieldB: foo
                condition: sel
        """)
    ) == ['<insert expected result here>']

def test_{{ cookiecutter.backend_package_name }}_cidr_query({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel:
                    field|cidr: 192.168.0.0/16
                condition: sel
        """)
    ) == ['<insert expected result here>']

def test_{{ cookiecutter.backend_package_name }}_field_name_with_whitespace({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    assert {{ cookiecutter.backend_package_name }}_backend.convert(
        SigmaCollection.from_yaml("""
            title: Test
            status: test
            logsource:
                category: test_category
                product: test_product
            detection:
                sel:
                    field name: value
                condition: sel
        """)
    ) == ['<insert expected result here>']

# TODO: implement tests for all backend features that don't belong to the base class defaults, e.g. features that were
# implemented with custom code, deferred expressions etc.

{% if cookiecutter.additional_output_formats %}
{% for format in cookiecutter.output_formats.split(",") %}
def test_{{ cookiecutter.backend_package_name }}_{{ format }}_output({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    """Test for output format {{ format }}."""
    # TODO: implement a test for the output format
    pass
{% endfor %}
{% endif %}
