module "aws-ec2" {
    source = "../aws/ec2"
    ami_id = var.ami_id
    instance_type = var.instance_type
    aws_region = var.aws_region
}
