MininetWeb
==========

                                                   		 English

MininetWeb is a user-friendly web interface to the emulation environment Mininet POX, written in Python using the Flask microframework.

The MininetWeb was developed by computer science student Eliseu Silva Torres guided by professor doctor Joberto Sergio Barbosa Martins as final project at the Universidade de Salvador (Unifacs).


To use the MinentWeb interface is necessary to install the Flask microframework.
  
  	$ sudo pip install flask
	
	or
	
  	# pip install flask
	
The Flask is executed by default on port 5000, to configure the port.

  	# iptables -A FORWARD -p tcp --dport 5000 -j ACCEPT
  	
Download the project source code
	
	$ cd
	
	$ git clone https://github.com/EliseuTorres/MininetWeb
	
Run the project

	$ cd MininetWeb
	
	$ sudo python web.py
	
After running the project, open the web browser and access the MininetWeb interface using the ip of the mininet and using the port 5000.
	
	ex: x.x.x.x:5000	 	

==============================================================================================================
                                        			    Português

MininetWeb é uma interface amigavel web para o ambiente de emulação Mininet POX, escrita em Python utilizando o microframework Flask.

O MininetWeb foi desenvolvido pelo aluno de Ciência da Computação Eliseu Silva Torres orientado pelo professor doutor Joberto Sergio Barbosa Martins como projeto de conclusão de curso na  Universidade de Salvador (Unifacs)


Para utilizar a interface do MinentWeb é necessario instalar o microframework Flask.

	$ sudo pip install flask

	ou

	# pip install flask

O Flask é executado por padrão na porta 5000, para configurar a porta.

	# iptables -A FORWARD -p tcp --dport 5000 -j ACCEPT
	
Baixar o codigo fonte do projeto
	
	$ cd
	
	$ git clone https://github.com/EliseuTorres/MininetWeb
	
Executar o projeto

	$ cd MininetWeb
	
	$ sudo python web.py
	
Após executar o projeto, abra o navegador web e acesse a interface do MininetWeb utilizando o ip da maquina e utilizando a porta 5000. 
	
	ex: x.x.x.x:5000	



