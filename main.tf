
#resource "aws_secretsmanager_secret" "db-pass" {
#  name = "db-${random_string.random.result}"
#
#  depends_on = [ random_string.random ]
#}
#
#resource "random_string" "random" {
#  length           = 14
#  special          = false
#  override_special = "/@£$"
#}

#resource "aws_secretsmanager_secret_version" "db-pass-val" {
#  secret_id = aws_secretsmanager_secret.db-pass.id
#  secret_string = jsonencode(
#    {
#      username = aws_db_instance.pessoa.username
#      password = aws_db_instance.pessoa.password
#      engine   = "mysql"
#      host     = aws_db_instance.pessoa.endpoint
#    }
#  )
#}

#resource "random_password" "password" {
#  length           = 16
#  special          = true
#  override_special = "!#$%&*()-_=+[]{}<>:?"
#}

#resource "aws_db_instance" "pessoa" {
#  allocated_storage    = 10
#  identifier           = "pessoa"
#  db_name              = "pessoa"
#  engine               = "mysql"
#  engine_version       = "8.0.36"
#  instance_class       = "db.t4g.micro"
#  username             = var.username
#  password             = random_password.password.result
#  parameter_group_name = "default.mysql8.0"
#  vpc_security_group_ids = [aws_security_group.sg.id]
#  skip_final_snapshot  = true
#  depends_on = [ random_password.password ]
#}


resource "aws_security_group" "sg" {
  name   = "sg"
  vpc_id = "vpc-0593b8e7d1aa65bae"

   ingress {
    from_port        = 0
    to_port          = 65535
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
    JDBC_CONNECTION_URL = "jdbc:mysql://pessoa.cl8rjp16vban.us-east-1.rds.amazonaws.com:3306/pessoa"
    PASSWORD            = "P|5G%1%}4MFvgUDO!yn}3AZ_8saw"
    USERNAME            = "admin"
  }

  name = "conexao com rds"

  physical_connection_requirements {
    availability_zone      =  "us-east-1f"
    security_group_id_list = [aws_security_group.sg.id]
    subnet_id              = "subnet-05a14f0bed1f307b8"
  }
}