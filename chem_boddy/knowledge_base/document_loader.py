import os
import fitz  # PyMuPDF
from docx import Document
from chem_boddy import CONFIG
from chem_boddy.knowledge_base.text_splitter import convert_Pages_ChunkinChar, convert_Chunk_Token, add_meta_data, add_document_to_collection
from chem_boddy.vector_db import create_chroma_client

def get_chroma_collection():
    chroma_client, chroma_collection = create_chroma_client()
    return chroma_collection

def build_knowledge_base(document_directory_path):  
    chroma_client, chroma_collection = create_chroma_client()
    
    current_id = 0 #chroma_collection.count()
    print(f"Current Number of Document Chunks in Vector DB : {current_id}")

    for filename in os.listdir(document_directory_path):
        file_path = os.path.join(document_directory_path, filename)
        file_extension = os.path.splitext(filename)[1]
        
        document = []

        if file_extension == '.pdf':
            with fitz.open(file_path) as doc:
                text = ''
                for page in doc:
                    text += page.get_text()
            document.append(text)
            print(f'\nPDF document {filename} loaded successfully from {file_path}')

            print(f"Processing the document {filename} to add to the {chroma_collection.name} collection")
            print(f"Current number of document chunks in Vector DB: {chroma_collection.count()} ")
            text_chunksinChar = convert_Pages_ChunkinChar(document)
            text_chunksinTokens = convert_Chunk_Token(text_chunksinChar)
            ids,metadatas = add_meta_data(text_chunksinTokens,filename, current_id)
            ids = [id + filename for id   in ids] 
            current_id =0 #current_id + len(text_chunksinTokens)
            chroma_collection = add_document_to_collection(ids, metadatas, text_chunksinTokens, chroma_collection)
            print(f"Id ler {ids}");
            print(f"metadatalar {metadatas}");
            print(f"Document {filename} added to the collection")
            print(f"Current number of document chunks in Vector DB: {chroma_collection.count()} ")            

