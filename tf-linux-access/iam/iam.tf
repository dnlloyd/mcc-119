# https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-quickstart.html

locals {
  students = jsondecode(file("/Users/dan/github/dnlloyd/mcc-csis-119-private/students.json"))
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

  user    = aws_iam_user.student[each.key].name
  # pgp public key
  # gpg --export dan@lloydconsulting.net | base64
  pgp_key = file("/Users/dan/tmp/secure/gpg-lc.pub")
}

resource "aws_iam_user_group_membership" "csis_119" {
  for_each = local.students

  user = aws_iam_user.student[each.key].name
  groups = ["csis_119"]
}

# output password | base64 --decode | gpg -d
# tf output -json passwords > /Users/dan/github/dnlloyd/mcc-csis-119-private/passwords.json
output "passwords" {
  value = {
    for k, v in aws_iam_user_login_profile.student : k => v.encrypted_password
  }
}
