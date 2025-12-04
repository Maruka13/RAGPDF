#carregar docs
#dividir os docs em chunks
#vetorizar os chunks com embedding

def criar_db():
    documentos = carregar_documentos()
    chunks = dividir_chunks(documentos)
    vetorizar_chunks(chunks)

criar_db()

