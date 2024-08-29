Clinica - Sistema de Agendamento Django REST API
Este documento é o README do projeto Clinica, uma aplicação Django RESTful desenvolvida para gerenciar agendamentos médicos.

Funcionalidades
Cadastro de pacientes, incluindo informações como nome, RG, data de nascimento, endereço e data de cadastro.
Cadastro de agendamentos, associando-os a um paciente específico. Os agendamentos possuem data e hora, observação opcional e indicação de cancelamento.
Registro de histórico clínico, vinculado a um agendamento específico. O histórico permite armazenar dados como aparecimento de sintomas, duração, localização e tipo de dor, conclusão do atendimento e outros detalhes relevantes.
Exibição de listas de pacientes, agendamentos e históricos através da API RESTful.
Realização de operações CRUD (Create, Read, Update, Delete) para os modelos Paciente, Agendamento e Histórico.
Tecnologias Utilizadas
Django: Framework Python robusto para desenvolvimento web, utilizado na construção da estrutura básica da aplicação.
Django REST Framework: Biblioteca de extensão para Django que facilita a criação de APIs RESTful, permitindo a comunicação com dados em formato JSON.
SQLite3: Banco de dados leve e embutido utilizado para armazenar os dados da aplicação (configuração padrão).
Instalação
Clone o Repositório:

Utilize o comando git clone https://github.com/<SEU_NOME_DE_USUARIO>/clinica.git para clonar o repositório da Clinica em sua máquina local.
Crie um Ambiente Virtual (Recomendado):

É altamente recomendado utilizar um ambiente virtual para gerenciar as dependências do projeto de forma isolada. Utilize ferramentas como venv ou virtualenv para criar um ambiente virtual e ative-o antes de prosseguir.
Instale as Dependências:

Acesse o diretório do projeto clonado e execute o comando pip install -r requirements.txt para instalar todas as bibliotecas e dependências necessárias para o funcionamento da API.
Migrações do Banco de Dados:

Execute o comando python manage.py migrate para criar as tabelas do banco de dados de acordo com os modelos definidos na aplicação.
Uso
1. Inicie o Servidor de Desenvolvimento:

Execute o comando python manage.py runserver para iniciar o servidor de desenvolvimento da API. O servidor estará acessível na porta 8000 por padrão (http://localhost:8000/).
2. Interagindo com a API:

A API RESTful utiliza o formato JSON para comunicação de dados.
Utilize ferramentas como Postman ou curl para enviar requisições HTTP e visualizar as respostas da API.
Consulte a documentação oficial do Django REST Framework para obter detalhes sobre as operações CRUD e o formato de requisições/respostas: https://www.django-rest-framework.org/
Exemplo de obtenção da lista de pacientes:

curl http://localhost:8000/pacientes/
