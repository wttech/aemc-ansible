![Logo](docs/logo-with-text.png)

**AEM Compose** - Ansible Collection.

Provides modules and roles built on top of [AEM Compose CLI](https://github.com/wttech/aemc).

## Example usage

```yaml
---
#- name: Print effective config (debugging)
#  wttech.aem.config:
#    command: print

- name: create instances
  wttech.aem.instance:
    command: create

- name: turn on instances
  wttech.aem.instance:
    command: up

- name: configure replication agent
  wttech.aem.repl_agent:
    command: setup
    instance_id: local_author
    location: author
    name: publish
    props:
      enabled: true
      transportUri: "{{ aem.instance.config.local_publish.http_url }}/bin/receive?sling:authRequestLogin=1"
      transportUser: "{{ aem.instance.config.local_publish.user }}"
      transportPassword: "{{ aem.instance.config.local_publish.password }}"
      userId: "{{ aem.instance.config.local_publish.user }}"

- name: download APM package
  get_url:
    url: https://github.com/wttech/APM/releases/download/apm-5.5.1/apm-all-5.5.1.zip
    dest: /tmp/apm-all-5.5.1.zip

- name: deploy APM package
  wttech.aem.pkg:
    command: deploy
    instance_id: local_author 
    file: /tmp/apm-all-5.5.1.zip

- name: read APM package
  wttech.aem.pkg:
    command: find
    instance_id: local_author
    file: /tmp/apm-all-5.5.1.zip

- name: read some node
  wttech.aem.repo_node:
    command: read
    instance_id: local_author
    path: /content/cq:tags/experience-fragments

- name: save some node
  wttech.aem.repo_node:
    command: save
    instance_id: local_author
    path: /content/foo
    props:
      foo: bar3

- name: read some bundle
  wttech.aem.osgi_bundle:
    command: read
    instance_id: local_author
    symbolic_name: com.day.cq.wcm.cq-wcm-core
  register: res

- name: print read bundle ID
  debug:
    msg: "Bundle 'com.day.cq.wcm.cq-wcm-core' has ID '{{ res.data.bundle.details.id }}'"

- name: enable CRX DE
  wttech.aem.osgi_config:
    command: save
    instance_id: "{{ item }}"
    pid: org.apache.sling.jcr.davex.impl.servlets.SlingDavExServlet
    props:
      alias: /crx/server
  with_items: [local_author, local_publish]

- name: read all bundles
  wttech.aem.osgi_bundle:
    command: list
    instance_id: local_author

- name: turn off instances
  wttech.aem.instance:
    command: down

- name: destroy instances
  wttech.aem.instance:
    command: destroy
```

## Development 

### Developer setup guide

1. Install Ansible

    Mac:
    
    ```shell
    brew install ansible gnu-tar
    ```

2. Setup collection to be visible by Ansible

    ```shell
    sh setup.sh
    ```

3. Configure IDE

   Intellij: Be sure to add Python SDK including global libraries as on screenshot below
   
   ![IntelliJ Python SDK](docs/intellij-python-sdk.png)

### Developer testing guide

Simply run command:

```shell
sh test.sh
```

See results:

![Ansible Results](docs/ansible-result.png)
