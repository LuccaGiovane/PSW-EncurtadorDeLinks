<div align="center">
   <h1><b>Encurtador de Links</b></h1><br><br>

   <a href="" target="_blank">![License](https://img.shields.io/badge/license-MIT-blue.svg)</a>
   ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
   ![Django](https://img.shields.io/badge/Django-darkgreen)
   ![Django Ninja](https://img.shields.io/badge/Django-Ninja-black)
   ![QRCode](https://img.shields.io/badge/QRCode-generator-gold)
   ![SQLite](https://img.shields.io/badge/SQLite-magenta.svg)

</div>

<div>
  
  <h2>📖 Descrição</h2>

  <p>Este projeto foi desenvolvido como parte da Pystack Week Returnal e contém o código-fonte de uma REST API criada com o framework Django, que permite aos usuários encurtarem links, gerarem QR Codes, configurarem expiração de links e visualizarem estatísticas de cliques.</p>
</div>

<div>
  <h2>🎯 Funcionalidades</h2>

  - **Encurtamento de links:** Permite criar links encurtados exclusivos com tokens automáticos.

  - **Redirecionamento automático:** Links encurtados redirecionam automaticamente para o destino configurado.

  - **Configuração de expiração:** Links podem ter tempo de expiração e limite de cliques únicos configurados.

  - **Estatísticas:** Exibe o total de cliques únicos e o total de cliques gerais de cada link.

  - **QRCode:** Gera QR Codes para os links encurtados.

  - **Desativação de links:** Usuários podem desativar links a qualquer momento

</div>

<div>

  <h2>👨🏻‍💻 Tecnologias Utilizadas</h2>

  - **Python 3.8**

  - **Django**: Framework web utilizado para o desenvolvimento do backend.

  - **Django Ninja**: Framework para a criação de APIs REST.

  - **SQLite**: Banco de dados utilizado para armazenar as informações.

  - **QRCode**: Biblioteca para geração de QR Codes.

</div>

<div>
  <h2>💾 Instalação e Configuração</h2>

1. **Clonar o repositório**
```bash
git clone https://github.com/LuccaGiovane/PSW-EncurtadorDeLinks.git
cd PSW-EncurtadorDeLinks
```

2. **Criar o ambiente virtual**
   
     2.1 Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
     2.2 Windows:
     ```bash
     python -m venv venv
     venv\Scripts\Activate
     ```

3. **Instalar as dependências**
```bash
pip install django django-ninja qrcode
```

4. **Executar migrações**
```bash
python manage.py migrate
```

5. **Iniciar o servidor**
```bash
python manage.py runserver
```
Acesse a API através do endereço:
```bash
http://127.0.0.1:8000/api/
```

</div>

<div>
  <h2>📁 Estrutura do Projeto</h2>

  ```bash
  .
  ├── core
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── shortener
  │   ├── migrations
  │   ├── api.py
  │   ├── models.py
  │   ├── schemas.py
  │   ├── tests.py
  │   ├── admin.py
  │   ├── apps.py
  │   └── views.py
  ├── manage.py
  └── LICENSE
  ```
  
</div>

<div>
  <h2>📑 Licença</h2>

  <p>Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.</p>
</div>

<div>
  <h2>🤝🏻 Contribuições</h2>

  <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.</p>
</div>
