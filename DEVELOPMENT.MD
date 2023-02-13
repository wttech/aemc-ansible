<img src="https://github.com/wttech/aemc-ansible/raw/main/docs/logo-with-text.png" alt="Logo">

**AEM Compose** - Ansible Collection - Development Guid

## Development

### Developer setup guide

1. Install Ansible

   Mac:

    ```shell
    brew install ansible ansible-lint gnu-tar
    ```

2. Setup collection to be visible by Ansible

    ```shell
    sh setup.sh
    ```

3. Configure IDE

   Intellij: Be sure to add Python SDK including global libraries as on screenshot below

   ![IntelliJ Python SDK](https://github.com/wttech/aemc-ansible/raw/main/docs/intellij-python-sdk.png)

### Developer testing guide

Simply run one of above commands:

```shell
sh test.sh
sh test.sh instance
sh test.sh instance minimal
sh test.sh instance minimal -vvv
sh test.sh instance extensive
sh test.sh instance extensive -vvv
```

See results:

![Ansible Results](https://github.com/wttech/aemc-ansible/raw/main/docs/ansible-result.png)
