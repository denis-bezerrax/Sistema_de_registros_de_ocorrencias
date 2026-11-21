<h1 align="center">
  Sistema de registros de ocorrências
</h1>
<h2>
  Desenvolvedores
</h2>
<p>
  Ana Paula - RM574458 <br>
  Denis Bezerra - RM575175
</p>

<h2>
  Descrição
</h2>

<p>
  Criamos um sistema de registros de ocorrências para a cidade de São Paulo, sendo utilizado ocorrências fictícias para demonstrar o funcionamento do programa. O intuito do desenvolvimento foi possibilitar o registro de problemas na cidade, como iluminação em determinado ponto não estar funcionando ou a rua estar com buracos, etc. Além de registrar, é possível realizar a consulta e o devido tratamento da ocorrência por parte da equipe administrativa. O script contribui para a manutenção e resolução de problemas que surgem na cidade.
</p>

<h2>
  Estrutura de dados
</h2>
<table>
  <thead>
    <tr>
      <th>Estrutura</th>
      <th>Onde é usada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lista</td>
      <td>Ocorrências, que reúne todos os registros.</td>
    </tr>
    <tr>
      <td>Dicionário</td>
      <td>Cada ocorrência (<code>id</code>, <code>categoria</code>, <code>descricao</code>, <code>local</code>, <code>situacao</code>, <code>data_abertura</code>, <code>data_inicio</code>, <code>data_conclusao</code>, <code>historico</code>, <code>devolutiva</code>) e os menus <code>CATEGORIAS</code> e <code>SITUACOES</code>.</td>
    </tr>
    <tr>
      <td>Fila (<code>deque</code>)</td>
      <td>Fila de pendências: a ocorrência mais antiga sai primeiro.</td>
    </tr>
    <tr>
      <td>Pilha (lista com <code>append</code> e <code>pop</code>)</td>
      <td>Eventos recentes: o último evento registrado é o primeiro a ser exibido.</td>
    </tr>
    <tr>
      <td>Matriz</td>
      <td>Contagem por categoria (linhas) e situação (colunas) nos indicadores.</td>
    </tr>
    <tr>
      <td>Consultas</td>
      <td>Percorrem a lista e comparam o campo escolhido com o valor informado.</td>
    </tr>
    <tr>
      <td>Cadastro</td>
      <td>Usa o maior ID existente mais 1 e começa sempre na situação Aberta.</td>
    </tr>
    <tr>
      <td>Situações</td>
      <td>Aberta, Em análise e Concluída.</td>
    </tr>
  </tbody>
</table>
<h2>
  Regras lógicas
</h2>

<table>
  <thead>
    <tr>
      <th>Regra lógica</th>
      <th>Aplicação no sistema</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Identificação de pendências</td>
      <td>Verifica se a ocorrência ainda não foi concluída para classificá-la como pendente.</td>
    </tr>
    <tr>
      <td>Controle de situações</td>
      <td>Permite que a ocorrência transite entre Aberta, Em análise e Concluída, respeitando seu estado atual.</td>
    </tr>
    <tr>
      <td>Início do acompanhamento</td>
      <td>Registra a data e hora de início quando a ocorrência entra em acompanhamento, evitando registros duplicados de início.</td>
    </tr>
    <tr>
      <td>Conclusão do acompanhamento</td>
      <td>Registra a data e hora de encerramento quando a ocorrência é concluída.</td>
    </tr>
    <tr>
      <td>Validação de dados</td>
      <td>Verifica se os campos obrigatórios foram preenchidos corretamente antes de cadastrar uma ocorrência.</td>
    </tr>
    <tr>
      <td>Identificação automática</td>
      <td>Gera um identificador único para cada ocorrência com base no maior ID existente, acrescido de 1.</td>
    </tr>
    <tr>
      <td>Controle de fila</td>
      <td>Prioriza o atendimento das ocorrências mais antigas, respeitando a ordem de entrada.</td>
    </tr>
    <tr>
      <td>Histórico de eventos</td>
      <td>Registra alterações e movimentações realizadas nas ocorrências, permitindo acompanhar sua evolução.</td>
    </tr>
    <tr>
      <td>Indicadores</td>
      <td>Utiliza condições e comparações para contabilizar ocorrências por categoria e situação.</td>
    </tr>
    <tr>
      <td>Consultas e filtros</td>
      <td>Compara os valores dos campos com os parâmetros informados pelo usuário para retornar os registros correspondentes.</td>
    </tr>
  </tbody>
</table>

<h2>
  Indicadores implementados
</h2>
<table>
  <thead>
    <tr>
      <th>Indicador</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total de ocorrências</td>
      <td>Apresenta a quantidade total de ocorrências registradas no sistema.</td>
    </tr>
    <tr>
      <td>Ocorrências abertas</td>
      <td>Contabiliza as ocorrências que permanecem na situação Aberta.</td>
    </tr>
    <tr>
      <td>Ocorrências em análise</td>
      <td>Apresenta a quantidade de ocorrências que estão sendo acompanhadas e analisadas.</td>
    </tr>
    <tr>
      <td>Ocorrências concluídas</td>
      <td>Contabiliza as ocorrências cujo acompanhamento foi encerrado.</td>
    </tr>
    <tr>
      <td>Ocorrências por categoria</td>
      <td>Apresenta a distribuição das ocorrências de acordo com suas categorias.</td>
    </tr>
    <tr>
      <td>Ocorrências por situação</td>
      <td>Exibe a quantidade de registros agrupados por situação.</td>
    </tr>
    <tr>
      <td>Pendências</td>
      <td>Identifica e contabiliza as ocorrências que ainda não foram concluídas.</td>
    </tr>
  </tbody>
