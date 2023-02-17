FROM cytopia/ansible:2.11-aws
ENV TERRAFORM_VERSION=1.2.9
ENV PACKER_VERSION=1.8.3

COPY src /controller

RUN apk --no-cache add zip unzip graphviz

RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && wget https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip \
  && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin \
  && unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin \
  && rm *.zip

RUN cd /controller/ansible && sh setup.sh
RUN cd /controller/terraform && sh setup.sh

WORKDIR "/controller"
CMD ["tail", "-f", "/dev/null"]
