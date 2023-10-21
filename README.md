# Objetivo 🎯
Nasa Images Scraper 

Projeto desenvolvido com o principal intuito de realizar uma pesquisa no banco de dados de mídias públicas da Nasa, por meio de uma API identificada no Front End do website. Por meio de um parâmetro passado como argumento, é enviado uma requisição para esta API que retorna informações sobre esse determinado parâmetro e links de imagem.

# Tecnologias utilizadas💻
    
    * Python
    * Unittest


# Instalação ⚙
Para executar o projeto siga os passos a seguir

  * Clone o repositório na máquina
  ```sh
  git clone https://github.com/Attenuare/nasa_images_scraper
  ```
  * Instale uma virtualenv
  ```sh
  pip install virtualenv
  ```
  * Crie um ambient virtual
  ```sh
  virtualenv venv 
  ```

  * Entre no ambiente virtual
  ```sh
  venv/Scripts/activate
  ```

  * Na raiz do projeto execute
  ```sh
  python main.py <parametro>
  ```
  A execução irá gerar um arquivo chamado CSV com o seguinte padrão de nome output_nasa_images_<parametro>.csv

# Download das imagens

Para extrair informações sobre as imagens e realizar o download delas:

  * Na raiz do projeto execute
  ```sh
  python main.py <parametro> -i down
  ```
Com esse argumento o script criará um diretório   ```nasa_images``` contendo as imagens baixadas

# Para execução dos testes

Necessário entrar na pasta de teste dentro do diretório libs por meio do comando:

  * Abra um terminal dentro da pasta que foi clonada
  ```sh
 cd libs/tests/
  ```
  E executar o comando para execução:

  ```sh
  python -m unittest load_tests.py
  ```

# Documentação do framework Unittest

```sh
https://docs.python.org/3/library/unittest.html
```

# Estrutura de arquivos

├── libs
│   ├── app
│   │   ├── data_manipulation_class.py
│   │   ├── __init__.py
│   │   ├── nasa_images_class.py
│   ├── context
│   │   ├── __init__.py
│   │   ├── nasa_context.py
│   └── tests
│       ├── load_tests.py
│       ├── testify_test
│       ├── unit_tests_api.py
│       └── unit_tests_structure.py
├── LICENSE
├── main.py
├── requirements.txt

## app
A classe data_manipulation_class realiza manipulação de arquivos CSV, realizando gravação e leitura de arquivos, convertendo os resultados em dicionário.

A classe nasa_images_class realiza a conexão com a API de front do reposítorio de mídias da Nasa, e trata s dados adicionando os campos necessário em uma estrutura de lista com dicionários.

## context
A classe nasa_context execução os outputs do script, realizando a incorporação da classe nasa_images_class, o contexto injeta um termo de pesquisa na classe de conexão com a API da nasa, e extrai as informações, e caso seja passado um argumento específico, ele realiza o download das imagens também.

## tests
Há duas classes de teste que testa separadamente as duas principais entidades do projeto:
  ``` 
nasa_images_class => unit_tests_api
nasa_context      => unit_tests_structure
  ```
E um carregador de testes load_tests junta todos os testes e executa todos.


## Bibliotecas

### **request_manager_attenuare**
Biblioteca que encapsula a biblioteca request, e realiza o manejamento de erros como SSL, ConnectionError etc... E realiza diversas tentativas até que o output seja o desejado ou se as tentativas atinjam um número específico. Essa biblioteca também gera um objeto do tipo BeautifulSoup caso a resposta seja favorável.
