# gerador_de_procuracao

Nesse repositório está um programa, feito em Python, que gera uma procuração automaticamente com dados de clientes de um escritório de advocacia que estão em um banco de dados SQL no SQLite. Os arquivos Python são:

**gerador_de_procuração.py** - arquivo que, à partir do cpf de um cliente, busca suas informações e gera a procuração. 

**func_procuração.py** - arquivo com a função que é chamada pelo gerador_de_procuração.py que faz a procuração no Microsoft Word.

Juntamente com esses arquivos, está um banco de dados do SQLite com dados fictícios de alguns clientes do escritório, para ser usado para ver como o gerador_de_procuração.py funciona. O nome do banco de dados é **escritório.db**.

Fique à vontade para usar esses códigos e alterá-lo. Ele é simplesmente uma "base" que pode ser usado para muito fins diferentes, agilizando vários processos.
