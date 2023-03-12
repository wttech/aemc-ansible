variable ansible_extra_vars {
  type =  string
  default = "aem_project_kind='classic'"
}

locals {
  timestamp = regex_replace(timestamp(), "[- TZ:]", "")

  workspace = "aemc"
  env_type = "aem-single"
  host = "aem_single"

  ssh_user = "ec2-user"

  tags = {
    Workspace = "aemc"
    Env = "image"
    EnvType = "aem-single"
    Host = "aem-single"
    Name = "${local.workspace}_${local.env_type}_${local.host}"
  }
}

source "amazon-ebs" "ami" {
  region = "eu-central-1"

  source_ami = "ami-043e06a423cbdca17" // RHEL 8
  ami_name = "${local.workspace}_${local.env_type}_${local.host}-${local.timestamp}"

  associate_public_ip_address = true
  instance_type = "m5.xlarge"

  communicator = "ssh"
  ssh_username = "${local.ssh_user}"
  //ssh_pty = true

  launch_block_device_mappings {
      device_name = "/dev/sda1"
      volume_type = "gp2"
      volume_size = "32"
      delete_on_termination = true
  }

  tags = "${local.tags}"
  run_tags = "${local.tags}"
  run_volume_tags = "${local.tags}"

  // TODO remove this when used in non-testing purposes
  skip_create_ami = true
}

build {
  sources = ["source.amazon-ebs.ami"]

  provisioner "file" {
    source = "managed-requirements.txt"
    destination = "/tmp/requirements.txt"
  }
  provisioner "shell" {
    script = "./managed-init.sh"
  }
  provisioner "ansible" {
    command = "./controller-run.sh"
    playbook_file = "aem_single.yml"
    extra_arguments = ["--verbose", "--extra-vars", "${var.ansible_extra_vars}"]
    host_alias = "${local.host}"
    user = "${local.ssh_user}"

    sftp_command = "/usr/libexec/openssh/sftp-server -e" // for Centos/RHEL only, comment out otherwise
    use_proxy = false // may fix Ansible SSH connection problems when gathering facts
  }
}
