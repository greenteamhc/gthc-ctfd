import os

# Detecta se estamos rodando via `flask run` e não aplica o monkey patch
if not os.getenv("FLASK_RUN_FROM_CLI"):
    from gevent import monkey
    monkey.patch_all()

from werkzeug.middleware.proxy_fix import ProxyFix  # Adiciona o middleware ProxyFix para reconhecer o prefixo
from CTFd import create_app

app = create_app()

# Aplica o middleware ProxyFix para ajustar o prefixo /ctf corretamente
app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0", port=8000)  # Porta 8000 exposta para o Docker

