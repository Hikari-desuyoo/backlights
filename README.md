# Backlights

Pequeno projeto em python para mudar a claridade dos LEDs do teclado de acordo com o aúdio.

## Antes de começar

Esse programa só foi testado em um Mint, e provavelmente só funciona em notebooks da Dell (possivelmente, apenas Dell Latitude).

## Dependências

As dependências de bibliotecas em python podem ser instaladas com `pip install -r requirements.txt`.
Além delas, é necessário executar os seguintes comandos em seu terminal:
- `sudo apt-get install portaudio19-dev python-pyaudio`
- `sudo apt-get install pavucontrol`

Também é necessário configurar o pavucontrol, seguindo as instruções propostas [nesse link](https://stackoverflow.com/questions/26573556/record-speakers-output-with-pyaudio), na resposta do usuário *antoineMoPa*, no subtítulo *configuration*

## Como iniciar
`python3 main.py`