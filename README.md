# 通信领域知识问答小助手

## 项目简介

目前，LLM的应用在众多垂直领域开花结果。通信（communication technology）作为一个成（xi）熟（yang）的领域，可以在LLM的赋能下焕发新的活力。本项目旨在通过fine tuning和RAG等技术，开发一个理解通信领域基础知识、能够支持常用通信标准文件中的专业内容问答交互的LLM应用。

## 实现计划

计划基于书生·浦语大模型（InternLM）及相关框架，通过微调和RAG等技术，实现通信领域general和expert知识的问答交互。

## 微调

基于InternLM2工具链中的xtuner微调框架，支持多数主流大模型和多类微调方法

源码安装：
git clone -b v0.1.19 https://github.com/InternLM/xtuner
cd /path/to/xtuner
pip install -e '.[all]'
或者pip安装：
pip install xtuner==0.1.19

xtuner微调参考教程：
https://github.com/InternLM/Tutorial/blob/camp2/xtuner/personal_assistant_document.md

### 使用的数据集

https://github.com/netop-team/TeleQnA

### 使用的模型

internlm-2：
https://github.com/InternLM/InternLM

phi-2：
https://huggingface.co/microsoft/phi-2

### 数据集格式调整

编写以下脚本，调整原始数据集的格式，以适应增量预训练和指令微调的要求：
- `teleqna_dataset_separation_by_categories.py`
- `teleqna_dataset_transfer_for_pretrain_fine_tuning.py`
- `teleqna_json_dataset_item_replicate.py`
- `teleqna_dataset_transfer_for_instruction_fine_tuning.py`
    
### 增量预训练（incremental pre-training）

希望采用TeleQnA数据集中的Research overview和Lexicon部分数据，通过QLoRA增量预训练，帮助模型学到一般性的知识。基于internlm-2-1_8b模型进行微调，由于所用的数据的丰富度有限，比较难以概括通信领域的一般性知识，使用xtuner进行增量预训练，loss值难以降到0.5以下，对话测试结果显示模型学习数据集内容的准确率不够。

数据集：
- `TeleQnA_Lexicon_and_Research_overview_pretrain.json`
- `TeleQnA_Lexicon_and_Research_overview_replicate_100_pretrain.json`
    
### 指令微调（supervised fine-tuning）

改用QLoRA指令微调方法，可以得到更低的loss值。以Research overview数据集的前10个sample为例，将每个sample重复1000次，基于microsoft phi-2模型训练大约0.5个epoch后得到权重文件iter_300.pth，发现模型对前10个sample的理解和问答能力得到了显著提升。

数据集：
- `TeleQnA_Research_overview_first_10_replicate_1000_instruction_ft.json`

## RAG

经过本周的微调实验，基本跑通了使用xtuner进行增量预训练和指令微调的全流程。从实验结果发现，指令微调更加适合于让模型准确地学到如何针对性地回答数据集中的问题。接下来计划进一步学习RAG，对于数据集中偏向于一般性的知识的samples，通过指令微调进一步训练；对于更加specialized samples，通过RAG实现prompt增强，从而提高模型在该数据集上的问答性能。
