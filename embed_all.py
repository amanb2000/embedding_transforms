# usage: python3 embed_file.py path/to/file.md 
# example: 

from pathlib import Path
import sys
import pdb
import numpy as np
from mlx_embeddings.utils import load


# Recommended approach - automatically handles file closing
def get_np_embed(file_path):
    with open(file_path, 'r') as file:
        content = file.read()


    # Load model directly
    print("length of content: ", len(content))


    # Load the model and tokenizer
    model_name = "mlx-community/all-MiniLM-L6-v2-4bit"
    model, tokenizer = load(model_name)

    # Prepare the text
    text = content

    # Tokenize and generate embedding
    input_ids = tokenizer.encode(text, return_tensors="mlx")
    outputs = model(input_ids)
    raw_embeds = outputs.last_hidden_state[:, 0, :] # CLS token
    text_embeds = outputs.text_embeds # mean pooled and normalized embeddings
    return np.array(raw_embeds)

def save_np_embed(file_path, np_embeds): 
    fpath=Path(file_path)
    npz_out_path=fpath.with_suffix('.npz')

    if npz_out_path.exists():
        print(f"output {npz_out_path} already exists, skipping...")
        return

    print(f"Saving to {npz_out_path} with shape {np_embeds.shape}")
    np.savez(npz_out_path, embeds=np_embeds)

def get_all_fpaths(base_path): 
    allp = [i for i in base_path.iterdir()]
    finalp = []
    for p in allp: 
        if p.suffix == '.md' or p.suffix == '.txt': 
            finalp.append(p)
    return finalp


base_path = Path(sys.argv[1])

allp=get_all_fpaths(base_path)

for file_path in allp:
    print("generating embeddings...")
    np_array=get_np_embed(file_path)
    print("done generating embeddings")

    print(f"file path: {file_path}")
    save_np_embed(file_path, np_array)

