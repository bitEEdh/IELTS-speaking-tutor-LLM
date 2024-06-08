#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from typing import Dict, List, Optional, Tuple, Union

PROMPT_TEMPLATE = dict(
    RAG_PROMPT_TEMPALTE="""Use the provided context to answer the user's question. If you do not know the answer, say that you do not know. Always respond in English.
        Question: {question}
        Available context:
        ···
        {context}
        ···
        If the given context does not provide enough information for you to answer, please respond that the content is not in the database and you do not know.
        Useful answer:""",
    InternLM_PROMPT_TEMPALTE="""First, summarize the content of the context, and then use the context to answer the user’s question. If you do not know the answer, say that you do not know. Always respond in English.
        Question: {question}
        Available context：
        ···
        {context}
        ···
        If the given context does not provide enough information for you to answer, please respond that the content is not in the database and you do not know.
        Useful answer:"""
)

class BaseModel:
    def __init__(self, path: str = '') -> None:
        self.path = path

    def chat(self, prompt: str, history: List[dict], content: str) -> str:
        pass

    def load_model(self):
        pass

class InternLMChat(BaseModel):
    def __init__(self, path: str = '') -> None:
        super().__init__(path)
        self.load_model()

    def chat(self, prompt: str, history: List = [], content: str='') -> str:
        prompt = PROMPT_TEMPLATE['InternLM_PROMPT_TEMPALTE'].format(question=prompt, context=content)
        response, history = self.model.chat(self.tokenizer, prompt, history)
        return response


    def load_model(self):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.tokenizer = AutoTokenizer.from_pretrained(self.path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(self.path, torch_dtype=torch.float16, trust_remote_code=True).cuda()
