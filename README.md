![AEM Compose Logo](https://github.com/wttech/aemc-ansible/raw/main/docs/logo-with-text.png)
[![WTT Logo](https://github.com/wttech/aemc-ansible/raw/main/docs/wtt-logo.png)](https://www.wundermanthompson.com/service/technology)

[![Last Release Version](https://img.shields.io/github/v/release/wttech/aemc?color=lightblue&label=Last%20Release)](https://github.com/wttech/aemc-ansible/tags)
[![Ansible Galaxy](https://img.shields.io/ansible/collection/2218?label=Ansible%20Galaxy)](https://galaxy.ansible.com/wttech/aem)
[![Apache License, Version 2.0, January 2004](https://github.com/wttech/aemc-ansible/raw/main/docs/apache-license-badge.svg)](http://www.apache.org/licenses/)

# AEM Compose - Ansible Collection

Provides modules and roles built on top of [AEM Compose CLI](https://github.com/wttech/aemc) to provision [AEM](https://business.adobe.com/products/experience-manager/adobe-experience-manager.html) instances to desired state.
Configuration changes are applied idempotently in the Ansible spirit to reduce execution time making the tool effective in practice. Published in [Ansible Galaxy](https://galaxy.ansible.com/wttech/aem).

## Example integrations

1. [Packer](examples/packer) - good starting point for baking AWS EC2 image using Ansible and AEM Compose Ansible modules
2. [Local](examples/local) - development & testing sandbox for AEM Compose CLI and Ansible Modules which runs Ansible locally/natively
3. Have an idea for the next one? Want to help? At least raise an [issue](https://github.com/wttech/aemc-ansible/issues/new) :)

## Example configuration

1. Vars 

   All configuration options available for AEM Compose CLI are also supported in Ansible. There are two ways to define configuration.
 
   The first way is **nesting config values** under `aem_config_dict` Ansible variable defined anywhere e.g in the playbook or custom role (according to own [preferences](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#where-to-set-variables)).
   This special variable is passed to all AEM Compose modules automatically for the sake of simplicity.

   ```yaml
   aem: 
     instance:
    
     config:
       local_author:
         http_url: http://127.0.0.1:4502
         user: admin
         password: admin
         run_modes: [ local ]
         # ...
       local_publish:
         # ...

     package:
       snapshot_patterns: [ "**/*-SNAPSHOT.zip" ]
       snapshot_deploy_skipping: true
   
   # ...
   ```
   This approach is used in [local example](examples/local/group_vars/all.yml#L25).

   The second way is **templating configuration file** (*aem.yml*). The path of the templated file need to be defined in `aem_config_file` Ansible variable to be automatically passed to AEM Compose CLI.
   This approach is used in [default instance role](roles/instance/templates/aem.yml)
 

2. Playbook:

   For better flexibility, it is recommended to create your own instance role by copying the default [instance role](roles/instance) and then adapting it for a project-specific use case.
   The tasks below are just showcasing meaningful features of AEM Compose Ansible modules.

    ```yaml 
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
    
    - name: setup Crypto Support
      wttech.aem.crypto:
        command: setup
    
    - name: deploy APM package
      wttech.aem.pkg:
        command: deploy
        url: https://github.com/wttech/APM/releases/download/apm-5.5.1/apm-all-5.5.1.zip
    
    - name: read some node
      wttech.aem.repo_node:
        command: read
        instance_id: local_author
        path: /content/cq:tags/experience-fragments
      register: res
    
    - name: print node creation time
      debug:
        msg: "Node '/content/cq:tags/experience-fragments' was created at '{{ res.data.node.properties['jcr:created'] }}'"
    
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
        pid: org.apache.sling.jcr.davex.impl.servlets.SlingDavExServlet
        props:
          alias: /crx/server
    ```
    
    Consider reviewing playbooks used in tests in [local example](examples/local) for more example usages.

# Contributing

Issues reported or pull requests created will be very appreciated.

1. Fork plugin source code using a dedicated GitHub button.
2. See [development guide](DEVELOPMENT.md)
3. Do code changes on a feature branch created from *main* branch.
4. Create a pull request with a base of *main* branch.

# License

**AEM Compose** is licensed under the [Apache License, Version 2.0 (the "License")](https://www.apache.org/licenses/LICENSE-2.0.txt)
