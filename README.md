
# Python Project Template

A low dependency and really simple to start project template for Python Projects.

See also 
- [Flask-Project-Template](https://github.com/rochacbruno/flask-project-template/) for a full feature Flask project including database, API, admin interface, etc.
- [FastAPI-Project-Template](https://github.com/rochacbruno/fastapi-project-template/) The base to start an openapi project featuring: SQLModel, Typer, FastAPI, JWT Token Auth, Interactive Shell, Management Commands.

### HOW TO USE THIS TEMPLATE

> **DO NOT FORK** this is meant to be used from **[Use this template](https://github.com/rochacbruno/python-project-template/generate)** feature.

1. Click on **[Use this template](https://github.com/rochacbruno/python-project-template/generate)**
3. Give a name to your project  
   (e.g. `my_awesome_project` recommendation is to use all lowercase and underscores separation for repo names.)
3. Wait until the first run of CI finishes  
   (Github Actions will process the template and commit to your new repo)
4. If you want [codecov](https://about.codecov.io/sign-up/) Reports and Automatic Release to [PyPI](https://pypi.org)  
  On the new repository `settings->secrets` add your `PYPI_API_TOKEN` and `CODECOV_TOKEN` (get the tokens on respective websites)
4. Read the file [CONTRIBUTING.md](CONTRIBUTING.md)
5. Then clone your new project and happy coding!

> **NOTE**: **WAIT** until first CI run on github actions before cloning your new project.

### What is included on this template?

- 🖼️ Templates for starting multiple application types:
  * **Basic low dependency** Python program (default) [use this template](https://github.com/rochacbruno/python-project-template/generate)
  * **Flask** with database, admin interface, restapi and authentication [use this template](https://github.com/rochacbruno/flask-project-template/generate).
  **or Run `make init` after cloning to generate a new project based on a template.**
- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <xtlsapi>` or `$ xtlsapi` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.

> Curious about architectural decisions on this template? read [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md)  
> If you want to contribute to this template please open an [issue](https://github.com/rochacbruno/python-project-template/issues) or fork and send a PULL REQUEST.

[❤️ Sponsor this project](https://github.com/sponsors/rochacbruno/)

<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---
# xtlsapi

[![codecov](https://codecov.io/gh/hiddify/xtlsapi/branch/main/graph/badge.svg?token=xtlsapi_token_here)](https://codecov.io/gh/hiddify/xtlsapi)
[![CI](https://github.com/hiddify/xtlsapi/actions/workflows/main.yml/badge.svg)](https://github.com/hiddify/xtlsapi/actions/workflows/main.yml)

Awesome xtlsapi created by hiddify

## Install it from PyPI

```bash
pip install xtlsapi
```

## Usage

```py
from xtlsapi import XrayClient, utils, exceptions

xray_client = XrayClient('1.2.3.4', 1234)
user_id = utils.generate_random_user_id()
user_email = utils.generate_random_email()
inbound_tag = 'inbound-tag'

# Get stats
print(utils.human_readable_bytes(xray_client.get_client_download_traffic('user-email@mail.com')))
print(utils.human_readable_bytes(xray_client.get_client_upload_traffic('user-email@mail.com')))
print(utils.human_readable_bytes(xray_client.get_inbound_download_traffic(inbound_tag)))
print(utils.human_readable_bytes(xray_client.get_inbound_upload_traffic(inbound_tag)))
print(utils.human_readable_bytes(xray_client.get_total_download_traffic()))
print(utils.human_readable_bytes(xray_client.get_total_upload_traffic()))

# Add & Remove client
user = xray_client.add_client(inbound_tag, user_id, user_email)
if user:
    print(user)
    xray_client.remove_client(inbound_tag, user_email)

# restart logger
xray_client.restart_logger()
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
