terraform {
  required_providers {
    ansible = {
      source = "nbering/ansible"
      version = "1.0.4"
    }
    aws = {
      source = "hashicorp/aws"
      version = "=4.31.0"
    }
    tls = {
      source = "hashicorp/tls"
      version = "=4.0.4"
    }
    time = {
      source = "hashicorp/time"
      version = "=0.7.2"
    }
  }
}
