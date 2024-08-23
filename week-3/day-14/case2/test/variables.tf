variable "ami_id" {
    type        = string
    default     = "ami-0a31f06d64a91614b"
    description = "AMI ID for the EC2 instance"
}
variable "instance_type" {
    default     = "t2.micro"
    description = "Instance type"
}

variable "aws_region" {
    description = "aws region"
    default     = "us-east-2"
}