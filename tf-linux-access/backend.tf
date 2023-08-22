terraform {
  backend "s3" {
    bucket       = "tf-remote-state-csis-119"
    key          = "remote-state.tfstate"
    region       = "us-east-1"
  }
}
