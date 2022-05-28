# pySigma Backend Cookiecutter Template

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a
[pySigma](https://github.com/SigmaHQ/pySigma) [backend](https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html).

## Features

* Backend and processing pipeline classes
* pyproject.toml template
* Testing with pytest
* CI testing with [GitHub Actions](https://docs.github.com/en/actions)
* Automatic test deployment on test PyPI on Git version tagging.
* Automatic deployment to PyPI on GitHub release.

## Usage

Install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) if not yet done with:

```
python3 -m pip install --user cookiecutter
```

This cookiecutter uses [Poetry](https://python-poetry.org) for installation of current dependencies. Install it as
described [here](https://python-poetry.org/docs/#installation).

Generate a pySigma backend project from this template with:

```
cookiecutter https://github.com/SigmaHQ/cookiecutter-pySigma-backend.git
```

## Developing a Backend

1. Define the tokens in the backend class.
1. Implement required Sigma rule transformations (e.g. field mappings, value transformations) as [processing
   pipeline](https://sigmahq-pysigma.readthedocs.io/en/latest/Processing_Pipelines.html#processing-pipeline)
1. [Implement further code](https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html) required to implement output
   in the backend targets query language.
1. Implement tests to ensure correctness and quality.
1. Remove pipelines directory if backend doesn't defines any pipelines.

Install dependencies as required with `poetry add <package>`.

## Publishing a Backend

Generally there are two options:

* Host the new backend within your own account and [publish the backend package to PyPI](https://packaging.python.org/en/latest/tutorials/packaging-projects/) on your
  own.
* [Ask the SigmaHQ project maintainers](https://github.com/SigmaHQ/pySigma/discussions/new) to host the backend within
  the [SigmaHQ organization](https://github.com/SigmaHQ) and take care of the PyPI release.

### Integration into Sigma CLI

A new backend has to be integrated into Sigma CLI. The technical integration is described in the [Sigma CLI
README](https://github.com/SigmaHQ/sigma-cli#integration-of-backends-and-pipelines). To be integrated in Sigma CLI
releases the backend has to meet some requirements:

* Custom backend code should be well tested with automatic CI tests.
* The backend must use the intended interfaces for initialization, processing and returning results as well as error
  states. It should not output anything directly or terminate the running program on errors.
* The developer of the backend takes over its ownership and actively maintains it (bug fixes etc.). Unmaintained or
  erroneous backends will be removed after a while.

These requirements should ensure a certain quality of the Sigma toolchain.

### Self-Publishing

#### PyPI

If you don't have a PyPI account or want to release the backend with a new account, register new accounts on the:

* [Test instance](https://test.pypi.org/account/register/) - this is not necessary to publish a package but strongly
  recommended.
* [Productive instance](https://pypi.org/account/register/)

As releasing packages is a sensitive thing, especially with security-related software, immediate configuration of
multifactor authentication of the PyPI accounts is strongly recommended.

Finally create an authentication token.

#### Repository Configuration

With the template configuration you need to configure the following secrets in your repository:

* `GIST_SECRET` (optional): the secret of the GitHub Gist containing the coverage badge information.
* `TEST_PYPI_API_TOKEN` (optional but recommended): PyPI token for deployment to [test instance](https://test.pypi.org/).
* `PYPI_API_TOKEN`: PyPI token for deployment to [productive instance](https://pypi.org/).

#### Release

1. Conduct a test release by tagging the commit with a version tag in the format `vx.y.z`, e.g. `v0.1.0`. This version
   has to be in sync with the version parameter of pyproject.toml.
1. If the test deployment finishes successfully, create a GitHub release from this tag to publish it to the productive PyPI.

After the first release the authentication token should be regenerated with a scope restricted to the backend package.