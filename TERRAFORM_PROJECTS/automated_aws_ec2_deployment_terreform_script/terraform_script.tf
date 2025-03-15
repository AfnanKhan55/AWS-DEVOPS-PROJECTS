provider "aws" {
  region     = "us-east-1"
  access_key = "YOUR_ACCESS_KEY"
  secret_key = "YOUR_SECRET_KEY"
}

resource "aws_instance" "child_1" {
  ami                    = "ami-04b4f1a9cf54c11d0"
  instance_type          = "t2.micro"
  key_name               = "selenium"
  vpc_security_group_ids = ["sg-05a251e19c0285bb4"]

  tags = {
    Name = "child-1"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update -y",
      "sudo apt install docker.io -y",
      "sudo usermod -aG docker ubuntu"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("/home/ubuntu/selenium.pem")
      host        = self.public_ip
    }
  }
}

resource "aws_instance" "child_2" {
  ami                    = "ami-04b4f1a9cf54c11d0"
  instance_type          = "t2.micro"
  key_name               = "selenium"
  vpc_security_group_ids = ["sg-05a251e19c0285bb4"]

  tags = {
    Name = "child-2"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update -y",
      "sudo apt install nginx -y"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("/home/ubuntu/selenium.pem")
      host        = self.public_ip
    }
  }
}

output "child_1_public_ip" {
  value = aws_instance.child_1.public_ip
}

output "child_2_public_ip" {
  value = aws_instance.child_2.public_ip
}
