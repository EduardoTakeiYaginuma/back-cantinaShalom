from flask import Response, jsonify

class ResponseEntity(Response):
    def __init__(self, status_code: int, message: str = None, data=None, headers: dict = None):
        # Inicializa os atributos
        self.status_code = status_code
        self.message = message
        self.data = data if data else []

        # Cria o corpo da resposta como JSON
        response_body = {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data
        }

        # Inicializa a classe Response do Flask com o JSON
        super().__init__(
            response=jsonify(response_body).get_data(as_text=True),
            status=self.status_code,
            mimetype="application/json"  # Define o tipo MIME padrão
        )

        # Adiciona headers padrão
        self.headers["X-Powered-By"] = "Flask-ResponseEntity"
        self.headers["Content-Type"] = "text/plain"  # Sobrescreve o Content-Type para 'text/plain'

        # Adiciona headers personalizados, se fornecidos
        if headers:
            for key, value in headers.items():
                self.headers[key] = value