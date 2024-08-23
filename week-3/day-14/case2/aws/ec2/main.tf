resource "aws_instance" "codecamp" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = "codecamp24-keypair"
  user_data = <<-EOF
              #!/bin/bash
              sudo yum clean all
              sudo yum update -y
              sudo amazon-linux-extras install -y nginx1
              echo "<h1>Muhammed Fatih Yildirim - Welcome to Codecamp</h1>" | sudo tee /usr/share/nginx/html/index.html
              sudo systemctl start nginx
              sudo systemctl enable nginx
              EOF


  tags = {
    Name = "codecamp"
  }
  vpc_security_group_ids = [aws_security_group.codecamp-bodyguard.id]
}

resource "aws_security_group" "codecamp-bodyguard" {
  name        = "ec2-defender-new"
  description = "case2"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }
    
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }

}

# resource "aws_security_group" "codecamp-bodyguard-2" {
#   name        = "ec2-defender"
#   description = "case2"

#   ingress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#     }

#     ingress {
#     from_port   = 443
#     to_port     = 443
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#     }

# }
