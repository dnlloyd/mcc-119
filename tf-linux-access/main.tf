resource "aws_security_group" "linux_server" {
  name        = "linux-server"
  description = "Access to Linux server"
  vpc_id      = local.vpc_id

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

  tags = { Name = "linux-server-access" }
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners = ["137112412989"]

  filter {
    name = "name"
    values = ["amazon/al2023-ami-2023.1.20230809.0-kernel-6.1-x86_64"]
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

  user_data = base64encode(templatefile("init-scripts/provision-users.sh", {users = local.users}))
}

