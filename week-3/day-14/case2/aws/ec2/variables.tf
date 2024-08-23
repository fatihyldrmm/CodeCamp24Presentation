variable "aws_region" {
  default     = "us-east-2"
  description = "aws region"
}

variable "ami_id" {
  type        = string
  description = "AMI ID for the EC2 instance"
}
variable "instance_type" {
  description = "Instance type"
}