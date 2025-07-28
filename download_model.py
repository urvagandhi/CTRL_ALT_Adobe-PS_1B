from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer
import os

# === Create a shared "model" folder ===
base_model_dir = os.path.abspath("./models")
os.makedirs(base_model_dir, exist_ok=True)

# === FLAN-T5 ===
flan_dir = os.path.join(base_model_dir, "flan_t5_small")
print("Downloading: google/flan-t5-small...")

flan_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
flan_tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

flan_model.save_pretrained(flan_dir)
flan_tokenizer.save_pretrained(flan_dir)

print(f"FLAN-T5 downloaded and saved to: {flan_dir}\n")

# === MiniLM ===
minilm_dir = os.path.join(base_model_dir, "all_MiniLM_L6_v2")
print("Downloading: all-MiniLM-L6-v2...")

minilm_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
minilm_model.save(minilm_dir)

print(f"MiniLM downloaded and saved to: {minilm_dir}")