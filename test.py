#%%
import chromadb
client = chromadb.PersistentClient()
#%%
collection = client.create_collection(
        name="collection_name",
        metadata={"hnsw:space": "cosine"} # l2 is the default
    )

# %%
collection.upsert(
    documents=["y1", "y1", "y33"],
    metadatas=[ {"chapter": "3", "verse": "16"},
                {"chapter": "3", "verse": "5"}, 
                {"chapter": "29", "verse": "11"}],
    ids=["id1", "id2", "id3"]
)
#%%
collection.get(["id1", "id2", "id3"])
#%%
# Koleksiyonları listele
collections = client.list_collections()
#client.get_collection("collection_name")

# Koleksiyonları yazdır
for collection in collections:
    print(collection.name)

#%%
client.delete_collection("collection_name")
#%%
from chem_boddy.knowledge_base import build_knowledge_base   

knowledge_base= build_knowledge_base(r'.\files')
#%%
import chromadb
from chromadb.utils import embedding_functions
client = chromadb.PersistentClient("./chroma_db")
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction( model_name="distiluse-base-multilingual-cased-v2")
chroma_collection = client.get_collection(
        "rag_collection",
        embedding_function=embedding_function)
chroma_collection.count()
#%%
def retrieve_chunks(chroma_collection, query, n_results=25,
                 return_only_docs=False, filterType=None, filterValue=None):
    
    if filterType is not None and filterValue is not None:
        results = chroma_collection.query(
            query_texts=[query],
            include=["documents", "metadatas", "distances"],
            where={filterType: filterValue},
            n_results=n_results)

    else:
        results = chroma_collection.query(
            query_texts=[query],
            include= [ "documents","metadatas",'distances' ],
            n_results=n_results)

    if return_only_docs:
        return results['documents'][0]
    else:
        return results
    
query = "Gazların özellikleri nelerdir?"
retrieved_documents= retrieve_chunks(chroma_collection, query, 1, return_only_docs=False,
                                     #filterType='metadatas.document', filterValue='Kimya gazlar meb kitabı.pdf'
                                     )
#%%
#client.delete_collection(name="rag_collection")
#%%
metin = """{'soru': 'Aşağıdakilerden hangisi gazların temel özelliklerinden biridir?', 'secenekler': {'A': 'Belirli bir şekil ve hacimleri vardır.', 'B': 'Sıkıştırılamazlardır.', 'C': 'Bulundukları kabın şeklini ve hacmini alırlar.', 'D': 'Akışkan değillerdir.', 'E': 'Moleküller arası mesafe çok azdır.'}, 'dogru_cevap': 'C', 'açıklama': 'Gazlar, bulundukları kabın şeklini ve hacmini alan akışkan maddelerdir.  Sıkıştırılabilirler ve molekülleri arasında büyük boşluklar bulunur.'}"""
import json
soru_data = json.loads(metin)