</table>
<h2>
  Como executar
</h2>

<h3>1. Clone o repositório</h3>

<pre><code>git clone https://github.com/denis-bezerrax/Sistema_de_registros_de_ocorrencias.git</code></pre>

<h3>2. Acesse a pasta do projeto</h3>

<pre><code>cd Sistema_de_registros_de_ocorrencias</code></pre>

<h3>3. Execute o sistema</h3>

<pre><code>python3 main.py</code></pre>

<h3>Pré-requisitos</h3>

<ul>
  <li>Python 3 instalado;</li>
  <li>Terminal ou ambiente compatível com execução Python.</li>
</ul>

<p>O sistema utiliza bibliotecas nativas do Python, não sendo necessária a instalação de dependências externas.</p>
<h2>
  Exemplo de cadastro
</h2>
<h2>Exemplo de Cadastro</h2>

<p>Ao selecionar a opção de cadastro, o sistema solicita as informações necessárias para registrar uma nova ocorrência.</p>

<h3>Exemplo de entrada</h3>

<pre>
Categoria: Iluminação
Descrição: Poste de iluminação pública está apagado durante a noite.
Local: Rua das Flores, Centro
</pre>

<h3>Registro gerado pelo sistema</h3>

<pre>
Resumo da ocorrência

Categoria: Iluminação
Descrição: Poste de iluminação pública está apagado durante a noite.
Local: Rua das Flores, Centro
Data de abertura: 21/11/2026 às 09:52:00

A sua ocorrência foi salva!

O id da sua ocorrência é 14.
</pre>

<p>Após o cadastro, a ocorrência recebe automaticamente um identificador único, a data e o horário de abertura, além da situação inicial <strong>Aberta</strong>. O registro fica disponível para consulta e acompanhamento posterior.</p>

<h2>
  Cuidados adotados com acessibilidade, inclusão e privacidade
</h2>
<h3>Acessibilidade</h3>
<ul>
  <li>Organização das informações de forma clara e objetiva, facilitando a utilização do sistema.</li>
  <li>Menu textual com opções numeradas, permitindo uma navegação simples e intuitiva.</li>
  <li>Possibilidade de registrar ocorrências relacionadas à acessibilidade urbana, como problemas em rampas e calçadas.</li>
</ul>

<h3>Inclusão</h3>
<ul>
  <li>Disponibilização de categorias que abrangem diferentes problemas urbanos e sociais.</li>
  <li>Possibilidade de registrar demandas relacionadas a escolas, hospitais, iluminação, ruas, calçadas e acessibilidade.</li>
  <li>Proposta de contribuir para a identificação de problemas que impactam diferentes grupos da população.</li>
</ul>

<h3>Privacidade</h3>
<ul>
  <li>Solicitação apenas das informações necessárias para o registro da ocorrência.</li>
  <li>Utilização de locais e descrições para contextualizar os problemas relatados.</li>
  <li>Ausência de solicitação de dados pessoais sensíveis durante o cadastro.</li>
</ul>

<h2>
  Link do Youtube
</h2>
<p>
  <href>https://youtu.be/Zdj9Z14_mbk</href>
</p>
<h2>
  Uso da IA
</h2>
<p>
  Utilizamos IA no estágio final do projeto para revisar o código e nos mostrar se faltava algo. A parte de tempo dos registros foi desenvolvida com o auxílio da IA por se tratar de algo mais complexo para nós. Além disso, determinadas partes do README foram criadas também com o auxílio dela.
</p>
<h2>
  Conclusão
</h2>
<p>
  O Neighborhood Action Dashboard mostrou como um sistema simples em Python pode ajudar no acompanhamento de problemas de um bairro. O morador registra uma demanda e recebe um número de ID, e quem acompanha o caso consegue localizar o registro, atualizar a situação e escrever uma devolutiva. Isso torna o processo mais organizado e transparente, já que cada alteração fica guardada no histórico, com data e hora.
</p>
<p>
  Durante o desenvolvimento, aplicamos estruturas de dados vistas na disciplina: lista e dicionários para os registros, fila para as pendências (a mais antiga sai primeiro), pilha para os eventos recentes e matriz para os indicadores por categoria e situação. Também melhoramos o código com menus em um único laço, validação das entradas e compatibilidade com Python 3.8 ou superior.
</p>
<p>
  O projeto tem limitações: os dados ficam só em memória e se perdem ao fechar o programa, e a data de abertura é automática. Como melhorias futuras, seria possível salvar os dados em arquivo ou banco de dados e criar uma interface mais amigável. Mesmo assim, o projeto cumpriu o objetivo de simular, de forma prática, o ciclo de uma ocorrência, do registro até a conclusão.
</p>
