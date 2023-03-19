![AEM Compose Logo](https://github.com/wttech/aemc-ansible/raw/main/docs/logo-with-text.png)
[![WTT Logo](https://github.com/wttech/aemc-ansible/raw/main/docs/wtt-logo.png)](https://www.wundermanthompson.com/service/technology)

[![Apache License, Version 2.0, January 2004](https://github.com/wttech/aemc-ansible/raw/main/docs/apache-license-badge.svg)](http://www.apache.org/licenses/)

# AEM Compose - Controller Example

Build a [Docker image](https://docs.docker.com/engine/reference/commandline/build/) being an [Ansible controller](https://docs.ansible.com/ansible/latest/network/getting_started/basic_concepts.html#control-node) with all dependent software installed.

- Allows to execute Ansible on any operate system via containerization (including Windows which is not supported by Ansible natively)
- Eliminates a need to perform OS-specific software installations (`brew install ansible` vs `apt-get install ansible`, etc)

## Prerequisites

- Docker 20.x and higher

# Building 

Run command:

```shell
sh build.sh
```
