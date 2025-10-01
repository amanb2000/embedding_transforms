#!/bin/bash

source venv/bin/activate
KERNEL_NAME="embedding_kernel"
DISPLAY_NAME="Embedding_Kernel"

python -m ipykernel install --user --name=${KERNEL_NAME} --display-name=$DISPLAY_NAME