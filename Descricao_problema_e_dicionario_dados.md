# Previsão de Salários a partir de Anúncios de Emprego

## Descrição do Problema

Dado um anúncio de emprego com suas informações estruturadas (título, localização, categoria, tipo de contrato, empresa) e textuais (descrição completa da vaga), prever o salário anual oferecido.

Trata-se de um problema de **regressão supervisionada**, onde a variável alvo (`salario`) é contínua e as variáveis preditoras combinam dados estruturados e não-estruturados (texto).

### Objetivo

Desenvolver e avaliar modelos de Machine Learning capazes de estimar a remuneração de vagas de emprego a partir das características e informações textuais presentes nos respectivos anúncios.

---

## Dicionário de Dados — `base_vagas.csv`

| Coluna | Descrição |
|---|---|
| `id_anuncio` | Identificador único do anúncio de emprego |
| `titulo` | Título da vaga conforme publicado no anúncio |
| `descricao` | Texto completo do anúncio, incluindo requisitos, responsabilidades e informações sobre a empresa |
| `localizacao_original` | Localização da vaga conforme informada pelo anunciante, sem padronização |
| `localizacao` | Localização da vaga após normalização/padronização |
| `tipo_contrato` | Tipo de jornada da vaga (ex: tempo integral, meio período) |
| `regime_contrato` | Regime do vínculo (ex: permanente, temporário) |
| `empresa` | Nome da empresa ou recrutadora que publicou o anúncio |
| `categoria` | Área de atuação da vaga (ex: TI, engenharia, vendas) |
| `salario` | **Variável alvo.** Salário anual normalizado da vaga |
| `fonte` | Site ou plataforma onde o anúncio foi publicado |
