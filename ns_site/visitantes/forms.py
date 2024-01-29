from django import forms
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]

        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante eh obrigatorio para o registro."
            },
            "cpf": {
                "required": "O cpf do visitante eh obrigatorio para o registro."
            },
            "data_nascimento": {
                "required": "A data de nascimento do visitante eh obrigatorio para o registro.",
                "invalid": "Por favor, informe um formato valido para a data de nascimento. (SUAMAE)"

            },
            "numero_casa": {
                "required": "O numero da casa do visitante eh obrigatorio para o registro."
            },
        }


