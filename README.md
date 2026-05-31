Minha ideia inicial era organizar os produtos do estoque em "departamenos" como eletrodomesticos, limpeza, saude.

Mas o tipo de produto para cada empresa varia muito,então eu tenho que criar um sistema que se adapta a qualquer tipo de produto idependentemente da empresa. 

Oque todos os produtos tem em comum? Todos os produtos tem um nome, um preço, uma quantidade em estoque e uma descrição.

Podemos por os produtos em um bancode dados algo interresante de se fazer.

Mas tem um detalhe, se um produto x estiver no estoque, esse produto tem uma certa quantidade, e a quantidade desse produto deve aparecer no banco de dados, a estrutura da tabela pode ser assim:
| id | nome | preço | quantidade | descrição |

Simplesmente isso, e a quantidade do produto x pode ser atualizada quando o produto for vendido ou comprado.

Um exemplo simples:
|01|Coca-cola|5.00|100|Refrigerante sabor cola|