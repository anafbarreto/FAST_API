import time
import asyncio # Ajuda trabalhar os metodos de execução assíncrona

async def async_task(task_id):
    print(f"Starting task {task_id}")
    await asyncio.sleep(2) # Preciso aguardar 2 segundos
    print(f"Finished task {task_id}")

async def main():
    tasks = [asyncio.create_task(async_task(task_id)) for task_id in range(10)] # Criando 10 tarefas
    await asyncio.gather(*tasks)

start_time = time.time() # Iniciando a contagem de tempo

asyncio.run(main()) # Executando o asyncio

end_time = time.time() # Terminando a contagem de tempo

print(f"Total time: {end_time - start_time:.2f}s")