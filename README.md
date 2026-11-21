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
<h2>
  Como executar
</h2>
<h2>
  Exemplo de cadastro
</h2>
<h2>
  Cuidados adotados com acessibilidade, inclusão e privacidade
</h2>
<h2>
  Link do Youtube
</h2>
<p>
  <href>https://youtu.be/Zdj9Z14_mbk</href>
</p>
<h2>
  Conclusão
</h2>
