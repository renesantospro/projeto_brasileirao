# MkDocs deployment testing with GitHub


\
Esse repositório é destinado a interesses meramente educacionais, sem qualquer fim lucrativo. Trata-se de uma dentre muitas formas de se implementar a aplicação MkDocs. Aplicação essa que tem por objetivo servir uma estrutura automatizada de HTMLs e CSSs, "por baixo dos panos", para o conteúdo desejado ser divulgado.  


\
____________________________________________________________________________________________________
### Links úteis:

- [The Markdown Guide](https://www.markdownguide.org/)

- [The official MkDocs documentation](https://www.mkdocs.org/)

- [GitHub Repo of usefull MkDocs Plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins)

- [Encrypt Content Plug-in documentation](https://github.com/CoinK0in/mkdocs-encryptcontent-plugin)


\
this_repo_url: https://github.com/renesantospro/mkdocs_deployment_testing_with_github.git

static_s3_url: http://mkdocs-deployment-testing-with-github.s3-website-us-east-1.amazonaws.com


\
____________________________________________________________________________________________________
### Breve descrição do conteúdo do repositório:

`./git` e `./github`    > dedicadas ao versionamento e automação;

`/site`                 > dedicada à geração de HTMLs para renderização do website;

`./mkdocs.yml`          > manifesto com a configuração dedicada ao build da aplicação MkDocs;

`./requirements.txt`    > requisitos de dependências em Python para que o workflow de automação possa rodar a aplicação em questão.

\
Todo o conteúdo desenvolvido encontra-se localizado no diretório **`./docs/`**.

- Para textos, acesse e/ou crie arquivos markdown (`.md`) em **`docs/content/engenharia/`**.

- Para anexar imagens aos tópicos ou páginas, salve o arquivo desejado em **`docs/pictures/`** e adicione o caminho do mesmo (sintaxe de link HTML) dentro de um `.md` onde é exposto o conteúdo relacionado.


\
____________________________________________________________________________________________________
*__Atenção:__* Antes de prosseguir, tenha em mente que o único diretório passível de receber conteúdo sobre o projeto é o **`./docs/`**.

*__Nessa documentação pode ser desenvolvida/encontrada todos os conteúdos referente à projetos bem como toda a estruturação de sua documentação técnica.__*

*__Não adicione, altere e/ou remova nenhum arquivo fora do diretório "./docs/". Faça isso apenas com a expressa exceção de ter plena ciência do que pretende fazer.__*


\
____________________________________________________________________________________________________
### Como trabalhar com a edição do conteúdo na documentação:

#### Clone repositório:

Para sua praticidade, esse repositório pode ser clonado localmente desde que possua os requisitos listados abaixo:

- git instalado (caso não possua siga no [link](https://git-scm.com/downloads) para devida instalação de acordo com seu sistema operacional)

- conta ativa no Git Hub (caso não possua conta, registre-se em [GitHub](https://github.com/signup))

\
Para clonar, por facilidade, no terminal Git Bash, escolha o diretório local para abrigar o clone desse repo e siga com os comandos:

`$ cd <diretório_local_desejado_para_abrigar_o_repo_clone>`

`$ git clone <url desse repo>`


\
#### Renderização local para efeitos de testes e pré-visualização:

Enquanto trabalha-se nas adições e edições de conteúdo, é conveniente simular o build da aplicação localmente utilizando o comando:

`$ mkdocs serve`

Tenha o cuidado de atentar-se para executar esse comando via terminal, na raiz do diretório clonado, onde encontra-se o arquivo manifesto mkdocs.yml.

\
Para ter a disponibilidade dessa aplicação local é necessária sua instalação local através do comnado:

`$ pip install mkdocs`
(via terminal)

\
A simulação de renderização será exibida em localhost:8080 (http://127.0.0.1:8000/). Para mais detalhes, consulte [Getting Started with MkDoks](https://www.mkdocs.org/getting-started/)


\
*__Importante__*: Não realizar alterações em outra pasta que não a **`./docs/`**.


\
____________________________________________________________________________________________________
## Quando da adição de novas páginas:


Para cada nova página adicionada no repo, ou seja, novo arquivo `.md`, não esquecer de acrescentar seu caminho na seção `nav` do arquivo `mkdocs.yml`, no diretório raiz. (Vide exemplo abaixo)


```
# Page tree
nav:
    - Home:
        - index.md ***Não alterar***
    
    - Engenharia: 
        - content/engenharia/engenharia.md
        - content/engenharia/arquitetura.md
        - (adicionar novos caminhos >aqui<)
        - (...)

        - Aplicações/Produtos: 
          - content/engenharia/opr.md
          - (adicionar novos caminhos >aqui<)
          - (...)
```

\
____________________________________________________________________________________________________
## Esteira CI-CD:

Para cada "PUSH" identificado pelo GitHub (trigger), na branch main, conforme o workflow configurado no **`./github/workflows/doc_ci_cd.yml`**, o repo em questão será sincronizado automaticamente com o aws_s3_bucket dedicado para tal documentação.

\
#### Operando as publicações:

Após trabalhar nas criações/edições necessárias e validar a pré-visualização no browser local, no terminal Git Bash, siga com os comandos abaixo para efetivar a publicação:

- Nunca se esqueça de sincronizar antes para puxar os commits de outros devs com esse comando, muito útil quando trabalha-se em equipe com varias colaborações.

`$ git pull`

- Adiciona todo o conteúdo ora criado/modificado na stage_area.

`$ git add .`

- Registra a nova versão com as modificações feitas e a identifica por hashes.

`$ git commit -m '<comentário_conforme_regras_de_commit_semântico>'`

- Sincroniza o ambiente local com o remoto.

`$ git push`


\
obs.: para orientação no comentário dos commits, veja a imagem abaixo:

![commit_semantico](./docs/pictures/commit_semantico.png)

\
Nessa automação também contamos com o re-build do MkDocs para sync automático do site dedicado.

![diagrama_deploy](./docs/pictures/deploy_mkdocs.png)
