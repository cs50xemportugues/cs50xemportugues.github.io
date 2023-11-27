'import check50
import check50.py
import check50.flask
import os


# Define um valor dummy para a variável de ambiente API_KEY. O código distro olha para esse valor, mas ele não é usado nas verificações.
os.environ["API_KEY"] = "foo"


@check50.check()
def existe():
    """app.py existe"""
    check50.exists("app.py")
    check50.include("lookup.py")
    check50.py.append_code("helpers.py", "lookup.py")


@check50.check(existe)
def inicializacao():
    """aplicação inicia"""
    Finance().get("/").status(200)


@check50.check(inicializacao)
def pagina_registro():
    """página de registro possui todos os elementos requeridos"""
    Finance().validate_form("/registrar", ["nome de usuário", "senha", "confirmação"])


@check50.check(pagina_registro)
def registro_simples():
    """registro de usuário é bem sucedido"""
    Finance().register("_cs50", "ohHai28!", "ohHai28!").status(200)


@check50.check(pagina_registro)
def registro_campo_vazio_falha():
    """registro com campo vazio falha"""
    for user in [("", "crimson", "crimson"), ("jharvard", "crimson", ""), ("jharvard", "", "")]:
        Finance().register(*user).status(400)


@check50.check(pagina_registro)
def registro_senhas_diferentes_falha():
    """registro com senhas diferentes falha"""
    Finance().register("check50user1", "thisiscs50", "crimson").status(400)


@check50.check(pagina_registro)
def registro_rejeita_usuario_duplicado():
    """registro rejeita nome de usuário duplicado"""
    user = ["elfie", "Doggo28!", "Doggo28!"]
    Finance().register(*user).status(200).register(*user).status(400)


@check50.check(inicializacao)
def pagina_login():
    """página de login possui todos os elementos requeridos"""
    if Finance().page_exists("/login"):
        Finance().validate_form("/login", ["nome de usuário", "senha"])
        return
    Finance().validate_form("/entrar", ["nome de usuário", "senha"])


@check50.check(registro_simples)
def pode_entrar():
    """fazer login como um usuário registrado é bem sucedido"""
    Finance().login("_cs50", "ohHai28!").status(200).get("/", follow_redirects=False).status(200)


@check50.check(pode_entrar)
def pagina_cotacao():
    """página de cotação possui todos os elementos requeridos"""
    Finance().login("_cs50", "ohHai28!").validate_form("/cotacao", "símbolo")


@check50.check(pagina_cotacao)
def cotacao_trata_invalido():
    """cotação trata símbolo inválido"""
    Finance().login("_cs50", "ohHai28!").cotacao("ZZZ").status(400)


@check50.check(pagina_cotacao)
def cotacao_trata_branco():
    """cotação trata símbolo em branco"""
    Finance().login("_cs50", "ohHai28!").cotacao("").status(400)


@check50.check(pagina_cotacao)
def cotacao_trata_valido():
    """cotação trata símbolo válido"""
    (Finance().login("_cs50", "ohHai28!")
              .cotacao("AAAA")
              .status(200)
              .content(r"28\.00", "28.00", name="corpo"))


@check50.check(pode_entrar)
def pagina_compra():
    """página de compra possui todos os elementos requeridos"""
    Finance().login("_cs50", "ohHai28!").validate_form("/comprar", ["ações", "símbolo"])


@check50.check(pagina_compra)
def compra_trata_invalido():
    """compra trata símbolo inválido"""
    Finance().login("_cs50", "ohHai28!").transaction("/comprar", "ZZZZ", "2").status(400)


@check50.check(pagina_compra)
def compra_trata_compra_incorreta():
    """compra trata ações fracionárias, negativas e não numéricas"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/comprar", "AAAA", "-1").status(400)
              .transaction("/comprar", "AAAA", "1.5").status(400)
              .transaction("/comprar", "AAAA", "foo").status(400))


@check50.check(pagina_compra)
def compra_trata_valida():
    """compra trata compra válida"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/comprar", "AAAA", "4")
              .content(r"112\.00", "112.00")
              .content(r"9,?888\.00", "9,888.00"))


@check50.check(compra_trata_valida)
def pagina_venda():
    """página de venda possui todos os elementos requeridos"""
    (Finance().login("_cs50", "ohHai28!")
              .validate_form("/vender", ["ações"])
              .validate_form("/vender", ["símbolo"], field_tag="select"))


@check50.check(compra_trata_valida)
def venda_trata_invalido():
    """venda trata número de ações inválido"""
    Finance().login("_cs50", "ohHai28!").transaction("/vender", "AAAA", "8").status(400)


@check50.check(compra_trata_valida)
def venda_trata_valida():
    """venda trata venda válida"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/vender", "AAAA", "2")
              .content(r"56\.00", "56.00")
              .content(r"9,?944\.00", "9,944.00"))



class Finance(check50.flask.app):
    """Extensão da classe flask.App que adiciona funções específicas para o Finance"""

    APP_NAME = "app.py"

    def __init__(self):
        """Função auxiliar para registrar usuário"""
        super().__init__(self.APP_NAME)

    def register(self, username, password, confirmation):
        """Registrar novo usuário"""
        form = {"username": username, "password": password, "confirmation": confirmation}
        return self.post("/registrar", data=form)

    def login(self, username, password):
        """Função auxiliar para fazer login"""
        route = "/entrar"
        if self.page_exists("/login"):
            route = "/login"
        return self.post(route, data={"username": username, "password": password})

    def cotacao(self, ticker):
        """Consultar o aplicativo por uma cotação para o `ticker`"""
        return self.post("/cotacao", data={"symbol": ticker})

    def transaction(self, route, symbol, shares):
        """Enviar uma requisição para `route` ("/comprar" ou "/vender") para realizar a transação relevante"""
        return self.post(route, data={"symbol": symbol, "shares": shares})

    def validate_form(self, route, fields, field_tag="input"):
        """Certificar-se de que o formulário HTML em `route` possui campos de entrada dados por `fields`"""
        if not isinstance(fields, list):
            fields = [fields]

        content = self.get(route).content()
        required = {field: False for field in fields}
        for tag in content.find_all(field_tag):
            try:
                name = tag.attrs["name"]
                if required[name]:
                    raise Error("encontrados mais do que um campo chamado \"{}\"".format(name))
            except KeyError:
                pass
            else:
                check50.log("encontrado campo requerido \"{}\"".format(name))
                required[name] = True

        try:
            missing = next(name for name, found in required.items() if not found)
        except StopIteration:
            pass
        else:
            raise check50.Failure(f"esperava encontrar campo {field_tag} com nome \"{missing}\", mas nenhum foi encontrado")

        if content.find("button", type="submit") is None:
            raise check50.Failure("esperava encontrar um botão para enviar o formulário, mas nenhum foi encontrado")

        return self

    def page_exists(self, route):
        return self.get(route).status() == 200
'