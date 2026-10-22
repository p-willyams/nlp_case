import pandas as pd
import numpy as np

# Carrega o dataset bruto
df = pd.read_csv("data/raw/base_vagas.csv")

# 1. Remove registros duplicados que diferem apenas no id_anuncio, mantendo a primeira ocorrência
df = df.drop_duplicates(
    subset=[col for col in df.columns if col != "id_anuncio"], keep="first"
).reset_index(drop=True)

# 2. Preenche valores faltantes em colunas selecionadas com 'unknown'
colunas_unknown = ["tipo_contrato", "regime_contrato", "empresa", "titulo", "fonte"]
for col in colunas_unknown:
    df[col] = df[col].fillna("unknown")

# 3. Cria colunas auxiliares indicando valores faltantes nas principais colunas
df["tipo_contrato_missing"] = (df["tipo_contrato"] == "unknown").astype(int)
df["regime_contrato_missing"] = (df["regime_contrato"] == "unknown").astype(int)
df["empresa_missing"] = (df["empresa"] == "unknown").astype(int)

# 4. Remove registros específicos (por index) e salários suspeitos
ids_remover = [227870, 76018, 36145, 229405, 63005, 19383]
mask = (df["salario"] == 5000) | df.index.isin(ids_remover)
df = df[~mask].copy()

# 5. Salva o dataframe limpo em processed ao invés de raw2
df.to_csv("data/processed/base_vagas.csv", index=False)
