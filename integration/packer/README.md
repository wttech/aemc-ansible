# AEMC Ansible - Packer 

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
