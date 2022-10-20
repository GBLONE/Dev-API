# Dev-API | "app.py"
<text>
  Projeto que possui exemplo de REST-API com Flask.<br>
  No arquivo chamando "app.py" a gente vê uma API que devolve o desenvolvedor pelo ID (0, 1 ou 2) utilizando o método GET, a gente também pode notar que ela também pode 
  alterar ou deletar um desenvolvedor utilizando os métodos PUT para alterar o desenvolvedor, e DELETE para deletar o desenvolvedor.<text/><br>
<text>
  Lembrando que necessita de ter o ID pelo caminho da rede, exemplo: http://127.0.0.1:5000/dev/(id:usuario)/ assim colocando o número do ID do usuário/desenvolvedor 
  a gente pode aplicar as modificações, desde que coloque qual método você precisa para realizar sua tarefa <br>(GET: para visualizar um único usuário, PUT: para alterar 
  o nome, ID ou Habilidades, DELETE: para deletar os usuários/desenvolvedores).<text/><br>
<text>
  Segunda parte do "app.py" é que tem um jeito de listar e adicionar novos usuários.<br>
  E para você listar o usuário você só precisa fazer a rota http://127.0.0.1:5000/dev/ com GET, assim irá aparecer um lista dos usuários/desenvolvedores e todos seus dados.<br> 
  E para adicionar um usuário você só precisa fazer a rota http://127.0.0.1:5000/dev/ com POST, e assim irá adicionar um novo usuário/desenvolvedor com novo ID 
  e com uma nova habilidade.<text/><br>
<text>
  Terceira parte é simples, aqui existe uns usuários e que usando a rota http://127.0.0.1:5000/dev/(id:usuario)/tarefa/ do flask vamos ver as tarefas do usuário quando 
  utilizamos o pelo método GET. E usando a mesma rota nós conseguimos pelo método PUT e DELETE, alterar as tarefas e deletar elas respectivamente.
  <text/><br><br>
  
 ##
  
 # Dev-API | "app_RESTful.py"
 <text>
   Projeto que possui exemplo de Flask-RESTful com Flask.<br>
   Nessa API vemos o uso do Flask-RESTful em "app_RESTful.py", explicando de forma reduzida, seria quase a mesma forma da REST-API de cima, mas com pequenas mudanças e 
   trazendo para o modelo e API do Flask-RESTful.<br>
   Lembrando que toda os testes foram feito no aplicativo "Postman", que é onde consigo mudar o método GET, PUT, POST, DELETE, etc... Para conduzir e fazer ele melhor 
   o possível.
 <text/>
