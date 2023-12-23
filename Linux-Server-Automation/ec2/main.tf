locals {
  students = jsondecode(file("/Users/dan/github/dnlloyd/mcc-csis-119-private/passwords-plain-text.json"))
}

resource "aws_security_group" "linux_server" {
  name        = "mcc-csis-119-linux"
  description = "Access to Linux server"
  vpc_id      = "vpc-2f83f048"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = { Name = "mcc-csis-119-linux" }
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners = ["137112412989"]

  filter {
    name = "name"
    values = ["al2023-ami-2023.1.20230809.0-kernel-6.1-x86_64"]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "linux" {
  ami = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  associate_public_ip_address = true
  iam_instance_profile = "SSMInstanceProfile"
  key_name = "aws-personal"
  vpc_security_group_ids = [aws_security_group.linux_server.id]

  tags = {
    Name = "mcc-csis-119-linux"
  }

  # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-shell-scripts
  # cat /var/log/cloud-init-output.log
  # /var/lib/cloud/instances/i-XXX/user-data.txt
  user_data = base64encode(templatefile("init-scripts/provision-users.tftpl", {students = local.students}))
}

output "public_ip" {
  value = aws_instance.linux.public_ip
}
