# simulator.py
import random
import numpy as np

def run_devops_simulation(params):
    devs = params['num_developers']
    testers = params['num_testers']
    sprint_days = params['sprint_days']
    automation = params['automation_level']
    bug_prob = params['bug_probability']
    num_sprints = params['num_sprints']
    tasks_per_sprint = params['tasks_per_sprint']
    
    # === Sistemas Dinámicos: deuda técnica acumulada ===
    technical_debt = 0  # bugs no resueltos que se arrastran
    velocity_history = []
    lead_time_history = []
    defect_history = []
    deploy_history = []
    debt_history = [0]  # empezamos sin deuda

    for sprint in range(num_sprints):
        tasks = tasks_per_sprint + int(technical_debt * 0.3)  # deuda genera más tareas
        completed = 0
        defects = 0
        lead_times = []
        current_debt = 0

        for _ in range(tasks):
            # --- Cadena de Markov: estados de una tarea ---
            # Estados: Backlog → Code → Build → Test → Deploy → Done (o Rework)
            time_spent = 0

            # Code
            time_spent += random.uniform(1, 4) / devs
            if random.random() < bug_prob * (1 + technical_debt * 0.1):
                defects += 1
                current_debt += 1
                time_spent += random.uniform(1, 3)  # rework

            # Build (siempre pasa)

            # Test (más rápido con automatización)
            test_time = random.uniform(0.5, 2) * (1 - automation * 0.85)
            if testers > 0:
                test_time /= testers
            time_spent += test_time

            # Deploy con probabilidad mejorada por automatización + deuda
            deploy_success_prob = 0.55 + automation * 0.45 - technical_debt * 0.08
            deploy_success_prob = max(0.1, min(0.99, deploy_success_prob))

            if random.random() < deploy_success_prob:
                completed += 1
                lead_times.append(time_spent)
            else:
                current_debt += 1  # fallo de deploy genera más deuda

        # === Actualización de deuda técnica (sistema dinámico) ===
        resolved_this_sprint = min(defects * 0.7, devs * 2)  # capacidad de resolución
        technical_debt = max(0, technical_debt + current_debt - resolved_this_sprint)
        debt_history.append(round(technical_debt, 1))

        # Métricas del sprint
        avg_lead = np.mean(lead_times) if lead_times else sprint_days * 2
        velocity_history.append(completed)
        lead_time_history.append(round(avg_lead, 2))
        defect_history.append(defects)
        deploy_history.append(completed)

    return {
        'lead_time_avg': round(np.mean(lead_time_history), 2),
        'defect_rate': round(np.mean(defect_history) / tasks_per_sprint * 100, 1),
        'deploy_success_rate': round(np.mean(deploy_history) / tasks_per_sprint * 100, 1),
        'final_debt': debt_history[-1],
        'sprint_data': {
            'lead_times': lead_time_history,
            'defects': defect_history,
            'deploys': deploy_history,
            'velocity': velocity_history,
            'debt': debt_history[1:]  # sin el 0 inicial
        }
    }