# Projeto IA - Aplicação de Técnicas de Reconhecimento e Análise de Padrões com Inteligência Artificial no Apoio ao Diagnóstico de Problemas Cognitivos em Crianças 

## Explicação do dataset

O dataset deste projeto é formado por imagens e suas respectivas marcações de segmentação, produzidas para identificar as regiões de interesse analisadas no projeto. Para documentar essa base, este repositório apresenta uma amostra do dataset com a imagem original e sua versão anotada, evidenciando como as marcações foram realizadas.

A base foi organizada em três subconjuntos: `train`, `valid` e `test`. Essa divisão permite separar as imagens usadas no treinamento do modelo. Os exemplos incluídos no repositório têm o objetivo de demonstrar, de forma clara, a estrutura da base e o processo de anotação utilizado no projeto.

## Justificativa sobre a ausência de análise exploratória tradicional e de tratamento dos dados (imagens)

Neste projeto, o dataset é composto por **imagens brutas**, utilizadas como dados de entrada para o modelo de Inteligência Artificial. Por essa característica, **não se aplica uma análise exploratória tradicional igual à realizada em bases tabulares**, como inspeção de valores nulos, médias, desvios, outliers numéricos, padronização de colunas ou limpeza de registros textuais.

Além disso, **não foi realizado tratamento das imagens nesta etapa** porque o objetivo do trabalho é preservar ao máximo as características originais do conjunto de dados, visto que o objetivo é avaliar a montagem da figura pela criança. Alterações como filtros, correções, recortes, aumento de contraste, remoção de ruído ou transformações visuais poderiam modificar padrões importantes presentes nas imagens e interferir na avaliação do modelo. Assim, optou-se por manter o dataset em seu estado original, garantindo maior fidelidade ao material coletado.

Isso **não significa ausência de análise do dataset**, mas sim que a análise foi conduzida de forma **compatível com a natureza visual dos dados**. Em vez de limpeza e transformação, a etapa de exploração concentrou-se na **caracterização estrutural do conjunto de imagens**, incluindo:

- distribuição por classes ou categorias (montagens de crianças de 3, 4, 5 e 6 anos)
- formatos de arquivo existentes (os arquivos em .heic foram transformados em .jpeg ou .jpg)
- identificação de imagens potencialmente corrompidas
- organização em pastas (conforme idade das crianças)
- distribuição entre treino, validação e teste (crucial para a marcação da base e treinamento do modelo)

Portanto, para este projeto, a preparação dos dados não consistiu em modificar o conteúdo visual das imagens, mas sim em **verificar a integridade, a organização e a consistência estrutural do dataset**, o que é mais adequado ao tipo de dado utilizado.
