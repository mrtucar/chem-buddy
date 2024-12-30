from .llm_interface import build_chatBot, generate_LLM_answer, generateAnswer,run_rag_pipeline,generateQuestion
from chem_boddy import CONFIG   

soru_json = """
{
"soru": "Aşağıdakilerden hangisi gazların özelliklerinden **değildir**?",
"secenekler": {
    "A": "Gazlar bulundukları kabın şeklini ve hacmini alır.",
    "B": "Gazlar kolaylıkla sıkıştırılabilir.",
    "C": "Gazların belirli bir şekli ve hacmi vardır.",
    "D": "Gaz molekülleri arasındaki boşluklar katı ve sıvılara göre çok daha fazladır.",
    "E": "Gazlar akışkandır."
},
"dogru_cevap": "Gazların belirli bir şekli ve hacmi vardır"
},
"aciklama": "Gazlar, belirli bir şekli ve hacmi olmayan, sıkıştır"
"""

# Access the system_prompt value
system_prompt = CONFIG['llm']['settings']['system_prompt']
soru_uretimi_prompt = CONFIG['llm']['settings']['soru_uretimi_prompt']

print("Sistem Komutları:" +system_prompt)

RAG_LLM = build_chatBot(system_prompt)
SoruUretici = build_chatBot(soru_uretimi_prompt+"\n"+soru_json)

__all__ = ['build_rag_llm', 'generate_LLM_answer', 'RAG_LLM', 'generateAnswer', 'run_rag_pipeline','generateQuestion'] 