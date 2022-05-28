{% if cookiecutter.test_badge %}![Tests](https://github.com/{{ cookiecutter.github_account }}/{{ cookiecutter.package_name }}/actions/workflows/test.yml/badge.svg){% endif %}}
{% if cookiecutter.coverage_badge %}![Coverage Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/{{ cookiecutter.github_account }}/{{ cookiecutter.coverage_gist }}/raw/{{ cookiecutter.github_account }}-{{ cookiecutter.package_name }}.json){% endif %}
{% if cookiecutter.status_badge %}![Status](https://img.shields.io/badge/Status-{{ cookiecutter.status }}){% endif %}

# pySigma {{ cookiecutter.target_name }} Backend

This is the {{ cookiecutter.target_name }} backend for pySigma. It provides the package `sigma.backends.{{
cookiecutter.backend_package_name }}` with the `{{ cookiecutter.backend_class_name }}` class.
Further, it contains the following processing pipelines in `sigma.pipelines.{{ cookiecutter.backend_package_name }}`:

* pipeline1: purpose
* pipeline2: purpose


It supports the following output formats:

* default: plain {{ cookiecutter.target_name }} queries
* format_1: purpose
* format_2: purpose

This backend is currently maintained by:

* [{{ cookiecutter.author }}](https://github.com/{{ cookiecutter.github_account }}/)