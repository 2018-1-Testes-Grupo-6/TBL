# Contribuindo com o PGTBL.

Caso queira contribuir com o projeto, talvez seja uma boa ideia começar pelo [README](https://github.com/VictorArnaud/TBL/blob/master/README.md) para conhecer melhor sobre nós. 
Outro documento importante e que deve ser lido é o [Código de Conduta](https://github.com/VictorArnaud/TBL/blob/master/CODE_OF_CONDUCT.md).

Obrigado por contribuir! :tada::+1: Sua ajuda será recebida com muita gratidão!

# Como eu posso contribuir?

## Reportando um Bug

* Esse projeto segue um padrão de [_Issues_](https://github.com/VictorArnaud/TBL/blob/master/ISSUE_TEMPLATE.md). Logo, caso encontre um bug, verifique se ele não se encontra em uma das nossas _Issues_. Os bugs devem ser marcados com _tag (label)_ __bug__.

* Se o bug encontrado não consta nas _Isses_, basta abrir uma [Nova _Issue_](https://github.com/VictorArnaud/TBL/issues/new).


## Adicionando e/ou modificando alguma funcionalidade

* Primeiro verifique que não existe nenhuma [_Issue_](https://github.com/VictorArnaud/TBL/blob/master/ISSUE_TEMPLATE.md) a respeito dessa modificação e/ou adição.

* Caso não exista, crie uma [Nova _Issue_](https://github.com/VictorArnaud/TBL/issues/new). Dê um título significativo a ela, coloque uma descrição e pelo menos uma _label_.

* As mudanças devem ser submetidas através de [_Pull Requests_](https://github.com/VictorArnaud/TBL/blob/master/PULL_REQUEST_TEMPLATE.md). Você pode encontrar mais sobre isso no [_Pull Requests Template_](https://github.com/fga-gpp-mds/2018.1-Dr-Down/blob/support/community-files/PULL_REQUEST_TEMPLATE.md).


# Padrão de _Commit_

### Por questões de padronização recomendamos que sigam nosso estilo de _commit_:

* Os _commits_ devem ser todos em __inglês__;

* Ele deve conter um título curto e objetivo do que foi feito naquele _commit_;

* Se for preciso, após esse título, deve-se descrever, com um pouco mais de detalhes, todas as atividades executadas.

* Caso esteja trabalhando em com algum associado assine nos seus _commits_ os seus parceiros

__Exemplo:__

    Creating project community files (Título curto e objetivo)

    Adds project license (Descrição de uma das atividades)

    Adds project code of conduct file

    Adds project contributing file

    Adds project issue template file

    Adds projects pull request file

    Co-authored-by: Victor Arnaud <victorhad@gmail.com> (Assinatura de parceria)

# Política de _Branchs_

Tendo como meta manter a integralidade e confiabilidade do código do projeto foi proposta a utilização de política de branches.
Essa Política de Branches deverá guiar os desenvolvedores na forma de organização de suas contribuições ao repositório.

* __master__ - Branch principal do repositório onde será permitida somente a integração de software consolidado e testado. Essa branch será exclusiva para a entrega de Realeases, ou seja, um conjunto maior de funcionalidades que integram o software, aqui estará a versão _**stable**_ do software.

* __dev__ - Branch para integração de novas funcionalidades, onde será permitido a entrega das features desenvolvidas e que estão em um estágio avançado de completude. Será o branch base para o início do desenvolvimento das features e da correção de bugs. Aqui também serão _mergeadas_ as releases.

* __<nome-da-feature>__ - Branch utilizada para o desenvolvimento de novas features do _backlog_. Caso a feature tenha sida proposta por uma _issue_ do repositório e aceita no _backlog_ o nome deverá conter o número da _issue_. 
Ex: 1-<nome-da-nova-feature> (Considerando que a feature tenha sido solicitada na _issue_ #1)
