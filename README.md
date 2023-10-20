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

# Para execução dos testes

Necessário entrar na pasta de teste dentro do diretório libs por meio do comando:

  * Abra um terminal dentro da pasta que foi clonada
  ```sh
 cd libs/tests/
  ```
  E executar o comando para execução:

  ```sh
  python -m unittest
  ```

# Documentação do framework Unittest

```sh
https://docs.python.org/3/library/unittest.html
```

# Estrutura de arquivos

## Bibliotecas


### **request_manager_attenuare**
Biblioteca que encapsula a biblioteca request, e realiza o manejamento de erros como SSL, ConnectionError etc... E realiza diversas tentativas até que o output seja o desejado ou se as tentativas atinjam um número específico. Essa biblioteca também gera um objeto do tipo BeautifulSoup caso a resposta seja favorável.