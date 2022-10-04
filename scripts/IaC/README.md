![capa](./docs/pictures/capaA3.png)



# Documentação projeto: Delta Lake;
### Cliente: 123 Milhas; Squad Batingas.
\
\
\
repo_url: https://github.com/A3Data/123milhas-deltalake-documentation.git\
aws_s3_bucket: arn:aws:s3:::123milhas-delta-lake-documentation (ambiente_dev)\
url_estática_s3: http://123milhas-delta-lake-documentation.s3-website-us-east-1.amazonaws.com/\
\
\
\
*__Atenção:__* Antes de prosseguir, tenha em mente que o único diretório passível de receber conteúdo sobre o projeto é o **"./docs/"**.\
\
*__Nesse repositório pode ser encontrado todos os conteúdos referente ao projeto Delta Lake - 123 Milhas bem como toda a estruturação de sua documentação técnica.__*\
\
*__Não adicione, altere e/ou remova nenhum arquivo fora do diretório "./docs/". Faça isso apenas com a expressa exceção de ter plena ciência do que pretende fazer.__*\
\
\
\
## Como trabalhar com a edição da documentação técnica:
\
Para sua praticidade, esse repositório pode ser clonado localmente desde que possua os requisitos listados abaixo:
- git instalado (caso não possua siga no link https://git-scm.com/downloads para devida instalação de acordo com seu sistema operacional)\
- conta ativa no Git Hub (caso não possua conta, registre-se em https://github.com/signup)\

Para clonar, por facilidade, no terminal Git Bash, escolha o diretório local para abrigar o clone do repo e siga com os comandos:\
\$ cd <diretório_local_desejado_para_abrigar_o_repo_clone>\
\$ git clone https://github.com/A3Data/123milhas-deltalake-documentation.git\

Após trabalhar nas criações e edições neessárias, também no terminal Git Bash, siga com:\
\$ git pull      # (nunca se esqueça de sincronizar antes para puxar os commits de outros devs)\
\$ git add .     # (adiciona todo o conteúdo ora criado/modificado na stage_area)\
\$ git commit -m '<comentário_conforme_regras_de_commit_semântico>'\
\$ git push      # (sincroniza o ambiente local com o remoto)\

obs.: para orientação no comentário dos commits, veja a imagem abaixo:\
![commit_semantico](./docs/pictures/commit_semantico.png)
\
\
\
*__Importante__*: Não realizar alterações em outra pasta que não a **`./doc/`**.
\
\
\
## Quando da adição de novas páginas:
\
Para cada nova página adicionada no repo, ou seja, novo arquivo `.md`, não esquecer de acrescentar seu caminho na seção 'nav' do arquivo `mkdocs.yml`, no diretório raiz. (Vide exemplo abaixo)\
\
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
\
\
## Esteira CI-CD:
\
Para cada "push" identificado pelo GitHub (trigger), na branch main, conforme o workflow configurado no **`./github/workflows/doc_ci_cd.yml`**, o repo em questão será sicornizado automaticamente com o aws_s3_bucket dedicado para documentação.\
\
Nessa automação também contamos com o re-build do MkDocs para atualização automática do site.\
![capa](./docs/pictures/deploy_mkdocs.png)
\
\
\
## Breve descrição do conteúdo do repositório:
`./git` e `./github`  >dedicadas ao versionamento e automação;\
`./material`          >dedicada ao tema visual (plug-in mkdocs-material) ;\
`./site`              >dedicada à geração de htmls para renderização do website;\
`./mkdocs.yml`        >manifesto com a configuração dedicada ao build da aplicação MkDocs;\
`./requirements.txt`  >requisitos de dependências em python para que o workflow de automação possa rodar a aplicação em questão.\
\
Todo o conteúdo desenvolvido encontra-se localizado no diretório **"./docs/"**.\
    - Para textos, acesse e/ou crie arquivos markdown (`.md`) em **`docs/content/engenharia/`**.\
    - Para anexar imagens aos tópicos ou páginas, salve o arquivo desejado em **`docs/pictures/`** e adicione o caminho (sintaxe de link html) do mesmo dentro de um `.md`.\
\
\
\
## Links 'úteis':
https://www.markdownguide.org/\
https://www.mkdocs.org/\
https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins\
https://squidfunk.github.io/mkdocs-material/\
https://github.com/CoinK0in/mkdocs-encryptcontent-plugin\

![logo_reduzida](./docs/pictures/logoA3++reduzida.png)