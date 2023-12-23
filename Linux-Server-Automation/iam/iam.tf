# https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-quickstart.html

variable "canvas_students_file" {}
variable "gpg_key" {}
variable "class_name" {}

locals {
  students = jsondecode(file(var.canvas_students_file))
}

resource "aws_iam_user" "student" {
  for_each = local.students

  name          = each.key
  path          = "/"
  force_destroy = true

  tags = {
    "SSMSessionRunAs": "bastion"
  }
}

resource "aws_iam_user_login_profile" "student" {
  for_each = local.students

  user = aws_iam_user.student[each.key].name
  # create GPG key
  # gpg --export dan@lloydconsulting.net | base64
  # /Users/dan/tmp/secure/gpg-lc.pub
  pgp_key = file(var.gpg_key)
}

resource "aws_iam_group" "class" {
  name = var.class_name
}

resource "aws_iam_user_group_membership" "csis_119" {
  for_each = local.students

  user = aws_iam_user.student[each.key].name
  groups = ["csis_119"]
}

resource "aws_iam_group_policy_attachment" "test-attach" {
  group      = aws_iam_group.class.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
}

# output password | base64 --decode | gpg -d
# tf output -json passwords > /Users/dan/github/dnlloyd/mcc-csis-119-private/passwords.json
output "passwords" {
  value = {
    for k, v in aws_iam_user_login_profile.student : k => v.encrypted_password
  }
}
