# Curso de Python para Analistas de Datos

Repositorio con 28 clases progresivas de Python aplicado a automatización y análisis de datos para un perfil de Analista Financiero/de Datos, usando una empresa ficticia (Comercial Andes S.A.) como caso de estudio.

## Contenido
- Fundamentos de Python (variables, listas, diccionarios, funciones, condicionales)
- Automatización con pandas (Excel, CSV, fechas, gráficos)
- Envío automático de correos con adjuntos
- SQL básico con sqlite3
- Manejo de errores (try/except)
- Programación de tareas automáticas (schedule)
- Limpieza de datos reales (duplicados, nulos, texto inconsistente)
- Programación Orientada a Objetos (clases, herencia)
- pandas avanzado (merge, pivot_table)
- Jupyter Notebook
- Conexión a bases de datos SQL Server reales con pyodbc


## Proyecto destacado: Analizador de Portafolio de Inversión (clase-30 a clase-32)

Análisis cuantitativo de un portafolio compuesto por 4 acciones (AAPL, MSFT, GOOGL, AMZN) usando datos reales de mercado (yfinance) y cálculos financieros con numpy:

- Retornos diarios y retorno total del período
- Volatilidad anualizada por acción (riesgo individual)
- Matriz de correlación entre activos
- Retorno y volatilidad del portafolio combinado (ponderado), demostrando el efecto de diversificación
- Visualización del crecimiento comparado de $1 invertido en cada acción

**Hallazgo principal:** el portafolio combinado (25% en cada acción) tuvo una volatilidad anual de 19.43%, inferior a la de cualquier acción individual (19.9% a 28.1%), evidenciando el beneficio de diversificación incluso dentro de un mismo sector.