import time

def sync_task(task_id):
    print(f"Starting task {task_id}")
    time.sleep(2)
    print(f"Finished task {task_id}")
    
start_time = time.time() # Iniciando a contagem de tempo

for task_id in range(10): # Criando 10 tarefas
    sync_task(task_id)

end_time = time.time() # Terminando a contagem de tempo

print(f"Total time: {end_time - start_time:.2f}s")