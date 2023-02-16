![AEM Compose Logo](https://github.com/wttech/aemc-ansible/raw/main/docs/logo-with-text.png)
[![WTT Logo](https://github.com/wttech/aemc-ansible/raw/main/docs/wtt-logo.png)](https://www.wundermanthompson.com/service/technology)

[![Apache License, Version 2.0, January 2004](https://github.com/wttech/aemc-ansible/raw/main/docs/apache-license-badge.svg)](http://www.apache.org/licenses/)

# AEM Compose - Packer Example

Set up AEM instances on [AWS EC2](https://aws.amazon.com/ec2/) machine using [AEM Compose Ansible](https://github.com/wttech/aemc-ansible) Modules.

[Packer](https://www.packer.io/) tool used in this example allows to:

* launch & terminate automatically machine for tests using `skip_create_ami = true` [option](https://developer.hashicorp.com/packer/plugins/builders/amazon/ebs#skip_create_ami).
* allows to bake machine image when `skip_create_ami = false`


## Prerequisites

1. Install OS-specific software

   a) Mac
    
   ```shell
   brew install ansible gnu-tar
   ```
   
   b) Other/Unix

   ```shell
   [yum/dnf/apt-get] install ansible
   ```

2. Run script

   ```shell
   sh controller-init.sh
   ```

3. Set up AWS environment variables

   ```shell
   export AWS_ACCESS_KEY_ID=xxx
   export AWS_SECRET_ACCESS_KEY=yyy
   ```

# Building 

Running this command will launch AWS EC2 Machine, invoke [Ansible playbook](aem_single.yml), then terminate machine.

```shell
sh build.sh
```


# Known issues

## Mitogen

This project is prepared for [Ansible Mitogen](https://mitogen.networkgenomics.com/ansible_detailed.html#demo) usage which could seriously improve Ansible execution time.
However, Mitogen comes with a little trade-off. It's not being updated regularly and sticks to a particular, not always up-to-date Ansible version. In other words, Mitogen disallows to use of the most recent Ansible version so using it should be considered with care. But still, in most cases using it could be very valuable.

### Enabling Mitogen

1. Uncomment line with `strategy_plugins` in [ansible.cfg](ansible.cfg)
2. Uncomment line `strategy: mitogen_linear` in playbook [aem_single.yml](aem_single.yml)
