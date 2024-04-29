

resource "aws_db_instance" "pessoa" {
  allocated_storage    = 10
  identifier           = "pessoa"
  db_name              = "pessoa"
  engine               = "mysql"
  engine_version       = "8.0.28"
  instance_class       = "db.t4g.micro"
  username             = "root"
  password             = "password"
  parameter_group_name = "default.mysql8.0"
  vpc_security_group_ids = [aws_security_group.sg.id]
  skip_final_snapshot  = true
}


resource "aws_security_group" "sg" {
  name   = "sg"
  vpc_id = "vpc-0593b8e7d1aa65bae"

   ingress {
    from_port        = 3306
    to_port          = 3306
    protocol         = "TCP"
    cidr_blocks      = ["172.31.0.0/16"]

  }
  
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}


resource "aws_glue_connection" "conexao_rds" {
  connection_properties = {
    JDBC_CONNECTION_URL = "jdbc:mysql://${aws_db_instance.pessoa.endpoint}/${aws_db_instance.pessoa.db_name}"
    PASSWORD            = "root"
    USERNAME            = "password"
  }

  name = "conexao com rds"

  physical_connection_requirements {
    availability_zone      =  "us-east-1"
    security_group_id_list = [aws_security_group.sg.id]
    subnet_id              = "subnet-0cb29b78f72ecaf17"
  }
}